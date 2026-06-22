import asyncio
import logging
import struct
from dataclasses import dataclass
from typing import Optional
from .CommandId import CommandId
from .DpType import DpType
from .TransmissionStatus import TransmissionStatus
logger = logging.getLogger(__name__)

@dataclass
class Ble20DeviceIdentification:
    name: Optional[str] = None
    device_series: Optional[int] = None
    device_variant: Optional[int] = None
    device_boot_variant: Optional[int] = None
    device_model: Optional[int] = None
    device_number: Optional[int] = None
    device_unique_id: Optional[int] = None
    fw_rs_version: Optional[str] = None
    fw_ts_version: Optional[int] = None
    device_production_date: Optional[int] = None
    device_sap_number: Optional[str] = None
    sales_product_sap_number: Optional[str] = None
    sales_product_serial_number: Optional[str] = None

def encode_address(dp_id: int, instance: Optional[int]=None) -> bytes:
    lo = dp_id & 255
    hi = dp_id >> 8 & 127
    if instance is not None:
        return bytes([lo, hi | 128, instance])
    return bytes([lo, hi])

def decode_address(data: bytes, offset: int=1) -> tuple[int, Optional[int], int]:
    lo = data[offset]
    hi = data[offset + 1]
    has_instance = bool(hi & 128)
    dp_id = (hi & 127) << 8 | lo
    if has_instance:
        return (dp_id, data[offset + 2], offset + 3)
    return (dp_id, None, offset + 2)

