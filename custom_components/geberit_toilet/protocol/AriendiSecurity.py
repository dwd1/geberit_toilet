import asyncio
import logging
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.cmac import CMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
logger = logging.getLogger(__name__)
_BID_MASK = bytes([78, 179, 39, 240, 92, 145, 168, 61, 118, 197, 15, 226, 147, 26, 104, 84])
_BID_STORED = bytes([159, 146, 173, 121, 170, 155, 106, 169, 91, 129, 47, 155, 231, 74, 255, 234])
geberit_toiletBridgeId = bytes((a ^ b for (a, b) in zip(_BID_STORED, _BID_MASK)))
_SEC_VERSION_REQ = 0
_SEC_VERSION_RESP = 1
_SEC_EP_REQ = 16
_SEC_EP_RESP = 17
_SEC_KE_REQ = 18
_SEC_KE_RESP = 19
_SEC_ENCRYPTED = 32
_HDLC_SABM_TYPE = 7
_HDLC_UA_TYPE = 12

def _crc16_kermit(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = crc >> 1 ^ 33800
            else:
                crc >>= 1
    return crc

def _cobs_encode(data: bytes) -> bytes:
    result = bytearray()
    code_pos = 0
    result.append(0)
    code = 1
    for byte in data:
        if byte == 0:
            result[code_pos] = code
            code_pos = len(result)
            result.append(0)
            code = 1
        else:
            result.append(byte)
            code += 1
            if code == 255:
                result[code_pos] = code
                code_pos = len(result)
                result.append(0)
                code = 1
    result[code_pos] = code
    return bytes(result)

def _cobs_decode(data: bytes) -> bytes:
    result = bytearray()
    i = 0
    while i < len(data):
        code = data[i]
        if code == 0:
            raise ValueError('COBS: unexpected 0x00 in encoded payload')
        i += 1
        for _ in range(code - 1):
            if i >= len(data):
                raise ValueError('COBS: truncated data')
            result.append(data[i])
            i += 1
        if code != 255 and i < len(data):
            result.append(0)
    return bytes(result)

class _AesCtrState:
    __slots__ = ('_encryptor', '_counter', '_ks', '_pos')

    def __init__(self, key: bytes, nonce2: bytes):
        enc = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor()
        self._encryptor = enc
        self._counter = bytearray(nonce2)
        self._ks = bytearray(enc.update(bytes(self._counter)))
        self._pos = 0
        cnt = int.from_bytes(self._counter[12:16], 'big')
        self._counter[12:16] = (cnt + 1 & 4294967295).to_bytes(4, 'big')

    def _next_block(self) -> None:
        self._ks = bytearray(self._encryptor.update(bytes(self._counter)))
        self._pos = 0
        cnt = int.from_bytes(self._counter[12:16], 'big')
        self._counter[12:16] = (cnt + 1 & 4294967295).to_bytes(4, 'big')

    def process(self, data: bytes) -> bytes:
        result = bytearray(len(data))
        for (i, b) in enumerate(data):
            if self._pos >= 16:
                self._next_block()
            result[i] = b ^ self._ks[self._pos]
            self._pos += 1
        return bytes(result)

def _hkdf(ikm: bytes, salt: bytes, length: int) -> bytes:
    return HKDF(algorithm=SHA256(), length=length, salt=salt, info=b'', backend=default_backend()).derive(ikm)

def _aes_cmac(key: bytes, data: bytes) -> bytes:
    c = CMAC(algorithms.AES(key), backend=default_backend())
    c.update(data)
    return c.finalize()

class AriendiSecurity:

    def __init__(self):
        self._rx_buf = bytearray()
        self._rx_queue: asyncio.Queue = asyncio.Queue()
        self._tx_seq = 0
        self._rx_ack = 0
        self._rx_cipher: _AesCtrState | None = None
        self._tx_cipher: _AesCtrState | None = None
        self._inner_cobs_buf: bytearray = bytearray()
        self._ack_send_fn = None
        self.handshake_done = False

    def reset(self) -> None:
        self._rx_buf = bytearray()
        self._rx_queue = asyncio.Queue()
        self._tx_seq = 0
        self._rx_ack = 0
        self._rx_cipher = None
        self._tx_cipher = None
        self._inner_cobs_buf = bytearray()
        self._ack_send_fn = None
        self.handshake_done = False

    @staticmethod
    def _u_ctrl(type_code: int) -> int:
        return type_code << 3 & 224 | type_code << 2 & 12 | 3

    def _i_ctrl(self) -> int:
        return self._rx_ack << 5 & 224 | self._tx_seq << 1 & 14

    def _s_ctrl_rr(self) -> int:
        return self._rx_ack << 5 & 224 | 1

    def _build_att(self, ctrl: int, payload: bytes) -> bytes:
        raw = bytes([ctrl]) + payload
        crc = _crc16_kermit(raw)
        return b'\x00' + _cobs_encode(raw + bytes([crc & 255, crc >> 8 & 255])) + b'\x00'

    def _att_u(self, hdlc_type: int) -> bytes:
        return self._build_att(self._u_ctrl(hdlc_type), b'')

    def _att_i(self, sec_payload: bytes) -> bytes:
        att = self._build_att(self._i_ctrl(), sec_payload)
        self._tx_seq = (self._tx_seq + 1) % 8
        return att

    def _att_s_rr(self) -> bytes:
        return self._build_att(self._s_ctrl_rr(), b'')

    def _feed_inner_cobs(self, data: bytes) -> list[bytes]:
        results = []
        self._inner_cobs_buf.extend(data)
        while 0 in self._inner_cobs_buf:
            idx = self._inner_cobs_buf.index(0)
            if idx == 0:
                del self._inner_cobs_buf[0]
                continue
            frame_bytes = bytes(self._inner_cobs_buf[:idx])
            del self._inner_cobs_buf[:idx + 1]
            try:
                decoded = _cobs_decode(frame_bytes)
            except ValueError as e:
                logger.debug(f'AriendiSecurity: inner COBS decode error: {e}')
                continue
            if len(decoded) < 2:
                continue
            crc_recv = decoded[-2] | decoded[-1] << 8
            if _crc16_kermit(decoded[:-2]) == crc_recv:
                results.append(decoded[:-2])
            else:
                logger.debug(f'AriendiSecurity: inner COBS CRC mismatch (got 0x{crc_recv:04X}, calc 0x{_crc16_kermit(decoded[:-2]):04X})')
        return results

    def feed_att_bytes(self, data: bytes) -> list:
        self._rx_buf.extend(data)
        self._process_rx_buf()
        if not self.handshake_done:
            return []
        results = []
        _q_before = self._rx_queue.qsize()
        while not self._rx_queue.empty():
            try:
                (ft, ctrl, payload) = self._rx_queue.get_nowait()
                if ft == 'I' and payload and (payload[0] == _SEC_ENCRYPTED):
                    decrypted = self._rx_cipher.process(payload[1:])
                    results.extend(self._feed_inner_cobs(decrypted))
                elif ft == 'I':
                    logger.debug(f'AriendiSecurity: post-handshake unexpected Security type 0x{payload[0]:02X}' if payload else '0x??')
            except asyncio.QueueEmpty:
                break
        logger.debug(f'AriendiSecurity: feed_att_bytes q_drained={_q_before} → {len(results)} plaintext payloads')
        return results

    def _process_rx_buf(self) -> None:
        while True:
            buf = self._rx_buf
            if not buf or buf[0] != 0:
                idx = buf.find(b'\x00')
                if idx == -1:
                    self._rx_buf = bytearray()
                    return
                self._rx_buf = buf[idx:]
                buf = self._rx_buf
            end = buf.find(b'\x00', 1)
            if end == -1:
                return
            cobs_content = bytes(buf[1:end])
            self._rx_buf = buf[end:]
            if not cobs_content:
                continue
            try:
                decoded = _cobs_decode(cobs_content)
            except ValueError as e:
                logger.debug(f'AriendiSecurity: COBS error: {e}')
                continue
            if len(decoded) < 3:
                continue
            crc_recv = decoded[-2] | decoded[-1] << 8
            crc_calc = _crc16_kermit(decoded[:-2])
            if crc_recv != crc_calc:
                logger.debug(f'AriendiSecurity: CRC mismatch rx=0x{crc_recv:04X} calc=0x{crc_calc:04X}')
                continue
            ctrl = decoded[0]
            hdlc_payload = decoded[1:-2]
            if ctrl & 1 == 0:
                peer_ns = ctrl >> 1 & 7
                self._rx_ack = (peer_ns + 1) % 8
                self._rx_queue.put_nowait(('I', ctrl, hdlc_payload))
                sec_str = f'0x{hdlc_payload[0]:02X}' if hdlc_payload else '0x??'
                logger.debug(f'AriendiSecurity: I-frame rx peer_ns={peer_ns} sec_type={sec_str}')
                if self.handshake_done and self._ack_send_fn is not None:
                    try:
                        asyncio.get_running_loop().create_task(self._ack_send_fn(self._att_s_rr()))
                    except RuntimeError:
                        pass
            elif ctrl & 3 == 3:
                self._rx_queue.put_nowait(('U', ctrl, hdlc_payload))
                logger.debug(f'AriendiSecurity: U-frame rx ctrl=0x{ctrl:02X}')

    async def _await_u_frame(self, expected_ctrl: int, timeout: float=5.0) -> None:
        deadline = asyncio.get_event_loop().time() + timeout
        while True:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                raise TimeoutError(f'AriendiSecurity: timeout waiting for U-frame ctrl=0x{expected_ctrl:02X}')
            try:
                (ft, ctrl, _) = await asyncio.wait_for(self._rx_queue.get(), timeout=remaining)
            except asyncio.TimeoutError:
                raise TimeoutError(f'AriendiSecurity: timeout waiting for U-frame ctrl=0x{expected_ctrl:02X}')
            if ft == 'U' and ctrl == expected_ctrl:
                return
            logger.debug(f'AriendiSecurity: discarding unexpected frame ft={ft} ctrl=0x{ctrl:02X}')

    async def _await_i_security(self, expected_type: int, timeout: float=5.0) -> bytes:
        deadline = asyncio.get_event_loop().time() + timeout
        while True:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                raise TimeoutError(f'AriendiSecurity: timeout waiting for Security type 0x{expected_type:02X}')
            try:
                (ft, ctrl, payload) = await asyncio.wait_for(self._rx_queue.get(), timeout=remaining)
            except asyncio.TimeoutError:
                raise TimeoutError(f'AriendiSecurity: timeout waiting for Security type 0x{expected_type:02X}')
            if ft == 'I' and payload and (payload[0] == expected_type):
                return payload
            sec_type_str = f'0x{payload[0]:02X}' if payload else '0x??'
            logger.debug(f'AriendiSecurity: discarding unexpected frame ft={ft} sec_type={sec_type_str}')

    async def perform_handshake(self, send_fn) -> None:
        self._tx_seq = 0
        self._rx_ack = 0
        logger.debug('AriendiSecurity: SABM →')
        await send_fn(self._att_u(_HDLC_SABM_TYPE))
        await self._await_u_frame(self._u_ctrl(_HDLC_UA_TYPE))
        logger.debug('AriendiSecurity: ← UA')
        logger.debug('AriendiSecurity: Version Request →')
        await send_fn(self._att_i(bytes([_SEC_VERSION_REQ])))
        vr = await self._await_i_security(_SEC_VERSION_RESP)
        if len(vr) >= 7:
            proto_ver = vr[6] + 1
            logger.debug(f'AriendiSecurity: ← Version Response (proto v{proto_ver})')
        else:
            logger.debug('AriendiSecurity: ← Version Response (short)')
        logger.debug('AriendiSecurity: EP Request →')
        await send_fn(self._att_i(bytes([_SEC_EP_REQ])))
        ep = await self._await_i_security(_SEC_EP_RESP)
        if len(ep) < 33:
            raise ValueError(f'AriendiSecurity: EP Response too short ({len(ep)} bytes)')
        nonce1 = ep[1:17]
        nonce2 = ep[17:33]
        if len(ep) >= 35:
            keyset_mask = ep[33] | ep[34] << 8
            logger.debug(f'AriendiSecurity: ← EP Response nonce1={nonce1.hex()} nonce2={nonce2.hex()} keyset_mask=0x{keyset_mask:04X}')
        else:
            logger.debug(f'AriendiSecurity: ← EP Response nonce1={nonce1.hex()} nonce2={nonce2.hex()} (no keyset_mask, len={len(ep)})')
        auth_key = _hkdf(ikm=geberit_toiletBridgeId, salt=nonce1, length=16)
        private_key = X25519PrivateKey.generate()
        client_public = private_key.public_key().public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw)
        client_cmac = _aes_cmac(auth_key, client_public)
        ke_req = bytes([_SEC_KE_REQ]) + client_public + client_cmac + bytes([0])
        logger.debug(f'AriendiSecurity: KE Request → {ke_req.hex()}')
        await send_fn(self._att_i(ke_req))
        ke = await self._await_i_security(_SEC_KE_RESP, timeout=5.0)
        if len(ke) < 49:
            raise ValueError(f'AriendiSecurity: KE Response too short ({len(ke)} bytes)')
        server_public_bytes = ke[1:33]
        server_cmac_bytes = ke[33:49]
        logger.debug(f'AriendiSecurity: ← KE Response server_pub={server_public_bytes.hex()[:16]}...')
        expected_cmac = _aes_cmac(auth_key, server_public_bytes)
        if server_cmac_bytes != expected_cmac:
            raise ValueError('AriendiSecurity: server CMAC verification failed')
        logger.debug('AriendiSecurity: server CMAC verified ✓')
        server_pub_key = X25519PublicKey.from_public_bytes(server_public_bytes)
        shared_secret = private_key.exchange(server_pub_key)
        key_material = _hkdf(ikm=shared_secret, salt=nonce1, length=32)
        rx_key = key_material[0:16]
        tx_key = key_material[16:32]
        logger.debug(f'AriendiSecurity: session_keys shared_secret={shared_secret.hex()} rx_key={rx_key.hex()} tx_key={tx_key.hex()} nonce2={nonce2.hex()}')
        self._rx_cipher = _AesCtrState(rx_key, nonce2)
        self._tx_cipher = _AesCtrState(tx_key, nonce2)
        await send_fn(self._att_s_rr())
        self.handshake_done = True
        logger.info('AriendiSecurity: handshake complete — session keys established')

    def wrap_for_send(self, geberit_payload: bytes) -> bytes:
        crc = _crc16_kermit(geberit_payload)
        inner_frame = b'\x00' + _cobs_encode(geberit_payload + bytes([crc & 255, crc >> 8 & 255])) + b'\x00'
        ciphertext = self._tx_cipher.process(inner_frame)
        return self._att_i(bytes([_SEC_ENCRYPTED]) + ciphertext)
