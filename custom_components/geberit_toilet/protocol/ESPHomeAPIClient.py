import asyncio
import logging
from typing import Callable, Dict, Union
from uuid import UUID
from aioesphomeapi import APIClient
logger = logging.getLogger(__name__)

class ESPHomeAPIClient:

    def __init__(self, api_client: APIClient, mac_address: str, disconnected_callback: Callable=None, address_type: int=0, feature_flags: int=0):
        self._api = api_client
        self._mac_address = mac_address
        self._mac_int = int(mac_address.replace(':', ''), 16)
        self._address_type = address_type
        self._feature_flags = feature_flags
        self._disconnected_callback = disconnected_callback
        self._is_connected = False
        self._services = None
        self._uuid_to_handle: Dict[str, int] = {}
        self._handle_to_uuid: Dict[int, str] = {}
        self._uuid_to_properties: Dict[str, int] = {}
        self._cccd_handles: Dict[int, int] = {}
        self._notify_callbacks: Dict[int, Callable] = {}
        self._notify_unsubs: list = []
        self._notify_queue: asyncio.Queue = asyncio.Queue()
        self._notify_worker_task = None
        self._cancel_connection = None
        logger.debug(f'[ESPHomeAPIClient] Initialized for device {mac_address} (int: {self._mac_int}, address_type: {address_type}, feature_flags: {feature_flags})')

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @property
    def services(self):
        if self._services is None:
            logger.warning('[ESPHomeAPIClient] Services accessed before connection')
            return ESPHomeGATTServiceCollection([])
        return self._services

    async def connect(self, timeout: float=30.0) -> bool:
        logger.debug(f'[ESPHomeAPIClient] Connecting to BLE device {self._mac_address} via ESP32 proxy')
        logger.debug(f'[ESPHomeAPIClient] Using feature_flags: {self._feature_flags}')
        connected_future = asyncio.get_running_loop().create_future()

        def on_bluetooth_connection_state(connected: bool, mtu: int, error: int) -> None:
            logger.debug(f'[ESPHomeAPIClient] on_bluetooth_connection_state called: connected={connected}, mtu={mtu}, error={error}, future_done={connected_future.done()}')
            if not connected_future.done():
                if error:
                    logger.error(f'[ESPHomeAPIClient] Connection error: {error}')
                    connected_future.set_exception(Exception(f'BLE connection error: {error}'))
                elif connected:
                    logger.debug(f'[ESPHomeAPIClient] BLE connected (MTU: {mtu})')
                    self._is_connected = True
                    connected_future.set_result(mtu)
                else:
                    logger.warning('[ESPHomeAPIClient] Disconnected during connection')
                    connected_future.set_exception(Exception('Disconnected during connection'))
            elif not connected:
                logger.debug('[ESPHomeAPIClient] Device disconnected')
                self._is_connected = False
                if self._disconnected_callback:
                    try:
                        self._disconnected_callback(self)
                    except Exception as e:
                        logger.error(f'[ESPHomeAPIClient] Error in disconnected callback: {e}')
        logger.debug(f'[ESPHomeAPIClient] Calling bluetooth_device_connect for mac_int={self._mac_int}, address_type={self._address_type}, feature_flags={self._feature_flags}')
        logger.debug(f'[ESPHomeAPIClient] Connection parameters: has_cache=False, disconnect_timeout=10.0, timeout={timeout}')
        logger.debug(f'[ESPHomeAPIClient] About to call bluetooth_device_connect')
        self._cancel_connection = await self._api.bluetooth_device_connect(self._mac_int, on_bluetooth_connection_state, address_type=self._address_type, feature_flags=self._feature_flags, has_cache=False, disconnect_timeout=10.0, timeout=timeout)
        logger.debug(f'[ESPHomeAPIClient] bluetooth_device_connect returned successfully, cancel_connection={self._cancel_connection is not None}')
        logger.debug(f'[ESPHomeAPIClient] Waiting for connection state callback')
        try:
            logger.debug(f'[ESPHomeAPIClient] Waiting for BLE connection (timeout={timeout}s)')
            mtu = await asyncio.wait_for(connected_future, timeout=timeout)
            logger.info(f'[ESPHomeAPIClient] Successfully connected to {self._mac_address} (MTU: {mtu})')
            await self._fetch_services()
            self._notify_worker_task = asyncio.create_task(self._notification_worker())
            return True
        except asyncio.TimeoutError:
            logger.error(f'[ESPHomeAPIClient] Connection timeout after {timeout}s')
            self._is_connected = False
            if self._cancel_connection:
                self._cancel_connection()
            raise Exception(f'Connection timeout after {timeout}s')
        except Exception as e:
            logger.error(f'[ESPHomeAPIClient] Connection failed: {e}')
            self._is_connected = False
            if self._cancel_connection:
                self._cancel_connection()
            raise

    async def _notification_worker(self):
        logger.debug('[ESPHomeAPIClient] notification_worker: started')
        while self._is_connected:
            try:
                (callback_fn, char_wrapper, data) = await self._notify_queue.get()
                logger.debug(f'[ESPHomeAPIClient] notification_worker: dequeued handle=0x{char_wrapper.handle:04x} len={len(data)}')
                result = callback_fn(char_wrapper, data)
                if asyncio.iscoroutine(result):
                    await result
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f'[ESPHomeAPIClient] Error in notification worker: {e}')
        logger.debug('[ESPHomeAPIClient] notification_worker: exited (_is_connected=False or cancelled)')

    async def _fetch_services(self):
        logger.debug(f'[ESPHomeAPIClient] Fetching GATT services for mac_int={self._mac_int}')
        try:
            resp = await self._api.bluetooth_gatt_get_services(self._mac_int)
            logger.debug(f'[ESPHomeAPIClient] Received {len(resp.services)} services from ESP32')
            services = []
            for svc in resp.services:
                logger.trace(f'[ESPHomeAPIClient] Service: {svc.uuid}')
                characteristics = []
                for char in svc.characteristics:
                    uuid_str = char.uuid.lower()
                    handle = char.handle
                    self._uuid_to_handle[uuid_str] = handle
                    self._handle_to_uuid[handle] = uuid_str
                    self._uuid_to_properties[uuid_str] = char.properties
                    cccd_uuid = '00002902-0000-1000-8000-00805f9b34fb'
                    for desc in char.descriptors:
                        if desc.uuid.lower() == cccd_uuid:
                            self._cccd_handles[handle] = desc.handle
                            logger.trace(f'[ESPHomeAPIClient]   CCCD descriptor: char 0x{handle:04x} → cccd 0x{desc.handle:04x}')
                    logger.trace(f'[ESPHomeAPIClient]   Characteristic: {uuid_str} → handle=0x{handle:04x} properties=0x{char.properties:02x}')
                    characteristics.append(ESPHomeGATTCharacteristic(uuid=uuid_str, handle=handle, properties=char.properties))
                services.append(ESPHomeGATTService(uuid=svc.uuid.lower(), characteristics=characteristics))
            self._services = ESPHomeGATTServiceCollection(services)
            logger.debug(f'[ESPHomeAPIClient] Service discovery complete: {len(services)} services, {len(self._uuid_to_handle)} characteristics')
        except Exception as e:
            logger.error(f'[ESPHomeAPIClient] Failed to fetch services: {e}')
            raise

    async def start_notify(self, char_specifier: Union[str, UUID, 'ESPHomeGATTCharacteristic'], callback: Callable):
        if isinstance(char_specifier, ESPHomeGATTCharacteristic):
            uuid_str = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            uuid_str = str(char_specifier).lower()
        else:
            uuid_str = str(char_specifier).lower()
        handle = self._uuid_to_handle.get(uuid_str)
        if handle is None:
            logger.error(f'[ESPHomeAPIClient] UUID {uuid_str} not found in services')
            raise ValueError(f'Characteristic UUID {uuid_str} not found in device services')
        logger.debug(f'[ESPHomeAPIClient] Registering notification: {uuid_str} (handle=0x{handle:04x})')
        self._notify_callbacks[handle] = callback

        def on_notify(handle: int, data: bytes) -> None:
            uuid = self._handle_to_uuid.get(handle)
            logger.debug(f"[ESPHomeAPIClient] Notification received: handle=0x{handle:04x} uuid={uuid} len={len(data)} data={data.hex()[:40]}{('...' if len(data) > 20 else '')}")
            callback_fn = self._notify_callbacks.get(handle)
            if callback_fn:
                char_wrapper = ESPHomeGATTCharacteristic(uuid=uuid, handle=handle, properties=16)
                logger.debug(f'[ESPHomeAPIClient] on_notify: enqueuing handle=0x{handle:04x} len={len(data)}')
                self._notify_queue.put_nowait((callback_fn, char_wrapper, data))
            else:
                logger.warning(f'[ESPHomeAPIClient] No callback registered for handle 0x{handle:04x}')
        try:
            (stop_notify, remove_cb) = await self._api.bluetooth_gatt_start_notify(self._mac_int, handle, on_notify)
            self._notify_unsubs.append((stop_notify, remove_cb))
            logger.debug(f'[ESPHomeAPIClient] Notification registered for {uuid_str} (handle=0x{handle:04x})')
            cccd_handle = self._cccd_handles.get(handle)
            if cccd_handle is not None:
                await self._api.bluetooth_gatt_write_descriptor(self._mac_int, cccd_handle, b'\x01\x00')
                logger.debug(f'[ESPHomeAPIClient] CCCD written for {uuid_str} (cccd_handle=0x{cccd_handle:04x})')
            else:
                logger.warning(f'[ESPHomeAPIClient] No CCCD descriptor found for {uuid_str} (handle=0x{handle:04x}), notifications may not work')
        except Exception as e:
            logger.error(f'[ESPHomeAPIClient] Failed to start notifications for {uuid_str}: {e}')
            raise

    async def write_gatt_char(self, char_specifier: Union[str, UUID, 'ESPHomeGATTCharacteristic'], data: bytes, response: bool=None):
        if isinstance(char_specifier, ESPHomeGATTCharacteristic):
            uuid_str = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            uuid_str = str(char_specifier).lower()
        else:
            uuid_str = str(char_specifier).lower()
        handle = self._uuid_to_handle.get(uuid_str)
        if handle is None:
            logger.error(f'[ESPHomeAPIClient] UUID {uuid_str} not found in services')
            raise ValueError(f'Characteristic UUID {uuid_str} not found in device services')
        if response is None:
            props = self._uuid_to_properties.get(uuid_str, 0)
            response = not bool(props & 4)
            logger.debug(f'[ESPHomeAPIClient] Write type auto-detected: {uuid_str} properties=0x{props:02x} → response={response}')
        logger.debug(f"[ESPHomeAPIClient] Write characteristic: {uuid_str} (handle=0x{handle:04x}) response={response} len={len(data)} data={data.hex()[:40]}{('...' if len(data) > 20 else '')}")
        try:
            await self._api.bluetooth_gatt_write(self._mac_int, handle, bytes(data), response=response)
            logger.debug(f'[ESPHomeAPIClient] Write successful: {uuid_str} (handle=0x{handle:04x})')
        except Exception as e:
            logger.error(f'[ESPHomeAPIClient] Write failed for {uuid_str}: {e}')
            raise

    async def read_gatt_char(self, char_specifier: Union[str, UUID, 'ESPHomeGATTCharacteristic']) -> bytes:
        if isinstance(char_specifier, ESPHomeGATTCharacteristic):
            uuid_str = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            uuid_str = str(char_specifier).lower()
        else:
            uuid_str = str(char_specifier).lower()
        handle = self._uuid_to_handle.get(uuid_str)
        if handle is None:
            logger.error(f'[ESPHomeAPIClient] UUID {uuid_str} not found in services')
            raise ValueError(f'Characteristic UUID {uuid_str} not found in device services')
        logger.debug(f'[ESPHomeAPIClient] Read characteristic: {uuid_str} (handle=0x{handle:04x})')
        try:
            data = await self._api.bluetooth_gatt_read(self._mac_int, handle)
            data_bytes = bytes(data)
            logger.debug(f"[ESPHomeAPIClient] Read successful: {uuid_str} (handle=0x{handle:04x}) len={len(data_bytes)} data={data_bytes.hex()[:40]}{('...' if len(data_bytes) > 20 else '')}")
            return data_bytes
        except Exception as e:
            logger.error(f'[ESPHomeAPIClient] Read failed for {uuid_str}: {e}')
            raise

    async def disconnect(self, close_api: bool=True):
        logger.debug(f'[ESPHomeAPIClient] Disconnecting from {self._mac_address}')
        if not self._is_connected:
            logger.debug('[ESPHomeAPIClient] Already disconnected')
            if self._cancel_connection:
                try:
                    self._cancel_connection()
                except Exception:
                    pass
                self._cancel_connection = None
            if close_api and self._api is not None:
                try:
                    await self._api.disconnect()
                    logger.debug('[ESPHomeAPIClient] Disconnected from ESP32 API (was already BLE-disconnected)')
                except Exception as e:
                    logger.debug(f'[ESPHomeAPIClient] ESP32 API disconnect: {e}')
            return
        ble_confirmed_disconnect = False
        try:
            if self._notify_worker_task:
                self._notify_worker_task.cancel()
                self._notify_worker_task = None
            for (_stop_notify, remove_cb) in self._notify_unsubs:
                try:
                    remove_cb()
                except Exception:
                    pass
            self._notify_unsubs.clear()
            self._notify_callbacks.clear()
            await self._api.bluetooth_device_disconnect(self._mac_int)
            for _ in range(50):
                if not self._is_connected:
                    ble_confirmed_disconnect = True
                    break
                await asyncio.sleep(0.1)
            else:
                logger.warning(f'[ESPHomeAPIClient] BLE disconnect not confirmed by ESP32 within 5 s for {self._mac_address} — closing API anyway')
            logger.debug(f'[ESPHomeAPIClient] Disconnected from {self._mac_address} (confirmed={ble_confirmed_disconnect})')
        except Exception as e:
            logger.warning(f'[ESPHomeAPIClient] Error during BLE disconnect: {e}')
        finally:
            if self._cancel_connection:
                self._cancel_connection()
                self._cancel_connection = None
            self._is_connected = False
            if close_api:
                try:
                    await self._api.disconnect()
                    logger.debug('[ESPHomeAPIClient] Disconnected from ESP32 API')
                except Exception as e:
                    logger.debug(f'[ESPHomeAPIClient] ESP32 API disconnect: {e}')
            else:
                logger.debug('[ESPHomeAPIClient] Keeping ESP32 API TCP connection alive (close_api=False)')
            if not ble_confirmed_disconnect and self._disconnected_callback:
                try:
                    self._disconnected_callback(self)
                except Exception as e:
                    logger.error(f'[ESPHomeAPIClient] Error in disconnected callback: {e}')

class ESPHomeGATTServiceCollection:

    def __init__(self, services: list):
        self._services = services

    def __iter__(self):
        return iter(self._services)

    def __len__(self):
        return len(self._services)

class ESPHomeGATTService:

    def __init__(self, uuid: str, characteristics: list):
        self.uuid = uuid
        self.characteristics = characteristics

    def __repr__(self):
        return f'ESPHomeGATTService(uuid={self.uuid}, chars={len(self.characteristics)})'

class ESPHomeGATTCharacteristic:

    def __init__(self, uuid: str, handle: int, properties: int):
        self.uuid = uuid
        self.handle = handle
        self.properties = properties

    def __repr__(self):
        return f'ESPHomeGATTCharacteristic(uuid={self.uuid}, handle=0x{self.handle:04x})'