class Ble20Client:
    RECV_TIMEOUT = 30.0

    def __init__(self, connector):
        self._connector = connector
        self._rx_queue: asyncio.Queue[bytes] = asyncio.Queue()
        self._notify_queues: dict[int, asyncio.Queue] = {}
        connector.data_received_handlers += self._on_data

    async def _on_data(self, data: bytes) -> None:
        if not data:
            return
        cmd = data[0]
        if cmd == CommandId.NotifyData and len(data) >= 3:
            (dp_id, _, _) = decode_address(data, 1)
            q = self._notify_queues.get(dp_id)
            if q is not None:
                q.put_nowait(data)
                return
        self._rx_queue.put_nowait(data)

    async def _recv(self, timeout: float=RECV_TIMEOUT) -> bytes:
        return await asyncio.wait_for(self._rx_queue.get(), timeout=timeout)

    async def _send(self, payload: bytes) -> None:
        logger.debug(f'Ble20 → {payload.hex()}')
        await self._connector.send_message(payload)

    async def inventory(self) -> dict[int, dict]:
        await self._send(bytes([CommandId.Inventory, 0]))
        while True:
            frame = await self._recv()
            logger.debug(f'Ble20 ← {frame.hex()}')
            if frame[0] == CommandId.InventoryCount:
                break
            logger.debug(f'Ble20: skipping pre-inventory frame cmd=0x{frame[0]:02X}')
        count = struct.unpack_from('<H', frame, 1)[0]
        logger.debug(f'Ble20: inventory count={count}')
        result: dict[int, dict] = {}
        received = 0
        while received < count:
            frame = await self._recv()
            logger.debug(f'Ble20 ← {frame.hex()}')
            if frame[0] != CommandId.InventoryData:
                logger.debug(f'Ble20: skipping non-inventory frame cmd=0x{frame[0]:02X}')
                continue
            (dp_id, instance, payload_off) = decode_address(frame, 1)
            payload = frame[payload_off:]
            if len(payload) < 11:
                logger.warning(f'Ble20: short InventoryData for DpId={dp_id}: {payload.hex()}')
                received += 1
                continue
            flags = payload[10]
            result[dp_id] = {'instance': instance, 'version': payload[0], 'datatype': payload[1], 'min_s': struct.unpack_from('<i', payload, 2)[0], 'max_s': struct.unpack_from('<i', payload, 6)[0], 'min_u': struct.unpack_from('<I', payload, 2)[0], 'max_u': struct.unpack_from('<I', payload, 6)[0], 'is_internal': bool(flags & 128), 'behavior': flags & 127}
            received += 1
        logger.info(f'Ble20: inventory complete — {len(result)} DpIds')
        return result

    async def read(self, dp_id: int, instance: Optional[int]=None) -> bytes:
        addr = encode_address(dp_id, instance)
        await self._send(bytes([CommandId.ReadCmd]) + addr)
        while True:
            frame = await self._recv()
            logger.debug(f'Ble20 ← {frame.hex()}')
            if frame[0] in (CommandId.ReadAns, CommandId.ReadError):
                break
            logger.debug(f'Ble20: skipping frame cmd=0x{frame[0]:02X} (awaiting ReadAns)')
        if frame[0] == CommandId.ReadError:
            (_, _, off) = decode_address(frame, 1)
            status = frame[off] if off < len(frame) else 255
            raise IOError(f'ReadError dp_id={dp_id}: {_tx_name(status)}')
        (_, _, off) = decode_address(frame, 1)
        return frame[off:]

    async def write(self, dp_id: int, value: bytes, instance: Optional[int]=None) -> None:
        addr = encode_address(dp_id, instance)
        await self._send(bytes([CommandId.WriteCmd]) + addr + value)
        while True:
            frame = await self._recv()
            logger.debug(f'Ble20 ← {frame.hex()}')
            if frame[0] in (CommandId.WriteAck, CommandId.WriteError):
                break
            logger.debug(f'Ble20: skipping frame cmd=0x{frame[0]:02X} (awaiting WriteAck)')
        if frame[0] == CommandId.WriteError:
            (_, _, off) = decode_address(frame, 1)
            status = frame[off] if off < len(frame) else 255
            raise IOError(f'WriteError dp_id={dp_id}: {_tx_name(status)}')

    async def enable_notification(self, dp_ids: list[int]) -> None:
        for dp_id in dp_ids:
            addr = encode_address(dp_id)
            await self._send(bytes([CommandId.NotifyEnable]) + addr)
            frame = await self._recv()
            logger.debug(f'Ble20 ← {frame.hex()}')
            if frame[0] == CommandId.NotifyAck:
                if dp_id not in self._notify_queues:
                    self._notify_queues[dp_id] = asyncio.Queue()
                logger.debug(f'Ble20: notification enabled for DpId={dp_id}')
            else:
                (_, _, off) = decode_address(frame, 1)
                status = frame[off] if off < len(frame) else 255
                logger.warning(f'Ble20: NotifyEnable DpId={dp_id} failed: {_tx_name(status)}')

    async def get_notification(self, dp_id: int, timeout: float=RECV_TIMEOUT) -> bytes:
        q = self._notify_queues.get(dp_id)
        if q is None:
            raise ValueError(f'DpId={dp_id} not subscribed — call enable_notification first')
        frame = await asyncio.wait_for(q.get(), timeout=timeout)
        (_, _, off) = decode_address(frame, 1)
        return frame[off:]

    async def capabilities(self) -> int:
        await self._send(bytes([CommandId.CapabilitiesCmd]))
        try:
            while True:
                frame = await self._recv()
                logger.debug(f'Ble20 ← {frame.hex()}')
                if frame[0] == CommandId.CapabilitiesAck:
                    flags = frame[1] if len(frame) > 1 else 0
                    logger.debug(f'Ble20: capabilities flags=0x{flags:02X}')
                    return flags
                logger.debug(f'Ble20: skipping frame cmd=0x{frame[0]:02X} (awaiting CapabilitiesAck)')
        except asyncio.TimeoutError:
            logger.warning('Ble20: CapabilitiesCmd timed out — device may not support it')
            return 0

    async def event_storage_inventory(self, capabilities_flags: int=0) -> None:
        extended = bool(capabilities_flags & 4)
        payload = bytes([CommandId.EventStorageInventory, 1]) if extended else bytes([CommandId.EventStorageInventory])
        await self._send(payload)
        try:
            remaining = 0
            while True:
                frame = await self._recv()
                logger.debug(f'Ble20 ← {frame.hex()}')
                if frame[0] == CommandId.EventStorageInventoryCount:
                    remaining = struct.unpack_from('<H', frame, 1)[0] if len(frame) >= 3 else 0
                    logger.debug(f'Ble20: event storage inventory count={remaining}')
                    if remaining == 0:
                        return
                elif frame[0] == CommandId.EventStorageInventoryData:
                    remaining -= 1
                    if remaining <= 0:
                        return
                else:
                    logger.debug(f'Ble20: skipping frame cmd=0x{frame[0]:02X} (draining event storage)')
        except asyncio.TimeoutError:
            logger.warning('Ble20: EventStorageInventory timed out — continuing anyway')

    async def join(self, pin: Optional[str]=None, inv: Optional[dict]=None, timeout: float=15.0) -> str:
        from .DpId import DpId
        DP_JOIN = int(DpId.DP_JOIN_DEVICE)
        DP_PROGRESS = int(DpId.DP_JOIN_DEVICE_PROGRESS)
        DP_ERROR = int(DpId.DP_JOIN_DEVICE_ERROR)
        if inv is not None and DP_JOIN not in inv:
            logger.debug('Ble20 join: DP_JOIN_DEVICE absent from inventory — skip')
            return 'skipped'
        join_version = inv[DP_JOIN]['version'] if inv and DP_JOIN in inv else 1
        try:
            series = (await self.read(int(DpId.DP_DEVICE_SERIES)))[0]
            variant = (await self.read(int(DpId.DP_DEVICE_VARIANT)))[0]
            unique_raw = await self.read(int(DpId.DP_UNIQUE_DEVICE_NUMBER))
            unique_id = struct.unpack_from('<I', unique_raw)[0] if len(unique_raw) >= 4 else 0
        except Exception as e:
            logger.warning(f'Ble20 join: could not read device identifiers — {e}')
            return 'skipped'

        def _build(pairing_secret: Optional[str]) -> bytes:
            if join_version == 0:
                data = bytearray(6)
                data[0] = series
                data[1] = variant
                struct.pack_into('<I', data, 2, unique_id)
                return bytes(data)
            size = 11 if join_version >= 2 else 10
            data = bytearray(size)
            data[0] = series
            data[1] = variant
            struct.pack_into('<I', data, 2, unique_id)
            if pairing_secret:
                encoded = pairing_secret.encode('utf-8')[:4]
                data[6:6 + len(encoded)] = encoded
            return bytes(data)
        await self.enable_notification([DP_PROGRESS, DP_ERROR])
        for attempt in range(2):
            secret = None if attempt == 0 else pin
            try:
                await self.write(DP_JOIN, _build(secret))
            except IOError as e:
                logger.debug(f'Ble20 join: WriteError on attempt {attempt} — {e} (continuing)')
            progress = 0
            deadline = asyncio.get_event_loop().time() + timeout
            while asyncio.get_event_loop().time() < deadline:
                remaining = deadline - asyncio.get_event_loop().time()
                try:
                    raw = await self.get_notification(DP_PROGRESS, timeout=remaining)
                    progress = raw[0] if raw else 255
                except asyncio.TimeoutError:
                    raise IOError('JOIN timed out waiting for progress notification')
                if progress in (3, 4):
                    break
            if progress == 3:
                logger.info(f"Ble20 join: done (attempt={attempt}, pin={('yes' if secret else 'no')})")
                return 'done'
            error_bits = 0
            try:
                err_raw = await self.get_notification(DP_ERROR, timeout=2.0)
                error_bits = err_raw[0] if err_raw else 0
            except asyncio.TimeoutError:
                pass
            logger.debug(f'Ble20 join: attempt {attempt} error=0x{error_bits:02X}')
            if attempt == 0 and error_bits & 2 and (pin is not None):
                logger.debug('Ble20 join: device is Protected — retrying with PIN')
                continue
            if error_bits & 4:
                raise IOError('JOIN failed: wrong PIN')
            if error_bits & 8:
                raise IOError('JOIN failed: too many devices registered')
            if error_bits & 16:
                raise IOError('JOIN failed: device not supported')
            if error_bits & 2 and pin is None:
                raise IOError('JOIN failed: device is Protected but no PIN configured')
            raise IOError(f'JOIN failed: error=0x{error_bits:02X}')
        raise IOError('JOIN: exhausted retries')

def _tx_name(status: int) -> str:
    try:
        return TransmissionStatus(status).name
    except ValueError:
        return f'0x{status:02X}'
