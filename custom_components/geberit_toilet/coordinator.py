from __future__ import annotations
import asyncio
from datetime import datetime, timedelta, timezone
import json
import logging
from pathlib import Path
import time
from typing import Any
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.storage import Store
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .config_helpers import normalize_communication_mode, parse_dpid_list
from .const import DOMAIN, CONF_DEVICE_ID, CONF_PIN, CONF_ESPHOME_HOST, CONF_ESPHOME_PORT, CONF_NOISE_PSK, CONF_POLL_INTERVAL, CONF_REQUEST_DATA_MODE, CONF_COMMUNICATION_MODE, CONF_INCLUDE_DPIDS, CONF_EXCLUDE_DPIDS, CONF_MAX_INSTANCES_PER_DPID_GROUP, CONF_EXPOSE_LARGE_INSTANCE_GROUPS, DEFAULT_ESPHOME_PORT, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_POLL_INTERVAL, DIFFERENCES_DIRNAME, COMMUNICATION_MODE_DPIDS, COMMUNICATION_MODE_GATT, COMMUNICATION_MODE_BOTH, REQUEST_DATA_MODE_ALL_KNOWN, REQUEST_DATA_MODE_INVENTORY_ONLY, REPORTS_DIRNAME
from .metadata import DpMetadata, HIDDEN_DP_IDS, build_dp_metadata
from .protocol.BluetoothLeConnector import BluetoothLeConnector
from .protocol.Ble20Client import Ble20Client
from .protocol.DpId import DpId
from .protocol.GattIdentifiers import RuntimeGattCharacteristic, decode_known_gatt_value, discover_known_gatt_characteristics
_LOGGER = logging.getLogger(__name__)

def wire_dp_id(dp_id: int) -> int:
    return int(dp_id) & 32767

def decode_value(dp_id: int, val_bytes: bytes) -> Any:
    if not val_bytes:
        return None
    if dp_id in (DpId.DP_NAME, DpId.DP_FW_RS_VERSION, DpId.DP_MCU_VERSION, DpId.DP_DEVICE_INFORMATION):
        try:
            return val_bytes.decode('utf-8', errors='ignore').strip('\x00')
        except Exception:
            pass
    length = len(val_bytes)
    if length == 1:
        return val_bytes[0]
    elif length == 2:
        return int.from_bytes(val_bytes, byteorder='little', signed=False)
    elif length == 4:
        return int.from_bytes(val_bytes, byteorder='little', signed=False)
    else:
        try:
            return val_bytes.decode('utf-8', errors='ignore').strip('\x00')
        except Exception:
            return val_bytes.hex()

