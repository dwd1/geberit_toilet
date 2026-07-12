from __future__ import annotations
from enum import IntEnum
import asyncio
import logging
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.cmac import CMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from collections import deque
import struct
from functools import wraps
from typing import Optional
from .const import _0xdaef1eb3
import time
from bleak import BleakClient, BleakScanner, BleakError
from bleak.backends.device import BLEDevice
from uuid import UUID
from typing import Any
from .const import _0xffe93664, _0xe80ee6c3, _0x0eb5e6c6
from typing import Callable, Dict, Union
from aioesphomeapi import APIClient
import inspect
from dataclasses import dataclass, field
from typing import List
from .const import _0x477e0659, _0x0eb5e6c6
from dataclasses import dataclass
from .const import _0x4b1c5d43, _0x7ffbba85, _0xe80ee6c3, _0x0eb5e6c6, _0xe4e079bc, _0x6871b74d, _0x6594c694

def _geberit_get_disabled_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL + 1)
    logger.propagate = False
    logger.disabled = True
    return logger

class _0xc716531b(IntEnum):
    _0x4d604dd8 = 0
    _0xcffd2071 = 1
    _0xb2dfbd87 = 2
    _0x7dbfbe1c = 5
    _0x62bc30ab = 6
    _0xc2134beb = 7
    _0xc94a1eb9 = 16
    _0x071f8983 = 17
    _0xdf9be6f7 = 18
    _0x1eadbef3 = 19
    _0x5aca2ef3 = 20
    _0x9f7a439e = 21
    _0xd3f8e401 = 32
    _0xbd0f346f = 33
    _0x4a02ea49 = 34
    _0x23d902b1 = 35
    _0x864393fb = 36
    _0xb45ec562 = 37
    _0x1433a198 = 48
    _0x11a466fd = 49
    _0x7d28e53e = 50
    _0x0466542e = 51
    _0x2a6ce99f = 52
    _0x7e7123b0 = 64
    _0x1fbf5387 = 65
    _0x9816151f = 66
    _0x19fa03b3 = 80
    _0xad77f653 = 81
    _0xe533bbb0 = 82
    _0x9caf43f2 = 85
    _0x48b475f3 = 86
    _0xfc5e347a = 87
    _0x62450550 = 88
    _0x3524989a = 89
    _0x1daf7d8b = 96
    _0x6ff1747e = 97
    _0x994be855 = 98
    _0xd61cb8a1 = 99
    _0x812489c7 = 112
    _0x606f4ed7 = 113
    _0x6c5cc45c = 114
    _0x267a37a0 = 115
    _0x24ffeeac = 116
    _0xb64e7353 = 117
    _0xa1773b63 = 118
    _0x4cde94d2 = 119
    _0x22de30c1 = 120
    _0xba9ba73b = 208
    _0x0ca96bc9 = 224
    _0xd5c91382 = 240
    _0xb1b03fb1 = 241
    _0x6f4105a2 = 242
    _0x011ab303 = 243
    _0xef7944b0 = 253
    _0xaa41449a = 254

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')

class _0x27401bf3(IntEnum):
    _0x4059b025 = 0
    _0xec53a8c4 = 1
    _0xee97be03 = 2
    _0x5208b345 = 3
    _0x56f0605c = 4
    _0x922337c3 = 5
_0x38d78852: dict[int, str] = {0: _0xd14e4b1f('496e666f'), 1: _0xd14e4b1f('537461747573'), 2: _0xd14e4b1f('436f6d6d616e64'), 3: _0xd14e4b1f('4e766d'), 4: _0xd14e4b1f('50726f746563746564'), 5: _0xd14e4b1f('436f6d6d616e644c6f636b6564')}

def _0x77301576(_0x2063c160):
    try:
        _0xa0982538 = int(_0x2063c160)
    except (TypeError, ValueError):
        return str(_0x2063c160)
    return _0x38d78852.get(_0xa0982538, str(_0xa0982538))

class _0x340e827c(IntEnum):
    _0x92e592d9 = 0
    _0x6ce976e8 = 1
    _0x127d04b8 = 2
    _0x8f19a8c7 = 3
    _0xf670ea66 = 4
    _0x6a7e7316 = 5
    _0xc442a6c2 = 6
    _0xadaaee4b = 7
    _0x27118326 = 8
    _0x64d12922 = 9
    _0xcf20423e = 10
    _0x084c8428 = 11
    _0x471c4cee = 12
    _0x95cc683e = 13
    _0x3b3e62b3 = 14
    _0x71fed0c3 = 15
_0xff237030: dict[int, str] = {0: _0xd14e4b1f('556e75736564'), 1: _0xd14e4b1f('42696e617279'), 2: _0xd14e4b1f('4d696c6c695365636f6e6473'), 3: _0xd14e4b1f('5365636f6e6473'), 4: _0xd14e4b1f('4d696e75746573'), 5: _0xd14e4b1f('486f757273'), 6: _0xd14e4b1f('5065726d696c6c'), 7: _0xd14e4b1f('50657263656e74'), 8: _0xd14e4b1f('537472696e67'), 9: _0xd14e4b1f('436f756e746572'), 10: _0xd14e4b1f('456e756d'), 11: _0xd14e4b1f('4f66664f6e'), 12: _0xd14e4b1f('4f66664f6e4175746f'), 13: _0xd14e4b1f('54696d655374616d70557463'), 14: _0xd14e4b1f('54696d655374616d704c6f63616c'), 15: _0xd14e4b1f('5369676e6564')}

def _0x4da742b9(_0x2063c160):
    try:
        _0xa0982538 = int(_0x2063c160)
    except (TypeError, ValueError):
        return str(_0x2063c160)
    return _0xff237030.get(_0xa0982538, str(_0xa0982538))

class _0xa7830531(IntEnum):
    _0xa60852f2 = 0
    _0xd17cc4f1 = 1
    _0xdf0df5de = 2
    _0x365b2699 = 3
    _0xe71e273e = 4
    _0xd0f2e537 = 5
    _0x148d8434 = 6
    _0xdb9e192b = 7
    _0x7410e537 = 8
    _0xc85f85f7 = 9
    _0x8a03add8 = 10
    _0x6d3cb253 = 11
    _0x144ff5d2 = 11
_0x2f0a2f65: dict[int, str] = {0: _0xd14e4b1f('4f6b'), 1: _0xd14e4b1f('496e76616c69644964'), 2: _0xd14e4b1f('496e76616c6964496e7374616e6365'), 3: _0xd14e4b1f('4f75744f6652616e6765'), 4: _0xd14e4b1f('496e76616c696453746f72616765'), 5: _0xd14e4b1f('4c6f636b6564'), 6: _0xd14e4b1f('4e6f744e6f7469666961626c65'), 7: _0xd14e4b1f('4f7074696f6e4e6f74537570706f72746564'), 8: _0xd14e4b1f('496e76616c69644c656e677468'), 9: _0xd14e4b1f('496e76616c696454797065'), 10: _0xd14e4b1f('496e76616c69644265686176696f72'), 11: _0xd14e4b1f('416c7265616479496e557365')}

def _0x367daf70(_0x2063c160):
    try:
        _0xa0982538 = int(_0x2063c160)
    except (TypeError, ValueError):
        return str(_0x2063c160)
    return _0x2f0a2f65.get(_0xa0982538, f"{_0xd14e4b1f('3078')}{_0xa0982538:{_0xd14e4b1f('303258')}}")

def _0xaf5f5547(h):
    return bytes.fromhex(h)
logger = _geberit_get_disabled_logger(__name__)
_0xf109778f = bytes([78, 179, 39, 240, 92, 145, 168, 61, 118, 197, 15, 226, 147, 26, 104, 84])
_0xbf2eeea2 = bytes([159, 146, 173, 121, 170, 155, 106, 169, 91, 129, 47, 155, 231, 74, 255, 234])
_0xa539a89b = bytes((a ^ b for (a, b) in zip(_0xbf2eeea2, _0xf109778f)))
_0xcc969a34 = 0
_0x88051683 = 1
_0x271d2e9f = 16
_0xb18d578a = 17
_0x9e8b3cf0 = 18
_0xdbfca2ed = 19
_0x3cf22d43 = 32
_0x99d7d08d = 7
_0x432c9900 = 12

def _0xb18a1d37(_0x8d777f38):
    _0xf5ad59c5 = 0
    for _0x40ea57d3 in _0x8d777f38:
        _0xf5ad59c5 ^= _0x40ea57d3
        for _ in range(8):
            if _0xf5ad59c5 & 1:
                _0xf5ad59c5 = _0xf5ad59c5 >> 1 ^ 33800
            else:
                _0xf5ad59c5 >>= 1
    return _0xf5ad59c5

def _0x1679fd0e(_0x8d777f38):
    _0xb4a88417 = bytearray()
    _0xac3a3498 = 0
    _0xb4a88417.append(0)
    _0xc1336794 = 1
    for _0x40ea57d3 in _0x8d777f38:
        if _0x40ea57d3 == 0:
            _0xb4a88417[_0xac3a3498] = _0xc1336794
            _0xac3a3498 = len(_0xb4a88417)
            _0xb4a88417.append(0)
            _0xc1336794 = 1
        else:
            _0xb4a88417.append(_0x40ea57d3)
            _0xc1336794 += 1
            if _0xc1336794 == 255:
                _0xb4a88417[_0xac3a3498] = _0xc1336794
                _0xac3a3498 = len(_0xb4a88417)
                _0xb4a88417.append(0)
                _0xc1336794 = 1
    _0xb4a88417[_0xac3a3498] = _0xc1336794
    return bytes(_0xb4a88417)

def _0x5eab4a1b(_0x8d777f38):
    _0xb4a88417 = bytearray()
    _0x865c0c0b = 0
    while _0x865c0c0b < len(_0x8d777f38):
        _0xc1336794 = _0x8d777f38[_0x865c0c0b]
        if _0xc1336794 == 0:
            raise ValueError(_0xd14e4b1f('434f42533a20756e6578706563746564203078303020696e20656e636f646564207061796c6f6164'))
        _0x865c0c0b += 1
        for _ in range(_0xc1336794 - 1):
            if _0x865c0c0b >= len(_0x8d777f38):
                raise ValueError(_0xd14e4b1f('434f42533a207472756e63617465642064617461'))
            _0xb4a88417.append(_0x8d777f38[_0x865c0c0b])
            _0x865c0c0b += 1
        if _0xc1336794 != 255 and _0x865c0c0b < len(_0x8d777f38):
            _0xb4a88417.append(0)
    return bytes(_0xb4a88417)

class _0x8fd6a4a1:
    __slots__ = (_0xd14e4b1f('5f30786462336166333762'), _0xd14e4b1f('5f30783935663438363463'), _0xd14e4b1f('5f30783038336538363433'), _0xd14e4b1f('5f30783963646666636533'))

    def __init__(self, key, nonce2):
        _0x41bb118a = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()).encryptor()
        self._0xdb3af37b = _0x41bb118a
        self._0x95f4864c = bytearray(nonce2)
        self._0x083e8643 = bytearray(_0x41bb118a.update(bytes(self._0x95f4864c)))
        self._0x9cdffce3 = 0
        _0x2817f701 = int.from_bytes(self._0x95f4864c[12:16], _0xd14e4b1f('626967'))
        self._0x95f4864c[12:16] = (_0x2817f701 + 1 & 4294967295).to_bytes(4, _0xd14e4b1f('626967'))

    def _0xff5d2a3d(self):
        self._0x083e8643 = bytearray(self._0xdb3af37b.update(bytes(self._0x95f4864c)))
        self._0x9cdffce3 = 0
        _0x2817f701 = int.from_bytes(self._0x95f4864c[12:16], _0xd14e4b1f('626967'))
        self._0x95f4864c[12:16] = (_0x2817f701 + 1 & 4294967295).to_bytes(4, _0xd14e4b1f('626967'))

    def process(self, data):
        _0xb4a88417 = bytearray(len(data))
        for (_0x865c0c0b, _0x92eb5ffe) in enumerate(data):
            if self._0x9cdffce3 >= 16:
                self._0xff5d2a3d()
            _0xb4a88417[_0x865c0c0b] = _0x92eb5ffe ^ self._0x083e8643[self._0x9cdffce3]
            self._0x9cdffce3 += 1
        return bytes(_0xb4a88417)

def _0xfee5b567(ikm, salt, length):
    return HKDF(algorithm=SHA256(), length=length, salt=salt, info=b'', backend=default_backend()).derive(ikm)

def _0x1e073f26(_0x3c6e0b8a, _0x8d777f38):
    _0x4a8a08f0 = CMAC(algorithms.AES(_0x3c6e0b8a), backend=default_backend())
    _0x4a8a08f0.update(_0x8d777f38)
    return _0x4a8a08f0.finalize()

