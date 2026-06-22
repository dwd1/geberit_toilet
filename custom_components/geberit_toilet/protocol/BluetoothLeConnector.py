import asyncio
import time
from bleak import BleakClient, BleakScanner, BleakError
from bleak.backends.scanner import AdvertisementData
from bleak.backends.device import BLEDevice
from uuid import UUID
from binascii import hexlify
import logging
from .EventHandler import EventHandler
from typing import Dict, Callable, Any
from ..const import CCC_DESCRIPTOR_UUID, DIS_SERVICE_UUID, STANDARD_GEBERIT_SERVICE_UUID
logger = logging.getLogger(__name__)

class ESPHomeConnectionError(Exception):

    def __init__(self, message: str, timeout: bool=False):
        super().__init__(message)
        self.timeout = timeout

class ESPHomeDeviceNotFoundError(Exception):
    pass

class IBluetoothLeConnector:
    pass

class BluetoothLeConnector(IBluetoothLeConnector):
    SERVICE_UUID = UUID(STANDARD_GEBERIT_SERVICE_UUID)
    BULK_CHAR_BULK_WRITE_0_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a13e0000')
    BULK_CHAR_BULK_WRITE_1_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a23e0000')
    BULK_CHAR_BULK_WRITE_2_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a33e0000')
    BULK_CHAR_BULK_WRITE_3_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a43e0000')
    BULK_CHAR_BULK_READ_0_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a53e0000')
    BULK_CHAR_BULK_READ_1_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a63e0000')
    BULK_CHAR_BULK_READ_2_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a73e0000')
    BULK_CHAR_BULK_READ_3_UUID = UUID('3334429d-90f3-4c41-a02d-5cb3a83e0000')
    CCC_UUID = UUID(CCC_DESCRIPTOR_UUID)
    SCAN_TIMEOUT_S: float = 10.0

    def __init__(self, esphome_host=None, esphome_port=6053, esphome_noise_psk=None, hass=None):
        self.client = None
        self.read_characteristics = {}
        self.data_received_handlers = EventHandler()
        self.data_received = None
        self.connection_status_changed_handlers = EventHandler()
        self.device_address = 'Unknown'
        self.device_name = 'Unknown'
        self.esphome_host = esphome_host
        self.esphome_port = esphome_port
        self.esphome_noise_psk = esphome_noise_psk
        self.esphome_proxy_name = None
        self.esphome_proxy_connected = False
        self.last_esphome_api_ms: int | None = None
        self._esphome_unsub_adv = None
        self.last_ble_ms: int | None = None
        self._esphome_api = None
        self._esphome_feature_flags = 0
        self.rssi: int | None = None
        self.esphome_wifi_rssi: float | None = None
        self.esphome_free_heap: int | None = None
        self.esphome_max_free_block: int | None = None
        self._esphome_wifi_key: int | None = None
        self._esphome_free_heap_key: int | None = None
        self._esphome_max_free_block_key: int | None = None
        self._hass = hass
        self._subscribed_characteristics: list = []
        self.ble_dis_info: dict | None = None
        self.is_variant_a: bool = False
        self._arendi_security = None
        self._arendi_raw_write = None

    @property
    def arendi_handshake_done(self) -> bool:
        return self._arendi_security is not None and self._arendi_security.handshake_done

    async def connect_async(self, device_id):
        logger.debug('BluetoothLeConnector: connect')
        if self.esphome_host:
            await self._connect_via_esphome(device_id)
        else:
            await self._connect_local(device_id)

    async def _connect_local(self, device_id):
        t0 = time.perf_counter()
        if self._hass is not None:
            device = await self._get_ble_device_via_ha(device_id)
            if device is None:
                raise BleakError(f'GeberitToilet device {device_id} not found by HA bluetooth scanner.')
            self.device_address = device.address
            self.device_name = device.name or 'Unknown'
            logger.debug(f'[HA-BLE] Connecting: address={device.address}, name={self.device_name}, rssi={self.rssi}')
            try:
                from bleak_retry_connector import establish_connection
                self.client = await establish_connection(BleakClient, device, device.name or device_id, disconnected_callback=self._on_disconnected)
            except ImportError:
                self.client = BleakClient(device, disconnected_callback=self._on_disconnected)
                await self.client.connect()
        else:
            device = await BleakScanner.find_device_by_address(device_id)
            if device is not None:
                self.device_address = device.address
                self.device_name = device.name
                self.rssi = getattr(device, 'rssi', None)
                logger.debug(f'device.address: {device.address}, device.name: {device.name}, rssi: {self.rssi}')
                self.client = BleakClient(address_or_ble_device=device, disconnected_callback=self._on_disconnected)
            else:
                logger.warning(f'BLE scan did not find {device_id} advertising — attempting direct connect by MAC address')
                self.device_address = device_id
                self.device_name = device_id
                self.rssi = None
                self.client = BleakClient(device_id, disconnected_callback=self._on_disconnected)
            await self.client.connect()
        self.last_esphome_api_ms = None
        self.last_ble_ms = int((time.perf_counter() - t0) * 1000)
        await self._post_connect()

    async def _get_ble_device_via_ha(self, device_id: str):
        from homeassistant.components import bluetooth
        from homeassistant.core import callback as ha_callback
        address = device_id.upper()
        service_info = bluetooth.async_last_service_info(self._hass, address, connectable=True)
        if service_info is not None:
            logger.debug(f'[HA-BLE] Device {address} found in HA bluetooth cache immediately')
            self.rssi = service_info.rssi
            return service_info.device
        logger.debug(f'[HA-BLE] Device {address} not in cache yet; waiting up to 30s for advertisement')
        found_event = asyncio.Event()
        found_device: list[BLEDevice | None] = [None]
        found_rssi: list[int | None] = [None]

        @ha_callback
        def _on_advertisement(service_info, change) -> None:
            found_device[0] = service_info.device
            found_rssi[0] = service_info.rssi
            found_event.set()
        cancel = bluetooth.async_register_callback(self._hass, _on_advertisement, {'address': address}, bluetooth.BluetoothScanningMode.ACTIVE)
        try:
            await asyncio.wait_for(found_event.wait(), timeout=30.0)
            self.rssi = found_rssi[0]
            logger.debug(f"[HA-BLE] Device {address} seen by HA scanner: {getattr(found_device[0], 'name', 'Unknown')}")
            return found_device[0]
        except asyncio.TimeoutError:
            logger.warning(f'[HA-BLE] Device {address} not seen by HA bluetooth scanner within 30s. Ensure the toilet is powered on and within BLE range.')
            return None
        finally:
            cancel()

    async def _ensure_esphome_api_connected(self):
        from aioesphomeapi import APIClient
        if self._esphome_api is not None:
            if getattr(self._esphome_api, '_connection', None) is not None:
                logger.debug('Reusing existing ESP32 API connection')
                self.last_esphome_api_ms = 0
                return self._esphome_api
            logger.warning('ESP32 API connection lost (ping timeout?); clearing stale client and reconnecting')
            self._esphome_api = None
            self.esphome_proxy_connected = False
        t0 = time.perf_counter()
        api = APIClient(address=self.esphome_host, port=self.esphome_port, password='', noise_psk=self.esphome_noise_psk)
        try:
            await asyncio.wait_for(api.connect(login=True), timeout=10.0)
        except asyncio.TimeoutError:
            raise ESPHomeConnectionError(f'Timeout connecting to ESPHome proxy at {self.esphome_host}:{self.esphome_port}', timeout=True)
        except Exception as e:
            raise ESPHomeConnectionError(f'Failed to connect to ESPHome proxy at {self.esphome_host}: {e}', timeout=False)
        try:
            device_info = await asyncio.wait_for(api.device_info(), timeout=10.0)
            self._esphome_feature_flags = getattr(device_info, 'bluetooth_proxy_feature_flags', 0)
            self.esphome_proxy_name = getattr(device_info, 'name', 'unknown')
        except Exception as e:
            logger.warning(f'Failed to get device info, using default feature_flags=0: {e}')
            self._esphome_feature_flags = 0
            self.esphome_proxy_name = 'unknown'
        self._esphome_api = api
        self.esphome_proxy_connected = True
        self.last_esphome_api_ms = int((time.perf_counter() - t0) * 1000)
        logger.debug(f'ESP32 proxy connected: {self.esphome_proxy_name} ({self.last_esphome_api_ms} ms)')
        return api

    async def _read_esphome_wifi_rssi_async(self) -> None:
        api = self._esphome_api
        if api is None:
            return
        try:
            if self._esphome_wifi_key is None or self._esphome_free_heap_key is None or self._esphome_max_free_block_key is None:
                (entities, _) = await asyncio.wait_for(api.list_entities_services(), timeout=5.0)
                if self._esphome_wifi_key is None:
                    self._esphome_wifi_key = next((e.key for e in entities if getattr(e, 'unit_of_measurement', '') == 'dBm' and 'wifi' in getattr(e, 'object_id', '').lower()), -1)
                    if self._esphome_wifi_key == -1:
                        logger.debug('No wifi_signal sensor on ESP32 (add platform: wifi_signal to ESPHome YAML)')
                if self._esphome_free_heap_key is None:
                    self._esphome_free_heap_key = next((e.key for e in entities if 'heap' in getattr(e, 'object_id', '').lower()), -1)
                    if self._esphome_free_heap_key == -1:
                        logger.debug('No free heap sensor on ESP32 (add platform: debug with free: to ESPHome YAML)')
                if self._esphome_max_free_block_key is None:
                    self._esphome_max_free_block_key = next((e.key for e in entities if 'block' in getattr(e, 'object_id', '').lower()), -1)
                    if self._esphome_max_free_block_key == -1:
                        logger.debug('No max free block sensor on ESP32 (add platform: debug with block: to ESPHome YAML)')
            keys_to_read: dict[int, str] = {}
            if self._esphome_wifi_key != -1:
                keys_to_read[self._esphome_wifi_key] = 'wifi'
            if self._esphome_free_heap_key != -1:
                keys_to_read[self._esphome_free_heap_key] = 'heap'
            if self._esphome_max_free_block_key != -1:
                keys_to_read[self._esphome_max_free_block_key] = 'block'
            if not keys_to_read:
                return
            captured: dict[int, object] = {}
            all_received = asyncio.Event()

            def _on_state(state) -> None:
                key = getattr(state, 'key', None)
                if key in keys_to_read and key not in captured:
                    captured[key] = getattr(state, 'state', None)
                    if len(captured) >= len(keys_to_read):
                        all_received.set()
            unsub = api.subscribe_states(_on_state)
            try:
                await asyncio.wait_for(all_received.wait(), timeout=3.0)
            except asyncio.TimeoutError:
                logger.debug(f'Timeout reading ESP32 diagnostic sensors (got {len(captured)}/{len(keys_to_read)})')
            finally:
                try:
                    unsub()
                except Exception:
                    pass
            if self._esphome_wifi_key in captured and captured[self._esphome_wifi_key] is not None:
                self.esphome_wifi_rssi = round(float(captured[self._esphome_wifi_key]), 1)
                logger.debug(f'ESP32 WiFi RSSI: {self.esphome_wifi_rssi} dBm')
            if self._esphome_free_heap_key in captured and captured[self._esphome_free_heap_key] is not None:
                self.esphome_free_heap = int(float(captured[self._esphome_free_heap_key]))
                logger.debug(f'ESP32 Free Heap: {self.esphome_free_heap} B')
            if self._esphome_max_free_block_key in captured and captured[self._esphome_max_free_block_key] is not None:
                self.esphome_max_free_block = int(float(captured[self._esphome_max_free_block_key]))
                logger.debug(f'ESP32 Max Free Block: {self.esphome_max_free_block} B')
        except Exception as e:
            logger.debug(f'Failed to read ESP32 diagnostic sensors: {e}')

    async def _connect_via_esphome(self, device_id):
        from .ESPHomeAPIClient import ESPHomeAPIClient
        logger.debug(f'BluetoothLeConnector: connecting to BLE device via ESPHome proxy')
        if self._esphome_unsub_adv is not None:
            try:
                self._esphome_unsub_adv()
                logger.debug('Cleaned up leftover advertisement subscription before scan')
            except Exception as e:
                logger.debug(f'Advertisement unsubscribe (pre-scan cleanup): {e}')
            self._esphome_unsub_adv = None
        try:
            api = await self._ensure_esphome_api_connected()
        except ESPHomeConnectionError:
            self._esphome_api = None
            raise
        await self._read_esphome_wifi_rssi_async()
        t_ble = time.perf_counter()
        mac_int = int(device_id.replace(':', ''), 16)
        found_event = asyncio.Event()
        device_name = ''
        address_type = 0
        total_packets = 0
        seen_addresses: dict[int, int] = {}

        def on_raw_advertisements(resp):
            nonlocal device_name, address_type, total_packets
            total_packets += len(resp.advertisements)
            for adv in resp.advertisements:
                seen_addresses[adv.address] = seen_addresses.get(adv.address, 0) + 1
                if adv.address == mac_int:
                    device_name = self._parse_local_name(bytes(adv.data))
                    address_type = getattr(adv, 'address_type', 0)
                    self.rssi = getattr(adv, 'rssi', None)
                    found_event.set()
        logger.debug(f'Scanning for BLE device {device_id} (mac_int={mac_int:#014x})')
        unsub_adv = api.subscribe_bluetooth_le_raw_advertisements(on_raw_advertisements)
        self._esphome_unsub_adv = unsub_adv
        try:
            await asyncio.wait_for(found_event.wait(), timeout=self.SCAN_TIMEOUT_S)
            logger.debug(f"Found BLE device {device_id}: name={device_name or 'Unknown'}, address_type={address_type}")
        except asyncio.TimeoutError:
            unsub_adv()
            self._esphome_unsub_adv = None
            top = sorted(seen_addresses.items(), key=lambda x: -x[1])[:8]
            addr_strs = ', '.join((f'{a:#014x}({c})' for (a, c) in top))
            logger.warning(f'BLE scan timeout: target={mac_int:#014x}, unique_addresses={len(seen_addresses)}, top_seen=[{addr_strs}]')
            hint = 'scanner may be stuck or subscription slot in use' if total_packets == 0 else 'device not advertising'
            raise ESPHomeDeviceNotFoundError(f'GeberitToilet device {device_id} not found via ESPHome proxy at {self.esphome_host} (received {total_packets} total BLE advertisement packet(s) during {self.SCAN_TIMEOUT_S:.0f} s scan — {hint})')
        self.device_address = device_id
        self.device_name = device_name or 'Unknown'
        logger.debug(f'Creating ESPHomeAPIClient for {device_id} (address_type={address_type})')
        self.client = ESPHomeAPIClient(api, device_id, self._on_disconnected, address_type, self._esphome_feature_flags)
        try:
            await self.client.connect(timeout=30.0)
            logger.info(f'BLE connection successful with address_type={address_type}')
        except Exception as e:
            logger.warning(f'BLE connection failed with address_type={address_type}: {e}')
            unsub_adv()
            self._esphome_unsub_adv = None
            raise
        self.last_ble_ms = int((time.perf_counter() - t_ble) * 1000)
        logger.debug(f'BLE connect complete ({self.last_ble_ms} ms)')
        await self._post_connect()

    def _parse_local_name(self, data: bytes) -> str:
        i = 0
        name = ''
        while i < len(data):
            length = data[i]
            if length == 0 or i + length >= len(data):
                break
            ad_type = data[i + 1]
            value = data[i + 2:i + 1 + length]
            if ad_type == 9:
                return value.decode('utf-8', errors='replace')
            elif ad_type == 8:
                name = value.decode('utf-8', errors='replace')
            i += 1 + length
        return name

    def _apply_gatt_variant_overrides(self):
        from .GattDiscovery import classify_services
        try:
            profile = classify_services(self.client.services)
        except Exception:
            return
        if profile.is_standard or not profile.write_uuids or (not profile.notify_uuids):
            return
        write_uuid = UUID(profile.write_uuids[0])
        notify_uuid = UUID(profile.notify_uuids[0])
        self.SERVICE_UUID = UUID(profile.svc_uuid)
        self.BULK_CHAR_BULK_WRITE_0_UUID = write_uuid
        self.BULK_CHAR_BULK_WRITE_1_UUID = write_uuid
        self.BULK_CHAR_BULK_WRITE_2_UUID = write_uuid
        self.BULK_CHAR_BULK_WRITE_3_UUID = write_uuid
        self.BULK_CHAR_BULK_READ_0_UUID = notify_uuid
        self.BULK_CHAR_BULK_READ_1_UUID = notify_uuid
        self.BULK_CHAR_BULK_READ_2_UUID = notify_uuid
        self.BULK_CHAR_BULK_READ_3_UUID = notify_uuid
        self.is_variant_a = True
        logger.info(f'Variant A GATT profile detected — overriding UUIDs: svc={profile.svc_uuid} write={profile.write_uuids[0]} notify={profile.notify_uuids[0]}')

    async def _read_device_information(self):
        if not hasattr(self.client, 'read_gatt_char'):
            logger.debug('_read_device_information: active client has no read_gatt_char support — skipping DIS reads')
            return
        CHARS = {'00002a29-0000-1000-8000-00805f9b34fb': 'manufacturer_name', '00002a24-0000-1000-8000-00805f9b34fb': 'model_number', '00002a25-0000-1000-8000-00805f9b34fb': 'serial_number', '00002a26-0000-1000-8000-00805f9b34fb': 'firmware_revision', '00002a27-0000-1000-8000-00805f9b34fb': 'hardware_revision', '00002a28-0000-1000-8000-00805f9b34fb': 'software_revision'}
        try:
            dis_svc = next((s for s in self.client.services if s.uuid.lower() == DIS_SERVICE_UUID), None)
            if dis_svc is None:
                logger.debug('_read_device_information: DIS service (0x180a) not found in GATT services')
                return
            info = {}
            for char in dis_svc.characteristics:
                key = CHARS.get(char.uuid.lower())
                if key:
                    try:
                        raw = await self.client.read_gatt_char(char)
                        info[key] = raw.decode('utf-8', errors='replace').strip('\x00').strip()
                    except Exception as e:
                        logger.warning(f'DIS read {char.uuid} ({key}) failed: {e}')
            if info:
                self.ble_dis_info = info
                logger.debug(f'BLE DIS: {info}')
            else:
                logger.warning('_read_device_information: DIS service found but all char reads failed')
        except Exception as e:
            logger.warning(f'_read_device_information failed: {e}')

    async def _post_connect(self):
        self._apply_gatt_variant_overrides()
        await self._read_device_information()
        if self.is_variant_a:
            from .AriendiSecurity import AriendiSecurity
            self._arendi_security = AriendiSecurity()
            self.read_characteristics = {self.BULK_CHAR_BULK_READ_0_UUID: self.data_received, self.BULK_CHAR_BULK_READ_1_UUID: self.data_received, self.BULK_CHAR_BULK_READ_2_UUID: self.data_received, self.BULK_CHAR_BULK_READ_3_UUID: self.data_received}
            notify_uuid_str = str(self.BULK_CHAR_BULK_READ_0_UUID)
            if hasattr(self.client, 'stop_notify'):
                try:
                    await self.client.stop_notify(notify_uuid_str)
                except Exception:
                    pass
            await self.client.start_notify(notify_uuid_str, self._on_data_received)
            self._subscribed_characteristics.append(self.BULK_CHAR_BULK_READ_0_UUID)
            logger.debug(f'Alba notify subscribed: {notify_uuid_str}')
            if hasattr(self.client, '_acquire_mtu'):
                try:
                    await self.client._acquire_mtu()
                except Exception as e:
                    logger.debug(f'Alba MTU negotiation failed, using default: {e}')
            chunk_size = 20
            try:
                write_char = self.client.services.get_characteristic(self.BULK_CHAR_BULK_WRITE_0_UUID)
                if write_char is not None:
                    chunk_size = write_char.max_write_without_response_size
            except AttributeError:
                pass
            logger.debug(f'Alba write chunk size: {chunk_size} bytes')

            async def _raw_write(att_bytes: bytes):
                n = (len(att_bytes) + chunk_size - 1) // chunk_size
                if n > 1:
                    logger.debug(f'Alba write {len(att_bytes)} bytes → {n} chunks of ≤{chunk_size}')
                for off in range(0, len(att_bytes), chunk_size):
                    await self.client.write_gatt_char(self.BULK_CHAR_BULK_WRITE_0_UUID, att_bytes[off:off + chunk_size], response=False)
            self._arendi_raw_write = _raw_write
            await self._arendi_security.perform_handshake(_raw_write)
            self._arendi_security._ack_send_fn = _raw_write
            self.connection_status_changed_handlers(self, True, self.device_address, self.device_name)
            return
        self.read_characteristics = {self.BULK_CHAR_BULK_READ_0_UUID: self.data_received, self.BULK_CHAR_BULK_READ_1_UUID: self.data_received, self.BULK_CHAR_BULK_READ_2_UUID: self.data_received, self.BULK_CHAR_BULK_READ_3_UUID: self.data_received}
        logger.debug(f'self.read_characteristics: {self.read_characteristics}')
        await self._list_services()
        self.connection_status_changed_handlers(self, True, self.device_address, self.device_name)

    async def _list_services(self):
        logger.debug('BluetoothLeConnector: _list_services')
        if not self.client.is_connected:
            logger.debug('1. Error. Client not connected.')
            await self.client.connect()
        else:
            logger.debug('1. in subscribe 1: connected.')
        svc_uuids = [s.uuid for s in self.client.services]
        logger.debug(f'_list_services: looking for {self.SERVICE_UUID} in {svc_uuids}')
        matched = False
        for service in self.client.services:
            if service.uuid == str(self.SERVICE_UUID):
                matched = True
                for characteristic in service.characteristics:
                    logger.debug(f'got characteristic.uuid {characteristic.uuid}')
                    if characteristic.uuid in str(self.read_characteristics):
                        logger.debug(f'Registering characteristic {characteristic.uuid} for notification.')
                        if hasattr(self.client, 'stop_notify'):
                            try:
                                await self.client.stop_notify(characteristic)
                                logger.debug(f'Preemptive stop_notify OK: {characteristic.uuid}')
                            except Exception as _stop_exc:
                                logger.debug(f'Preemptive stop_notify failed (expected if not notifying): {characteristic.uuid}: {type(_stop_exc).__name__}: {_stop_exc}')
                        await self.client.start_notify(characteristic, self._on_data_received)
                        self._subscribed_characteristics.append(characteristic)
        if not matched:
            logger.debug(f'_list_services: service {self.SERVICE_UUID} not found — no notifications subscribed')

    async def _on_data_received(self, sender, data):
        logger.debug('BluetoothLeConnector: _on_data_received')
        logger.debug(f"Received data from characteristic {sender.uuid} data: {''.join((f'{b:02X}' for b in data))}")
        _hs_done = self._arendi_security.handshake_done if self._arendi_security else None
        logger.debug(f'BluetoothLeConnector: _on_data_received arendi={self._arendi_security is not None} handshake_done={_hs_done} len={len(data)}')
        if self._arendi_security is not None:
            decrypted_list = self._arendi_security.feed_att_bytes(bytes(data))
            logger.debug(f'BluetoothLeConnector: _on_data_received → {len(decrypted_list)} plaintext payload(s)')
            for payload in decrypted_list:
                await self.data_received_handlers.invoke_async(payload)
        else:
            await self.data_received_handlers.invoke_async(data)

    def _on_disconnected(self, client):
        logger.debug('BluetoothLeConnector: _on_disconnected')
        self.connection_status_changed_handlers(self, False)

    async def send_message(self, data):
        logger.debug(f"Sending data to characteristic {self.BULK_CHAR_BULK_WRITE_0_UUID} data: {''.join((f'{b:02X}' for b in data))}")
        if self._arendi_security is not None and self._arendi_security.handshake_done:
            att_bytes = self._arendi_security.wrap_for_send(data)
            await self._arendi_raw_write(att_bytes)
        else:
            result = await self.client.write_gatt_char(self.BULK_CHAR_BULK_WRITE_0_UUID, data)
            logger.debug(f'result: {result}')

    def get_services(self):
        if self.client is None:
            return []
        try:
            return list(self.client.services)
        except Exception:
            return []

    async def read_characteristic(self, char_specifier: Any) -> bytes:
        if self.client is None:
            raise BleakError('Client not connected')
        if not hasattr(self.client, 'read_gatt_char'):
            raise BleakError('Active BLE client does not support read_gatt_char')
        data = await self.client.read_gatt_char(char_specifier)
        return bytes(data)

    async def write_characteristic(self, char_specifier: Any, data: bytes, response: bool | None=None) -> None:
        if self.client is None:
            raise BleakError('Client not connected')
        await self.client.write_gatt_char(char_specifier, data, response=response)

    async def disconnect(self):
        if self.client:
            is_connected = self.client.is_connected
            logger.debug(f'[disconnect] is_connected={is_connected}, subscribed chars={len(self._subscribed_characteristics)}')
            for char in self._subscribed_characteristics:
                try:
                    await self.client.stop_notify(char)
                    logger.debug(f'[disconnect] stop_notify OK: {char}')
                except Exception as e:
                    logger.debug(f'[disconnect] stop_notify FAILED: {char}: {type(e).__name__}: {e}')
            self._subscribed_characteristics = []
            logger.debug(f'before asyncio.create_task(self.client.disconnect())')
            if self.esphome_host:
                await self.client.disconnect(close_api=False)
                if self._esphome_unsub_adv is not None:
                    try:
                        self._esphome_unsub_adv()
                        await asyncio.sleep(0.1)
                    except Exception:
                        pass
                    self._esphome_unsub_adv = None
                if self._esphome_api is not None:
                    try:
                        await self._esphome_api.disconnect()
                        logger.debug('[BluetoothLeConnector] Closed ESP32 API TCP connection')
                    except Exception as e:
                        logger.debug(f'[BluetoothLeConnector] ESP32 API TCP close: {e}')
            else:
                await self.client.disconnect()
            self.client = None
            import gc
            gc.collect()
        else:
            logger.debug(f'not self.client, no need to disconnect BLE.')
            if self._esphome_api is not None:
                try:
                    await self._esphome_api.disconnect()
                    logger.debug('[BluetoothLeConnector] Closed ESP32 API TCP connection (no BLE client was established)')
                except Exception as e:
                    logger.debug(f'[BluetoothLeConnector] ESP32 API TCP close: {e}')
        if self._esphome_unsub_adv is not None:
            try:
                self._esphome_unsub_adv()
            except Exception:
                pass
            self._esphome_unsub_adv = None
        self._arendi_security = None
        self._arendi_raw_write = None
        if self.esphome_host:
            self.esphome_proxy_connected = False
            self._esphome_api = None