class GeberitToiletCoordinator(DataUpdateCoordinator[dict[int, Any]]):

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self._entry = entry
        conf = {**entry.data, **entry.options}
        self._device_id = conf[CONF_DEVICE_ID]
        self._esphome_host = conf.get(CONF_ESPHOME_HOST) or None
        self._esphome_port = conf.get(CONF_ESPHOME_PORT, DEFAULT_ESPHOME_PORT)
        self._noise_psk = conf.get(CONF_NOISE_PSK) or None
        self._pin = conf.get(CONF_PIN) or None
        self._request_data_mode = conf.get(CONF_REQUEST_DATA_MODE, REQUEST_DATA_MODE_INVENTORY_ONLY)
        self._communication_mode = normalize_communication_mode(
            conf.get(CONF_COMMUNICATION_MODE)
        )
        self._configured_include_dpids = parse_dpid_list(conf.get(CONF_INCLUDE_DPIDS))
        self._configured_exclude_dpids = set(parse_dpid_list(conf.get(CONF_EXCLUDE_DPIDS)))
        self._max_instances_per_dpid_group = int(conf.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP))
        self._expose_large_instance_groups = bool(conf.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, False))
        poll_interval = conf.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL)
        self._poll_interval = timedelta(seconds=poll_interval)
        self._ble_lock = asyncio.Lock()
        self._inventory: dict[int, Any] | None = None
        self._dp_metadata: dict[int, DpMetadata] = {}
        self._capabilities: dict[int, Any] | None = None
        self._raw_cache: dict[int, bytes] = {}
        self._gatt_characteristics: dict[str, RuntimeGattCharacteristic] = {}
        self._gatt_raw_values: dict[str, bytes] = {}
        self._gatt_decoded_values: dict[str, Any] = {}
        self._discovered_non_inventory_dpids: set[int] = set()
        self._all_known_scan_completed = False
        self._read_targets: dict[int, tuple[int | None, ...]] = {}
        self._discovery_cache_dirty = False
        self.poll_enabled = True
        self._connection_enabled_event = asyncio.Event()
        self._connection_enabled_event.set()
        self._discovery_store: Store[dict[str, Any]] = Store(hass, 1, f'{DOMAIN}_{entry.entry_id}_discovery')
        self._state_store: Store[dict[str, Any]] = Store(hass, 1, f'{DOMAIN}_{entry.entry_id}_state')
        self._report_files: list[str] = []
        self._selected_report_left: str | None = None
        self._selected_report_right: str | None = None
        self._metadata_name_translations: dict[str, str] = {}
        self._active_connector: BluetoothLeConnector | None = None
        self._active_client: Ble20Client | None = None
        self._listener_tasks: list[asyncio.Task] = []
        self._connection_loop_task: asyncio.Task | None = None
        self._startup_cache_loaded = False
        self._integration_ready = False
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=self._poll_interval)
        self._connection_loop_task = asyncio.create_task(self._connection_loop())

    def set_metadata_name_translations(self, translations: dict[str, str]) -> None:
        self._metadata_name_translations = dict(translations)

    def localize_metadata_name(self, meta: DpMetadata | None) -> str | None:
        if meta is None:
            return None
        return self._metadata_name_translations.get(meta.key, meta.name)

    @property
    def reports_dir(self) -> Path:
        return Path(self.hass.config.path(REPORTS_DIRNAME))

    @property
    def differences_dir(self) -> Path:
        return Path(self.hass.config.path(DIFFERENCES_DIRNAME))

    @property
    def report_files(self) -> list[str]:
        return list(self._report_files)

    @property
    def report_files_left(self) -> list[str]:
        return list(self._report_files)

    @property
    def report_files_right(self) -> list[str]:
        if self._selected_report_left is None:
            return list(self._report_files)
        return [name for name in self._report_files if name != self._selected_report_left]

    @property
    def selected_report_left(self) -> str | None:
        return self._selected_report_left

    @property
    def selected_report_right(self) -> str | None:
        return self._selected_report_right

    def _serialize_data_key(self, key: Any) -> dict[str, Any]:
        if isinstance(key, tuple) and len(key) == 2:
            return {'dp_id': int(key[0]), 'instance': int(key[1]), 'composite_key': f'{int(key[0])}:{int(key[1])}'}
        return {'dp_id': int(key), 'instance': None, 'composite_key': str(int(key))}

    def _json_safe(self, value: Any) -> Any:
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, bytes):
            return value.hex()
        if isinstance(value, dict):
            return {str(k): self._json_safe(v) for (k, v) in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [self._json_safe(item) for item in value]
        return str(value)

    def _build_report_payload(self) -> dict[str, Any]:
        data = self.data or {}
        entity_states: list[dict[str, Any]] = []
        entity_registry = er.async_get(self.hass)
        entity_ids = sorted({entry.entity_id for entry in er.async_entries_for_config_entry(entity_registry, self._entry.entry_id) if entry.entity_id})
        for entity_id in entity_ids:
            state = self.hass.states.get(entity_id)
            if state is None:
                continue
            attrs = state.attributes
            entity_states.append({'entity_id': entity_id, 'state': state.state, 'attributes': self._json_safe(dict(attrs)), 'last_changed': state.last_changed.isoformat(), 'last_updated': state.last_updated.isoformat()})
        dp_values: list[dict[str, Any]] = []
        for key in sorted(data, key=lambda item: str(item)):
            key_info = self._serialize_data_key(key)
            meta = self.get_dp_metadata(key_info['dp_id'])
            raw_key = key if key in self._raw_cache else key_info['dp_id']
            raw_value = self._raw_cache.get(raw_key)
            dp_values.append({**key_info, 'name': meta.name if meta else None, 'dp_key': meta.key if meta else None, 'decoded_value': self._json_safe(data[key]), 'raw_hex': raw_value.hex() if isinstance(raw_value, bytes) else None})
        gatt_values: list[dict[str, Any]] = []
        for (uuid, runtime_char) in sorted(self._gatt_characteristics.items()):
            raw_value = self._gatt_raw_values.get(uuid)
            gatt_values.append({'uuid': uuid, 'service_uuid': runtime_char.service_uuid, 'service_name': runtime_char.service_name, 'key': runtime_char.key, 'name': runtime_char.name, 'source': runtime_char.source, 'properties': list(runtime_char.properties), 'readable': runtime_char.readable, 'writable': runtime_char.writable, 'notifiable': runtime_char.notifiable, 'indicatable': runtime_char.indicatable, 'decoded_value': self._json_safe(self._gatt_decoded_values.get(uuid)), 'raw_hex': raw_value.hex() if isinstance(raw_value, bytes) else None})
        return {'generated_at': datetime.now(timezone.utc).isoformat(), 'domain': DOMAIN, 'device_id': self._device_id, 'request_data_mode': self._request_data_mode, 'communication_mode': self._communication_mode, 'max_instances_per_dpid_group': self._max_instances_per_dpid_group, 'expose_large_instance_groups': self._expose_large_instance_groups, 'poll_enabled': self.poll_enabled, 'ble_connected': self.ble_connected, 'supported_dp_ids': sorted(self.supported_dp_ids), 'configured_include_dpids': list(self._configured_include_dpids), 'configured_exclude_dpids': sorted(self._configured_exclude_dpids), 'discovered_non_inventory_dpids': sorted(self._discovered_non_inventory_dpids), 'dp_values': dp_values, 'gatt_values': gatt_values, 'entity_states': sorted(entity_states, key=lambda item: item['entity_id'])}

    def _sync_write_json(self, path: Path, payload: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True), encoding='utf-8')

    def _sync_read_json(self, path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding='utf-8'))

    def _sync_list_report_files(self) -> list[str]:
        reports_dir = self.reports_dir
        reports_dir.mkdir(parents=True, exist_ok=True)
        return sorted((path.name for path in reports_dir.glob('*.json')), reverse=True)

    async def async_refresh_report_catalog(self) -> None:
        report_files = await self.hass.async_add_executor_job(self._sync_list_report_files)
        self._report_files = report_files
        if not report_files:
            self._selected_report_left = None
            self._selected_report_right = None
        else:
            if self._selected_report_left not in report_files:
                self._selected_report_left = report_files[0]
            right_candidates = self.report_files_right
            if not right_candidates:
                self._selected_report_right = None
            elif self._selected_report_right not in right_candidates:
                self._selected_report_right = right_candidates[0]
        self.async_update_listeners()

    async def async_select_report_left(self, filename: str) -> None:
        await self.async_refresh_report_catalog()
        if filename not in self._report_files:
            raise ValueError(f'Unknown report file: {filename}')
        self._selected_report_left = filename
        right_candidates = self.report_files_right
        if not right_candidates:
            self._selected_report_right = None
        elif self._selected_report_right not in right_candidates:
            self._selected_report_right = right_candidates[0]
        self.async_update_listeners()

    async def async_select_report_right(self, filename: str) -> None:
        await self.async_refresh_report_catalog()
        if filename not in self.report_files_right:
            raise ValueError(f'Unknown report file: {filename}')
        self._selected_report_right = filename
        self.async_update_listeners()

    async def async_create_report(self) -> str:
        payload = self._build_report_payload()
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
        filename = f"{self._device_id.replace(':', '-')}_{timestamp}.json"
        path = self.reports_dir / filename
        await self.hass.async_add_executor_job(self._sync_write_json, path, payload)
        await self.async_refresh_report_catalog()
        return str(path)

    def _build_diff_text(self, left_name: str, left_payload: dict[str, Any], right_name: str, right_payload: dict[str, Any]) -> str:
        lines = [f'Geberit Toilet report differences', f'Left : {left_name}', f'Right: {right_name}', '']
        left_dp = {item['composite_key']: item for item in left_payload.get('dp_values', [])}
        right_dp = {item['composite_key']: item for item in right_payload.get('dp_values', [])}
        all_dp_keys = sorted(set(left_dp) | set(right_dp))
        dp_changes: list[str] = []
        for key in all_dp_keys:
            old = left_dp.get(key)
            new = right_dp.get(key)
            if old is None:
                dp_changes.append(f"+ DPID {key} added: {new.get('decoded_value')!r} raw={new.get('raw_hex')}")
                continue
            if new is None:
                dp_changes.append(f"- DPID {key} removed: {old.get('decoded_value')!r} raw={old.get('raw_hex')}")
                continue
            if old.get('decoded_value') != new.get('decoded_value') or old.get('raw_hex') != new.get('raw_hex'):
                name = new.get('name') or old.get('name') or key
                dp_changes.append(f"* DPID {key} ({name}): {old.get('decoded_value')!r} -> {new.get('decoded_value')!r} | raw {old.get('raw_hex')} -> {new.get('raw_hex')}")
        lines.append('DPID changes:')
        if dp_changes:
            lines.extend(dp_changes)
        else:
            lines.append('No DPID changes.')
        lines.append('')
        left_entities = {item['entity_id']: item for item in left_payload.get('entity_states', [])}
        right_entities = {item['entity_id']: item for item in right_payload.get('entity_states', [])}
        all_entity_ids = sorted(set(left_entities) | set(right_entities))
        entity_changes: list[str] = []
        for entity_id in all_entity_ids:
            old = left_entities.get(entity_id)
            new = right_entities.get(entity_id)
            if old is None:
                entity_changes.append(f"+ Entity {entity_id} added with state {new.get('state')!r}")
                continue
            if new is None:
                entity_changes.append(f"- Entity {entity_id} removed (was {old.get('state')!r})")
                continue
            if old.get('state') != new.get('state'):
                entity_changes.append(f"* Entity {entity_id} state: {old.get('state')!r} -> {new.get('state')!r}")
            if old.get('attributes') != new.get('attributes'):
                entity_changes.append(f'* Entity {entity_id} attributes changed')
        lines.append('Entity changes:')
        if entity_changes:
            lines.extend(entity_changes)
        else:
            lines.append('No entity changes.')
        lines.append('')
        return '\n'.join(lines)

    async def async_compare_selected_reports(self) -> str:
        await self.async_refresh_report_catalog()
        left_name = self._selected_report_left
        right_name = self._selected_report_right
        if not left_name or not right_name:
            raise ValueError('Two report files must be available and selected before comparison')
        if left_name == right_name:
            raise ValueError('Please choose two different report files for comparison')
        left_path = self.reports_dir / left_name
        right_path = self.reports_dir / right_name
        (left_payload, right_payload) = await asyncio.gather(self.hass.async_add_executor_job(self._sync_read_json, left_path), self.hass.async_add_executor_job(self._sync_read_json, right_path))
        diff_text = self._build_diff_text(left_name, left_payload, right_name, right_payload)
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
        diff_filename = f'{Path(left_name).stem}__vs__{Path(right_name).stem}__{timestamp}.txt'
        diff_path = self.differences_dir / diff_filename
        await self.hass.async_add_executor_job(self._sync_write_text, diff_path, diff_text)
        return str(diff_path)

    def _sync_write_text(self, path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def _sync_clear_directory(self, path: Path, pattern: str) -> int:
        path.mkdir(parents=True, exist_ok=True)
        deleted = 0
        for file_path in path.glob(pattern):
            if not file_path.is_file():
                continue
            file_path.unlink(missing_ok=True)
            deleted += 1
        return deleted

    async def async_clear_reports(self) -> int:
        deleted = await self.hass.async_add_executor_job(self._sync_clear_directory, self.reports_dir, '*.json')
        await self.async_refresh_report_catalog()
        return deleted

    async def async_clear_differences(self) -> int:
        return await self.hass.async_add_executor_job(self._sync_clear_directory, self.differences_dir, '*.txt')

    def _make_connector(self) -> BluetoothLeConnector:
        ha = self.hass if not self._esphome_host else None
        return BluetoothLeConnector(self._esphome_host, self._esphome_port, self._noise_psk, hass=ha)

    @property
    def use_dpids(self) -> bool:
        return self._communication_mode in (COMMUNICATION_MODE_DPIDS, COMMUNICATION_MODE_BOTH)

    @property
    def use_gatt(self) -> bool:
        return self._communication_mode in (COMMUNICATION_MODE_GATT, COMMUNICATION_MODE_BOTH)

    def encode_value(self, dp_id: int, value: Any) -> bytes:
        if isinstance(value, bool):
            return bytes([1 if value else 0])
        if isinstance(value, int):
            cached_bytes = self._raw_cache.get(dp_id)
            length = len(cached_bytes) if cached_bytes else 1
            return value.to_bytes(length, byteorder='little')
        if isinstance(value, str):
            return value.encode('utf-8')
        raise TypeError(f'Unsupported value type: {type(value)}')

    async def _initialize_inventory(self, client: Ble20Client) -> None:
        if self._inventory is not None:
            return
        inv = await client.inventory()
        for dp_id in self._configured_include_dpids:
            if dp_id not in inv:
                inv[dp_id] = {'instance': 0, 'version': 1, 'datatype': 0, 'min_s': 0, 'max_s': 0, 'min_u': 0, 'max_u': 0, 'is_internal': False, 'behavior': 0}
        self._inventory = inv
        self._dp_metadata = build_dp_metadata(inv)
        for dp_id in self._discovered_non_inventory_dpids:
            self._register_runtime_dp_id(dp_id)
        await self._async_save_state_cache()

    @property
    def known_dp_ids(self) -> set[int]:
        return {wire_dp_id(int(member.value)) for member in DpId if wire_dp_id(int(member.value)) not in HIDDEN_DP_IDS}

    def _register_runtime_dp_id(self, dp_id: int) -> None:
        if self._inventory is None or dp_id in self._inventory:
            return
        self._inventory[dp_id] = {'instance': 0, 'version': 0, 'datatype': None, 'min_s': None, 'max_s': None, 'min_u': None, 'max_u': None, 'is_internal': False, 'behavior': 0}
        self._dp_metadata = build_dp_metadata(self._inventory)

    async def async_load_discovery_cache(self) -> None:
        cached = await self._discovery_store.async_load()
        if not cached:
            return
        if cached.get('request_data_mode') != self._request_data_mode:
            return
        discovered = cached.get('discovered_non_inventory_dpids', [])
        self._discovered_non_inventory_dpids = {int(dp_id) for dp_id in discovered if int(dp_id) not in HIDDEN_DP_IDS}
        read_targets_raw = cached.get('read_targets', {})
        parsed_targets: dict[int, tuple[int | None, ...]] = {}
        for (raw_dp_id, raw_targets) in read_targets_raw.items():
            dp_id = int(raw_dp_id)
            parsed_targets[dp_id] = tuple((None if target is None else int(target) for target in raw_targets))
        self._read_targets = parsed_targets
        if self._inventory is not None:
            for dp_id in self._discovered_non_inventory_dpids:
                self._register_runtime_dp_id(dp_id)
        self._all_known_scan_completed = bool(cached.get('all_known_scan_completed', False))

    async def _async_save_discovery_cache(self) -> None:
        if not self._discovery_cache_dirty:
            return
        await self._discovery_store.async_save({'request_data_mode': self._request_data_mode, 'discovered_non_inventory_dpids': sorted(self._discovered_non_inventory_dpids), 'read_targets': {str(dp_id): list(targets) for (dp_id, targets) in self._read_targets.items()}, 'all_known_scan_completed': self._all_known_scan_completed})
        self._discovery_cache_dirty = False

    @property
    def startup_cache_loaded(self) -> bool:
        return self._startup_cache_loaded

    @property
    def integration_ready(self) -> bool:
        return self._integration_ready and self.poll_enabled and self.ble_connected

    def _serialize_data_cache_key(self, key: Any) -> str:
        if isinstance(key, tuple) and len(key) == 2:
            return f'{int(key[0])}:{int(key[1])}'
        return str(int(key))

    def _deserialize_data_cache_key(self, key: str) -> int | tuple[int, int]:
        if ':' not in key:
            return int(key)
        raw_dp_id, raw_instance = key.split(':', 1)
        return (int(raw_dp_id), int(raw_instance))

    async def async_load_state_cache(self) -> None:
        cached = await self._state_store.async_load()
        if not cached:
            return
        loaded_any = False
        if self.use_dpids:
            inventory_raw = cached.get('inventory')
            if isinstance(inventory_raw, dict) and inventory_raw:
                inventory: dict[int, Any] = {}
                for raw_dp_id, inv_entry in inventory_raw.items():
                    try:
                        inventory[int(raw_dp_id)] = dict(inv_entry)
                    except (TypeError, ValueError):
                        continue
                if inventory:
                    for dp_id in self._configured_include_dpids:
                        if dp_id not in inventory:
                            inventory[dp_id] = {'instance': 0, 'version': 1, 'datatype': 0, 'min_s': 0, 'max_s': 0, 'min_u': 0, 'max_u': 0, 'is_internal': False, 'behavior': 0}
                    self._inventory = inventory
                    self._dp_metadata = build_dp_metadata(inventory)
                    for dp_id in self._discovered_non_inventory_dpids:
                        self._register_runtime_dp_id(dp_id)
                    raw_cache_payload = cached.get('raw_cache', {})
                    parsed_raw_cache: dict[int | tuple[int, int], bytes] = {}
                    if isinstance(raw_cache_payload, dict):
                        for raw_key, raw_hex in raw_cache_payload.items():
                            if not isinstance(raw_hex, str):
                                continue
                            try:
                                parsed_raw_cache[self._deserialize_data_cache_key(str(raw_key))] = bytes.fromhex(raw_hex)
                            except ValueError:
                                continue
                    self._raw_cache = parsed_raw_cache
                    data_payload = cached.get('data', {})
                    parsed_data: dict[int | tuple[int, int], Any] = {}
                    if isinstance(data_payload, dict):
                        for raw_key, value in data_payload.items():
                            try:
                                parsed_data[self._deserialize_data_cache_key(str(raw_key))] = value
                            except ValueError:
                                continue
                    if parsed_data:
                        self.async_set_updated_data(parsed_data)
                    loaded_any = True
        if self.use_gatt:
            gatt_chars_payload = cached.get('gatt_characteristics', {})
            parsed_chars: dict[str, RuntimeGattCharacteristic] = {}
            if isinstance(gatt_chars_payload, dict):
                for uuid, payload in gatt_chars_payload.items():
                    if not isinstance(payload, dict):
                        continue
                    try:
                        parsed_chars[str(uuid).lower()] = RuntimeGattCharacteristic(
                            uuid=str(payload['uuid']).lower(),
                            service_uuid=str(payload['service_uuid']).lower(),
                            service_name=str(payload['service_name']),
                            key=str(payload['key']),
                            name=str(payload['name']),
                            source=str(payload['source']),
                            decoder=str(payload['decoder']),
                            properties=tuple(payload.get('properties', ())),
                            descriptors=tuple(payload.get('descriptors', ())),
                            readable=bool(payload.get('readable', False)),
                            writable=bool(payload.get('writable', False)),
                            notifiable=bool(payload.get('notifiable', False)),
                            indicatable=bool(payload.get('indicatable', False)),
                            entity_registry_enabled_default=bool(payload.get('entity_registry_enabled_default', True)),
                            hidden=bool(payload.get('hidden', False)),
                        )
                    except KeyError:
                        continue
            if parsed_chars:
                self._gatt_characteristics = parsed_chars
                gatt_raw_payload = cached.get('gatt_raw_values', {})
                if isinstance(gatt_raw_payload, dict):
                    parsed_gatt_raw: dict[str, bytes] = {}
                    for uuid, raw_hex in gatt_raw_payload.items():
                        if not isinstance(raw_hex, str):
                            continue
                        try:
                            parsed_gatt_raw[str(uuid).lower()] = bytes.fromhex(raw_hex)
                        except ValueError:
                            continue
                    self._gatt_raw_values = parsed_gatt_raw
                gatt_decoded_payload = cached.get('gatt_decoded_values', {})
                if isinstance(gatt_decoded_payload, dict):
                    self._gatt_decoded_values = {str(uuid).lower(): value for uuid, value in gatt_decoded_payload.items()}
                loaded_any = True
        self._startup_cache_loaded = loaded_any

    async def _async_save_state_cache(self) -> None:
        if not self.use_dpids and not self.use_gatt:
            return
        inventory_payload = {}
        if self._inventory is not None:
            inventory_payload = {str(dp_id): dict(inv_entry) for dp_id, inv_entry in self._inventory.items()}
        data_payload: dict[str, Any] = {}
        if self.data:
            data_payload = {self._serialize_data_cache_key(key): self._json_safe(value) for key, value in self.data.items()}
        raw_cache_payload = {self._serialize_data_cache_key(key): value.hex() for key, value in self._raw_cache.items()}
        gatt_chars_payload = {
            uuid: {
                'uuid': runtime_char.uuid,
                'service_uuid': runtime_char.service_uuid,
                'service_name': runtime_char.service_name,
                'key': runtime_char.key,
                'name': runtime_char.name,
                'source': runtime_char.source,
                'decoder': runtime_char.decoder,
                'properties': list(runtime_char.properties),
                'descriptors': list(runtime_char.descriptors),
                'readable': runtime_char.readable,
                'writable': runtime_char.writable,
                'notifiable': runtime_char.notifiable,
                'indicatable': runtime_char.indicatable,
                'entity_registry_enabled_default': runtime_char.entity_registry_enabled_default,
                'hidden': runtime_char.hidden,
            } for uuid, runtime_char in self._gatt_characteristics.items()
        }
        gatt_raw_payload = {uuid: value.hex() for uuid, value in self._gatt_raw_values.items()}
        gatt_decoded_payload = {uuid: self._json_safe(value) for uuid, value in self._gatt_decoded_values.items()}
        await self._state_store.async_save({'inventory': inventory_payload, 'data': data_payload, 'raw_cache': raw_cache_payload, 'gatt_characteristics': gatt_chars_payload, 'gatt_raw_values': gatt_raw_payload, 'gatt_decoded_values': gatt_decoded_payload})

    def _candidate_read_targets(self, dp_id: int) -> tuple[int | None, ...]:
        meta = self.get_dp_metadata(dp_id)
        if meta is None:
            return (None,)
        candidates: list[int | None] = [None]
        if meta.instance > 0:
            upper_bound = min(meta.instance, 32)
            candidates.extend(range(0, upper_bound + 1))
        deduped: list[int | None] = []
        seen: set[int | None] = set()
        for candidate in candidates:
            if candidate in seen:
                continue
            seen.add(candidate)
            deduped.append(candidate)
        return tuple(deduped)

    async def _discover_read_targets(self, client: Ble20Client, dp_id: int) -> tuple[int | None, ...]:
        successful: list[int | None] = []
        for instance in self._candidate_read_targets(dp_id):
            try:
                await client.read(dp_id, instance=instance)
                successful.append(instance)
            except Exception:
                continue
        return tuple(successful)

    @property
    def supported_dp_ids(self) -> set[int]:
        if self._inventory is None:
            return set()
        supported = {int(dp_id) for dp_id in self._inventory.keys() if int(dp_id) not in HIDDEN_DP_IDS}
        supported.update(self._discovered_non_inventory_dpids)
        return supported

    @property
    def dp_metadata(self) -> dict[int, DpMetadata]:
        return self._dp_metadata

    def get_dp_metadata(self, dp_id: int | DpId | None) -> DpMetadata | None:
        if dp_id is None:
            return None
        return self._dp_metadata.get(int(dp_id))

    @property
    def gatt_characteristics(self) -> dict[str, RuntimeGattCharacteristic]:
        return self._gatt_characteristics

    def get_gatt_characteristic(self, uuid: str) -> RuntimeGattCharacteristic | None:
        return self._gatt_characteristics.get(str(uuid).lower())

    @property
    def gatt_decoded_values(self) -> dict[str, Any]:
        return self._gatt_decoded_values

    @property
    def gatt_raw_values(self) -> dict[str, bytes]:
        return self._gatt_raw_values

    async def _refresh_known_gatt_state(self, connector: BluetoothLeConnector) -> None:
        services = connector.get_services()
        if not services:
            return
        self._gatt_characteristics = discover_known_gatt_characteristics(services)
        present_uuids = set(self._gatt_characteristics)
        self._gatt_raw_values = {uuid: value for (uuid, value) in self._gatt_raw_values.items() if uuid in present_uuids}
        self._gatt_decoded_values = {uuid: value for (uuid, value) in self._gatt_decoded_values.items() if uuid in present_uuids}
        for (uuid, runtime_char) in self._gatt_characteristics.items():
            if not runtime_char.readable:
                continue
            try:
                raw_value = await connector.read_characteristic(uuid)
            except Exception as err:
                _LOGGER.debug('Failed to read GATT characteristic %s: %s', uuid, err)
                continue
            self._gatt_raw_values[uuid] = raw_value
            self._gatt_decoded_values[uuid] = decode_known_gatt_value(runtime_char, raw_value)
        await self._async_save_state_cache()

    def instance_count_for_dp_id(self, dp_id: int) -> int:
        data = self.data or {}
        return sum((1 for key in data if isinstance(key, tuple) and len(key) == 2 and (int(key[0]) == int(dp_id))))

    def should_expose_data_key_as_entity(self, data_key: Any) -> bool:
        dp_id = int(data_key[0] if isinstance(data_key, tuple) else data_key)
        if dp_id in self._configured_exclude_dpids:
            return False
        if not isinstance(data_key, tuple) or len(data_key) != 2:
            return True
        if self._expose_large_instance_groups:
            return True
        return self.instance_count_for_dp_id(dp_id) <= self._max_instances_per_dpid_group

    def should_expose_dp_id_as_entity(self, dp_id: int | DpId) -> bool:
        return int(dp_id) not in self._configured_exclude_dpids

    @property
    def ble_connected(self) -> bool:
        return self._active_connector is not None

    def _set_update_interval(self, interval: timedelta | None) -> None:
        if hasattr(self, 'async_set_update_interval'):
            self.async_set_update_interval(interval)
        else:
            self.update_interval = interval

    async def async_enable_connection(self) -> None:
        self.poll_enabled = True
        self._connection_enabled_event.set()
        self._set_update_interval(self._poll_interval)

    async def async_disable_connection(self) -> None:
        self.poll_enabled = False
        self._connection_enabled_event.clear()
        self._set_update_interval(None)
        await self._clean_disconnect()

    async def _async_update_data(self) -> dict[int, Any]:
        if not self.poll_enabled:
            _LOGGER.debug('Polling skipped because Connection switch is off.')
            return self.data or {}
        async with self._ble_lock:
            if self._active_connector is not None:
                _LOGGER.debug('Using active persistent BLE connection to read sensors')
                try:
                    if self.use_dpids and self._active_client is not None:
                        data = await self._read_all_supported(self._active_client)
                        self._integration_ready = True
                        return data
                    if self.use_gatt:
                        await self._refresh_known_gatt_state(self._active_connector)
                        self._integration_ready = True
                        return self.data or {}
                except Exception as err:
                    _LOGGER.warning('Failed to read over persistent connection, disconnecting: %s', err)
                    await self._clean_disconnect()
                    _LOGGER.warning('Returning cached data, will reconnect in background')
                    return self.data or {}
            connector = self._make_connector()
            try:
                await connector.connect_async(self._device_id)
                if self.use_dpids:
                    if not connector.arendi_handshake_done:
                        _LOGGER.warning('Arendi security handshake failed, returning cached data')
                        return self.data or {}
                    client = Ble20Client(connector)
                    if self._inventory is None:
                        await self._initialize_inventory(client)
                        self._capabilities = await client.capabilities()
                        await client.event_storage_inventory(self._capabilities)
                    await client.join(pin=self._pin, inv=self._inventory)
                    data = await self._read_all_supported(client)
                    self._integration_ready = True
                    return data
                if self.use_gatt:
                    await self._refresh_known_gatt_state(connector)
                    self._integration_ready = True
                return self.data or {}
            except Exception as err:
                _LOGGER.warning('Error polling Geberit Toilet device: %s — returning cached data', err)
                return self.data or {}
            finally:
                try:
                    await connector.disconnect()
                except Exception:
                    pass

    async def _read_all_supported(self, client: Ble20Client) -> dict[int, Any]:
        if self.use_gatt:
            await self._refresh_known_gatt_state(client._connector)
        if DpId.DP_LOCAL_TIME in self._inventory and DpId.DP_SET_RTC_TIME in self._inventory:
            try:
                local_time_bytes = await client.read(DpId.DP_LOCAL_TIME)
                wc_local_ts = int.from_bytes(local_time_bytes, byteorder='little')
                offset_seconds = 0
                if DpId.DP_TIME_ZONE_OFFSET in self._inventory:
                    tz_val = await client.read(DpId.DP_TIME_ZONE_OFFSET)
                    offset_seconds = int.from_bytes(tz_val, byteorder='little')
                    if offset_seconds > 2147483647:
                        offset_seconds -= 4294967296
                dst_active = 0
                if DpId.DP_TIME_DAYLIGHT_SAVING in self._inventory:
                    dst_val = await client.read(DpId.DP_TIME_DAYLIGHT_SAVING)
                    dst_active = int.from_bytes(dst_val, byteorder='little')
                total_offset = offset_seconds + (3600 if dst_active == 1 else 0)
                current_ts = int(time.time())
                expected_wc_local_ts = current_ts + total_offset
                if abs(wc_local_ts - expected_wc_local_ts) > 60:
                    corrected_ts = current_ts - total_offset
                    _LOGGER.info('Syncing Geberit Toilet time. Clock local: %s, Expected local: %s', wc_local_ts, expected_wc_local_ts)
                    await client.write(DpId.DP_SET_RTC_TIME, corrected_ts.to_bytes(4, byteorder='little'))
            except Exception as time_err:
                _LOGGER.debug('Failed to auto-sync time: %s', time_err)
        data: dict[Any, Any] = {}
        supported_set = self.supported_dp_ids
        read_candidates = set(supported_set)
        if self._request_data_mode == REQUEST_DATA_MODE_ALL_KNOWN and (not self._all_known_scan_completed):
            read_candidates.update(self.known_dp_ids)
        for dp_id in sorted(read_candidates):
            dp_name = getattr(dp_id, 'name', str(dp_id))
            read_targets = self._read_targets.get(dp_id)
            if read_targets is None:
                discovered_targets = await self._discover_read_targets(client, dp_id)
                if discovered_targets or dp_id not in supported_set:
                    self._read_targets[dp_id] = discovered_targets
                    self._discovery_cache_dirty = True
                read_targets = discovered_targets or ((None,) if dp_id in supported_set else ())
            read_any = False
            for instance in read_targets:
                try:
                    val_bytes = await client.read(dp_id, instance=instance)
                    data_key: Any = dp_id if instance is None else (dp_id, instance)
                    self._raw_cache[data_key] = val_bytes
                    decoded = decode_value(dp_id, val_bytes)
                    data[data_key] = decoded
                    read_any = True
                    _LOGGER.debug('Read DpId %s (%s) instance=%s SUCCESS decoded=%r', dp_name, dp_id, instance, decoded)
                except Exception as ex:
                    _LOGGER.debug('Failed to read DpId %s (%s) instance=%s: %s', dp_name, dp_id, instance, ex)
            if read_any and dp_id not in supported_set:
                self._discovered_non_inventory_dpids.add(dp_id)
                self._register_runtime_dp_id(dp_id)
                self._discovery_cache_dirty = True
        if self._request_data_mode == REQUEST_DATA_MODE_ALL_KNOWN and (not self._all_known_scan_completed):
            self._all_known_scan_completed = True
            self._discovery_cache_dirty = True
        await self._async_save_discovery_cache()
        await self._async_save_state_cache()
        return data

    async def _connection_loop(self) -> None:
        await asyncio.sleep(5.0)
        while True:
            try:
                if not self.poll_enabled:
                    if self._active_connector is not None:
                        _LOGGER.info('Connection switch turned off, closing persistent BLE connection')
                        await self._clean_disconnect()
                    await self._connection_enabled_event.wait()
                    continue
                if self._active_connector is not None:
                    if self.use_dpids and self._listener_tasks and all((t.done() for t in self._listener_tasks)):
                        _LOGGER.info('All notification listeners stopped, reconnecting...')
                        await self._clean_disconnect()
                    else:
                        await asyncio.sleep(1.0)
                    continue
                _LOGGER.info('Attempting to establish persistent BLE connection to Geberit Toilet...')
                async with self._ble_lock:
                    connector = self._make_connector()
                    try:
                        await connector.connect_async(self._device_id)
                        self._active_connector = connector
                        if self.use_dpids:
                            if not connector.arendi_handshake_done:
                                raise Exception('Arendi security handshake failed')
                            client = Ble20Client(connector)
                            if self._inventory is None:
                                await self._initialize_inventory(client)
                                self._capabilities = await client.capabilities()
                                await client.event_storage_inventory(self._capabilities)
                            await client.join(pin=self._pin, inv=self._inventory)
                            data = await self._read_all_supported(client)
                            self.async_set_updated_data(data)
                            self._integration_ready = True
                            to_subscribe = sorted((dp_id for (dp_id, meta) in self._dp_metadata.items() if meta.notifiable and meta.subscribe_notifications and meta.readable and (not meta.hidden) and (meta.instance == 0)))
                            subscribed = []
                            for nid in to_subscribe:
                                try:
                                    await client.enable_notification([nid])
                                    if nid in client._notify_queues:
                                        subscribed.append(nid)
                                    else:
                                        _LOGGER.debug('Notification subscription rejected by device for DpId %d, skipping', nid)
                                except Exception as sub_err:
                                    _LOGGER.debug('Failed to subscribe notification for DpId %d: %s', nid, sub_err)
                            self._active_client = client
                            for nid in subscribed:
                                task = asyncio.create_task(self._listen_notifications(client, nid))
                                self._listener_tasks.append(task)
                            _LOGGER.info('Persistent BLE connection established, subscribed to %d/%d notifications: %s', len(subscribed), len(to_subscribe), subscribed)
                        else:
                            if self.use_gatt:
                                await self._refresh_known_gatt_state(connector)
                            self._active_client = None
                            self._integration_ready = True
                            self.async_set_updated_data(self.data or {})
                            _LOGGER.info('Persistent BLE connection established in %s mode without Ble20 notifications', self._communication_mode)
                    except Exception:
                        try:
                            await connector.disconnect()
                        except Exception:
                            pass
                        raise
            except Exception as err:
                _LOGGER.warning('Error in persistent BLE connection loop: %s', err)
                await self._clean_disconnect()
                await asyncio.sleep(10.0)

    async def _listen_notifications(self, client: Ble20Client, dp_id: int) -> None:
        try:
            while True:
                val_bytes = await client.get_notification(dp_id, timeout=3600)
                decoded = decode_value(dp_id, val_bytes)
                _LOGGER.debug('Notification received: DpId %d -> %s', dp_id, decoded)
                self._raw_cache[dp_id] = val_bytes
                new_data = dict(self.data) if self.data else {}
                new_data[dp_id] = decoded
                self.async_set_updated_data(new_data)
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            _LOGGER.warning('Notification listener for DpId %d stopped: %s', dp_id, ex)

    async def _clean_disconnect(self) -> None:
        for task in self._listener_tasks:
            task.cancel()
        if self._listener_tasks:
            await asyncio.gather(*self._listener_tasks, return_exceptions=True)
            self._listener_tasks.clear()
        self._active_client = None
        if self._active_connector is not None:
            try:
                await self._active_connector.disconnect()
            except Exception:
                pass
            self._active_connector = None

    async def async_write_dp(self, dp_id: int, value: Any, instance: int=0) -> None:
        if not self.poll_enabled:
            raise UpdateFailed('Connection switch is off; BLE connection is fully released and writes are disabled')
        raw_val = self.encode_value(dp_id, value)
        async with self._ble_lock:
            if self._active_client is not None:
                try:
                    await self._active_client.write(dp_id, raw_val, instance=instance)
                    self._raw_cache[dp_id] = raw_val
                    new_data = dict(self.data) if self.data else {}
                    new_data[dp_id] = value
                    self.async_set_updated_data(new_data)
                    _LOGGER.info('Wrote DpId %d value: %s (via persistent connection)', dp_id, value)
                    return
                except Exception as err:
                    _LOGGER.warning('Failed to write over persistent connection, disconnecting: %s', err)
                    await self._clean_disconnect()
            connector = self._make_connector()
            try:
                await connector.connect_async(self._device_id)
                client = Ble20Client(connector)
                if self._inventory is None:
                    await self._initialize_inventory(client)
                await client.join(pin=self._pin, inv=self._inventory)
                await client.write(dp_id, raw_val, instance=instance)
                self._raw_cache[dp_id] = raw_val
                new_data = dict(self.data) if self.data else {}
                new_data[dp_id] = value
                self.async_set_updated_data(new_data)
                _LOGGER.info('Wrote DpId %d value: %s (via temporary connection)', dp_id, value)
            except Exception as err:
                _LOGGER.error('Failed to write DpId %d: %s', dp_id, err)
                raise UpdateFailed(f'Failed to write DpId {dp_id}: {err}') from err
            finally:
                try:
                    await connector.disconnect()
                except Exception:
                    pass

    async def async_close(self) -> None:
        if self._connection_loop_task is not None:
            self._connection_loop_task.cancel()
            try:
                await self._connection_loop_task
            except asyncio.CancelledError:
                pass
        await self._clean_disconnect()