class _0xb588dc14:

    def __init__(self):
        self._0x616cdacf = bytearray()
        self._0x9ec303ef = asyncio.Queue()
        self._0x94cec6e0 = 0
        self._0xc131c528 = 0
        self._0x70076ca9 = 0
        self._0x830f9761 = None
        self._0x5bb33f10 = None
        self._0x8ca8c867 = bytearray()
        self._0x926af308 = None
        self.handshake_done = False
        self._0x35f6c984 = False

    @staticmethod
    def _0x29e810fc(_0x59558d2c):
        return _0x59558d2c << 3 & 224 | _0x59558d2c << 2 & 12 | 3

    def _0xed95bcf5(self):
        return self._0xc131c528 << 5 & 224 | self._0x94cec6e0 << 1 & 14

    def _0xbc90f604(self):
        return self._0xc131c528 << 5 & 224 | 1

    def _0x6c8bbe77(self, _0xbbf7ea1d, _0x321c3cf4):
        _0xbdd166af = bytes([_0xbbf7ea1d]) + _0x321c3cf4
        _0xf5ad59c5 = _0xb18a1d37(_0xbdd166af)
        return _0xaf5f5547('00') + _0x1679fd0e(_0xbdd166af + bytes([_0xf5ad59c5 & 255, _0xf5ad59c5 >> 8 & 255])) + _0xaf5f5547('00')

    def _0xc4078f48(self, _0x93cc3e76):
        return self._0x6c8bbe77(self._0x29e810fc(_0x93cc3e76), b'')

    def _0xa30984c4(self, _0x937b5a2e):
        _0x65db43f2 = self._0x6c8bbe77(self._0xed95bcf5(), _0x937b5a2e)
        self._0x94cec6e0 = (self._0x94cec6e0 + 1) % 8
        return _0x65db43f2

    def _0x5c8ffadd(self):
        return self._0x6c8bbe77(self._0xbc90f604(), b'')

    def _0x001bcb2c(self, _0x8d777f38):
        _0x53e61336 = []
        self._0x8ca8c867.extend(_0x8d777f38)
        while 0 in self._0x8ca8c867:
            _0x7f9bec28 = self._0x8ca8c867.index(0)
            if _0x7f9bec28 == 0:
                del self._0x8ca8c867[0]
                continue
            _0x48110db5 = bytes(self._0x8ca8c867[:_0x7f9bec28])
            del self._0x8ca8c867[:_0x7f9bec28 + 1]
            try:
                _0xad054584 = _0x5eab4a1b(_0x48110db5)
            except ValueError as _0xe1671797:
                continue
            if len(_0xad054584) < 2:
                continue
            _0xb8d6cb23 = _0xad054584[-2] | _0xad054584[-1] << 8
            if _0xb18a1d37(_0xad054584[:-2]) == _0xb8d6cb23:
                _0x53e61336.append(_0xad054584[:-2])
        return _0x53e61336

    def feed_att_bytes(self, data):
        self._0x616cdacf.extend(data)
        self._0x370ef30c()
        if not self.handshake_done:
            return []
        _0x53e61336 = []
        _0x410722c5 = self._0x9ec303ef.qsize()
        while not self._0x9ec303ef.empty():
            try:
                (_0x49af3b64, _0xbbf7ea1d, _0x321c3cf4) = self._0x9ec303ef.get_nowait()
                if _0x49af3b64 == _0xd14e4b1f('49') and _0x321c3cf4 and (_0x321c3cf4[0] == _0x3cf22d43):
                    _0x63b65568 = self._0x830f9761.process(_0x321c3cf4[1:])
                    _0x53e61336.extend(self._0x001bcb2c(_0x63b65568))
                elif _0x49af3b64 == _0xd14e4b1f('49'):
                    pass
            except asyncio.QueueEmpty:
                break
        return _0x53e61336

    def _0x370ef30c(self):
        while True:
            _0xcb7e52b2 = self._0x616cdacf
            if not _0xcb7e52b2 or _0xcb7e52b2[0] != 0:
                _0x7f9bec28 = _0xcb7e52b2.find(_0xaf5f5547('00'))
                if _0x7f9bec28 == -1:
                    self._0x616cdacf = bytearray()
                    return
                self._0x616cdacf = _0xcb7e52b2[_0x7f9bec28:]
                _0xcb7e52b2 = self._0x616cdacf
            _0x7f021a14 = _0xcb7e52b2.find(_0xaf5f5547('00'), 1)
            if _0x7f021a14 == -1:
                return
            _0x73b9aaa3 = bytes(_0xcb7e52b2[1:_0x7f021a14])
            self._0x616cdacf = _0xcb7e52b2[_0x7f021a14:]
            if not _0x73b9aaa3:
                continue
            try:
                _0xad054584 = _0x5eab4a1b(_0x73b9aaa3)
            except ValueError as _0xe1671797:
                continue
            if len(_0xad054584) < 3:
                continue
            _0xb8d6cb23 = _0xad054584[-2] | _0xad054584[-1] << 8
            _0xbec5ba31 = _0xb18a1d37(_0xad054584[:-2])
            if _0xb8d6cb23 != _0xbec5ba31:
                continue
            _0xbbf7ea1d = _0xad054584[0]
            _0xe46df7f3 = _0xad054584[1:-2]
            if _0xbbf7ea1d & 1 == 0:
                _0x317d05d7 = _0xbbf7ea1d >> 1 & 7
                if _0x317d05d7 == self._0x70076ca9:
                    self._0x70076ca9 = (self._0x70076ca9 + 1) % 8
                    self._0xc131c528 = (_0x317d05d7 + 1) % 8
                    self._0x9ec303ef.put_nowait((_0xd14e4b1f('49'), _0xbbf7ea1d, _0xe46df7f3))
                    _0xdb1e3628 = f"{_0xd14e4b1f('3078')}{_0xe46df7f3[0]:{_0xd14e4b1f('303258')}}" if _0xe46df7f3 else _0xd14e4b1f('30783f3f')
                if self.handshake_done and self._0x926af308 is not None:
                    if not self._0x35f6c984:
                        self._0x35f6c984 = True
                        try:
                            asyncio.get_running_loop().create_task(self._0x4777b5b7())
                        except RuntimeError:
                            pass
            elif _0xbbf7ea1d & 3 == 3:
                self._0x9ec303ef.put_nowait((_0xd14e4b1f('55'), _0xbbf7ea1d, _0xe46df7f3))

    async def _0x5feda47d(self, _0xe29863a0, _0x90272dda=5.0):
        _0x30e482a8 = asyncio.get_event_loop().time() + _0x90272dda
        while True:
            _0x2626772c = _0x30e482a8 - asyncio.get_event_loop().time()
            if _0x2626772c <= 0:
                raise TimeoutError(f"{_0xd14e4b1f('4172656e646953656375726974793a2074696d656f75742077616974696e6720666f7220552d6672616d65206374726c3d3078')}{_0xe29863a0:{_0xd14e4b1f('303258')}}")
            try:
                (_0x49af3b64, _0xbbf7ea1d, _) = await asyncio.wait_for(self._0x9ec303ef.get(), timeout=_0x2626772c)
            except asyncio.TimeoutError:
                raise TimeoutError(f"{_0xd14e4b1f('4172656e646953656375726974793a2074696d656f75742077616974696e6720666f7220552d6672616d65206374726c3d3078')}{_0xe29863a0:{_0xd14e4b1f('303258')}}")
            if _0x49af3b64 == _0xd14e4b1f('55') and _0xbbf7ea1d == _0xe29863a0:
                return

    async def _0x5fef2e5d(self, _0x8ae82a23, _0x90272dda=5.0):
        _0x30e482a8 = asyncio.get_event_loop().time() + _0x90272dda
        while True:
            _0x2626772c = _0x30e482a8 - asyncio.get_event_loop().time()
            if _0x2626772c <= 0:
                raise TimeoutError(f"{_0xd14e4b1f('4172656e646953656375726974793a2074696d656f75742077616974696e6720666f722053656375726974792074797065203078')}{_0x8ae82a23:{_0xd14e4b1f('303258')}}")
            try:
                (_0x49af3b64, _0xbbf7ea1d, _0x321c3cf4) = await asyncio.wait_for(self._0x9ec303ef.get(), timeout=_0x2626772c)
            except asyncio.TimeoutError:
                raise TimeoutError(f"{_0xd14e4b1f('4172656e646953656375726974793a2074696d656f75742077616974696e6720666f722053656375726974792074797065203078')}{_0x8ae82a23:{_0xd14e4b1f('303258')}}")
            if _0x49af3b64 == _0xd14e4b1f('49') and _0x321c3cf4 and (_0x321c3cf4[0] == _0x8ae82a23):
                return _0x321c3cf4
            _0x78336efc = f"{_0xd14e4b1f('3078')}{_0x321c3cf4[0]:{_0xd14e4b1f('303258')}}" if _0x321c3cf4 else _0xd14e4b1f('30783f3f')

    async def perform_handshake(self, send_fn):
        self._0x94cec6e0 = 0
        self._0xc131c528 = 0
        self._0x70076ca9 = 0
        await send_fn(self._0xc4078f48(_0x99d7d08d))
        await self._0x5feda47d(self._0x29e810fc(_0x432c9900))
        await send_fn(self._0xa30984c4(bytes([_0xcc969a34])))
        _0x8295c40b = await self._0x5fef2e5d(_0x88051683)
        if len(_0x8295c40b) >= 7:
            _0xadee6e2d = _0x8295c40b[6] + 1
        await send_fn(self._0xa30984c4(bytes([_0x271d2e9f])))
        _0x6aa1e040 = await self._0x5fef2e5d(_0xb18d578a)
        if len(_0x6aa1e040) < 33:
            raise ValueError(f"{_0xd14e4b1f('4172656e646953656375726974793a20455020526573706f6e736520746f6f2073686f72742028')}{len(_0x6aa1e040)}{_0xd14e4b1f('20627974657329')}")
        _0xc9f5731c = _0x6aa1e040[1:17]
        _0xb4d446e2 = _0x6aa1e040[17:33]
        if len(_0x6aa1e040) >= 35:
            _0xecf8b61d = _0x6aa1e040[33] | _0x6aa1e040[34] << 8
        _0xf0729595 = _0xfee5b567(ikm=_0xa539a89b, salt=_0xc9f5731c, length=16)
        _0x156a1733 = X25519PrivateKey.generate()
        _0x4231b3e7 = _0x156a1733.public_key().public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw)
        _0x3f252313 = _0x1e073f26(_0xf0729595, _0x4231b3e7)
        _0xfb639400 = bytes([_0x9e8b3cf0]) + _0x4231b3e7 + _0x3f252313 + bytes([0])
        await send_fn(self._0xa30984c4(_0xfb639400))
        _0x25bc6654 = await self._0x5fef2e5d(_0xdbfca2ed, _0x90272dda=5.0)
        if len(_0x25bc6654) < 49:
            raise ValueError(f"{_0xd14e4b1f('4172656e646953656375726974793a204b4520526573706f6e736520746f6f2073686f72742028')}{len(_0x25bc6654)}{_0xd14e4b1f('20627974657329')}")
        _0xc54e4fb8 = _0x25bc6654[1:33]
        _0x38cf27af = _0x25bc6654[33:49]
        _0xc4f54c9e = _0x1e073f26(_0xf0729595, _0xc54e4fb8)
        if _0x38cf27af != _0xc4f54c9e:
            raise ValueError(_0xd14e4b1f('4172656e646953656375726974793a2073657276657220434d414320766572696669636174696f6e206661696c6564'))
        _0x831c5c24 = X25519PublicKey.from_public_bytes(_0xc54e4fb8)
        _0x17b3483a = _0x156a1733.exchange(_0x831c5c24)
        _0x07ae8b01 = _0xfee5b567(ikm=_0x17b3483a, salt=_0xc9f5731c, length=32)
        _0x9aba22e0 = _0x07ae8b01[0:16]
        _0x690d3dcf = _0x07ae8b01[16:32]
        self._0x830f9761 = _0x8fd6a4a1(_0x9aba22e0, _0xb4d446e2)
        self._0x5bb33f10 = _0x8fd6a4a1(_0x690d3dcf, _0xb4d446e2)
        await send_fn(self._0x5c8ffadd())
        self.handshake_done = True

    async def _0x4777b5b7(self):
        self._0x35f6c984 = False
        try:
            await self._0x926af308(self._0x5c8ffadd())
        except Exception as _0x56bd7107:
            pass

    def wrap_for_send(self, geberit_payload):
        _0xf5ad59c5 = _0xb18a1d37(geberit_payload)
        _0x46f91065 = _0xaf5f5547('00') + _0x1679fd0e(geberit_payload + bytes([_0xf5ad59c5 & 255, _0xf5ad59c5 >> 8 & 255])) + _0xaf5f5547('00')
        _0xcb546167 = self._0x5bb33f10.process(_0x46f91065)
        return self._0xa30984c4(bytes([_0x3cf22d43]) + _0xcb546167)
_0xd10dc178 = int | tuple[int, int]

def _0xd2cdd886(_0xea9f6aca):

    @wraps(_0xea9f6aca)
    async def _0x3a807a13(self, *_0xa956af09, **_0x9d6f6736):
        async with self._0xfdfb8170:
            return await _0xea9f6aca(self, *_0xa956af09, **_0x9d6f6736)
    return _0x3a807a13

def _0x12215fbb(_0x32e2cb0f, _0x7123a699=None):
    _0x7ce8636c = _0x32e2cb0f & 255
    _0x49f68a5c = _0x32e2cb0f >> 8 & 127
    if _0x7123a699 is not None:
        return bytes([_0x7ce8636c, _0x49f68a5c | 128, _0x7123a699])
    return bytes([_0x7ce8636c, _0x49f68a5c])

def _0xbefb508d(_0x8d777f38, _0x7a86c157=1):
    _0x7ce8636c = _0x8d777f38[_0x7a86c157]
    _0x49f68a5c = _0x8d777f38[_0x7a86c157 + 1]
    _0x81d6838a = bool(_0x49f68a5c & 128)
    _0x32e2cb0f = (_0x49f68a5c & 127) << 8 | _0x7ce8636c
    if _0x81d6838a:
        return (_0x32e2cb0f, _0x8d777f38[_0x7a86c157 + 2], _0x7a86c157 + 3)
    return (_0x32e2cb0f, None, _0x7a86c157 + 2)

