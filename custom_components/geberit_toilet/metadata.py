from __future__ import annotations
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import PERCENTAGE, UnitOfTime
from homeassistant.helpers.entity import EntityCategory
from .protocol.DpBehavior import DpBehavior
from .protocol.DpId import DpId
from .protocol.DpType import DpType

class EntityKind(str, Enum):
    SENSOR = 'sensor'
    BINARY_SENSOR = 'binary_sensor'
    NUMBER = 'number'
    SELECT = 'select'
    SWITCH = 'switch'
    BUTTON = 'button'
    UNKNOWN = 'unknown'
HIDDEN_DP_IDS: frozenset[int] = frozenset({83})
METADATA_OVERRIDES: dict[int, dict[str, Any]] = {int(DpId.DP_LED_COLOR): {'options': ['blue', 'turquoise', 'magenta', 'orange', 'yellow', 'red', 'white']}, int(DpId.DP_ODOUR_EXTRACTION_FILTER_CHANGE): {'button': True}}

def _load_translation_payload_sync(language: str) -> dict[str, Any]:
    for candidate in (language, 'en'):
        path = Path(__file__).with_name('translations') / f'{candidate}.json'
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            continue
    return {}

def load_metadata_name_translations_sync(language: str) -> dict[str, str]:
    payload = _load_translation_payload_sync(language)
    lookup = payload.get('lookup', {})
    names = lookup.get('metadata_names', {})
    return {str(key): str(value) for (key, value) in names.items() if value}

@dataclass(frozen=True)
class DpMetadata:
    dp_id: int
    name: str
    key: str
    datatype: DpType | None
    behavior: DpBehavior | None
    min_value: int | None
    max_value: int | None
    readable: bool
    writable: bool
    notifiable: bool
    instance: int
    version: int
    options: tuple[str, ...] = ()
    binary_sensor_device_class: BinarySensorDeviceClass | None = None
    button: bool = False
    hidden: bool = False
    entity_category: EntityCategory | None = None
    entity_registry_enabled_default: bool = True
    subscribe_notifications: bool = True

    @property
    def is_boolean(self) -> bool:
        return self.datatype in (DpType.Binary, DpType.OffOn)

    @property
    def is_select(self) -> bool:
        return self.datatype in (DpType.Enum, DpType.OffOnAuto)

    @property
    def unit(self) -> str | None:
        if self.datatype == DpType.Seconds:
            return UnitOfTime.SECONDS
        if self.datatype == DpType.Minutes:
            return UnitOfTime.MINUTES
        if self.datatype == DpType.Hours:
            return UnitOfTime.HOURS
        if self.datatype == DpType.Percent:
            return PERCENTAGE
        if self.datatype == DpType.Permill:
            return 'permille'
        return None

    @property
    def sensor_device_class(self) -> SensorDeviceClass | None:
        if self.datatype in (DpType.Seconds, DpType.Minutes, DpType.Hours):
            return SensorDeviceClass.DURATION
        if self.datatype in (DpType.TimeStampUtc, DpType.TimeStampLocal):
            return SensorDeviceClass.TIMESTAMP
        if self.datatype == DpType.Percent:
            return None
        return None

    @property
    def sensor_state_class(self) -> SensorStateClass | None:
        if self.datatype in (DpType.Seconds, DpType.Minutes, DpType.Hours, DpType.Percent, DpType.Permill, DpType.Signed, DpType.Counter):
            return SensorStateClass.MEASUREMENT
        return None

    @property
    def preferred_kind(self) -> EntityKind:
        if self.button:
            return EntityKind.BUTTON
        if self.behavior in (DpBehavior.Command, DpBehavior.CommandLocked):
            return EntityKind.BUTTON
        if self.is_select and self.writable:
            return EntityKind.SELECT
        if self.is_boolean and self.writable:
            return EntityKind.SWITCH
        if self.is_boolean and self.readable:
            return EntityKind.BINARY_SENSOR
        if self.writable and self.datatype not in (None, DpType.String, DpType.TimeStampUtc, DpType.TimeStampLocal):
            return EntityKind.NUMBER
        if self.readable:
            return EntityKind.SENSOR
        return EntityKind.UNKNOWN

    def options_for_select(self) -> tuple[str, ...]:
        if self.options:
            return self.options
        if self.datatype == DpType.OffOnAuto:
            return ('off', 'on', 'auto')
        if self.datatype == DpType.Enum and self.min_value is not None and (self.max_value is not None):
            return tuple((str(i) for i in range(self.min_value, self.max_value + 1)))
        return ()

def _to_dp_type(value: Any) -> DpType | None:
    try:
        return DpType(int(value))
    except (TypeError, ValueError):
        return None

def _to_dp_behavior(value: Any) -> DpBehavior | None:
    try:
        return DpBehavior(int(value))
    except (TypeError, ValueError):
        return None

def default_key(dp_id: int) -> str:
    try:
        enum_value = DpId(dp_id)
        return enum_value.name.lower().removeprefix('dp_')
    except ValueError:
        return f'dpid_{dp_id}'

def default_name_from_key(key: str) -> str:
    return key.replace('_', ' ').title()

def _safe_int(value: Any, default: int=0) -> int:
    try:
        if value is None:
            return default
        return int(value)
    except (TypeError, ValueError):
        return default