class _0x6e2f7964:
    _0x8f4d52f0 = 30.0
    _0xf4946ef5 = _0xdaef1eb3

    def __init__(self, connector):
        self._0xa74bbcc7 = connector
        self._0x9ec303ef = asyncio.Queue()
        self._0x01a92fb8 = deque()
        self._0xe918bbec = {}
        self._0xfdfb8170 = asyncio.Lock()
        connector.data_received_handlers += self._0x5df4c7c4

    def _0x739494eb(self, _0x32e2cb0f, _0x7123a699=None):
        return _0x32e2cb0f if _0x7123a699 is None else (_0x32e2cb0f, _0x7123a699)

    async def _0x5df4c7c4(self, _0x8d777f38):
        if not _0x8d777f38:
            return
        _0xdfff0a7f = _0x8d777f38[0]
        if _0xdfff0a7f == _0xc716531b._0x2a6ce99f and len(_0x8d777f38) >= 3:
            (_0x32e2cb0f, _0x7123a699, _) = _0xbefb508d(_0x8d777f38, 1)
            _0x958b30d4 = self._0x739494eb(_0x32e2cb0f, _0x7123a699)
            _0x7694f4a6 = self._0xe918bbec.get(_0x958b30d4)
            if _0x7694f4a6 is None and _0x7123a699 is not None:
                _0x7694f4a6 = self._0xe918bbec.get(_0x32e2cb0f)
            if _0x7694f4a6 is not None:
                _0x7694f4a6.put_nowait(_0x8d777f38)
                return
        self._0x9ec303ef.put_nowait(_0x8d777f38)

    async def _0xa1f56c48(self, _0x90272dda=_0x8f4d52f0):
        if self._0x01a92fb8:
            return self._0x01a92fb8.popleft()
        return await asyncio.wait_for(self._0x9ec303ef.get(), timeout=_0x90272dda)

    def _0xf011d8a1(self, _0xdcdc1ac0):
        for _0xdcf3e36e in reversed(_0xdcdc1ac0):
            self._0x01a92fb8.appendleft(_0xdcf3e36e)

    async def _0x54f479aa(self, _0xf670ef68, _0x90272dda, _0x69c9a2c9):
        _0x30e482a8 = asyncio.get_event_loop().time() + _0x90272dda
        _0x67dd31fa = []
        try:
            while True:
                _0x2626772c = _0x30e482a8 - asyncio.get_event_loop().time()
                if _0x2626772c <= 0:
                    raise asyncio.TimeoutError()
                _0xdcf3e36e = await self._0xa1f56c48(_0x90272dda=_0x2626772c)
                if _0xf670ef68(_0xdcf3e36e):
                    self._0xf011d8a1(_0x67dd31fa)
                    return _0xdcf3e36e
                _0x67dd31fa.append(_0xdcf3e36e)
        except Exception:
            self._0xf011d8a1(_0x67dd31fa)
            raise

    async def _0xaa362864(self, _0x321c3cf4):
        await self._0xa74bbcc7.send_message(_0x321c3cf4)

    def _0xd9d1654b(self, _0xdcf3e36e, _0x32e2cb0f, _0x7123a699):
        if _0xdcf3e36e[0] not in (_0xc716531b._0x7d28e53e, _0xc716531b._0x0466542e):
            return False
        (_0x50fd69a3, _0x1b395a2b, _) = _0xbefb508d(_0xdcf3e36e, 1)
        return _0x50fd69a3 == _0x32e2cb0f and _0x1b395a2b == _0x7123a699

    @_0xd2cdd886
    async def inventory(self):
        await self._0xaa362864(bytes([_0xc716531b._0x4d604dd8, 0]))
        while True:
            _0xdcf3e36e = await self._0xa1f56c48()
            if _0xdcf3e36e[0] == _0xc716531b._0xcffd2071:
                break
        _0xe2942a04 = struct.unpack_from(_0xd14e4b1f('3c48'), _0xdcf3e36e, 1)[0]
        _0xb4a88417 = {}
        _0xc5946eb9 = 0
        while _0xc5946eb9 < _0xe2942a04:
            _0xdcf3e36e = await self._0xa1f56c48()
            if _0xdcf3e36e[0] != _0xc716531b._0xb2dfbd87:
                continue
            (_0x32e2cb0f, _0x7123a699, _0xbf993e7e) = _0xbefb508d(_0xdcf3e36e, 1)
            _0x321c3cf4 = _0xdcf3e36e[_0xbf993e7e:]
            if len(_0x321c3cf4) < 11:
                _0xc5946eb9 += 1
                continue
            _0x4e5868d6 = _0x321c3cf4[10]
            _0xb4a88417[_0x32e2cb0f] = {_0xd14e4b1f('696e7374616e6365'): _0x7123a699, _0xd14e4b1f('76657273696f6e'): _0x321c3cf4[0], _0xd14e4b1f('6461746174797065'): _0x321c3cf4[1], _0xd14e4b1f('6d696e5f73'): struct.unpack_from(_0xd14e4b1f('3c69'), _0x321c3cf4, 2)[0], _0xd14e4b1f('6d61785f73'): struct.unpack_from(_0xd14e4b1f('3c69'), _0x321c3cf4, 6)[0], _0xd14e4b1f('6d696e5f75'): struct.unpack_from(_0xd14e4b1f('3c49'), _0x321c3cf4, 2)[0], _0xd14e4b1f('6d61785f75'): struct.unpack_from(_0xd14e4b1f('3c49'), _0x321c3cf4, 6)[0], _0xd14e4b1f('69735f696e7465726e616c'): bool(_0x4e5868d6 & 128), _0xd14e4b1f('6265686176696f72'): _0x4e5868d6 & 127}
            _0xc5946eb9 += 1
        return _0xb4a88417

    @_0xd2cdd886
    async def read(self, dp_id, instance=None):
        _0x3ef9a0d7 = _0x12215fbb(dp_id, instance)
        await self._0xaa362864(bytes([_0xc716531b._0xc94a1eb9]) + _0x3ef9a0d7)

        def _0x303e48f2(_0xdcf3e36e):
            if _0xdcf3e36e[0] not in (_0xc716531b._0x071f8983, _0xc716531b._0xdf9be6f7):
                return False
            (_0x50fd69a3, _0x1b395a2b, _) = _0xbefb508d(_0xdcf3e36e, 1)
            return _0x50fd69a3 == dp_id and _0x1b395a2b == instance
        _0xdcf3e36e = await self._0x54f479aa(_0x303e48f2, self._0x8f4d52f0, _0xd14e4b1f('426c6532303a20736b697070696e67206672616d6520636d643d30782530325820286177616974696e67206d61746368696e672052656164416e7329'))
        if _0xdcf3e36e[0] == _0xc716531b._0xdf9be6f7:
            (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
            _0x9acb4454 = _0xdcf3e36e[_0x3262d48d] if _0x3262d48d < len(_0xdcf3e36e) else 255
            raise IOError(f"{_0xd14e4b1f('526561644572726f722064705f69643d')}{dp_id}{_0xd14e4b1f('3a20')}{_0x2104ae2e(_0x9acb4454)}")
        (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
        return _0xdcf3e36e[_0x3262d48d:]

    @_0xd2cdd886
    async def read_many(self, addresses, timeout=_0x8f4d52f0):
        if not addresses:
            return ({}, {})
        _0xcd26d9e1 = {}
        _0x7c2d8e76 = []
        for _0x447b7147 in addresses:
            if isinstance(_0x447b7147, tuple):
                _0x3c6e0b8a = (int(_0x447b7147[0]), int(_0x447b7147[1]))
            else:
                _0x3c6e0b8a = int(_0x447b7147)
            if _0x3c6e0b8a in _0xcd26d9e1:
                continue
            _0xcd26d9e1[_0x3c6e0b8a] = _0x3c6e0b8a
            _0x7c2d8e76.append(_0x3c6e0b8a)
        _0xa9f0a3a6 = {}
        _0x07213a01 = {}
        _0x79e9522c = {}
        _0x88c2c94b = 0

        async def _0x681c23be():
            nonlocal _0x88c2c94b
            _0x3c6e0b8a = _0x7c2d8e76[_0x88c2c94b]
            _0x88c2c94b += 1
            if isinstance(_0x3c6e0b8a, tuple):
                (_0x32e2cb0f, _0x7123a699) = _0x3c6e0b8a
            else:
                (_0x32e2cb0f, _0x7123a699) = (_0x3c6e0b8a, None)
            await self._0xaa362864(bytes([_0xc716531b._0xc94a1eb9]) + _0x12215fbb(_0x32e2cb0f, _0x7123a699))
            _0x79e9522c[_0x3c6e0b8a] = asyncio.get_event_loop().time() + timeout
        _0x67dd31fa = []
        try:
            while _0x79e9522c or _0x88c2c94b < len(_0x7c2d8e76):
                while _0x88c2c94b < len(_0x7c2d8e76) and len(_0x79e9522c) < self._0xf4946ef5:
                    await _0x681c23be()
                _0x97bc592b = asyncio.get_event_loop().time()
                _0x1f1a575a = [_0x3c6e0b8a for (_0x3c6e0b8a, _0xc8fa1376) in _0x79e9522c.items() if _0xc8fa1376 <= _0x97bc592b]
                for _0x3c6e0b8a in _0x1f1a575a:
                    (_0x32e2cb0f, _) = _0x3c6e0b8a if isinstance(_0x3c6e0b8a, tuple) else (_0x3c6e0b8a, None)
                    _0x07213a01[_0x3c6e0b8a] = IOError(f"{_0xd14e4b1f('526561644572726f722064705f69643d')}{_0x32e2cb0f}{_0xd14e4b1f('3a2074696d656f7574')}")
                    del _0x79e9522c[_0x3c6e0b8a]
                if _0x1f1a575a:
                    continue
                _0x2626772c = min(_0x79e9522c.values()) - _0x97bc592b
                try:
                    _0xdcf3e36e = await self._0xa1f56c48(_0x90272dda=_0x2626772c)
                except asyncio.TimeoutError:
                    continue
                if _0xdcf3e36e[0] not in (_0xc716531b._0x071f8983, _0xc716531b._0xdf9be6f7):
                    _0x67dd31fa.append(_0xdcf3e36e)
                    continue
                (_0x32e2cb0f, _0x7123a699, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
                _0xbb3a7a75 = _0x32e2cb0f if _0x7123a699 is None else (_0x32e2cb0f, _0x7123a699)
                _0xb23b9c06 = _0xbb3a7a75
                if _0xb23b9c06 not in _0xcd26d9e1 and _0x7123a699 is not None and (_0x32e2cb0f in _0xcd26d9e1):
                    _0xb23b9c06 = _0x32e2cb0f
                if _0xb23b9c06 not in _0xcd26d9e1:
                    _0x67dd31fa.append(_0xdcf3e36e)
                    continue
                if _0xb23b9c06 not in _0x79e9522c:
                    continue
                if _0xdcf3e36e[0] == _0xc716531b._0xdf9be6f7:
                    _0x9acb4454 = _0xdcf3e36e[_0x3262d48d] if _0x3262d48d < len(_0xdcf3e36e) else 255
                    _0x07213a01[_0xb23b9c06] = IOError(f"{_0xd14e4b1f('526561644572726f722064705f69643d')}{_0x32e2cb0f}{_0xd14e4b1f('3a20')}{_0x2104ae2e(_0x9acb4454)}")
                else:
                    _0xa9f0a3a6[_0xb23b9c06] = _0xdcf3e36e[_0x3262d48d:]
                del _0x79e9522c[_0xb23b9c06]
        finally:
            self._0xf011d8a1(_0x67dd31fa)
        for _0x3c6e0b8a in _0x7c2d8e76:
            if _0x3c6e0b8a in _0xa9f0a3a6 or _0x3c6e0b8a in _0x07213a01:
                continue
            if isinstance(_0x3c6e0b8a, tuple):
                (_0x32e2cb0f, _) = _0x3c6e0b8a
            else:
                _0x32e2cb0f = _0x3c6e0b8a
            _0x07213a01[_0x3c6e0b8a] = IOError(f"{_0xd14e4b1f('526561644572726f722064705f69643d')}{_0x32e2cb0f}{_0xd14e4b1f('3a2074696d656f7574')}")
        return (_0xa9f0a3a6, _0x07213a01)

    @_0xd2cdd886
    async def write(self, dp_id, value, instance=None):
        _0x3ef9a0d7 = _0x12215fbb(dp_id, instance)
        await self._0xaa362864(bytes([_0xc716531b._0xd3f8e401]) + _0x3ef9a0d7 + value)

        def _0x303e48f2(_0xdcf3e36e):
            if _0xdcf3e36e[0] not in (_0xc716531b._0xbd0f346f, _0xc716531b._0x4a02ea49):
                return False
            (_0x50fd69a3, _0x1b395a2b, _) = _0xbefb508d(_0xdcf3e36e, 1)
            return _0x50fd69a3 == dp_id and _0x1b395a2b == instance
        _0xdcf3e36e = await self._0x54f479aa(_0x303e48f2, self._0x8f4d52f0, _0xd14e4b1f('426c6532303a20736b697070696e67206672616d6520636d643d30782530325820286177616974696e67206d61746368696e6720577269746541636b29'))
        if _0xdcf3e36e[0] == _0xc716531b._0x4a02ea49:
            (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
            _0x9acb4454 = _0xdcf3e36e[_0x3262d48d] if _0x3262d48d < len(_0xdcf3e36e) else 255
            raise IOError(f"{_0xd14e4b1f('57726974654572726f722064705f69643d')}{dp_id}{_0xd14e4b1f('3a20')}{_0x2104ae2e(_0x9acb4454)}")

    @_0xd2cdd886
    async def enable_notification(self, dp_ids):
        _0xa1031145 = set()
        for _0x447b7147 in dp_ids:
            if isinstance(_0x447b7147, tuple):
                _0x32e2cb0f = int(_0x447b7147[0])
                _0x7123a699 = int(_0x447b7147[1])
            else:
                _0x32e2cb0f = int(_0x447b7147)
                _0x7123a699 = None
            _0x3ef9a0d7 = _0x12215fbb(_0x32e2cb0f, _0x7123a699)
            await self._0xaa362864(bytes([_0xc716531b._0x1433a198]) + _0x3ef9a0d7)
            _0xdcf3e36e = await self._0x54f479aa(lambda _0xdcf3e36e: self._0xd9d1654b(_0xdcf3e36e, _0x32e2cb0f, _0x7123a699), self._0x8f4d52f0, _0xd14e4b1f('426c6532303a20736b697070696e67206672616d6520636d643d30782530325820286177616974696e67206d61746368696e67204e6f7469667941636b29'))
            if _0xdcf3e36e[0] == _0xc716531b._0x7d28e53e:
                _0x958b30d4 = self._0x739494eb(_0x32e2cb0f, _0x7123a699)
                if _0x958b30d4 not in self._0xe918bbec:
                    self._0xe918bbec[_0x958b30d4] = asyncio.Queue()
                _0xa1031145.add(_0x958b30d4)
            else:
                (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
                _0x9acb4454 = _0xdcf3e36e[_0x3262d48d] if _0x3262d48d < len(_0xdcf3e36e) else 255
        return _0xa1031145

    @_0xd2cdd886
    async def disable_notification(self, dp_ids):
        _0x075ae3d2 = set()
        for _0x447b7147 in dp_ids:
            if isinstance(_0x447b7147, tuple):
                _0x32e2cb0f = int(_0x447b7147[0])
                _0x7123a699 = int(_0x447b7147[1])
            else:
                _0x32e2cb0f = int(_0x447b7147)
                _0x7123a699 = None
            _0x3ef9a0d7 = _0x12215fbb(_0x32e2cb0f, _0x7123a699)
            await self._0xaa362864(bytes([_0xc716531b._0x11a466fd]) + _0x3ef9a0d7)
            _0xdcf3e36e = await self._0x54f479aa(lambda _0xdcf3e36e: self._0xd9d1654b(_0xdcf3e36e, _0x32e2cb0f, _0x7123a699), self._0x8f4d52f0, _0xd14e4b1f('426c6532303a20736b697070696e67206672616d6520636d643d30782530325820286177616974696e67206d61746368696e67204e6f7469667941636b29'))
            if _0xdcf3e36e[0] == _0xc716531b._0x7d28e53e:
                _0x958b30d4 = self._0x739494eb(_0x32e2cb0f, _0x7123a699)
                self._0xe918bbec.pop(_0x958b30d4, None)
                _0x075ae3d2.add(_0x958b30d4)
            else:
                (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
                _0x9acb4454 = _0xdcf3e36e[_0x3262d48d] if _0x3262d48d < len(_0xdcf3e36e) else 255
        return _0x075ae3d2

    async def get_notification(self, dp_id, instance=None, timeout=_0x8f4d52f0):
        _0x7694f4a6 = self._0xe918bbec.get(self._0x739494eb(dp_id, instance))
        if _0x7694f4a6 is None:
            raise ValueError(f"{_0xd14e4b1f('447049643d')}{dp_id}{_0xd14e4b1f('20696e7374616e63653d')}{instance}{_0xd14e4b1f('206e6f742073756273637269626564202d2063616c6c20656e61626c655f6e6f74696669636174696f6e206669727374')}")
        if timeout is None:
            _0xdcf3e36e = await _0x7694f4a6.get()
        else:
            _0xdcf3e36e = await asyncio.wait_for(_0x7694f4a6.get(), timeout=timeout)
        (_, _, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
        return _0xdcf3e36e[_0x3262d48d:]

    async def get_notification_frame(self, dp_id, instance=None, timeout=_0x8f4d52f0):
        _0x7694f4a6 = self._0xe918bbec.get(self._0x739494eb(dp_id, instance))
        if _0x7694f4a6 is None:
            raise ValueError(f"{_0xd14e4b1f('447049643d')}{dp_id}{_0xd14e4b1f('20696e7374616e63653d')}{instance}{_0xd14e4b1f('206e6f742073756273637269626564202d2063616c6c20656e61626c655f6e6f74696669636174696f6e206669727374')}")
        if timeout is None:
            return await _0x7694f4a6.get()
        return await asyncio.wait_for(_0x7694f4a6.get(), timeout=timeout)

    @_0xd2cdd886
    async def capabilities(self):
        await self._0xaa362864(bytes([_0xc716531b._0xef7944b0]))
        try:
            while True:
                _0xdcf3e36e = await self._0xa1f56c48()
                if _0xdcf3e36e[0] == _0xc716531b._0xaa41449a:
                    _0x4e5868d6 = _0xdcf3e36e[1] if len(_0xdcf3e36e) > 1 else 0
                    return _0x4e5868d6
        except asyncio.TimeoutError:
            return 0

    @_0xd2cdd886
    async def event_storage_inventory(self, capabilities_flags=0):
        _0xd3e78e3d = bool(capabilities_flags & 4)
        _0x321c3cf4 = bytes([_0xc716531b._0x19fa03b3, 1]) if _0xd3e78e3d else bytes([_0xc716531b._0x19fa03b3])
        await self._0xaa362864(_0x321c3cf4)
        try:
            _0x2626772c = 0
            while True:
                _0xdcf3e36e = await self._0xa1f56c48()
                if _0xdcf3e36e[0] == _0xc716531b._0xad77f653:
                    _0x2626772c = struct.unpack_from(_0xd14e4b1f('3c48'), _0xdcf3e36e, 1)[0] if len(_0xdcf3e36e) >= 3 else 0
                    if _0x2626772c == 0:
                        return
                elif _0xdcf3e36e[0] == _0xc716531b._0xe533bbb0:
                    _0x2626772c -= 1
                    if _0x2626772c <= 0:
                        return
        except asyncio.TimeoutError:
            pass

    async def join(self, pin=None, inv=None, timeout=15.0):
        from .DpId import DpId
        _0x15a46118 = int(543)
        _0x11973b64 = int(545)
        _0x1629a1bc = int(546)
        if inv is not None and _0x15a46118 not in inv:
            return _0xd14e4b1f('736b6970706564')
        _0x146625d1 = inv[_0x15a46118][_0xd14e4b1f('76657273696f6e')] if inv and _0x15a46118 in inv else 1
        try:
            _0xbef99584 = (await self.read(int(0)))[0]
            _0xaa7ac8cd = (await self.read(int(1)))[0]
            _0x2b8c0551 = await self.read(int(236))
            _0x69080cee = struct.unpack_from(_0xd14e4b1f('3c49'), _0x2b8c0551)[0] if len(_0x2b8c0551) >= 4 else 0
        except Exception as _0xe1671797:
            return _0xd14e4b1f('736b6970706564')

        def _0x0c26655a(_0x44fe6920):
            if _0x146625d1 == 0:
                _0x8d777f38 = bytearray(6)
                _0x8d777f38[0] = _0xbef99584
                _0x8d777f38[1] = _0xaa7ac8cd
                struct.pack_into(_0xd14e4b1f('3c49'), _0x8d777f38, 2, _0x69080cee)
                return bytes(_0x8d777f38)
            _0xf7bd60b7 = 11 if _0x146625d1 >= 2 else 10
            _0x8d777f38 = bytearray(_0xf7bd60b7)
            _0x8d777f38[0] = _0xbef99584
            _0x8d777f38[1] = _0xaa7ac8cd
            struct.pack_into(_0xd14e4b1f('3c49'), _0x8d777f38, 2, _0x69080cee)
            if _0x44fe6920:
                _0x4b719ace = _0x44fe6920.encode(_0xd14e4b1f('7574662d38'))[:4]
                _0x8d777f38[6:6 + len(_0x4b719ace)] = _0x4b719ace
            return bytes(_0x8d777f38)
        _0xc25b3700 = await self.enable_notification([_0x11973b64, _0x1629a1bc])
        _0x6b7259a5 = self._0x739494eb(_0x11973b64, None)
        _0x0fea988d = self._0x739494eb(_0x1629a1bc, None)
        if _0x6b7259a5 not in _0xc25b3700:
            return _0xd14e4b1f('736b6970706564')
        for _0x1db222fe in range(2):
            _0x5ebe2294 = None if _0x1db222fe == 0 else pin
            try:
                await self.write(_0x15a46118, _0x0c26655a(_0x5ebe2294))
            except IOError as _0xe1671797:
                return _0xd14e4b1f('736b6970706564')
            _0x3c709b10 = 0
            _0x30e482a8 = asyncio.get_event_loop().time() + timeout
            while asyncio.get_event_loop().time() < _0x30e482a8:
                _0x2626772c = _0x30e482a8 - asyncio.get_event_loop().time()
                try:
                    _0xbdd166af = await self.get_notification(_0x11973b64, timeout=_0x2626772c)
                    _0x3c709b10 = _0xbdd166af[0] if _0xbdd166af else 255
                except asyncio.TimeoutError:
                    raise IOError(_0xd14e4b1f('4a4f494e2074696d6564206f75742077616974696e6720666f722070726f6772657373206e6f74696669636174696f6e'))
                if _0x3c709b10 in (3, 4):
                    break
            if _0x3c709b10 == 3:
                return _0xd14e4b1f('646f6e65')
            _0xc77fa840 = 0
            if _0x0fea988d in _0xc25b3700:
                try:
                    _0x4431699c = await self.get_notification(_0x1629a1bc, timeout=2.0)
                    _0xc77fa840 = _0x4431699c[0] if _0x4431699c else 0
                except asyncio.TimeoutError:
                    pass
            if _0x1db222fe == 0 and _0xc77fa840 & 2 and (pin is not None):
                continue
            if _0xc77fa840 & 4:
                raise IOError(_0xd14e4b1f('4a4f494e206661696c65643a2077726f6e672050494e'))
            if _0xc77fa840 & 8:
                raise IOError(_0xd14e4b1f('4a4f494e206661696c65643a20746f6f206d616e7920646576696365732072656769737465726564'))
            if _0xc77fa840 & 16:
                raise IOError(_0xd14e4b1f('4a4f494e206661696c65643a20646576696365206e6f7420737570706f72746564'))
            if _0xc77fa840 & 2 and pin is None:
                raise IOError(_0xd14e4b1f('4a4f494e206661696c65643a206465766963652069732050726f74656374656420627574206e6f2050494e20636f6e66696775726564'))
            raise IOError(f"{_0xd14e4b1f('4a4f494e206661696c65643a206572726f723d3078')}{_0xc77fa840:{_0xd14e4b1f('303258')}}")
        raise IOError(_0xd14e4b1f('4a4f494e3a206578686175737465642072657472696573'))

def _0x2104ae2e(_0x9acb4454):
    try:
        return _0x367daf70(_0xa7830531(_0x9acb4454))
    except ValueError:
        return f"{_0xd14e4b1f('3078')}{_0x9acb4454:{_0xd14e4b1f('303258')}}"

class _0x788712fe(Exception):
    pass

class _0x4cd72f90(Exception):
    pass

class _0x7dfe691f:
    pass

class _0xabcea1bc(_0x7dfe691f):
    _0x84b86b1b = UUID(_0x0eb5e6c6)
    _0xbf33edd0 = UUID(_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336131336530303030'))
    _0xfb31c69d = UUID(_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336135336530303030'))
    _0x9779b131 = UUID(_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336136336530303030'))
    _0xd4669443 = UUID(_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336137336530303030'))
    _0x7b1b6cda = UUID(_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336138336530303030'))
    _0xb3d5daa7 = UUID(_0xffe93664)
    _0x39e608b9: float = 10.0

    def __init__(self, esphome_host=None, esphome_port=6053, esphome_noise_psk=None, hass=None):
        self.client = None
        self.read_characteristics = {}
        self.data_received_handlers = _0x22109af8()
        self.data_received = None
        self.connection_status_changed_handlers = _0x22109af8()
        self.device_address = _0xd14e4b1f('556e6b6e6f776e')
        self.device_name = _0xd14e4b1f('556e6b6e6f776e')
        self.esphome_host = esphome_host
        self.esphome_port = esphome_port
        self.esphome_noise_psk = esphome_noise_psk
        self.esphome_proxy_name = None
        self.last_esphome_api_ms = None
        self._0xf1274d64 = None
        self.last_ble_ms = None
        self._0xcb4675ce = None
        self._0x8af7b457 = 0
        self.rssi = None
        self._0x70b8e2d2 = None
        self.esphome_free_heap = None
        self.esphome_max_free_block = None
        self._0x625f9fc1 = None
        self._0xd6c066b2 = None
        self._0x748cc826 = None
        self._0xc18fec1f = hass
        self._0x26cf2c97 = []
        self.is_variant_a = False
        self._0xf4986b9d = None
        self._0xd6639f87 = None
        self._0xdb81bd7c = asyncio.Lock()

    @property
    def arendi_handshake_done(self):
        return self._0xf4986b9d is not None and self._0xf4986b9d.handshake_done

    async def connect_async(self, device_id):
        if self.esphome_host:
            await self._0xfb0a72a6(device_id)
        else:
            await self._0xa0684c60(device_id)

    async def _0xa0684c60(self, _0x9379346c):
        _0x809d4580 = time.perf_counter()
        if self._0xc18fec1f is not None:
            _0x913f9c49 = await self._0x3da0c064(_0x9379346c)
            if _0x913f9c49 is None:
                raise BleakError(f"{_0xd14e4b1f('47656265726974546f696c65742064657669636520')}{_0x9379346c}{_0xd14e4b1f('206e6f7420666f756e6420627920484120626c7565746f6f7468207363616e6e65722e')}")
            self.device_address = _0x913f9c49.address
            self.device_name = _0x913f9c49.name or _0xd14e4b1f('556e6b6e6f776e')
            try:
                from bleak_retry_connector import establish_connection
                self.client = await establish_connection(BleakClient, _0x913f9c49, _0x913f9c49.name or _0x9379346c, disconnected_callback=self._0xba05fe7f)
            except ImportError:
                self.client = BleakClient(_0x913f9c49, disconnected_callback=self._0xba05fe7f)
                await self.client.connect()
        else:
            _0x913f9c49 = await BleakScanner.find_device_by_address(_0x9379346c)
            if _0x913f9c49 is not None:
                self.device_address = _0x913f9c49.address
                self.device_name = _0x913f9c49.name
                self.rssi = getattr(_0x913f9c49, _0xd14e4b1f('72737369'), None)
                self.client = BleakClient(address_or_ble_device=_0x913f9c49, disconnected_callback=self._0xba05fe7f)
            else:
                self.device_address = _0x9379346c
                self.device_name = _0x9379346c
                self.rssi = None
                self.client = BleakClient(_0x9379346c, disconnected_callback=self._0xba05fe7f)
            await self.client.connect()
        self.last_esphome_api_ms = None
        self.last_ble_ms = int((time.perf_counter() - _0x809d4580) * 1000)
        await self._0x27666992()

    async def _0x3da0c064(self, _0x9379346c):
        from homeassistant.components import bluetooth
        from homeassistant.core import callback as ha_callback
        _0x884d9804 = _0x9379346c.upper()
        _0xcd1dc320 = bluetooth.async_last_service_info(self._0xc18fec1f, _0x884d9804, connectable=True)
        if _0xcd1dc320 is not None:
            self.rssi = _0xcd1dc320.rssi
            return _0xcd1dc320.device
        _0xb8460429 = asyncio.Event()
        _0xa99f9ff8 = [None]
        _0x5e38b7e8 = [None]

        @ha_callback
        def _0x8d737ba6(_0xcd1dc320, _0xeb399bca):
            _0xa99f9ff8[0] = _0xcd1dc320.device
            _0x5e38b7e8[0] = _0xcd1dc320.rssi
            _0xb8460429.set()
        _0x10aec353 = bluetooth.async_register_callback(self._0xc18fec1f, _0x8d737ba6, {_0xd14e4b1f('61646472657373'): _0x884d9804}, bluetooth.BluetoothScanningMode.ACTIVE)
        try:
            await asyncio.wait_for(_0xb8460429.wait(), timeout=30.0)
            self.rssi = _0x5e38b7e8[0]
            return _0xa99f9ff8[0]
        except asyncio.TimeoutError:
            return None
        finally:
            _0x10aec353()

    async def _0xe50a3ca7(self):
        from aioesphomeapi import APIClient
        if self._0xcb4675ce is not None:
            if getattr(self._0xcb4675ce, _0xd14e4b1f('5f636f6e6e656374696f6e'), None) is not None:
                self.last_esphome_api_ms = 0
                return self._0xcb4675ce
            self._0xcb4675ce = None
        _0x809d4580 = time.perf_counter()
        _0x8a5da52e = APIClient(address=self.esphome_host, port=self.esphome_port, password='', noise_psk=self.esphome_noise_psk)
        try:
            await asyncio.wait_for(_0x8a5da52e.connect(login=True), timeout=10.0)
        except asyncio.TimeoutError:
            raise _0x788712fe(f"{_0xd14e4b1f('54696d656f757420636f6e6e656374696e6720746f20455350486f6d652070726f787920617420')}{self.esphome_host}{_0xd14e4b1f('3a')}{self.esphome_port}")
        except Exception as _0xe1671797:
            raise _0x788712fe(f"{_0xd14e4b1f('4661696c656420746f20636f6e6e65637420746f20455350486f6d652070726f787920617420')}{self.esphome_host}{_0xd14e4b1f('3a20')}{_0xe1671797}")
        try:
            _0xa95eca9e = await asyncio.wait_for(_0x8a5da52e.device_info(), timeout=10.0)
            self._0x8af7b457 = getattr(_0xa95eca9e, _0xd14e4b1f('626c7565746f6f74685f70726f78795f666561747572655f666c616773'), 0)
            self.esphome_proxy_name = getattr(_0xa95eca9e, _0xd14e4b1f('6e616d65'), _0xd14e4b1f('756e6b6e6f776e'))
        except Exception as _0xe1671797:
            self._0x8af7b457 = 0
            self.esphome_proxy_name = _0xd14e4b1f('756e6b6e6f776e')
        self._0xcb4675ce = _0x8a5da52e
        self.last_esphome_api_ms = int((time.perf_counter() - _0x809d4580) * 1000)
        return _0x8a5da52e

    def _0x5c161f39(self, _0x5c18ef72):
        _0xa013658e = self._0xf1274d64
        self._0xf1274d64 = None
        if _0xa013658e is None:
            return
        try:
            _0xa013658e()
        except Exception as _0x56bd7107:
            pass

    async def _0xf3cfbfb1(self):
        _0x8a5da52e = self._0xcb4675ce
        if _0x8a5da52e is None:
            return
        try:
            if self._0x625f9fc1 is None or self._0xd6c066b2 is None or self._0x748cc826 is None:
                (_0x07214c67, _) = await asyncio.wait_for(_0x8a5da52e.list_entities_services(), timeout=5.0)
                if self._0x625f9fc1 is None:
                    self._0x625f9fc1 = next((_0xe1671797.key for _0xe1671797 in _0x07214c67 if getattr(_0xe1671797, _0xd14e4b1f('756e69745f6f665f6d6561737572656d656e74'), '') == _0xd14e4b1f('64426d') and _0xd14e4b1f('77696669') in getattr(_0xe1671797, _0xd14e4b1f('6f626a6563745f6964'), '').lower()), -1)
                    if self._0x625f9fc1 == -1:
                        pass
                if self._0xd6c066b2 is None:
                    self._0xd6c066b2 = next((_0xe1671797.key for _0xe1671797 in _0x07214c67 if _0xd14e4b1f('68656170') in getattr(_0xe1671797, _0xd14e4b1f('6f626a6563745f6964'), '').lower()), -1)
                    if self._0xd6c066b2 == -1:
                        pass
                if self._0x748cc826 is None:
                    self._0x748cc826 = next((_0xe1671797.key for _0xe1671797 in _0x07214c67 if _0xd14e4b1f('626c6f636b') in getattr(_0xe1671797, _0xd14e4b1f('6f626a6563745f6964'), '').lower()), -1)
                    if self._0x748cc826 == -1:
                        pass
            _0x6fb18710 = {}
            if self._0x625f9fc1 != -1:
                _0x6fb18710[self._0x625f9fc1] = _0xd14e4b1f('77696669')
            if self._0xd6c066b2 != -1:
                _0x6fb18710[self._0xd6c066b2] = _0xd14e4b1f('68656170')
            if self._0x748cc826 != -1:
                _0x6fb18710[self._0x748cc826] = _0xd14e4b1f('626c6f636b')
            if not _0x6fb18710:
                return
            _0x2f77656f = {}
            _0x446c4293 = asyncio.Event()

            def _0x886b8afa(_0x9ed39e2e):
                _0x3c6e0b8a = getattr(_0x9ed39e2e, _0xd14e4b1f('6b6579'), None)
                if _0x3c6e0b8a in _0x6fb18710 and _0x3c6e0b8a not in _0x2f77656f:
                    _0x2f77656f[_0x3c6e0b8a] = getattr(_0x9ed39e2e, _0xd14e4b1f('7374617465'), None)
                    if len(_0x2f77656f) >= len(_0x6fb18710):
                        _0x446c4293.set()
            _0xcba13a44 = _0x8a5da52e.subscribe_states(_0x886b8afa)
            try:
                await asyncio.wait_for(_0x446c4293.wait(), timeout=3.0)
            except asyncio.TimeoutError:
                pass
            finally:
                try:
                    _0xcba13a44()
                except Exception:
                    pass
            if self._0x625f9fc1 in _0x2f77656f and _0x2f77656f[self._0x625f9fc1] is not None:
                self._0x70b8e2d2 = round(float(_0x2f77656f[self._0x625f9fc1]), 1)
            if self._0xd6c066b2 in _0x2f77656f and _0x2f77656f[self._0xd6c066b2] is not None:
                self.esphome_free_heap = int(float(_0x2f77656f[self._0xd6c066b2]))
            if self._0x748cc826 in _0x2f77656f and _0x2f77656f[self._0x748cc826] is not None:
                self.esphome_max_free_block = int(float(_0x2f77656f[self._0x748cc826]))
        except Exception as _0xe1671797:
            pass

    async def _0xfb0a72a6(self, _0x9379346c):
        self._0x5c161f39(_0xd14e4b1f('7072652d7363616e20636c65616e7570'))
        try:
            _0x8a5da52e = await self._0xe50a3ca7()
        except _0x788712fe:
            self._0xcb4675ce = None
            raise
        await self._0xf3cfbfb1()
        _0xbc1f43fa = time.perf_counter()
        _0x9b18458b = int(_0x9379346c.replace(_0xd14e4b1f('3a'), ''), 16)
        _0xb8460429 = asyncio.Event()
        _0x3b92d741 = ''
        _0x0a497d6c = 0
        _0x1bc68618 = 0
        _0xfbe827aa = {}

        def on_raw_advertisements(resp):
            nonlocal _0x3b92d741, _0x0a497d6c, _0x1bc68618
            _0x1bc68618 += len(resp.advertisements)
            for _0x4acedbc1 in resp.advertisements:
                _0xfbe827aa[_0x4acedbc1.address] = _0xfbe827aa.get(_0x4acedbc1.address, 0) + 1
                if _0x4acedbc1.address == _0x9b18458b:
                    _0x3b92d741 = self._0x933576e5(bytes(_0x4acedbc1.data))
                    _0x0a497d6c = getattr(_0x4acedbc1, _0xd14e4b1f('616464726573735f74797065'), 0)
                    self.rssi = getattr(_0x4acedbc1, _0xd14e4b1f('72737369'), None)
                    _0xb8460429.set()
        _0x4694c2b5 = _0x8a5da52e.subscribe_bluetooth_le_raw_advertisements(on_raw_advertisements)
        self._0xf1274d64 = _0x4694c2b5
        try:
            await asyncio.wait_for(_0xb8460429.wait(), timeout=self._0x39e608b9)
        except asyncio.TimeoutError:
            self._0x5c161f39(_0xd14e4b1f('7363616e2074696d656f7574'))
            _0xb28354b5 = sorted(_0xfbe827aa.items(), key=lambda x: -x[1])[:8]
            _0x40e926f3 = _0xd14e4b1f('2c20').join((f"{_0x0cc175b9:{_0xd14e4b1f('2330313478')}}{_0xd14e4b1f('28')}{_0x4a8a08f0}{_0xd14e4b1f('29')}" for (_0x0cc175b9, _0x4a8a08f0) in _0xb28354b5))
            _0xee2faeed = _0xd14e4b1f('7363616e6e6572206d617920626520737475636b206f7220737562736372697074696f6e20736c6f7420696e20757365') if _0x1bc68618 == 0 else _0xd14e4b1f('646576696365206e6f74206164766572746973696e67')
            raise _0x4cd72f90(f"{_0xd14e4b1f('47656265726974546f696c65742064657669636520')}{_0x9379346c}{_0xd14e4b1f('206e6f7420666f756e642076696120455350486f6d652070726f787920617420')}{self.esphome_host}{_0xd14e4b1f('2028726563656976656420')}{_0x1bc68618}{_0xd14e4b1f('20746f74616c20424c45206164766572746973656d656e74207061636b657428732920647572696e6720')}{self._0x39e608b9:{_0xd14e4b1f('2e3066')}}{_0xd14e4b1f('2073207363616e20e2809420')}{_0xee2faeed}{_0xd14e4b1f('29')}")
        self._0x5c161f39(_0xd14e4b1f('74617267657420666f756e64'))
        self.device_address = _0x9379346c
        self.device_name = _0x3b92d741 or _0xd14e4b1f('556e6b6e6f776e')
        self.client = _0xcc466a73(_0x8a5da52e, _0x9379346c, self._0xba05fe7f, _0x0a497d6c, self._0x8af7b457)
        try:
            await self.client.connect(timeout=30.0)
        except Exception as _0xe1671797:
            raise
        self.last_ble_ms = int((time.perf_counter() - _0xbc1f43fa) * 1000)
        await self._0x27666992()

    def _0x933576e5(self, _0x8d777f38):
        _0x865c0c0b = 0
        _0xb068931c = ''
        while _0x865c0c0b < len(_0x8d777f38):
            _0x2fa47f7c = _0x8d777f38[_0x865c0c0b]
            if _0x2fa47f7c == 0 or _0x865c0c0b + _0x2fa47f7c >= len(_0x8d777f38):
                break
            _0x6ec0305b = _0x8d777f38[_0x865c0c0b + 1]
            _0x2063c160 = _0x8d777f38[_0x865c0c0b + 2:_0x865c0c0b + 1 + _0x2fa47f7c]
            if _0x6ec0305b == 9:
                return _0x2063c160.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('7265706c616365'))
            elif _0x6ec0305b == 8:
                _0xb068931c = _0x2063c160.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('7265706c616365'))
            _0x865c0c0b += 1 + _0x2fa47f7c
        return _0xb068931c

    def _0x79fae301(self):
        try:
            _0x7d97481b = _0x7bed062f(self.client.services)
        except Exception:
            return
        if _0x7d97481b._0xbf104bbb or not _0x7d97481b._0xebc9e48e or (not _0x7d97481b._0xac67ba21):
            return
        _0x9a596173 = UUID(_0x7d97481b._0xebc9e48e[0])
        _0xc7374a96 = UUID(_0x7d97481b._0xac67ba21[0])
        self._0x84b86b1b = UUID(_0x7d97481b._0xd63cb1d8)
        self._0xbf33edd0 = _0x9a596173
        self._0xfb31c69d = _0xc7374a96
        self._0x9779b131 = _0xc7374a96
        self._0xd4669443 = _0xc7374a96
        self._0x7b1b6cda = _0xc7374a96
        self.is_variant_a = True

    async def _0xfc39a9ea(self):
        if not hasattr(self.client, _0xd14e4b1f('726561645f676174745f63686172')):
            return
        _0xdb8615d2 = {_0xd14e4b1f('30303030326132392d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('6d616e7566616374757265725f6e616d65'), _0xd14e4b1f('30303030326132342d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('6d6f64656c5f6e756d626572'), _0xd14e4b1f('30303030326132352d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('73657269616c5f6e756d626572'), _0xd14e4b1f('30303030326132362d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('6669726d776172655f7265766973696f6e'), _0xd14e4b1f('30303030326132372d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('68617264776172655f7265766973696f6e'), _0xd14e4b1f('30303030326132382d303030302d313030302d383030302d303038303566396233346662'): _0xd14e4b1f('736f6674776172655f7265766973696f6e')}
        try:
            _0x6dca2670 = next((_0x03c7c0ac for _0x03c7c0ac in self.client.services if _0x03c7c0ac.uuid.lower() == _0xe80ee6c3), None)
            if _0x6dca2670 is None:
                return
            _0xcaf9b6b9 = {}
            for _0xa87deb01 in _0x6dca2670.characteristics:
                _0x3c6e0b8a = _0xdb8615d2.get(_0xa87deb01.uuid.lower())
                if _0x3c6e0b8a:
                    try:
                        _0xbdd166af = await self.client.read_gatt_char(_0xa87deb01)
                        _0xcaf9b6b9[_0x3c6e0b8a] = _0xbdd166af.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('7265706c616365')).strip(_0xd14e4b1f('00')).strip()
                    except Exception as _0xe1671797:
                        pass
            if _0xcaf9b6b9:
                pass
        except Exception as _0xe1671797:
            pass

    async def _0x27666992(self):
        self._0x79fae301()
        await self._0xfc39a9ea()
        if self.is_variant_a:
            self._0xf4986b9d = _0xb588dc14()
            self.read_characteristics = {self._0xfb31c69d: self.data_received, self._0x9779b131: self.data_received, self._0xd4669443: self.data_received, self._0x7b1b6cda: self.data_received}
            _0x3a7d27e7 = str(self._0xfb31c69d)
            if hasattr(self.client, _0xd14e4b1f('73746f705f6e6f74696679')):
                try:
                    await self.client.stop_notify(_0x3a7d27e7)
                except Exception:
                    pass
            await self.client.start_notify(_0x3a7d27e7, self._0xcfe894c7)
            self._0x26cf2c97.append(self._0xfb31c69d)
            if hasattr(self.client, _0xd14e4b1f('5f616371756972655f6d7475')):
                try:
                    await self.client._acquire_mtu()
                except Exception as _0xe1671797:
                    pass
            _0x377f1423 = 20
            try:
                _0x7d571ffa = self.client.services.get_characteristic(self._0xbf33edd0)
                if _0x7d571ffa is not None:
                    _0x377f1423 = _0x7d571ffa.max_write_without_response_size
            except AttributeError:
                pass

            async def _0x8602d936(_0xbd32c32b):
                async with self._0xdb81bd7c:
                    _0x7b8b965a = (len(_0xbd32c32b) + _0x377f1423 - 1) // _0x377f1423
                    if _0x7b8b965a > 1:
                        pass
                    for _0x3262d48d in range(0, len(_0xbd32c32b), _0x377f1423):
                        await self.client.write_gatt_char(self._0xbf33edd0, _0xbd32c32b[_0x3262d48d:_0x3262d48d + _0x377f1423], response=False)
            self._0xd6639f87 = _0x8602d936
            await self._0xf4986b9d.perform_handshake(_0x8602d936)
            self._0xf4986b9d._0x926af308 = _0x8602d936
            self.connection_status_changed_handlers(self, True, self.device_address, self.device_name)
            return
        self.read_characteristics = {self._0xfb31c69d: self.data_received, self._0x9779b131: self.data_received, self._0xd4669443: self.data_received, self._0x7b1b6cda: self.data_received}
        await self._0xae5dca35()
        self.connection_status_changed_handlers(self, True, self.device_address, self.device_name)

    async def _0xae5dca35(self):
        if not self.client.is_connected:
            await self.client.connect()
        _0xb69cc26c = {str(_0xef7c876f).lower() for _0xef7c876f in self.read_characteristics}
        _0xbc0a15a6 = [_0x03c7c0ac.uuid for _0x03c7c0ac in self.client.services]
        _0x73d80800 = False
        for _0xaaabf0d3 in self.client.services:
            if _0xaaabf0d3.uuid == str(self._0x84b86b1b):
                _0x73d80800 = True
                for _0xa2de09ab in _0xaaabf0d3.characteristics:
                    if str(_0xa2de09ab.uuid).lower() in _0xb69cc26c:
                        if hasattr(self.client, _0xd14e4b1f('73746f705f6e6f74696679')):
                            try:
                                await self.client.stop_notify(_0xa2de09ab)
                            except Exception as _0x98847a58:
                                pass
                        await self.client.start_notify(_0xa2de09ab, self._0xcfe894c7)
                        self._0x26cf2c97.append(_0xa2de09ab)
        if not _0x73d80800:
            pass

    async def _0xcfe894c7(self, _0x86c61d25, _0x8d777f38):
        _0x088fa52d = self._0xf4986b9d.handshake_done if self._0xf4986b9d else None
        if self._0xf4986b9d is not None:
            _0x7232ad5f = self._0xf4986b9d.feed_att_bytes(bytes(_0x8d777f38))
            for _0x321c3cf4 in _0x7232ad5f:
                await self.data_received_handlers.invoke_async(_0x321c3cf4)
        else:
            await self.data_received_handlers.invoke_async(_0x8d777f38)

    def _0xba05fe7f(self, _0x62608e08):
        self.connection_status_changed_handlers(self, False)

    async def send_message(self, data):
        if self._0xf4986b9d is not None and self._0xf4986b9d.handshake_done:
            _0xbd32c32b = self._0xf4986b9d.wrap_for_send(data)
            await self._0xd6639f87(_0xbd32c32b)
        else:
            async with self._0xdb81bd7c:
                _0xb4a88417 = await self.client.write_gatt_char(self._0xbf33edd0, data)

    def get_services(self):
        if self.client is None:
            return []
        try:
            return list(self.client.services)
        except Exception:
            return []

    async def read_characteristic(self, char_specifier):
        if self.client is None:
            raise BleakError(_0xd14e4b1f('436c69656e74206e6f7420636f6e6e6563746564'))
        if not hasattr(self.client, _0xd14e4b1f('726561645f676174745f63686172')):
            raise BleakError(_0xd14e4b1f('41637469766520424c4520636c69656e7420646f6573206e6f7420737570706f727420726561645f676174745f63686172'))
        _0x8d777f38 = await self.client.read_gatt_char(char_specifier)
        return bytes(_0x8d777f38)

    async def disconnect(self):
        if self.client:
            _0x54a61d9e = self.client.is_connected
            for _0xa87deb01 in self._0x26cf2c97:
                try:
                    await self.client.stop_notify(_0xa87deb01)
                except Exception as _0xe1671797:
                    pass
            self._0x26cf2c97 = []
            if self.esphome_host:
                await self.client.disconnect(close_api=False)
                if self._0xf1274d64 is not None:
                    self._0x5c161f39(_0xd14e4b1f('646973636f6e6e656374'))
                    await asyncio.sleep(0.1)
                if self._0xcb4675ce is not None:
                    try:
                        await self._0xcb4675ce.disconnect()
                    except Exception as _0xe1671797:
                        pass
            else:
                await self.client.disconnect()
            self.client = None
        elif self._0xcb4675ce is not None:
            try:
                await self._0xcb4675ce.disconnect()
            except Exception as _0xe1671797:
                pass
        self._0x5c161f39(_0xd14e4b1f('66696e616c20636c65616e7570'))
        self._0xf4986b9d = None
        self._0xd6639f87 = None
        if self.esphome_host:
            self._0xcb4675ce = None

class _0xcc466a73:

    def __init__(self, api_client, mac_address, disconnected_callback=None, address_type=0, feature_flags=0):
        self._0xae9aed3e = api_client
        self._0x1c654ad0 = mac_address
        self._0x3d4dbdbc = int(mac_address.replace(_0xd14e4b1f('3a'), ''), 16)
        self._0x1e150cdc = address_type
        self._0xcfba72f2 = feature_flags
        self._0x7a9feaf2 = disconnected_callback
        self._0x5347d968 = False
        self._0xd2d9191f = None
        self._0x01e21548 = {}
        self._0xf1ab4581 = {}
        self._0x168ba680 = {}
        self._0xf231f310 = {}
        self._0x01bd2764 = {}
        self._0xcae41a3f = {}
        self._0xa93d9c96 = asyncio.Queue()
        self._0x2ac50843 = None
        self._0x9d117f86 = None

    @property
    def is_connected(self):
        return self._0x5347d968

    @property
    def services(self):
        if self._0xd2d9191f is None:
            return _0x1e93f7f7([])
        return self._0xd2d9191f

    async def connect(self, timeout=30.0):
        _0x32a1022a = asyncio.get_running_loop().create_future()

        def on_bluetooth_connection_state(connected, mtu, error):
            if not _0x32a1022a.done():
                if error:
                    _0x32a1022a.set_exception(Exception(f"{_0xd14e4b1f('424c4520636f6e6e656374696f6e206572726f723a20')}{error}"))
                elif connected:
                    self._0x5347d968 = True
                    _0x32a1022a.set_result(mtu)
                else:
                    _0x32a1022a.set_exception(Exception(_0xd14e4b1f('446973636f6e6e656374656420647572696e6720636f6e6e656374696f6e')))
            elif not connected:
                self._0x5347d968 = False
                if self._0x2ac50843 is not None:
                    self._0x2ac50843.cancel()
                if self._0x7a9feaf2:
                    try:
                        self._0x7a9feaf2(self)
                    except Exception as _0xe1671797:
                        pass
        self._0x9d117f86 = await self._0xae9aed3e.bluetooth_device_connect(self._0x3d4dbdbc, on_bluetooth_connection_state, address_type=self._0x1e150cdc, feature_flags=self._0xcfba72f2, has_cache=False, disconnect_timeout=10.0, timeout=timeout)
        try:
            _0x661a504c = await asyncio.wait_for(_0x32a1022a, timeout=timeout)
            await self._0x2ce30215()
            self._0x2ac50843 = asyncio.create_task(self._0x173574e9())
            return True
        except asyncio.TimeoutError:
            self._0x5347d968 = False
            if self._0x9d117f86:
                self._0x9d117f86()
            raise Exception(f"{_0xd14e4b1f('436f6e6e656374696f6e2074696d656f757420616674657220')}{timeout}{_0xd14e4b1f('73')}")
        except Exception as _0xe1671797:
            self._0x5347d968 = False
            if self._0x9d117f86:
                self._0x9d117f86()
            raise

    async def _0x173574e9(self):
        while True:
            try:
                (_0x2c1c8f39, _0x67ce43fb, _0x8d777f38) = await self._0xa93d9c96.get()
                _0xb4a88417 = _0x2c1c8f39(_0x67ce43fb, _0x8d777f38)
                if asyncio.iscoroutine(_0xb4a88417):
                    await _0xb4a88417
            except asyncio.CancelledError:
                break
            except Exception as _0xe1671797:
                pass

    async def _0x2ce30215(self):
        try:
            _0xbd86bced = await self._0xae9aed3e.bluetooth_gatt_get_services(self._0x3d4dbdbc)
            _0x10cd395c = []
            for _0x961e38b5 in _0xbd86bced.services:
                _0x27f04ac1 = []
                for _0xa87deb01 in _0x961e38b5.characteristics:
                    _0x393879fa = _0xa87deb01.uuid.lower()
                    _0xe1260894 = _0xa87deb01.handle
                    self._0x01e21548[_0x393879fa] = _0xe1260894
                    self._0xf1ab4581[_0xe1260894] = _0x393879fa
                    self._0x168ba680[_0x393879fa] = _0xa87deb01.properties
                    _0x952dc1e5 = _0xd14e4b1f('30303030323930322d303030302d313030302d383030302d303038303566396233346662')
                    for _0x1dee80c7 in _0xa87deb01.descriptors:
                        if _0x1dee80c7.uuid.lower() == _0x952dc1e5:
                            self._0xf231f310[_0xe1260894] = _0x1dee80c7.handle
                    _0x27f04ac1.append(_0x89ff388d(uuid=_0x393879fa, handle=_0xe1260894, properties=_0xa87deb01.properties, descriptors=[_0xfece8a4b(uuid=_0x1dee80c7.uuid.lower(), handle=_0x1dee80c7.handle) for _0x1dee80c7 in _0xa87deb01.descriptors]))
                _0x10cd395c.append(_0xcff2c4bc(uuid=_0x961e38b5.uuid.lower(), characteristics=_0x27f04ac1))
            self._0xd2d9191f = _0x1e93f7f7(_0x10cd395c)
        except Exception as _0xe1671797:
            raise

    async def start_notify(self, char_specifier, callback):
        if isinstance(char_specifier, _0x89ff388d):
            _0x393879fa = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            _0x393879fa = str(char_specifier).lower()
        else:
            _0x393879fa = str(char_specifier).lower()
        _0xe1260894 = self._0x01e21548.get(_0x393879fa)
        if _0xe1260894 is None:
            raise ValueError(f"{_0xd14e4b1f('4368617261637465726973746963205555494420')}{_0x393879fa}{_0xd14e4b1f('206e6f7420666f756e6420696e20646576696365207365727669636573')}")
        if _0xe1260894 in self._0xcae41a3f:
            await self.stop_notify(char_specifier)
        self._0x01bd2764[_0xe1260894] = callback

        def on_notify(handle, data):
            _0xef7c876f = self._0xf1ab4581.get(handle)
            _0x2c1c8f39 = self._0x01bd2764.get(handle)
            if _0x2c1c8f39:
                _0x67ce43fb = _0x89ff388d(uuid=_0xef7c876f, handle=handle, properties=16)
                self._0xa93d9c96.put_nowait((_0x2c1c8f39, _0x67ce43fb, data))
        try:
            (_0xf931fa61, _0x8aa8571e) = await self._0xae9aed3e.bluetooth_gatt_start_notify(self._0x3d4dbdbc, _0xe1260894, on_notify)
            self._0xcae41a3f[_0xe1260894] = (_0xf931fa61, _0x8aa8571e)
            _0xd4656ffc = self._0xf231f310.get(_0xe1260894)
            if _0xd4656ffc is not None:
                await self._0xae9aed3e.bluetooth_gatt_write_descriptor(self._0x3d4dbdbc, _0xd4656ffc, _0xaf5f5547('0100'))
        except Exception as _0xe1671797:
            self._0x01bd2764.pop(_0xe1260894, None)
            raise

    async def stop_notify(self, char_specifier):
        if isinstance(char_specifier, _0x89ff388d):
            _0x393879fa = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            _0x393879fa = str(char_specifier).lower()
        else:
            _0x393879fa = str(char_specifier).lower()
        _0xe1260894 = self._0x01e21548.get(_0x393879fa)
        if _0xe1260894 is None:
            return
        _0x89885eff = self._0xcae41a3f.pop(_0xe1260894, None)
        self._0x01bd2764.pop(_0xe1260894, None)
        if _0x89885eff is None:
            return
        (_0xf931fa61, _0x8aa8571e) = _0x89885eff
        try:
            _0xb4a88417 = _0xf931fa61()
            if asyncio.iscoroutine(_0xb4a88417):
                await _0xb4a88417
        finally:
            _0x8aa8571e()

    async def _0x7802d5bb(self):
        for _0xe1260894 in tuple(self._0xcae41a3f):
            _0x393879fa = self._0xf1ab4581.get(_0xe1260894)
            if _0x393879fa is not None:
                try:
                    await self.stop_notify(_0x393879fa)
                except Exception as _0x56bd7107:
                    pass
        self._0xcae41a3f.clear()
        self._0x01bd2764.clear()

    async def write_gatt_char(self, char_specifier, data, response=None):
        if isinstance(char_specifier, _0x89ff388d):
            _0x393879fa = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            _0x393879fa = str(char_specifier).lower()
        else:
            _0x393879fa = str(char_specifier).lower()
        _0xe1260894 = self._0x01e21548.get(_0x393879fa)
        if _0xe1260894 is None:
            raise ValueError(f"{_0xd14e4b1f('4368617261637465726973746963205555494420')}{_0x393879fa}{_0xd14e4b1f('206e6f7420666f756e6420696e20646576696365207365727669636573')}")
        if response is None:
            _0x50fe03ab = self._0x168ba680.get(_0x393879fa, 0)
            response = not bool(_0x50fe03ab & 4)
        try:
            await self._0xae9aed3e.bluetooth_gatt_write(self._0x3d4dbdbc, _0xe1260894, bytes(data), response=response)
        except Exception as _0xe1671797:
            raise

    async def read_gatt_char(self, char_specifier):
        if isinstance(char_specifier, _0x89ff388d):
            _0x393879fa = char_specifier.uuid
        elif isinstance(char_specifier, UUID):
            _0x393879fa = str(char_specifier).lower()
        else:
            _0x393879fa = str(char_specifier).lower()
        _0xe1260894 = self._0x01e21548.get(_0x393879fa)
        if _0xe1260894 is None:
            raise ValueError(f"{_0xd14e4b1f('4368617261637465726973746963205555494420')}{_0x393879fa}{_0xd14e4b1f('206e6f7420666f756e6420696e20646576696365207365727669636573')}")
        try:
            _0x8d777f38 = await self._0xae9aed3e.bluetooth_gatt_read(self._0x3d4dbdbc, _0xe1260894)
            _0x2dfac627 = bytes(_0x8d777f38)
            return _0x2dfac627
        except Exception as _0xe1671797:
            raise

    async def disconnect(self, close_api=True):
        if self._0x2ac50843:
            self._0x2ac50843.cancel()
            await asyncio.gather(self._0x2ac50843, return_exceptions=True)
            self._0x2ac50843 = None
        await self._0x7802d5bb()
        if not self._0x5347d968:
            if self._0x9d117f86:
                try:
                    self._0x9d117f86()
                except Exception:
                    pass
                self._0x9d117f86 = None
            if close_api and self._0xae9aed3e is not None:
                try:
                    await self._0xae9aed3e.disconnect()
                except Exception as _0xe1671797:
                    pass
            return
        _0x9fd3bda6 = False
        try:
            await self._0xae9aed3e.bluetooth_device_disconnect(self._0x3d4dbdbc)
            for _ in range(50):
                if not self._0x5347d968:
                    _0x9fd3bda6 = True
                    break
                await asyncio.sleep(0.1)
        except Exception as _0xe1671797:
            pass
        finally:
            if self._0x9d117f86:
                self._0x9d117f86()
                self._0x9d117f86 = None
            self._0x5347d968 = False
            if close_api:
                try:
                    await self._0xae9aed3e.disconnect()
                except Exception as _0xe1671797:
                    pass
            if not _0x9fd3bda6 and self._0x7a9feaf2:
                try:
                    self._0x7a9feaf2(self)
                except Exception as _0xe1671797:
                    pass

class _0x1e93f7f7:

    def __init__(self, services):
        self._0xd2d9191f = services

    def __iter__(self):
        return iter(self._0xd2d9191f)

    def __len__(self):
        return len(self._0xd2d9191f)

    def get_characteristic(self, char_specifier):
        _0x393879fa = str(char_specifier).lower()
        for _0xaaabf0d3 in self._0xd2d9191f:
            for _0xa2de09ab in _0xaaabf0d3.characteristics:
                if _0xa2de09ab.uuid == _0x393879fa:
                    return _0xa2de09ab
        return None

class _0xcff2c4bc:

    def __init__(self, uuid, characteristics):
        self.uuid = uuid
        self.characteristics = characteristics

    def __repr__(self):
        return f"{_0xd14e4b1f('455350486f6d65474154545365727669636528757569643d')}{self.uuid}{_0xd14e4b1f('2c2063686172733d')}{len(self.characteristics)}{_0xd14e4b1f('29')}"

class _0x89ff388d:

    def __init__(self, uuid, handle, properties, descriptors=None):
        self.uuid = uuid
        self.handle = handle
        self.properties = properties
        self.descriptors = descriptors or []

    def __repr__(self):
        return f"{_0xd14e4b1f('455350486f6d6547415454436861726163746572697374696328757569643d')}{self.uuid}{_0xd14e4b1f('2c2068616e646c653d3078')}{self.handle:{_0xd14e4b1f('303478')}}{_0xd14e4b1f('29')}"

class _0xfece8a4b:

    def __init__(self, uuid, handle):
        self.uuid = uuid
        self.handle = handle

class _0x22109af8:

    def __init__(self):
        self._0x5a0dd37e = []

    def __iadd__(self, handler):
        self._0x5a0dd37e.append(handler)
        return self

    def __isub__(self, handler):
        try:
            self._0x5a0dd37e.remove(handler)
        except ValueError:
            pass
        return self

    def __call__(self, *args, **kwargs):
        for _0xc1cbfe27 in self._0x5a0dd37e:
            _0xc1cbfe27(*args, **kwargs)

    async def invoke_async(self, *args, **kwargs):
        for _0xc1cbfe27 in self._0x5a0dd37e:
            if inspect.iscoroutinefunction(_0xc1cbfe27):
                await _0xc1cbfe27(*args, **kwargs)
            else:
                _0xc1cbfe27(*args, **kwargs)
_0xfaa92834 = _0x0eb5e6c6
_0xe230e072 = 4
_0x98be9e6c = 8
_0xb1f930f8 = 16

@dataclass
class _0x08e6ebbe:
    _0xbf104bbb: bool
    _0xd63cb1d8: str
    _0xebc9e48e: List[str] = field(default_factory=list)
    _0xac67ba21: List[str] = field(default_factory=list)

def _0x64325b3a(_0xa87deb01):
    _0x50fe03ab = _0xa87deb01.properties
    if isinstance(_0x50fe03ab, int):
        return bool(_0x50fe03ab & (_0xe230e072 | _0x98be9e6c))
    if isinstance(_0x50fe03ab, (list, tuple)):
        return any((_0x83878c91 in _0x50fe03ab for _0x83878c91 in (_0xd14e4b1f('7772697465'), _0xd14e4b1f('77726974652d776974686f75742d726573706f6e7365'))))
    return False

def _0x2ebafaf1(_0xa87deb01):
    _0x50fe03ab = _0xa87deb01.properties
    if isinstance(_0x50fe03ab, int):
        return bool(_0x50fe03ab & _0xb1f930f8)
    if isinstance(_0x50fe03ab, (list, tuple)):
        return _0xd14e4b1f('6e6f74696679') in _0x50fe03ab
    return False

def _0x7bed062f(_0x7ba7f01d):
    try:
        _0x10cd395c = list(_0x7ba7f01d)
    except Exception:
        return _0x08e6ebbe(_0xbf104bbb=True, _0xd63cb1d8=_0xfaa92834)
    for _0x961e38b5 in _0x10cd395c:
        if _0x961e38b5.uuid.lower() == _0xfaa92834:
            return _0x08e6ebbe(_0xbf104bbb=True, _0xd63cb1d8=_0xfaa92834)
    for _0x961e38b5 in _0x10cd395c:
        _0xd63cb1d8 = _0x961e38b5.uuid.lower()
        _0xa0306c03 = _0xd63cb1d8.endswith(_0x477e0659) and _0xd63cb1d8.startswith(_0xd14e4b1f('30303030'))
        _0xe1a8bd85 = any((not (_0x4a8a08f0.uuid.lower().endswith(_0x477e0659) and _0x4a8a08f0.uuid.lower().startswith(_0xd14e4b1f('30303030'))) for _0x4a8a08f0 in _0x961e38b5.characteristics))
        if _0xa0306c03 and (not _0xe1a8bd85):
            continue
        _0xebc9e48e = []
        _0xac67ba21 = []
        _0x84679292 = set()
        for _0xa87deb01 in _0x961e38b5.characteristics:
            _0xe1260894 = getattr(_0xa87deb01, _0xd14e4b1f('68616e646c65'), None)
            if _0x64325b3a(_0xa87deb01) and _0xe1260894 not in _0x84679292:
                if _0xe1260894 is not None:
                    _0x84679292.add(_0xe1260894)
                _0xebc9e48e.append(_0xa87deb01.uuid)
            if _0x2ebafaf1(_0xa87deb01):
                _0xac67ba21.append(_0xa87deb01.uuid)
        if _0xebc9e48e and _0xac67ba21:
            return _0x08e6ebbe(_0xbf104bbb=False, _0xd63cb1d8=_0xd63cb1d8, _0xebc9e48e=_0xebc9e48e, _0xac67ba21=_0xac67ba21)
    return _0x08e6ebbe(_0xbf104bbb=False, _0xd63cb1d8=_0xd14e4b1f('756e6b6e6f776e'))

@dataclass(frozen=True)
class _0xe4020c0f:
    uuid: str
    key: str
    name: str
    _0x10c1ecca: str
    _0x36cd38f4: str
    _0x3a6bdba8: str = _0xd14e4b1f('686578')
    entity_registry_enabled_default: bool = True
    _0x662f707d: bool = False

@dataclass(frozen=True)
class _0x689dc327:
    uuid: str
    key: str
    name: str
    _0x36cd38f4: str

@dataclass(frozen=True)
class _0x80bb1bf9:
    uuid: str
    _0x10c1ecca: str
    _0xd505dfd5: str
    key: str
    name: str
    _0x36cd38f4: str
    _0x3a6bdba8: str
    properties: tuple[str, ...]
    descriptors: tuple[str, ...]
    _0x500f1c43: bool
    _0xc83e24cd: bool
    _0x09f821ba: bool
    _0xdecb0dc3: bool
    entity_registry_enabled_default: bool
    _0x662f707d: bool
_0x568a6545: dict[str, _0x689dc327] = {_0x4b1c5d43: _0x689dc327(uuid=_0x4b1c5d43, key=_0xd14e4b1f('676170'), name=_0xd14e4b1f('47656e6572696320416363657373'), _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947')), _0x7ffbba85: _0x689dc327(uuid=_0x7ffbba85, key=_0xd14e4b1f('67617474'), name=_0xd14e4b1f('47656e6572696320417474726962757465'), _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947')), _0xe80ee6c3: _0x689dc327(uuid=_0xe80ee6c3, key=_0xd14e4b1f('6465766963655f696e666f726d6174696f6e'), name=_0xd14e4b1f('44657669636520496e666f726d6174696f6e'), _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947')), _0x0eb5e6c6: _0x689dc327(uuid=_0x0eb5e6c6, key=_0xd14e4b1f('676562657269745f7374616e646172645f64617461'), name=_0xd14e4b1f('47656265726974205374616e646172642044617461204368616e6e656c'), _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374')), _0x6871b74d: _0x689dc327(uuid=_0x6871b74d, key=_0xd14e4b1f('676562657269745f76656e646f725f736572766963655f61'), name=_0xd14e4b1f('476562657269742056656e646f7220536572766963652041'), _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374202f20476562657269742e4f54412e4c696272617279')), _0xe4e079bc: _0x689dc327(uuid=_0xe4e079bc, key=_0xd14e4b1f('676562657269745f76617269616e745f615f64617461'), name=_0xd14e4b1f('476562657269742056617269616e7420412044617461204368616e6e656c'), _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374')), _0x6594c694: _0x689dc327(uuid=_0x6594c694, key=_0xd14e4b1f('676562657269745f6f74615f7374'), name=_0xd14e4b1f('47656265726974204f54412053542053657276696365'), _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'))}
_0x3f37432f: dict[str, _0xe4020c0f] = {_0xd14e4b1f('30303030326130302d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326130302d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6761705f6465766963655f6e616d65'), name=_0xd14e4b1f('4741545420446576696365204e616d65'), _0x10c1ecca=_0x4b1c5d43, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326130312d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326130312d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6761705f617070656172616e6365'), name=_0xd14e4b1f('4741545420417070656172616e6365'), _0x10c1ecca=_0x4b1c5d43, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75696e7431365f6c65')), _0xd14e4b1f('30303030326130342d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326130342d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6761705f7072656665727265645f636f6e6e656374696f6e5f706172616d6574657273'), name=_0xd14e4b1f('50726566657272656420436f6e6e656374696f6e20506172616d6574657273'), _0x10c1ecca=_0x4b1c5d43, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('686578')), _0xd14e4b1f('30303030326130352d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326130352d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('676174745f736572766963655f6368616e676564'), name=_0xd14e4b1f('53657276696365204368616e676564'), _0x10c1ecca=_0x7ffbba85, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('30303030326132342d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132342d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f6d6f64656c5f6e756d626572'), name=_0xd14e4b1f('444953204d6f64656c204e756d626572'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326132352d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132352d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f73657269616c5f6e756d626572'), name=_0xd14e4b1f('4449532053657269616c204e756d626572'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326132362d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132362d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f6669726d776172655f7265766973696f6e'), name=_0xd14e4b1f('444953204669726d77617265205265766973696f6e'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326132372d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132372d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f68617264776172655f7265766973696f6e'), name=_0xd14e4b1f('444953204861726477617265205265766973696f6e'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326132382d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132382d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f736f6674776172655f7265766973696f6e'), name=_0xd14e4b1f('44495320536f667477617265205265766973696f6e'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('30303030326132392d303030302d313030302d383030302d303038303566396233346662'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030326132392d303030302d313030302d383030302d303038303566396233346662'), key=_0xd14e4b1f('6469735f6d616e7566616374757265725f6e616d65'), name=_0xd14e4b1f('444953204d616e756661637475726572204e616d65'), _0x10c1ecca=_0xe80ee6c3, _0x36cd38f4=_0xd14e4b1f('426c7565746f6f746820534947'), _0x3a6bdba8=_0xd14e4b1f('75746638')), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336131336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336131336530303030'), key=_0xd14e4b1f('7374616e646172645f77726974655f30'), name=_0xd14e4b1f('5374616e646172642057726974652030'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336132336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336132336530303030'), key=_0xd14e4b1f('7374616e646172645f77726974655f31'), name=_0xd14e4b1f('5374616e646172642057726974652031'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336133336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336133336530303030'), key=_0xd14e4b1f('7374616e646172645f77726974655f32'), name=_0xd14e4b1f('5374616e646172642057726974652032'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336134336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336134336530303030'), key=_0xd14e4b1f('7374616e646172645f77726974655f33'), name=_0xd14e4b1f('5374616e646172642057726974652033'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336135336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336135336530303030'), key=_0xd14e4b1f('7374616e646172645f6e6f746966795f30'), name=_0xd14e4b1f('5374616e64617264204e6f746966792030'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336136336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336136336530303030'), key=_0xd14e4b1f('7374616e646172645f6e6f746966795f31'), name=_0xd14e4b1f('5374616e64617264204e6f746966792031'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336137336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336137336530303030'), key=_0xd14e4b1f('7374616e646172645f6e6f746966795f32'), name=_0xd14e4b1f('5374616e64617264204e6f746966792032'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336138336530303030'): _0xe4020c0f(uuid=_0xd14e4b1f('33333334343239642d393066332d346334312d613032642d356362336138336530303030'), key=_0xd14e4b1f('7374616e646172645f6e6f746966795f33'), name=_0xd14e4b1f('5374616e64617264204e6f746966792033'), _0x10c1ecca=_0x0eb5e6c6, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e4c65676163792e41717561436c65616e50726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623130312d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623130312d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f6f74615f72657175657374'), name=_0xd14e4b1f('56617269616e742041204f54412052657175657374'), _0x10c1ecca=_0x6871b74d, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279202f20476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623131302d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623131302d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f73797374656d5f696e666f'), name=_0xd14e4b1f('56617269616e7420412053797374656d20496e666f'), _0x10c1ecca=_0x6871b74d, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279202f20476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374'), _0x3a6bdba8=_0xd14e4b1f('686578')), _0xd14e4b1f('35353965623132302d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623132302d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f6f74615f636f6e74726f6c'), name=_0xd14e4b1f('56617269616e742041204f544120436f6e74726f6c'), _0x10c1ecca=_0x6871b74d, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623132312d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623132312d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f6f74615f636f6e6669726d6174696f6e'), name=_0xd14e4b1f('56617269616e742041204f544120436f6e6669726d6174696f6e'), _0x10c1ecca=_0x6871b74d, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623132322d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623132322d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f6f74615f64617461'), name=_0xd14e4b1f('56617269616e742041204f54412044617461'), _0x10c1ecca=_0x6871b74d, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623030312d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623030312d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f77726974655f30'), name=_0xd14e4b1f('56617269616e7420412057726974652030'), _0x10c1ecca=_0xe4e079bc, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('35353965623030322d323339302d313165382d623436372d306564356638396637313862'): _0xe4020c0f(uuid=_0xd14e4b1f('35353965623030322d323339302d313165382d623436372d306564356638396637313862'), key=_0xd14e4b1f('76617269616e745f615f6e6f746966795f30'), name=_0xd14e4b1f('56617269616e742041204e6f746966792030'), _0x10c1ecca=_0xe4e079bc, _0x36cd38f4=_0xd14e4b1f('476562657269742e436f6d4c69622e426c7565746f6f74682e426c65323050726f64756374'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('30303030666531312d386532322d343534312d396434632d323165646165383265643139'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030666531312d386532322d343534312d396434632d323165646165383265643139'), key=_0xd14e4b1f('6f74615f73745f72657175657374'), name=_0xd14e4b1f('4f54412053542052657175657374'), _0x10c1ecca=_0x6594c694, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('30303030666532322d386532322d343534312d396434632d323165646165383265643139'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030666532322d386532322d343534312d396434632d323165646165383265643139'), key=_0xd14e4b1f('6f74615f73745f636f6e74726f6c'), name=_0xd14e4b1f('4f544120535420436f6e74726f6c'), _0x10c1ecca=_0x6594c694, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('30303030666532332d386532322d343534312d396434632d323165646165383265643139'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030666532332d386532322d343534312d396434632d323165646165383265643139'), key=_0xd14e4b1f('6f74615f73745f636f6e6669726d6174696f6e'), name=_0xd14e4b1f('4f544120535420436f6e6669726d6174696f6e'), _0x10c1ecca=_0x6594c694, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True), _0xd14e4b1f('30303030666532342d386532322d343534312d396434632d323165646165383265643139'): _0xe4020c0f(uuid=_0xd14e4b1f('30303030666532342d386532322d343534312d396434632d323165646165383265643139'), key=_0xd14e4b1f('6f74615f73745f64617461'), name=_0xd14e4b1f('4f54412053542044617461'), _0x10c1ecca=_0x6594c694, _0x36cd38f4=_0xd14e4b1f('476562657269742e4f54412e4c696272617279'), entity_registry_enabled_default=False, _0x662f707d=True)}

def _0x11906462(_0x2063c160):
    return str(_0x2063c160).lower()

def _0x4b49ea2d(_0xa2de09ab):
    _0x50fe03ab = _0xa2de09ab.properties
    if isinstance(_0x50fe03ab, int):
        _0x14f42e76 = []
        if _0x50fe03ab & 2:
            _0x14f42e76.append(_0xd14e4b1f('72656164'))
        if _0x50fe03ab & 4:
            _0x14f42e76.append(_0xd14e4b1f('77726974652d776974686f75742d726573706f6e7365'))
        if _0x50fe03ab & 8:
            _0x14f42e76.append(_0xd14e4b1f('7772697465'))
        if _0x50fe03ab & 16:
            _0x14f42e76.append(_0xd14e4b1f('6e6f74696679'))
        if _0x50fe03ab & 32:
            _0x14f42e76.append(_0xd14e4b1f('696e646963617465'))
        return tuple(_0x14f42e76)
    if isinstance(_0x50fe03ab, (list, tuple)):
        return tuple((str(_0x23a5b8ab).lower() for _0x23a5b8ab in _0x50fe03ab))
    return ()

def _0x4c284fb2(_0x7ba7f01d):
    _0x538416cf = {}
    for _0xaaabf0d3 in _0x7ba7f01d:
        _0x10c1ecca = _0x11906462(_0xaaabf0d3.uuid)
        _0x83140d05 = _0x568a6545.get(_0x10c1ecca)
        _0xd505dfd5 = _0x83140d05.name if _0x83140d05 else f"{_0xd14e4b1f('5365727669636520')}{_0x10c1ecca}"
        for _0xa2de09ab in _0xaaabf0d3.characteristics:
            _0x60bca6fc = _0x11906462(_0xa2de09ab.uuid)
            _0xc90ae688 = _0x3f37432f.get(_0x60bca6fc)
            if _0xc90ae688 is None:
                continue
            _0x74693d2f = _0x4b49ea2d(_0xa2de09ab)
            _0x1ebe3f3e = tuple((_0x11906462(_0x1dee80c7.uuid) for _0x1dee80c7 in getattr(_0xa2de09ab, _0xd14e4b1f('64657363726970746f7273'), ())))
            _0x538416cf[_0x60bca6fc] = _0x80bb1bf9(uuid=_0x60bca6fc, _0x10c1ecca=_0x10c1ecca, _0xd505dfd5=_0xd505dfd5, key=_0xc90ae688.key, name=_0xc90ae688.name, _0x36cd38f4=_0xc90ae688._0x36cd38f4, _0x3a6bdba8=_0xc90ae688._0x3a6bdba8, properties=_0x74693d2f, descriptors=_0x1ebe3f3e, _0x500f1c43=_0xd14e4b1f('72656164') in _0x74693d2f, _0xc83e24cd=_0xd14e4b1f('7772697465') in _0x74693d2f or _0xd14e4b1f('77726974652d776974686f75742d726573706f6e7365') in _0x74693d2f, _0x09f821ba=_0xd14e4b1f('6e6f74696679') in _0x74693d2f, _0xdecb0dc3=_0xd14e4b1f('696e646963617465') in _0x74693d2f, entity_registry_enabled_default=_0xc90ae688.entity_registry_enabled_default, _0x662f707d=_0xc90ae688._0x662f707d)
    return _0x538416cf

def _0xd3278554(_0x756bb351, _0x7f6f2cd1):
    _0x3a6bdba8 = _0x756bb351._0x3a6bdba8
    if _0x3a6bdba8 == _0xd14e4b1f('75746638'):
        return _0x7f6f2cd1.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('7265706c616365')).strip(_0xd14e4b1f('00')).strip()
    if _0x3a6bdba8 == _0xd14e4b1f('75696e7431365f6c65'):
        if len(_0x7f6f2cd1) >= 2:
            return int.from_bytes(_0x7f6f2cd1[:2], byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
        return None
    return _0x7f6f2cd1.hex()