def _default_subscribe_notifications(key: str, datatype: DpType | None, behavior: DpBehavior | None) -> bool:
    if datatype not in (DpType.TimeStampUtc, DpType.TimeStampLocal):
        return True
    if behavior != DpBehavior.Status:
        return True
    lowered = key.lower()
    clock_like_tokens = ('time', 'clock', 'rtc', 'local', 'utc')
    if not any((token in lowered for token in clock_like_tokens)):
        return True
    stable_event_tokens = ('backup', 'installation', 'production', 'change_over', 'moment', 'timestamp', 'date')
    if any((token in lowered for token in stable_event_tokens)):
        return True
    return False

def _default_binary_sensor_device_class(key: str, datatype: DpType | None, behavior: DpBehavior | None) -> BinarySensorDeviceClass | None:
    if datatype not in (DpType.Binary, DpType.OffOn):
        return None
    if behavior not in (DpBehavior.Info, DpBehavior.Status, DpBehavior.Nvm, DpBehavior.Protected):
        return None
    lowered = key.lower()
    if 'door' in lowered:
        return BinarySensorDeviceClass.DOOR
    if 'power_supply' in lowered or lowered == 'power_supply':
        return BinarySensorDeviceClass.PLUG
    if 'sensor_move' in lowered or 'motion' in lowered:
        return BinarySensorDeviceClass.MOTION
    if any((token in lowered for token in ('error', 'fault', 'alarm', 'change', 'disabled'))):
        return BinarySensorDeviceClass.PROBLEM
    return None

def _default_entity_category(key: str, behavior: DpBehavior | None, writable: bool) -> EntityCategory | None:
    if behavior in (DpBehavior.Command, DpBehavior.CommandLocked):
        return None
    if writable:
        return None
    lowered = key.lower()
    diagnostic_tokens = ('serial', 'version', 'production', 'installation', 'sap', 'watchdog', 'fatal', 'quartz', 'gbus', 'idc', 'hash', 'loader', 'wireless_stack', 'statistic', 'counter', 'backup', 'rtc', 'offset', 'reserve', 'information')
    if any((token in lowered for token in diagnostic_tokens)):
        return EntityCategory.DIAGNOSTIC
    return None

def build_dp_metadata(inventory: dict[int, dict[str, Any]] | None) -> dict[int, DpMetadata]:
    if not inventory:
        return {}
    metadata: dict[int, DpMetadata] = {}
    for (raw_dp_id, inv_entry) in inventory.items():
        dp_id = int(raw_dp_id)
        override = METADATA_OVERRIDES.get(dp_id, {})
        datatype = _to_dp_type(inv_entry.get('datatype'))
        behavior = _to_dp_behavior(inv_entry.get('behavior'))
        min_value = inv_entry.get('min_s')
        max_value = inv_entry.get('max_s')
        if datatype not in (DpType.Signed, DpType.String, DpType.TimeStampUtc, DpType.TimeStampLocal):
            min_value = inv_entry.get('min_u')
            max_value = inv_entry.get('max_u')
        readable = behavior in (DpBehavior.Info, DpBehavior.Status, DpBehavior.Nvm, DpBehavior.Protected)
        writable = behavior in (DpBehavior.Command, DpBehavior.Nvm, DpBehavior.Protected, DpBehavior.CommandLocked)
        notifiable = behavior == DpBehavior.Status
        key = str(inv_entry.get('key') or override.get('key') or default_key(dp_id))
        metadata_name = inv_entry.get('metadata_name') or inv_entry.get('name')
        if metadata_name is not None:
            metadata_name = str(metadata_name).strip()
        if not metadata_name:
            metadata_name = override.get('name') or default_name_from_key(key)
        entity_category = override.get('entity_category')
        if entity_category is None:
            entity_category = _default_entity_category(key, behavior, writable)
        metadata[dp_id] = DpMetadata(dp_id=dp_id, name=metadata_name, key=key, datatype=datatype, behavior=behavior, min_value=int(min_value) if min_value is not None else None, max_value=int(max_value) if max_value is not None else None, readable=readable, writable=writable, notifiable=notifiable, instance=_safe_int(inv_entry.get('instance'), 0), version=_safe_int(inv_entry.get('version'), 0), options=tuple(override.get('options', ())), binary_sensor_device_class=override.get('binary_sensor_device_class', _default_binary_sensor_device_class(key, datatype, behavior)), button=bool(override.get('button', False)), hidden=dp_id in HIDDEN_DP_IDS or bool(override.get('hidden', False)), entity_category=entity_category, entity_registry_enabled_default=bool(override.get('entity_registry_enabled_default', True)), subscribe_notifications=bool(override.get('subscribe_notifications', _default_subscribe_notifications(key, datatype, behavior))))
    return metadata

def metadata_value_to_native(meta: DpMetadata, value: Any) -> Any:
    if value is None:
        return None
    if meta.datatype in (DpType.TimeStampUtc, DpType.TimeStampLocal):
        try:
            return datetime.fromtimestamp(int(value), timezone.utc)
        except (TypeError, ValueError, OverflowError):
            return None
    if meta.datatype == DpType.Enum and meta.options:
        try:
            idx = int(value)
        except (TypeError, ValueError):
            return value
        if 0 <= idx < len(meta.options):
            return meta.options[idx]
    return value
