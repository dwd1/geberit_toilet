from __future__ import annotations
from .protocol import _0x27401bf3, _0x340e827c, _0xa7830531, _0x367daf70

def _geberit_get_disabled_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL + 1)
    logger.propagate = False
    logger.disabled = True
    return logger

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')

def _0xaf5f5547(h):
    return bytes.fromhex(h)
import asyncio
from datetime import datetime, timedelta, timezone
import json
import logging
from pathlib import Path
import time
from typing import Any
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.storage import Store
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .config_helpers import _0x36ddd560, _0x1f4fdd89
from .log_helpers import device_log_context
from .const import _0xbf7c9959, _0xcff93a68, _0xc9d4372f, _0xcfc35486, _0xc83ac5c7, _0xdf46d1bc, _0xa9d4a173, _0xb8a5e944, _0x2dd4cb7c, _0xe4b27365, _0x2cbe1305, _0x378188b4, _0xb11e8fce, _0x7180920c, _0xb5df4305, _0xe4204fbd, _0x3c717acb, _0x3d99575a, _0xf2330fa3, _0x98513e7d, _0xcbc3ea1a, _0x5600d296, _0x515d6cbe, _0x5452b02e, _0xb98f4261, _0xeeafb6f6, _0x011c5d45, _0xc880a522, _0x8b0c8ba7, _0x5223e47e, _0x9755795a, _0x218f0966, _0x847653f3, _0x042bca9f
from .metadata import _0xfb98c9d8, _0xc9ed32a4, _0x64a7c4d5
from .catalog import _0xabe76933, _0xd7cd945d, _0x47e82895, _0x44eacae4
from .protocol import _0xabcea1bc
from .protocol import _0x6e2f7964, _0xbefb508d
from .DpId import DpId
from .protocol import _0x80bb1bf9, _0xd3278554, _0x4c284fb2
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x8a9cbaca = object()

def _0x85f8d15a(_0x32e2cb0f):
    return int(_0x32e2cb0f) & 32767

def _0x02583d67(_0x32e2cb0f):
    try:
        from .catalog import _0xb7aa207c
        _0x1a025ad3 = DpId(_0x32e2cb0f)
        _0x30618b3b = _0xb7aa207c(_0x1a025ad3.name, _0x2af72f10=None, _0x6fa93254=None)
        if _0x30618b3b is not None:
            return _0x340e827c(_0x30618b3b._0x3931108d)
    except Exception:
        pass
    return None

def _0xf86b1c33(_0x32e2cb0f, _0x37dc56b4, _0x3931108d=None):
    if not _0x37dc56b4:
        return None
    if _0x3931108d is None:
        _0x3931108d = _0x02583d67(_0x32e2cb0f)
    if _0x3931108d == _0x340e827c._0x27118326:
        try:
            _0xad054584 = _0x37dc56b4.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('69676e6f7265'))
            if _0xd14e4b1f('00') in _0xad054584:
                return _0xad054584.split(_0xd14e4b1f('00'), 1)[0]
            return _0xad054584
        except Exception:
            pass
    elif _0x3931108d == _0x340e827c._0x71fed0c3:
        return int.from_bytes(_0x37dc56b4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=True)
    elif _0x3931108d in (_0x340e827c._0x127d04b8, _0x340e827c._0x8f19a8c7, _0x340e827c._0xf670ea66, _0x340e827c._0x6a7e7316, _0x340e827c._0xc442a6c2, _0x340e827c._0xadaaee4b, _0x340e827c._0x64d12922, _0x340e827c._0xcf20423e, _0x340e827c._0x084c8428, _0x340e827c._0x471c4cee, _0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
        _0x2fa47f7c = len(_0x37dc56b4)
        if _0x2fa47f7c == 1:
            return _0x37dc56b4[0]
        else:
            return int.from_bytes(_0x37dc56b4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
    _0x2fa47f7c = len(_0x37dc56b4)
    if _0x2fa47f7c == 1:
        return _0x37dc56b4[0]
    elif _0x2fa47f7c == 2:
        return int.from_bytes(_0x37dc56b4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
    elif _0x2fa47f7c == 4:
        return int.from_bytes(_0x37dc56b4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
    else:
        try:
            _0xad054584 = _0x37dc56b4.decode(_0xd14e4b1f('7574662d38'), errors=_0xd14e4b1f('69676e6f7265'))
            if _0xd14e4b1f('00') in _0xad054584:
                return _0xad054584.split(_0xd14e4b1f('00'), 1)[0]
            return _0xad054584
        except Exception:
            return _0x37dc56b4.hex()

def _0x825031bd(_0x32e2cb0f, _0x7123a699=None):
    return int(_0x32e2cb0f) if _0x7123a699 is None else (int(_0x32e2cb0f), int(_0x7123a699))

def _0x726b25f9(_0x3c6e0b8a):
    if isinstance(_0x3c6e0b8a, tuple):
        return (int(_0x3c6e0b8a[0]), int(_0x3c6e0b8a[1]))
    return (int(_0x3c6e0b8a), None)

def _0x9e46b199(_0x3c6e0b8a):
    (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x3c6e0b8a)
    return (_0x32e2cb0f, -1 if _0x7123a699 is None else int(_0x7123a699))

def _0xc9e514d3(_0xf09cc7ee, _0xf7bd60b7):
    if _0xf7bd60b7 <= 0:
        return [_0xf09cc7ee]
    return [_0xf09cc7ee[_0x6a992d55:_0x6a992d55 + _0xf7bd60b7] for _0x6a992d55 in range(0, len(_0xf09cc7ee), _0xf7bd60b7)]

class _0x0409f5bf(DataUpdateCoordinator[dict[int, Any]]):

    def __init__(self, hass, entry):
        self._0x5f3f26ad = entry
        _0x3a8e4c06 = {**entry.data, **entry.options}
        self._device_id = _0x3a8e4c06[_0xcff93a68]
        self._0x1a77b829 = _0x3a8e4c06.get(_0xcfc35486) or None
        self._0x62b5eb13 = _0x3a8e4c06.get(_0xc83ac5c7, _0x3c717acb)
        self._0xb035b8bf = _0x3a8e4c06.get(_0xdf46d1bc) or None
        self._0x9803e4e7 = _0x3a8e4c06.get(_0xc9d4372f) or None
        self._0x96ffac89 = _0x3a8e4c06.get(_0xb8a5e944, _0x9755795a)
        self._0x44904414 = _0x36ddd560(_0x3a8e4c06.get(_0x2dd4cb7c))
        self._0x10eef11a = bool(_0x3a8e4c06.get(_0xe4b27365, True))
        self._0xda99faac = bool(_0x3a8e4c06.get(_0x2cbe1305, True))
        self._0x361c3e6d = set(_0x1f4fdd89(_0x3a8e4c06.get(_0x378188b4))) if self._0x10eef11a else set()
        self._0xe364388d = {int(_0x42aefbae[0]) if isinstance(_0x42aefbae, tuple) else int(_0x42aefbae) for _0x42aefbae in self._0x361c3e6d}
        self._0x87b637aa = set(_0x1f4fdd89(_0x3a8e4c06.get(_0xb11e8fce))) if self._0xda99faac else set()
        self._0x05ecc105 = {int(_0x42aefbae) for _0x42aefbae in self._0x87b637aa if isinstance(_0x42aefbae, int)}
        self._0x66fef6a3 = {int(_0x32e2cb0f) for _0x32e2cb0f in _0x847653f3}
        self._0x4202d2ae = int(_0x3a8e4c06.get(_0x7180920c, _0x3d99575a))
        self._0x285f2b4b = bool(_0x3a8e4c06.get(_0xb5df4305, False))
        self._0x39779d0f = float(_0x3a8e4c06.get(_0xe4204fbd, _0x98513e7d))
        _0x1937ffd8 = _0x3a8e4c06.get(_0xa9d4a173, _0xf2330fa3)
        self._0x5755254e = timedelta(seconds=_0x1937ffd8)
        self._0xadbbed2f = asyncio.Lock()
        self._0x25cb3c49 = None
        self._0x77ad7fd7 = {}
        self._0x5db8c29c = None
        self._0xdedd8ef4 = {}
        self._0x4250c6b6 = {}
        self._0x3522077d = {}
        self._0x93b9730d = {}
        self._0x84f90afc = {}
        self._0xa6f36771 = set()
        self._0xd05acf0b = set()
        self._0x68eea019 = False
        self._0x94b57abb = {}
        self._0xaaf9910f = set()
        self._0x01aa0845 = set()
        self._0x8f41c896 = False
        self.poll_enabled = True
        self._0xe86ce9bc = asyncio.Event()
        self._0xe86ce9bc.set()
        self._0xfb5e2f47 = Store(hass, 1, f"{_0xbf7c9959}{_0xd14e4b1f('5f')}{entry.entry_id}{_0xd14e4b1f('5f646973636f76657279')}")
        self._0x87d447af = Store(hass, 1, f"{_0xbf7c9959}{_0xd14e4b1f('5f')}{entry.entry_id}{_0xd14e4b1f('5f7374617465')}")
        self._0x613d9d8a = []
        self._0x05e7f539 = None
        self._0x336f52c9 = None
        self._0x8dfd5bd3 = {}
        self._0x4aec38a9 = None
        self._0xffe5c0a0 = None
        self._0x084706dd = None
        self._0xd4252973 = None
        self._0x5d1bb011 = []
        self._0xd3a0bb01 = {}
        self._0x9ff434a9 = {}
        self._0xb8223521 = set()
        self._0xe68baedb = None
        self._0xf6b7615e = asyncio.Lock()
        self._0x5eda439f = False
        self._0x80c14035 = False
        self._0xd8c19966 = asyncio.Event()
        self._0xcbec47bb = False
        self._0xe77f8e52 = []
        self._0xb41ecae5 = None
        self._0x60d33921 = None
        self._0x92e70e01 = None
        self._0xabcb4e1a = False
        self._0x73d4c228 = False
        self._0x57274421 = _0xcbc3ea1a
        self._0xbe3450d2 = False
        self._0x878b4eb8 = None
        self._0x49464da6 = None
        self._0x0104f66a = False
        self._0xa1de6604 = False
        self._0xbb786552 = False
        self._0xf3e35bdf = _0x5600d296
        self._0x23c6e6a5 = False
        self._0x5d231dfe = asyncio.Lock()
        self._0x2ce69584 = None
        self._0xe8e1c9b0 = False
        if hass:
            self._0x2ce69584 = hass.bus.async_listen(er.EVENT_ENTITY_REGISTRY_UPDATED, self._0x616f970c)
        super().__init__(hass, _LOGGER, name=_0xbf7c9959, update_interval=self._0x5755254e)

    def _0xb0ae159e(self):
        if self._0xbb786552 or self._0x80c14035 or self._0x5eda439f or (self._0xe68baedb is not None):
            return
        self._0xe68baedb = asyncio.create_task(self._0x77e0443f())

    def _0xa67a8c65(self, _0x2ed18faf):
        self._0x8dfd5bd3 = dict(_0x2ed18faf)

    def _0x3147b7f8(self, _0x78e73102, *_0xa956af09):
        if _0x042bca9f:
            pass

    def _0x18ad59bd(self, _0x32e2cb0f, _0x37dc56b4):
        _0x3931108d = None
        if self._0x25cb3c49 is not None:
            _0x1043bfc7 = self._0x25cb3c49.get(_0x32e2cb0f)
            if _0x1043bfc7 is not None:
                _0x3931108d = _0x1043bfc7.get(_0xd14e4b1f('6461746174797065'))
        return _0xf86b1c33(_0x32e2cb0f, _0x37dc56b4, _0x3931108d=_0x3931108d)

    def _0xa25b26bb(self, _0x2063c160):
        if _0x2063c160 > 2147483647:
            return _0x2063c160 - 4294967296
        return _0x2063c160

    def _0x57023259(self):
        _0x0c52488c = 0
        _0x729548c7 = self._0xf096db62(705, _0xc21f969b=None)
        if isinstance(_0x729548c7, int):
            _0x0c52488c = self._0xa25b26bb(_0x729548c7)
        if hasattr(DpId, _0xd14e4b1f('44505f4441594c494748545f534156494e475f4f4646534554')):
            _0x2cd933f2 = self._0xf096db62(706, _0xc21f969b=None)
            if isinstance(_0x2cd933f2, int):
                _0x0c52488c += self._0xa25b26bb(_0x2cd933f2)
                return _0x0c52488c
        _0x5e625e25 = self._0xf096db62(548, _0xc21f969b=None)
        if _0x5e625e25 == 1:
            _0x0c52488c += 3600
        return _0x0c52488c

    def _0xf1dfc2fd(self, _0xe9a23cbc):
        if _0xe9a23cbc is None:
            return None
        return self._0x8dfd5bd3.get(_0xe9a23cbc.key, _0xe9a23cbc.name)

    def _0xf096db62(self, _0x32e2cb0f, _0x7123a699=0, _0xc21f969b=None):
        _0x8d777f38 = self.data or {}
        if _0x7123a699 is not None:
            _0xe98f27c3 = _0x825031bd(int(_0x32e2cb0f), _0x7123a699)
            if _0xe98f27c3 in _0x8d777f38:
                return _0x8d777f38[_0xe98f27c3]
        _0xeef79ba5 = int(_0x32e2cb0f)
        if _0xeef79ba5 in _0x8d777f38:
            return _0x8d777f38[_0xeef79ba5]
        if _0x7123a699 is None:
            _0x686090eb = _0x825031bd(int(_0x32e2cb0f), 0)
            if _0x686090eb in _0x8d777f38:
                return _0x8d777f38[_0x686090eb]
        return _0xc21f969b

    @property
    def _0xe1c408bb(self):
        _0x2063c160 = self._0xf096db62(0)
        if isinstance(_0x2063c160, int):
            return _0x2063c160
        return self._0x4aec38a9

    @property
    def _0x98f64478(self):
        _0x2063c160 = self._0xf096db62(1)
        if isinstance(_0x2063c160, int):
            return _0x2063c160
        return self._0xffe5c0a0

    async def _0x071e72da(self, _0x62608e08):
        if self._0x4aec38a9 is not None and self._0xffe5c0a0 is not None:
            return (self._0x4aec38a9, self._0xffe5c0a0)
        try:
            _0x5cff356a = await _0x62608e08.read(int(0))
            _0xf0f57759 = await _0x62608e08.read(int(1))
        except Exception as _0x56bd7107:
            return (self._0x4aec38a9, self._0xffe5c0a0)
        if _0x5cff356a:
            self._0x4aec38a9 = int(_0x5cff356a[0])
        if _0xf0f57759:
            self._0xffe5c0a0 = int(_0xf0f57759[0])
        return (self._0x4aec38a9, self._0xffe5c0a0)

    @property
    def _0x7f4be311(self):
        return _0x47e82895(self._0xe1c408bb, self._0x98f64478)

    @property
    def _0x9ddac438(self):
        if self._0x084706dd:
            return self._0x084706dd.rssi
        return None

    @property
    def _0x70b8e2d2(self):
        if self._0x084706dd:
            return self._0x084706dd._0x70b8e2d2
        return None

    def _0x971a9022(self, _0xa68071d3):
        _0xa1031145 = _0xd7cd945d(self._0xe1c408bb, self._0x98f64478)
        if _0xa1031145 is None:
            return None
        _0x14f42e76 = _0xa68071d3.upper()
        if not _0x14f42e76.startswith(_0xd14e4b1f('44505f')):
            _0x14f42e76 = f"{_0xd14e4b1f('44505f')}{_0x14f42e76}"
        return _0x14f42e76 in _0xa1031145

    @property
    def _0xf38a44f4(self):
        return Path(self.hass.config.path(_0x218f0966))

    @property
    def _0x650796ba(self):
        return Path(self.hass.config.path(_0xeeafb6f6))

    @property
    def _0x078cf264(self):
        return self._device_id.replace(_0xd14e4b1f('3a'), _0xd14e4b1f('2d'))

    @property
    def _0x26e0440e(self):
        return list(self._0x613d9d8a)

    @property
    def _0x94131d13(self):
        return list(self._0x613d9d8a)

    @property
    def _0x70308f6c(self):
        if self._0x05e7f539 is None:
            return list(self._0x613d9d8a)
        return [_0xb068931c for _0xb068931c in self._0x613d9d8a if _0xb068931c != self._0x05e7f539]

    @property
    def _0x555427b0(self):
        return self._0x05e7f539

    @property
    def _0xfac3be13(self):
        return self._0x336f52c9

    def _0xb0084e77(self, _0x3c6e0b8a):
        if isinstance(_0x3c6e0b8a, tuple) and len(_0x3c6e0b8a) == 2:
            return {_0xd14e4b1f('64705f6964'): int(_0x3c6e0b8a[0]), _0xd14e4b1f('696e7374616e6365'): int(_0x3c6e0b8a[1]), _0xd14e4b1f('636f6d706f736974655f6b6579'): f"{int(_0x3c6e0b8a[0])}{_0xd14e4b1f('3a')}{int(_0x3c6e0b8a[1])}"}
        return {_0xd14e4b1f('64705f6964'): int(_0x3c6e0b8a), _0xd14e4b1f('696e7374616e6365'): None, _0xd14e4b1f('636f6d706f736974655f6b6579'): str(int(_0x3c6e0b8a))}

    def _0xe822d7dd(self, _0x2063c160):
        if isinstance(_0x2063c160, (str, int, float, bool)) or _0x2063c160 is None:
            return _0x2063c160
        if isinstance(_0x2063c160, bytes):
            return _0x2063c160.hex()
        if isinstance(_0x2063c160, dict):
            return {str(_0x8ce4b16b): self._0xe822d7dd(_0x9e3669d1) for (_0x8ce4b16b, _0x9e3669d1) in _0x2063c160.items()}
        if isinstance(_0x2063c160, (list, tuple, set)):
            return [self._0xe822d7dd(_0x447b7147) for _0x447b7147 in _0x2063c160]
        return str(_0x2063c160)

    def _0xc5ab37b2(self):
        _0x8d777f38 = self.data or {}
        _0x8e9fd395 = []
        _0xf9fb410d = er.async_get(self.hass)
        _0x22b7b841 = sorted({_0x1043bfc7.entity_id for _0x1043bfc7 in er.async_entries_for_config_entry(_0xf9fb410d, self._0x5f3f26ad.entry_id) if _0x1043bfc7.entity_id})
        for _0xdffc4713 in _0x22b7b841:
            _0x9ed39e2e = self.hass.states.get(_0xdffc4713)
            if _0x9ed39e2e is None:
                continue
            _0x425ce871 = _0x9ed39e2e.attributes
            _0x8e9fd395.append({_0xd14e4b1f('656e746974795f6964'): _0xdffc4713, _0xd14e4b1f('7374617465'): _0x9ed39e2e.state, _0xd14e4b1f('61747472696275746573'): self._0xe822d7dd(dict(_0x425ce871)), _0xd14e4b1f('6c6173745f6368616e676564'): _0x9ed39e2e.last_changed.isoformat(), _0xd14e4b1f('6c6173745f75706461746564'): _0x9ed39e2e.last_updated.isoformat()})
        _0xd2ab55e1 = []
        for _0x3c6e0b8a in sorted(_0x8d777f38, key=lambda item: str(item)):
            _0xe67a0377 = self._0xb0084e77(_0x3c6e0b8a)
            _0xe9a23cbc = self._0xf1645e71(_0xe67a0377[_0xd14e4b1f('64705f6964')])
            _0xfa89cff0 = _0x3c6e0b8a if _0x3c6e0b8a in self._0xdedd8ef4 else _0xe67a0377[_0xd14e4b1f('64705f6964')]
            _0x7f6f2cd1 = self._0xdedd8ef4.get(_0xfa89cff0)
            _0xd2ab55e1.append({**_0xe67a0377, _0xd14e4b1f('6e616d65'): _0xe9a23cbc.name if _0xe9a23cbc else None, _0xd14e4b1f('64705f6b6579'): _0xe9a23cbc.key if _0xe9a23cbc else None, _0xd14e4b1f('6465636f6465645f76616c7565'): self._0xe822d7dd(_0x8d777f38[_0x3c6e0b8a]), _0xd14e4b1f('7261775f686578'): _0x7f6f2cd1.hex() if isinstance(_0x7f6f2cd1, bytes) else None})
        _0xeadea811 = []
        for (_0xef7c876f, _0x756bb351) in sorted(self._0x3522077d.items()):
            _0x7f6f2cd1 = self._0x93b9730d.get(_0xef7c876f)
            _0xeadea811.append({_0xd14e4b1f('75756964'): _0xef7c876f, _0xd14e4b1f('736572766963655f75756964'): _0x756bb351._0x10c1ecca, _0xd14e4b1f('736572766963655f6e616d65'): _0x756bb351._0xd505dfd5, _0xd14e4b1f('6b6579'): _0x756bb351.key, _0xd14e4b1f('6e616d65'): _0x756bb351.name, _0xd14e4b1f('736f75726365'): _0x756bb351._0x36cd38f4, _0xd14e4b1f('70726f70657274696573'): list(_0x756bb351.properties), _0xd14e4b1f('7265616461626c65'): _0x756bb351._0x500f1c43, _0xd14e4b1f('7772697461626c65'): _0x756bb351._0xc83e24cd, _0xd14e4b1f('6e6f7469666961626c65'): _0x756bb351._0x09f821ba, _0xd14e4b1f('696e646963617461626c65'): _0x756bb351._0xdecb0dc3, _0xd14e4b1f('6465636f6465645f76616c7565'): self._0xe822d7dd(self._0x84f90afc.get(_0xef7c876f)), _0xd14e4b1f('7261775f686578'): _0x7f6f2cd1.hex() if isinstance(_0x7f6f2cd1, bytes) else None})
        return {_0xd14e4b1f('67656e6572617465645f6174'): datetime.now(timezone.utc).isoformat(), _0xd14e4b1f('646f6d61696e'): _0xbf7c9959, _0xd14e4b1f('6465766963655f6964'): self._device_id, _0xd14e4b1f('726571756573745f646174615f6d6f6465'): self._0x96ffac89, _0xd14e4b1f('636f6d6d756e69636174696f6e5f6d6f6465'): self._0x44904414, _0xd14e4b1f('6d61785f696e7374616e6365735f7065725f647069645f67726f7570'): self._0x4202d2ae, _0xd14e4b1f('6578706f73655f6c617267655f696e7374616e63655f67726f757073'): self._0x285f2b4b, _0xd14e4b1f('706f6c6c5f656e61626c6564'): self.poll_enabled, _0xd14e4b1f('626c655f636f6e6e6563746564'): self._0x3a821fc7, _0xd14e4b1f('737570706f727465645f64705f696473'): sorted(self._0x3a3a4684), _0xd14e4b1f('636f6e666967757265645f696e636c7564655f74617267657473'): [str(_0x42aefbae) for _0x42aefbae in sorted(self._0x361c3e6d, key=str)], _0xd14e4b1f('636f6e666967757265645f6578636c7564655f74617267657473'): [str(_0x42aefbae) for _0x42aefbae in sorted(self._0x87b637aa, key=str)], _0xd14e4b1f('646973636f76657265645f6e6f6e5f696e76656e746f72795f6470696473'): sorted(self._0xa6f36771), _0xd14e4b1f('64705f76616c756573'): _0xd2ab55e1, _0xd14e4b1f('676174745f76616c756573'): _0xeadea811, _0xd14e4b1f('656e746974795f737461746573'): sorted(_0x8e9fd395, key=lambda item: item[_0xd14e4b1f('656e746974795f6964')])}

    def _0xa745bc87(self, _0x32e2cb0f, _0xcd89a998=0):
        return {_0xd14e4b1f('696e7374616e6365'): max(0, int(_0xcd89a998)), _0xd14e4b1f('76657273696f6e'): 1, _0xd14e4b1f('6461746174797065'): 0, _0xd14e4b1f('6d696e5f73'): 0, _0xd14e4b1f('6d61785f73'): 0, _0xd14e4b1f('6d696e5f75'): 0, _0xd14e4b1f('6d61785f75'): 0, _0xd14e4b1f('69735f696e7465726e616c'): False, _0xd14e4b1f('6265686176696f72'): 0}

    def _0x8855987e(self, _0x584a4881):
        if self._0x25cb3c49 is None:
            return
        _0x8977dfac = False
        for _0x32e2cb0f in sorted({int(_0x32e2cb0f) for _0x32e2cb0f in _0x584a4881}):
            if self._0xc97399be(_0x32e2cb0f) or _0x32e2cb0f in self._0x25cb3c49:
                continue
            self._0x25cb3c49[_0x32e2cb0f] = self._0xa745bc87(_0x32e2cb0f)
            self._0xd05acf0b.add(_0x32e2cb0f)
            _0x8977dfac = True
        if _0x8977dfac:
            self._0x77ad7fd7 = _0x64a7c4d5(self._0x25cb3c49)

    def _0x4ef26b0c(self):
        if self._0x25cb3c49 is None:
            return
        if self._0x96ffac89 == _0x5223e47e:
            self._0x8855987e(self._0x63735d9e)

    def _0xa24b5ca2(self, _0x7a1eabc3):
        for _0x42aefbae in sorted(self._0x361c3e6d, key=str):
            if isinstance(_0x42aefbae, tuple):
                _0x32e2cb0f = int(_0x42aefbae[0])
                _0x7123a699 = int(_0x42aefbae[1])
                _0xf4e0ac58 = _0x7a1eabc3.get(_0x32e2cb0f)
                _0x7bf81a74 = _0x7123a699 + 1
                if _0xf4e0ac58 is None:
                    _0x7a1eabc3[_0x32e2cb0f] = self._0xa745bc87(_0x32e2cb0f, _0x7bf81a74)
                    continue
                _0xc7a133de = int(_0xf4e0ac58.get(_0xd14e4b1f('696e7374616e6365')) or 0)
                if _0x7bf81a74 > _0xc7a133de:
                    _0x0f81d52e = dict(_0xf4e0ac58)
                    _0x0f81d52e[_0xd14e4b1f('696e7374616e6365')] = _0x7bf81a74
                    _0x7a1eabc3[_0x32e2cb0f] = _0x0f81d52e
                continue
            _0x32e2cb0f = int(_0x42aefbae)
            if _0x32e2cb0f not in _0x7a1eabc3:
                _0x7a1eabc3[_0x32e2cb0f] = self._0xa745bc87(_0x32e2cb0f)

    def _0xc2158c33(self, _0x32e2cb0f):
        return int(_0x32e2cb0f) in self._0x66fef6a3

    def _0x5a04c375(self, _0x32e2cb0f):
        return int(_0x32e2cb0f) in self._0xd05acf0b

    def _0xfb787114(self, _0x32e2cb0f):
        return int(_0x32e2cb0f) in self._0xe364388d

    def _0x5ac01e09(self, _0x958b30d4):
        _0x32e2cb0f = int(_0x958b30d4[0] if isinstance(_0x958b30d4, tuple) else _0x958b30d4)
        if self._0xfb787114(_0x32e2cb0f):
            return True
        return _0x958b30d4 in self._0x361c3e6d

    def _0xc97399be(self, _0x958b30d4):
        _0x32e2cb0f = int(_0x958b30d4[0] if isinstance(_0x958b30d4, tuple) else _0x958b30d4)
        if not self._0xc2158c33(_0x32e2cb0f):
            return False
        return not self._0x5ac01e09(_0x958b30d4)

    def _0x4cc51d69(self, _0x7a1eabc3):
        return {int(_0x32e2cb0f): _0xa4ade155 for (_0x32e2cb0f, _0xa4ade155) in _0x7a1eabc3.items() if not self._0xc97399be(int(_0x32e2cb0f))}

    def _0x170e46b0(self, _0xd6fe1d0b, _0x321c3cf4):
        _0xd6fe1d0b.parent.mkdir(parents=True, exist_ok=True)
        _0xd6fe1d0b.write_text(json.dumps(_0x321c3cf4, indent=2, ensure_ascii=False, sort_keys=True), encoding=_0xd14e4b1f('7574662d38'))

    def _0x1140dba0(self, _0xd6fe1d0b):
        return json.loads(_0xd6fe1d0b.read_text(encoding=_0xd14e4b1f('7574662d38')))

    def _0x0612dd7f(self):
        _0xf38a44f4 = self._0xf38a44f4
        _0xf38a44f4.mkdir(parents=True, exist_ok=True)
        _0x851f5ac9 = f"{self._0x078cf264.lower()}{_0xd14e4b1f('5f')}"
        return sorted((_0xd6fe1d0b.name for _0xd6fe1d0b in _0xf38a44f4.glob(_0xd14e4b1f('2a2e6a736f6e')) if _0xd6fe1d0b.name.lower().startswith(_0x851f5ac9)), reverse=True)

    async def _0x009a3261(self):
        _0x26e0440e = await self.hass.async_add_executor_job(self._0x0612dd7f)
        self._0x613d9d8a = _0x26e0440e
        if not _0x26e0440e:
            self._0x05e7f539 = None
            self._0x336f52c9 = None
        else:
            if self._0x05e7f539 not in _0x26e0440e:
                self._0x05e7f539 = _0x26e0440e[0]
            _0xf3625bbe = self._0x70308f6c
            if not _0xf3625bbe:
                self._0x336f52c9 = None
            elif self._0x336f52c9 not in _0xf3625bbe:
                self._0x336f52c9 = _0xf3625bbe[0]
        self.async_update_listeners()

    async def _0x4fc51951(self, _0x435ed7e9):
        await self._0x009a3261()
        if _0x435ed7e9 not in self._0x613d9d8a:
            raise ValueError(f"{_0xd14e4b1f('556e6b6e6f776e207265706f72742066696c653a20')}{_0x435ed7e9}")
        self._0x05e7f539 = _0x435ed7e9
        _0xf3625bbe = self._0x70308f6c
        if not _0xf3625bbe:
            self._0x336f52c9 = None
        elif self._0x336f52c9 not in _0xf3625bbe:
            self._0x336f52c9 = _0xf3625bbe[0]
        self.async_update_listeners()

    async def _0x6060d761(self, _0x435ed7e9):
        await self._0x009a3261()
        if _0x435ed7e9 not in self._0x70308f6c:
            raise ValueError(f"{_0xd14e4b1f('556e6b6e6f776e207265706f72742066696c653a20')}{_0x435ed7e9}")
        self._0x336f52c9 = _0x435ed7e9
        self.async_update_listeners()

    async def _0x9d135782(self):
        _0x321c3cf4 = self._0xc5ab37b2()
        _0xd7e6d55b = datetime.now(timezone.utc).strftime(_0xd14e4b1f('2559256d25642d2548254d25532d2566'))
        _0x435ed7e9 = f"{self._0x078cf264}{_0xd14e4b1f('5f')}{_0xd7e6d55b}{_0xd14e4b1f('2e6a736f6e')}"
        _0xd6fe1d0b = self._0xf38a44f4 / _0x435ed7e9
        await self.hass.async_add_executor_job(self._0x170e46b0, _0xd6fe1d0b, _0x321c3cf4)
        await self._0x009a3261()
        return str(_0xd6fe1d0b)

    def _0x042d512d(self, _0xf52b4660, _0x4ea12c72, _0xd598e8f9, _0xf38d2c59):
        _0x980da984 = [f"{_0xd14e4b1f('4765626572697420546f696c6574207265706f727420646966666572656e636573')}", f"{_0xd14e4b1f('4c656674203a20')}{_0xf52b4660}", f"{_0xd14e4b1f('52696768743a20')}{_0xd598e8f9}", '']
        _0x9f90b10f = {_0x447b7147[_0xd14e4b1f('636f6d706f736974655f6b6579')]: _0x447b7147 for _0x447b7147 in _0x4ea12c72.get(_0xd14e4b1f('64705f76616c756573'), [])}
        _0x53f78e1d = {_0x447b7147[_0xd14e4b1f('636f6d706f736974655f6b6579')]: _0x447b7147 for _0x447b7147 in _0xf38d2c59.get(_0xd14e4b1f('64705f76616c756573'), [])}
        _0xbab69c5e = sorted(set(_0x9f90b10f) | set(_0x53f78e1d))
        _0xcff2507a = []
        for _0x3c6e0b8a in _0xbab69c5e:
            _0x149603e6 = _0x9f90b10f.get(_0x3c6e0b8a)
            _0x22af645d = _0x53f78e1d.get(_0x3c6e0b8a)
            if _0x149603e6 is None:
                _0xcff2507a.append(f"""{_0xd14e4b1f('2b204450494420')}{_0x3c6e0b8a}{_0xd14e4b1f('2061646465643a20')}{_0x22af645d.get(f"{_0xd14e4b1f('6465636f6465645f76616c7565')}")!r}{_0xd14e4b1f('207261773d')}{_0x22af645d.get(f"{_0xd14e4b1f('7261775f686578')}")}""")
                continue
            if _0x22af645d is None:
                _0xcff2507a.append(f"""{_0xd14e4b1f('2d204450494420')}{_0x3c6e0b8a}{_0xd14e4b1f('2072656d6f7665643a20')}{_0x149603e6.get(f"{_0xd14e4b1f('6465636f6465645f76616c7565')}")!r}{_0xd14e4b1f('207261773d')}{_0x149603e6.get(f"{_0xd14e4b1f('7261775f686578')}")}""")
                continue
            if _0x149603e6.get(_0xd14e4b1f('6465636f6465645f76616c7565')) != _0x22af645d.get(_0xd14e4b1f('6465636f6465645f76616c7565')) or _0x149603e6.get(_0xd14e4b1f('7261775f686578')) != _0x22af645d.get(_0xd14e4b1f('7261775f686578')):
                _0xb068931c = _0x22af645d.get(_0xd14e4b1f('6e616d65')) or _0x149603e6.get(_0xd14e4b1f('6e616d65')) or _0x3c6e0b8a
                _0xcff2507a.append(f"""{_0xd14e4b1f('2a204450494420')}{_0x3c6e0b8a}{_0xd14e4b1f('2028')}{_0xb068931c}{_0xd14e4b1f('293a20')}{_0x149603e6.get(f"{_0xd14e4b1f('6465636f6465645f76616c7565')}")!r}{_0xd14e4b1f('202d3e20')}{_0x22af645d.get(f"{_0xd14e4b1f('6465636f6465645f76616c7565')}")!r}{_0xd14e4b1f('207c2072617720')}{_0x149603e6.get(f"{_0xd14e4b1f('7261775f686578')}")}{_0xd14e4b1f('202d3e20')}{_0x22af645d.get(f"{_0xd14e4b1f('7261775f686578')}")}""")
        _0x980da984.append(_0xd14e4b1f('44504944206368616e6765733a'))
        if _0xcff2507a:
            _0x980da984.extend(_0xcff2507a)
        else:
            _0x980da984.append(_0xd14e4b1f('4e6f2044504944206368616e6765732e'))
        _0x980da984.append('')
        _0xb366c561 = {_0x447b7147[_0xd14e4b1f('656e746974795f6964')]: _0x447b7147 for _0x447b7147 in _0x4ea12c72.get(_0xd14e4b1f('656e746974795f737461746573'), [])}
        _0x4356d759 = {_0x447b7147[_0xd14e4b1f('656e746974795f6964')]: _0x447b7147 for _0x447b7147 in _0xf38d2c59.get(_0xd14e4b1f('656e746974795f737461746573'), [])}
        _0x376de6d7 = sorted(set(_0xb366c561) | set(_0x4356d759))
        _0x12eae98b = []
        for _0xdffc4713 in _0x376de6d7:
            _0x149603e6 = _0xb366c561.get(_0xdffc4713)
            _0x22af645d = _0x4356d759.get(_0xdffc4713)
            if _0x149603e6 is None:
                _0x12eae98b.append(f"""{_0xd14e4b1f('2b20456e7469747920')}{_0xdffc4713}{_0xd14e4b1f('206164646564207769746820737461746520')}{_0x22af645d.get(f"{_0xd14e4b1f('7374617465')}")!r}""")
                continue
            if _0x22af645d is None:
                _0x12eae98b.append(f"""{_0xd14e4b1f('2d20456e7469747920')}{_0xdffc4713}{_0xd14e4b1f('2072656d6f766564202877617320')}{_0x149603e6.get(f"{_0xd14e4b1f('7374617465')}")!r}{_0xd14e4b1f('29')}""")
                continue
            if _0x149603e6.get(_0xd14e4b1f('7374617465')) != _0x22af645d.get(_0xd14e4b1f('7374617465')):
                _0x12eae98b.append(f"""{_0xd14e4b1f('2a20456e7469747920')}{_0xdffc4713}{_0xd14e4b1f('2073746174653a20')}{_0x149603e6.get(f"{_0xd14e4b1f('7374617465')}")!r}{_0xd14e4b1f('202d3e20')}{_0x22af645d.get(f"{_0xd14e4b1f('7374617465')}")!r}""")
            if _0x149603e6.get(_0xd14e4b1f('61747472696275746573')) != _0x22af645d.get(_0xd14e4b1f('61747472696275746573')):
                _0x12eae98b.append(f"{_0xd14e4b1f('2a20456e7469747920')}{_0xdffc4713}{_0xd14e4b1f('2061747472696275746573206368616e676564')}")
        _0x980da984.append(_0xd14e4b1f('456e74697479206368616e6765733a'))
        if _0x12eae98b:
            _0x980da984.extend(_0x12eae98b)
        else:
            _0x980da984.append(_0xd14e4b1f('4e6f20656e74697479206368616e6765732e'))
        _0x980da984.append('')
        return _0xd14e4b1f('0a').join(_0x980da984)

    async def _0xf9668b85(self):
        await self._0x009a3261()
        _0xf52b4660 = self._0x05e7f539
        _0xd598e8f9 = self._0x336f52c9
        if not _0xf52b4660 or not _0xd598e8f9:
            raise ValueError(_0xd14e4b1f('54776f207265706f72742066696c6573206d75737420626520617661696c61626c6520616e642073656c6563746564206265666f726520636f6d70617269736f6e'))
        if _0xf52b4660 == _0xd598e8f9:
            raise ValueError(_0xd14e4b1f('506c656173652063686f6f73652074776f20646966666572656e74207265706f72742066696c657320666f7220636f6d70617269736f6e'))
        _0x277bfd11 = self._0xf38a44f4 / _0xf52b4660
        _0xbb24175b = self._0xf38a44f4 / _0xd598e8f9
        (_0x4ea12c72, _0xf38d2c59) = await asyncio.gather(self.hass.async_add_executor_job(self._0x1140dba0, _0x277bfd11), self.hass.async_add_executor_job(self._0x1140dba0, _0xbb24175b))
        _0x5d84972c = self._0x042d512d(_0xf52b4660, _0x4ea12c72, _0xd598e8f9, _0xf38d2c59)
        _0xd7e6d55b = datetime.now(timezone.utc).strftime(_0xd14e4b1f('2559256d25642d2548254d25532d2566'))
        _0x89b2f702 = f"{Path(_0xf52b4660).stem}{_0xd14e4b1f('5f5f76735f5f')}{Path(_0xd598e8f9).stem}{_0xd14e4b1f('5f5f')}{_0xd7e6d55b}{_0xd14e4b1f('2e747874')}"
        _0x412c0d51 = self._0x650796ba / _0x89b2f702
        await self.hass.async_add_executor_job(self._0x7ce538b3, _0x412c0d51, _0x5d84972c)
        return str(_0x412c0d51)

    def _0x7ce538b3(self, _0xd6fe1d0b, _0x1cb251ec):
        _0xd6fe1d0b.parent.mkdir(parents=True, exist_ok=True)
        _0xd6fe1d0b.write_text(_0x1cb251ec, encoding=_0xd14e4b1f('7574662d38'))

    def _0x9ec9c46e(self, _0xd6fe1d0b, _0x240bf022):
        _0xd6fe1d0b.mkdir(parents=True, exist_ok=True)
        _0xda602f0b = 0
        for _0x97fd815a in _0xd6fe1d0b.glob(_0x240bf022):
            if not _0x97fd815a.is_file():
                continue
            _0x97fd815a.unlink(missing_ok=True)
            _0xda602f0b += 1
        return _0xda602f0b

    async def _0x6ab718b4(self):
        _0xda602f0b = await self.hass.async_add_executor_job(self._0x9ec9c46e, self._0xf38a44f4, f"{self._0x078cf264}{_0xd14e4b1f('5f2a2e6a736f6e')}")
        await self._0x009a3261()
        return _0xda602f0b

    async def _0x6e4869fd(self):
        return await self.hass.async_add_executor_job(self._0x9ec9c46e, self._0x650796ba, f"{self._0x078cf264}{_0xd14e4b1f('5f2a2e747874')}")

    def _0x231b3f6f(self):
        _0x925cc8d2 = self.hass if not self._0x1a77b829 else None
        return _0xabcea1bc(self._0x1a77b829, self._0x62b5eb13, self._0xb035b8bf, hass=_0x925cc8d2)

    @property
    def _0xc2d0990a(self):
        return self._0x44904414 in (_0x011c5d45, _0x8b0c8ba7)

    @property
    def _0xb605ddfc(self):
        return self._0x44904414 in (_0xc880a522, _0x8b0c8ba7)

    def _0x0a23c6b4(self, _0x32e2cb0f, _0x2063c160, _0x7123a699=None):
        if isinstance(_0x2063c160, bool):
            return bytes([1 if _0x2063c160 else 0])
        if isinstance(_0x2063c160, int):
            _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
            _0x958b30d4 = _0x825031bd(_0x32e2cb0f, _0x7123a699)
            _0x045e9e68 = self._0xdedd8ef4.get(_0x958b30d4)
            if _0x045e9e68 is None and _0x7123a699 in (None, 0):
                _0x045e9e68 = self._0xdedd8ef4.get(int(_0x32e2cb0f))
            if _0x045e9e68 is None and _0x7123a699 is None:
                _0x045e9e68 = self._0xdedd8ef4.get(_0x825031bd(_0x32e2cb0f, 0))
            if _0x045e9e68 is not None:
                return _0x2063c160.to_bytes(len(_0x045e9e68), byteorder=_0xd14e4b1f('6c6974746c65'), signed=_0x2063c160 < 0)
            if _0xe9a23cbc is not None and _0xe9a23cbc._0x3931108d in (_0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
                return _0x2063c160.to_bytes(4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
            if _0xe9a23cbc is not None and _0xe9a23cbc._0x3931108d == _0x340e827c._0x64d12922:
                return _0x2063c160.to_bytes(4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
            _0xbef2e239 = [_0x2063c160]
            if _0xe9a23cbc is not None:
                if _0xe9a23cbc._0x56dda363 is not None:
                    _0xbef2e239.append(int(_0xe9a23cbc._0x56dda363))
                if _0xe9a23cbc._0xc6a35ba1 is not None:
                    _0xbef2e239.append(int(_0xe9a23cbc._0xc6a35ba1))
            _0x43ca94dd = any((_0x65afdfb4 < 0 for _0x65afdfb4 in _0xbef2e239))
            if _0x43ca94dd:
                _0xe383234c = min(_0xbef2e239)
                _0x65b0e288 = max(_0xbef2e239)
                if -128 <= _0xe383234c and _0x65b0e288 <= 127:
                    _0x2fa47f7c = 1
                elif -32768 <= _0xe383234c and _0x65b0e288 <= 32767:
                    _0x2fa47f7c = 2
                else:
                    _0x2fa47f7c = 4
            else:
                _0x65b0e288 = max(_0xbef2e239)
                if _0x65b0e288 <= 255:
                    _0x2fa47f7c = 1
                elif _0x65b0e288 <= 65535:
                    _0x2fa47f7c = 2
                else:
                    _0x2fa47f7c = 4
            return _0x2063c160.to_bytes(_0x2fa47f7c, byteorder=_0xd14e4b1f('6c6974746c65'), signed=_0x43ca94dd)
        if isinstance(_0x2063c160, str):
            return _0x2063c160.encode(_0xd14e4b1f('7574662d38'))
        raise TypeError(f"{_0xd14e4b1f('556e737570706f727465642076616c756520747970653a20')}{type(_0x2063c160)}")

    def _0x16390971(self, _0x32e2cb0f, _0x7123a699=None):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None:
            raise UpdateFailed(f"{_0xd14e4b1f('4e6f206d6574616461746120617661696c61626c6520666f7220636f6d6d616e64204470496420')}{_0x32e2cb0f}")
        if _0xe9a23cbc._0xb140af3d not in (_0x27401bf3._0xee97be03, _0x27401bf3._0x922337c3):
            raise UpdateFailed(f"{_0xd14e4b1f('4470496420')}{_0x32e2cb0f}{_0xd14e4b1f('206973206e6f74206120636f6d6d616e642064617461706f696e74')}")
        if _0xe9a23cbc._0x3931108d == _0x340e827c._0x92e592d9:
            return b''
        if _0xe9a23cbc._0x3931108d in (_0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
            return int(time.time()).to_bytes(4, byteorder=_0xd14e4b1f('6c6974746c65'), signed=False)
        if _0xe9a23cbc._0x3931108d in (_0x340e827c._0x6ce976e8, _0x340e827c._0x084c8428):
            return _0xaf5f5547('01')
        raise UpdateFailed(f"{_0xd14e4b1f('556e737570706f727465642067656e6572696320636f6d6d616e64207061796c6f616420666f72204470496420')}{_0x32e2cb0f}{_0xd14e4b1f('3a2064617461747970653d')}{_0xe9a23cbc._0x3931108d}")

    async def _0x9788b30f(self, _0x62608e08):
        if self._0x25cb3c49 is not None:
            return
        (_0xa08cee2d, _0x444abb90) = await self._0x071e72da(_0x62608e08)
        _0xf953ee8b = _0xabe76933(_0xa08cee2d, _0x444abb90)
        _0xbb5e9d49 = await _0x62608e08.inventory()
        _0x545f7f57 = _0x44eacae4(_0xf953ee8b, _0xbb5e9d49)
        _0x545f7f57 = self._0x4cc51d69(_0x545f7f57)
        self._0xa24b5ca2(_0x545f7f57)
        self._0x25cb3c49 = _0x545f7f57
        self._0xd05acf0b = set()
        self._0x4ef26b0c()
        self._0x77ad7fd7 = _0x64a7c4d5(_0x545f7f57)
        for _0x32e2cb0f in self._0xa6f36771:
            self._0x8c009663(_0x32e2cb0f)
        self._0x696cd6fe(0.0)

    async def _0xdf782ed6(self, _0x266e0d3d):
        if not _0x266e0d3d.arendi_handshake_done:
            raise Exception(_0xd14e4b1f('4172656e64692073656375726974792068616e647368616b65206661696c6564'))
        _0x62608e08 = _0x6e2f7964(_0x266e0d3d)
        if self._0x25cb3c49 is None:
            await self._0x9788b30f(_0x62608e08)
            self._0x5db8c29c = await _0x62608e08.capabilities()
            await _0x62608e08.event_storage_inventory(self._0x5db8c29c)
        await _0x62608e08.join(pin=self._0x9803e4e7, inv=self._0x7f68e801())
        return _0x62608e08

    async def _0x4691f650(self):
        if self._0xc2d0990a and self._0x25cb3c49 is None:
            _0xc3f62fb2 = _0xabe76933(self._0xe1c408bb, self._0x98f64478)
            if _0xc3f62fb2:
                _0x7a1eabc3 = self._0x4cc51d69(_0xc3f62fb2)
                self._0xa24b5ca2(_0x7a1eabc3)
                self._0x25cb3c49 = _0x7a1eabc3
                self._0xd05acf0b = set()
                self._0x4ef26b0c()
                self._0x77ad7fd7 = _0x64a7c4d5(_0x7a1eabc3)
                for _0x32e2cb0f in self._0xa6f36771:
                    self._0x8c009663(_0x32e2cb0f)
        if self._0xb605ddfc and (not self._0x3522077d) and (self._0x084706dd is not None):
            _0x10cd395c = self._0x084706dd.get_services()
            if _0x10cd395c:
                self._0x3522077d = _0x4c284fb2(_0x10cd395c)
                self._0x696cd6fe(0.0)

    @property
    def _0x63735d9e(self):
        return {_0x32e2cb0f for _0xaa08769c in DpId for _0x32e2cb0f in (_0x85f8d15a(int(_0xaa08769c.value)),) if not self._0xc97399be(_0x32e2cb0f)}

    def _0x8c009663(self, _0x32e2cb0f):
        if self._0x25cb3c49 is None:
            return
        self._0xd05acf0b.discard(int(_0x32e2cb0f))
        if _0x32e2cb0f in self._0x25cb3c49:
            return
        self._0x25cb3c49[_0x32e2cb0f] = {_0xd14e4b1f('696e7374616e6365'): 0, _0xd14e4b1f('76657273696f6e'): 0, _0xd14e4b1f('6461746174797065'): None, _0xd14e4b1f('6d696e5f73'): None, _0xd14e4b1f('6d61785f73'): None, _0xd14e4b1f('6d696e5f75'): None, _0xd14e4b1f('6d61785f75'): None, _0xd14e4b1f('69735f696e7465726e616c'): False, _0xd14e4b1f('6265686176696f72'): 0}
        self._0x77ad7fd7 = _0x64a7c4d5(self._0x25cb3c49)

    def _0x151b8dd7(self):
        return {_0xd14e4b1f('76657273696f6e'): 2, _0xd14e4b1f('726571756573745f646174615f6d6f6465'): self._0x96ffac89, _0xd14e4b1f('636f6d6d756e69636174696f6e5f6d6f6465'): self._0x44904414, _0xd14e4b1f('696e636c7564655f74617267657473'): sorted((self._0x0d99ec5f(_0x42aefbae) for _0x42aefbae in self._0x361c3e6d)), _0xd14e4b1f('6578636c7564655f74617267657473'): sorted((self._0x0d99ec5f(_0x42aefbae) for _0x42aefbae in self._0x87b637aa)), _0xd14e4b1f('6d61785f696e7374616e6365735f7065725f647069645f67726f7570'): self._0x4202d2ae, _0xd14e4b1f('6578706f73655f6c617267655f696e7374616e63655f67726f757073'): self._0x285f2b4b}

    async def _0xaf0e34c6(self):
        _0x1fb1a060 = await self._0xfb5e2f47.async_load()
        if not _0x1fb1a060:
            return
        if _0x1fb1a060.get(_0xd14e4b1f('726571756573745f646174615f6d6f6465')) != self._0x96ffac89:
            return
        _0x21de7104 = _0x1fb1a060.get(_0xd14e4b1f('70726f66696c65')) == self._0x151b8dd7()
        _0x538416cf = _0x1fb1a060.get(_0xd14e4b1f('646973636f76657265645f6e6f6e5f696e76656e746f72795f6470696473'), [])
        self._0xa6f36771 = {int(_0x32e2cb0f) for _0x32e2cb0f in _0x538416cf if not self._0xc97399be(int(_0x32e2cb0f))}
        _0xe46185c7 = _0x1fb1a060.get(_0xd14e4b1f('726561645f74617267657473'), {})
        _0x1d8475b9 = {}
        for (_0x06e1a2e9, _0x21b52d8a) in _0xe46185c7.items():
            _0x32e2cb0f = int(_0x06e1a2e9)
            _0x1d8475b9[_0x32e2cb0f] = tuple((None if _0x42aefbae is None else int(_0x42aefbae) for _0x42aefbae in _0x21b52d8a))
        self._0x94b57abb = _0x1d8475b9 if _0x21de7104 else {}
        _0x8ccdd640 = _0x1fb1a060.get(_0xd14e4b1f('696e76616c69645f726561645f616464726573736573'), [])
        _0x3810e299 = set()
        for _0xfa89cff0 in _0x8ccdd640:
            try:
                _0x3810e299.add(self._0xacbab4dd(str(_0xfa89cff0)))
            except ValueError:
                continue
        self._0xaaf9910f = _0x3810e299
        if self._0x25cb3c49 is not None:
            for _0x32e2cb0f in self._0xa6f36771:
                self._0x8c009663(_0x32e2cb0f)
        self._0x68eea019 = bool(_0x1fb1a060.get(_0xd14e4b1f('616c6c5f6b6e6f776e5f7363616e5f636f6d706c65746564'), False)) if _0x21de7104 else False
        if not _0x21de7104:
            self._0x8f41c896 = True
            self._0x3147b7f8(_0xd14e4b1f('446973636f766572792063616368652070726f66696c65206368616e676564206f72206973206c65676163793b207265616420746172676574732077696c6c2062652072656275696c74'))

    async def _0x9bca487c(self):
        if not self._0x8f41c896:
            return
        await self._0xfb5e2f47.async_save({_0xd14e4b1f('726571756573745f646174615f6d6f6465'): self._0x96ffac89, _0xd14e4b1f('70726f66696c65'): self._0x151b8dd7(), _0xd14e4b1f('646973636f76657265645f6e6f6e5f696e76656e746f72795f6470696473'): sorted(self._0xa6f36771), _0xd14e4b1f('726561645f74617267657473'): {str(_0x32e2cb0f): list(_0xaa6f6d62) for (_0x32e2cb0f, _0xaa6f6d62) in self._0x94b57abb.items()}, _0xd14e4b1f('696e76616c69645f726561645f616464726573736573'): sorted((self._0x0d99ec5f(_0x3c6e0b8a) for _0x3c6e0b8a in self._0xaaf9910f)), _0xd14e4b1f('616c6c5f6b6e6f776e5f7363616e5f636f6d706c65746564'): self._0x68eea019})
        self._0x8f41c896 = False

    @property
    def _0x15151b9c(self):
        return bool(self.data) or bool(self._0x84f90afc) or bool(self._0x93b9730d)

    @property
    def _0xfd0f740a(self):
        return bool(self._0x77ad7fd7)

    @property
    def _0x1a94487b(self):
        return bool(self.data)

    @property
    def _0x714cfe92(self):
        return bool(self._0x3522077d)

    @property
    def _0xd90bbd0e(self):
        return bool(self._0x84f90afc) or bool(self._0x93b9730d)

    @property
    def _0xc5f8f30d(self):
        if self._0xc2d0990a and (not self._0xfd0f740a):
            return False
        if self._0xb605ddfc and (not (self._0x714cfe92 or self._0xd90bbd0e)):
            return False
        return self._0xfd0f740a or self._0x714cfe92 or self._0x15151b9c

    @property
    def _0xd92c6474(self):
        return self._0x73d4c228 and self.poll_enabled and self._0x3a821fc7

    def _0x0d99ec5f(self, _0x3c6e0b8a):
        if isinstance(_0x3c6e0b8a, tuple) and len(_0x3c6e0b8a) == 2:
            return f"{int(_0x3c6e0b8a[0])}{_0xd14e4b1f('3a')}{int(_0x3c6e0b8a[1])}"
        return str(int(_0x3c6e0b8a))

    def _0xacbab4dd(self, _0x3c6e0b8a):
        if _0xd14e4b1f('3a') not in _0x3c6e0b8a:
            return int(_0x3c6e0b8a)
        (_0x06e1a2e9, _0x3b2d0e92) = _0x3c6e0b8a.split(_0xd14e4b1f('3a'), 1)
        return (int(_0x06e1a2e9), int(_0x3b2d0e92))

    async def _0xc75f438a(self):
        _0x1fb1a060 = await self._0x87d447af.async_load()
        if not _0x1fb1a060:
            return
        if self._0xc2d0990a:
            _0x3499aedc = _0x1fb1a060.get(_0xd14e4b1f('696e76656e746f7279'))
            if isinstance(_0x3499aedc, dict) and _0x3499aedc:
                _0x7a1eabc3 = {}
                for (_0x06e1a2e9, _0xa4ade155) in _0x3499aedc.items():
                    try:
                        _0x7a1eabc3[int(_0x06e1a2e9)] = dict(_0xa4ade155)
                    except (TypeError, ValueError):
                        continue
                if _0x7a1eabc3:
                    _0xf953ee8b = _0xabe76933(self._0xe1c408bb, self._0x98f64478)
                    _0x7a1eabc3 = _0x44eacae4(_0xf953ee8b, _0x7a1eabc3)
                    _0x7a1eabc3 = self._0x4cc51d69(_0x7a1eabc3)
                    self._0xa24b5ca2(_0x7a1eabc3)
                    self._0x25cb3c49 = _0x7a1eabc3
                    _0x2dbd42af = _0xd14e4b1f('736565645f6f6e6c795f706c616365686f6c6465725f6470696473') in _0x1fb1a060
                    _0x3affac83 = _0x1fb1a060.get(_0xd14e4b1f('736565645f6f6e6c795f706c616365686f6c6465725f6470696473'), [])
                    _0x68fdd37c = self._0xa745bc87(0)
                    self._0xd05acf0b = set()
                    if isinstance(_0x3affac83, (list, tuple, set)):
                        for _0x06e1a2e9 in _0x3affac83:
                            try:
                                _0x32e2cb0f = int(_0x06e1a2e9)
                            except (TypeError, ValueError):
                                continue
                            _0xa4ade155 = _0x7a1eabc3.get(_0x32e2cb0f)
                            if _0xa4ade155 is not None and all((_0xa4ade155.get(_0x06e3d36f) == _0x2063c160 for (_0x06e3d36f, _0x2063c160) in _0x68fdd37c.items())):
                                self._0xd05acf0b.add(_0x32e2cb0f)
                    if not _0x2dbd42af:
                        for _0x3c6e0b8a in self._0xaaf9910f:
                            if isinstance(_0x3c6e0b8a, tuple):
                                continue
                            _0x32e2cb0f = int(_0x3c6e0b8a)
                            _0xa4ade155 = _0x7a1eabc3.get(_0x32e2cb0f)
                            if _0xa4ade155 is None:
                                continue
                            if all((_0xa4ade155.get(_0x06e3d36f) == _0x2063c160 for (_0x06e3d36f, _0x2063c160) in _0x68fdd37c.items())):
                                self._0xd05acf0b.add(_0x32e2cb0f)
                    self._0x4ef26b0c()
                    self._0x77ad7fd7 = _0x64a7c4d5(_0x7a1eabc3)
                    for _0x32e2cb0f in self._0xa6f36771:
                        self._0x8c009663(_0x32e2cb0f)
                    _0x45e4a199 = _0x1fb1a060.get(_0xd14e4b1f('7261775f6361636865'), {})
                    _0x72b2f709 = {}
                    if isinstance(_0x45e4a199, dict):
                        for (_0xfa89cff0, _0x3e7e6051) in _0x45e4a199.items():
                            if not isinstance(_0x3e7e6051, str):
                                continue
                            try:
                                _0x72b2f709[self._0xacbab4dd(str(_0xfa89cff0))] = bytes.fromhex(_0x3e7e6051)
                            except ValueError:
                                continue
                    self._0xdedd8ef4 = _0x72b2f709
                    _0x271c3b69 = _0x1fb1a060.get(_0xd14e4b1f('64617461'), {})
                    _0x52efa1cd = {}
                    if isinstance(_0x271c3b69, dict):
                        for (_0xfa89cff0, _0x2063c160) in _0x271c3b69.items():
                            try:
                                _0x52efa1cd[self._0xacbab4dd(str(_0xfa89cff0))] = _0x2063c160
                            except ValueError:
                                continue
                    _0x751eb3ee = _0x52efa1cd.get(_0x825031bd(int(0), 0))
                    if not isinstance(_0x751eb3ee, int):
                        _0x751eb3ee = _0x52efa1cd.get(int(0))
                    if isinstance(_0x751eb3ee, int):
                        self._0x4aec38a9 = _0x751eb3ee
                    _0x8a239f28 = _0x52efa1cd.get(_0x825031bd(int(1), 0))
                    if not isinstance(_0x8a239f28, int):
                        _0x8a239f28 = _0x52efa1cd.get(int(1))
                    if isinstance(_0x8a239f28, int):
                        self._0xffe5c0a0 = _0x8a239f28
                    (_0x52efa1cd, _0x72b2f709) = self._0x1d0c6f37(_0x52efa1cd, _0x72b2f709)
                    if _0x52efa1cd:
                        self.async_set_updated_data(_0x52efa1cd)
        if self._0xb605ddfc:
            _0xf998bcbd = _0x1fb1a060.get(_0xd14e4b1f('676174745f636861726163746572697374696373'), {})
            _0x933209e1 = {}
            if isinstance(_0xf998bcbd, dict):
                for (_0xef7c876f, _0x321c3cf4) in _0xf998bcbd.items():
                    if not isinstance(_0x321c3cf4, dict):
                        continue
                    try:
                        _0x933209e1[str(_0xef7c876f).lower()] = _0x80bb1bf9(uuid=str(_0x321c3cf4[_0xd14e4b1f('75756964')]).lower(), _0x10c1ecca=str(_0x321c3cf4[_0xd14e4b1f('736572766963655f75756964')]).lower(), _0xd505dfd5=str(_0x321c3cf4[_0xd14e4b1f('736572766963655f6e616d65')]), key=str(_0x321c3cf4[_0xd14e4b1f('6b6579')]), name=str(_0x321c3cf4[_0xd14e4b1f('6e616d65')]), _0x36cd38f4=str(_0x321c3cf4[_0xd14e4b1f('736f75726365')]), _0x3a6bdba8=str(_0x321c3cf4[_0xd14e4b1f('6465636f646572')]), properties=tuple(_0x321c3cf4.get(_0xd14e4b1f('70726f70657274696573'), ())), descriptors=tuple(_0x321c3cf4.get(_0xd14e4b1f('64657363726970746f7273'), ())), _0x500f1c43=bool(_0x321c3cf4.get(_0xd14e4b1f('7265616461626c65'), False)), _0xc83e24cd=bool(_0x321c3cf4.get(_0xd14e4b1f('7772697461626c65'), False)), _0x09f821ba=bool(_0x321c3cf4.get(_0xd14e4b1f('6e6f7469666961626c65'), False)), _0xdecb0dc3=bool(_0x321c3cf4.get(_0xd14e4b1f('696e646963617461626c65'), False)), entity_registry_enabled_default=bool(_0x321c3cf4.get(_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'), True)), _0x662f707d=bool(_0x321c3cf4.get(_0xd14e4b1f('68696464656e'), False)))
                    except KeyError:
                        continue
            if _0x933209e1:
                self._0x3522077d = _0x933209e1
                _0x29cd1942 = _0x1fb1a060.get(_0xd14e4b1f('676174745f7261775f76616c756573'), {})
                if isinstance(_0x29cd1942, dict):
                    _0xf6595579 = {}
                    for (_0xef7c876f, _0x3e7e6051) in _0x29cd1942.items():
                        if not isinstance(_0x3e7e6051, str):
                            continue
                        try:
                            _0xf6595579[str(_0xef7c876f).lower()] = bytes.fromhex(_0x3e7e6051)
                        except ValueError:
                            continue
                    self._0x93b9730d = _0xf6595579
                _0x154bd0f8 = _0x1fb1a060.get(_0xd14e4b1f('676174745f6465636f6465645f76616c756573'), {})
                if isinstance(_0x154bd0f8, dict):
                    self._0x84f90afc = {str(_0xef7c876f).lower(): _0x2063c160 for (_0xef7c876f, _0x2063c160) in _0x154bd0f8.items()}

    async def _0x9308b7eb(self):
        if not self._0xc2d0990a and (not self._0xb605ddfc):
            return
        _0x809ba52a = {}
        if self._0x25cb3c49 is not None:
            _0x809ba52a = {str(_0x32e2cb0f): dict(_0xa4ade155) for (_0x32e2cb0f, _0xa4ade155) in self._0x25cb3c49.items()}
        _0x271c3b69 = {}
        if self.data:
            _0x271c3b69 = {self._0x0d99ec5f(_0x3c6e0b8a): self._0xe822d7dd(_0x2063c160) for (_0x3c6e0b8a, _0x2063c160) in self.data.items()}
        _0x45e4a199 = {self._0x0d99ec5f(_0x3c6e0b8a): _0x2063c160.hex() for (_0x3c6e0b8a, _0x2063c160) in self._0xdedd8ef4.items()}
        _0xf998bcbd = {_0xef7c876f: {_0xd14e4b1f('75756964'): _0x756bb351.uuid, _0xd14e4b1f('736572766963655f75756964'): _0x756bb351._0x10c1ecca, _0xd14e4b1f('736572766963655f6e616d65'): _0x756bb351._0xd505dfd5, _0xd14e4b1f('6b6579'): _0x756bb351.key, _0xd14e4b1f('6e616d65'): _0x756bb351.name, _0xd14e4b1f('736f75726365'): _0x756bb351._0x36cd38f4, _0xd14e4b1f('6465636f646572'): _0x756bb351._0x3a6bdba8, _0xd14e4b1f('70726f70657274696573'): list(_0x756bb351.properties), _0xd14e4b1f('64657363726970746f7273'): list(_0x756bb351.descriptors), _0xd14e4b1f('7265616461626c65'): _0x756bb351._0x500f1c43, _0xd14e4b1f('7772697461626c65'): _0x756bb351._0xc83e24cd, _0xd14e4b1f('6e6f7469666961626c65'): _0x756bb351._0x09f821ba, _0xd14e4b1f('696e646963617461626c65'): _0x756bb351._0xdecb0dc3, _0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): _0x756bb351.entity_registry_enabled_default, _0xd14e4b1f('68696464656e'): _0x756bb351._0x662f707d} for (_0xef7c876f, _0x756bb351) in self._0x3522077d.items()}
        _0x29cd1942 = {_0xef7c876f: _0x2063c160.hex() for (_0xef7c876f, _0x2063c160) in self._0x93b9730d.items()}
        _0x154bd0f8 = {_0xef7c876f: self._0xe822d7dd(_0x2063c160) for (_0xef7c876f, _0x2063c160) in self._0x84f90afc.items()}
        await self._0x87d447af.async_save({_0xd14e4b1f('696e76656e746f7279'): _0x809ba52a, _0xd14e4b1f('736565645f6f6e6c795f706c616365686f6c6465725f6470696473'): sorted(self._0xd05acf0b), _0xd14e4b1f('64617461'): _0x271c3b69, _0xd14e4b1f('7261775f6361636865'): _0x45e4a199, _0xd14e4b1f('676174745f636861726163746572697374696373'): _0xf998bcbd, _0xd14e4b1f('676174745f7261775f76616c756573'): _0x29cd1942, _0xd14e4b1f('676174745f6465636f6465645f76616c756573'): _0x154bd0f8})
        self._0x92e70e01 = asyncio.get_running_loop().time()

    def _0x696cd6fe(self, _0x7243f8be):
        if self._0xbb786552:
            return
        _0xe48b981f = asyncio.get_running_loop()
        _0x97bc592b = _0xe48b981f.time()
        _0x972ff19c = _0x97bc592b + max(0.0, float(_0x7243f8be))
        if self._0x92e70e01 is not None:
            _0x972ff19c = max(_0x972ff19c, self._0x92e70e01 + _0x515d6cbe)
        _0x553f9e1c = self._0x60d33921
        if _0x553f9e1c is not None and _0x553f9e1c <= _0x972ff19c:
            return
        self._0x60d33921 = _0x972ff19c
        if self._0xb41ecae5 is not None and (not self._0xb41ecae5.done()):
            self._0xb41ecae5.cancel()
        self._0xb41ecae5 = self.hass.async_create_task(self._0x2f2d6cfe())

    async def _0x2f2d6cfe(self):
        _0xebbf574e = asyncio.current_task()
        try:
            while True:
                _0x86ba50d9 = self._0x60d33921
                if _0x86ba50d9 is None:
                    return
                _0x2626772c = _0x86ba50d9 - asyncio.get_running_loop().time()
                if _0x2626772c > 0:
                    await asyncio.sleep(_0x2626772c)
                if self._0x60d33921 != _0x86ba50d9:
                    continue
                self._0x60d33921 = None
                await self._0x9308b7eb()
                return
        except asyncio.CancelledError:
            raise
        except Exception as _0x56bd7107:
            pass
        finally:
            if self._0xb41ecae5 is _0xebbf574e:
                self._0xb41ecae5 = None

    def _0x2f435d32(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None:
            return (None,)
        _0xbef2e239 = [None]
        if _0xe9a23cbc._0x7123a699 > 0:
            _0xda040c8d = min(self._0x9076348f(_0xe9a23cbc._0x7123a699), 32)
            _0xbef2e239.extend(range(0, _0xda040c8d))
        _0x88ff4783 = []
        _0xd5b4a9a5 = set()
        for _0x65afdfb4 in _0xbef2e239:
            if _0x65afdfb4 in _0xd5b4a9a5:
                continue
            _0xd5b4a9a5.add(_0x65afdfb4)
            _0x88ff4783.append(_0x65afdfb4)
        return tuple(_0x88ff4783)

    def _0x94c69b93(self, _0x56bd7107):
        _0x78e73102 = str(_0x56bd7107)
        _0x04ca3602 = (_0x367daf70(_0xa7830531._0xd17cc4f1), _0x367daf70(_0xa7830531._0x8a03add8), _0x367daf70(_0xa7830531._0xdf0df5de))
        return any((_0xb068931c in _0x78e73102 for _0xb068931c in _0x04ca3602))

    def _0x4c068da5(self, _0x56bd7107):
        return _0xd14e4b1f('74696d656f7574') in str(_0x56bd7107).lower()

    def _0x01fa193e(self, _0x32e2cb0f, _0x7123a699):
        _0x884d9804 = _0x825031bd(_0x32e2cb0f, _0x7123a699)
        if _0x884d9804 not in self._0xaaf9910f:
            self._0xaaf9910f.add(_0x884d9804)
            self._0x8f41c896 = True
        _0x214ae76e = self._0x94b57abb.get(_0x32e2cb0f)
        if _0x214ae76e is None:
            return
        _0xee2be73d = tuple((_0x42aefbae for _0x42aefbae in _0x214ae76e if _0x42aefbae != _0x7123a699))
        if _0xee2be73d != _0x214ae76e:
            self._0x94b57abb[_0x32e2cb0f] = _0xee2be73d
            self._0x8f41c896 = True

    def _0xe9f71d53(self, _0x32e2cb0f):
        return tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in self._0x2f435d32(_0x32e2cb0f)))

    def _0xfc17d6bb(self, _0x958b30d4):
        _0x32e2cb0f = int(_0x958b30d4[0] if isinstance(_0x958b30d4, tuple) else _0x958b30d4)
        if _0x32e2cb0f in self._0x05ecc105:
            return True
        return _0x958b30d4 in self._0x87b637aa

    def _0x649a2aaa(self, _0x32e2cb0f, _0x7123a699):
        if _0x32e2cb0f in self._0x05ecc105:
            return True
        return _0x825031bd(_0x32e2cb0f, _0x7123a699) in self._0x87b637aa

    def _0x9076348f(self, _0x643ba291):
        if self._0x285f2b4b:
            return max(0, int(_0x643ba291))
        return max(0, min(int(_0x643ba291), self._0x4202d2ae))

    def _0x10fcb2d9(self, _0x32e2cb0f, _0xe9a23cbc):
        if _0xe9a23cbc._0x7123a699 > 0:
            _0xda040c8d = min(self._0x9076348f(_0xe9a23cbc._0x7123a699), 32)
            return tuple(range(0, _0xda040c8d))
        return (None,)

    def _0x682db4bd(self, _0x32e2cb0f):
        _0x6fa93254 = []
        if _0x32e2cb0f in self._0xe364388d:
            _0x6fa93254.append(None)
        for _0x42aefbae in sorted(self._0x361c3e6d, key=str):
            if isinstance(_0x42aefbae, tuple) and int(_0x42aefbae[0]) == _0x32e2cb0f:
                _0x6fa93254.append(int(_0x42aefbae[1]))
        _0x88ff4783 = []
        _0xd5b4a9a5 = set()
        for _0x7123a699 in _0x6fa93254:
            if _0x7123a699 in _0xd5b4a9a5:
                continue
            _0xd5b4a9a5.add(_0x7123a699)
            _0x88ff4783.append(_0x7123a699)
        return tuple(_0x88ff4783)

    def _0xcddc3a51(self, _0x32e2cb0f, *, _0x42bd4c08):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0x42bd4c08 and _0xe9a23cbc is not None:
            _0x8b26c685 = list(self._0x10fcb2d9(_0x32e2cb0f, _0xe9a23cbc))
        else:
            _0x8b26c685 = list(self._0x2f435d32(_0x32e2cb0f))
        for _0x3c30a548 in self._0x682db4bd(_0x32e2cb0f):
            if _0x3c30a548 not in _0x8b26c685:
                _0x8b26c685.append(_0x3c30a548)
        return tuple(_0x8b26c685)

    def _0x99bc22f6(self, _0x9b504c43, _0xde5eac3b):
        for _0x32e2cb0f in sorted(_0x9b504c43):
            if self._0xc97399be(_0x32e2cb0f):
                continue
            if _0x32e2cb0f in self._0x94b57abb:
                continue
            _0xaa6f6d62 = self._0xcddc3a51(_0x32e2cb0f, _0x42bd4c08=_0x32e2cb0f in _0xde5eac3b)
            _0xaa6f6d62 = tuple((_0x7123a699 for _0x7123a699 in _0xaa6f6d62 if not self._0x649a2aaa(_0x32e2cb0f, _0x7123a699)))
            if not _0xaa6f6d62:
                continue
            self._0x94b57abb[_0x32e2cb0f] = _0xaa6f6d62
            self._0x8f41c896 = True

    def _0xd8ace7ec(self, _0x32e2cb0f, *, _0x42bd4c08):
        _0x12fba141 = self._0x94b57abb.get(_0x32e2cb0f)
        if _0x12fba141:
            _0x963e3a2f = tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in _0x12fba141))
        else:
            _0x963e3a2f = ()
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if not _0x963e3a2f:
            if _0x42bd4c08 and _0xe9a23cbc is not None:
                _0x963e3a2f = tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in self._0x10fcb2d9(_0x32e2cb0f, _0xe9a23cbc)))
            else:
                _0x963e3a2f = self._0xe9f71d53(_0x32e2cb0f)
        _0xdce4a640 = tuple((_0x884d9804 for _0x884d9804 in _0x963e3a2f if not self._0xc97399be(_0x884d9804) and _0x884d9804 not in self._0xaaf9910f and (not self._0xfc17d6bb(_0x884d9804)) and (_0x884d9804 not in self._0x01aa0845)))
        return _0xdce4a640

    def _0x76e5bb59(self):
        _0x52d08984 = [_0x32e2cb0f for (_0x32e2cb0f, _0xaa6f6d62) in self._0x94b57abb.items() if not _0xaa6f6d62]
        if not _0x52d08984:
            return
        for _0x32e2cb0f in _0x52d08984:
            del self._0x94b57abb[_0x32e2cb0f]
        self._0x8f41c896 = True

    def _0x27940332(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None or self._0x5a04c375(_0x32e2cb0f) or (not _0xe9a23cbc._0x09f821ba) or (not _0xe9a23cbc._0xd706b7c5) or _0xe9a23cbc._0x662f707d:
            return ()
        if _0xe9a23cbc._0x7123a699 > 0:
            _0xaa6f6d62 = self._0x94b57abb.get(_0x32e2cb0f)
            if _0xaa6f6d62:
                return tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in _0xaa6f6d62 if _0x7123a699 is not None))
            return tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in self._0x10fcb2d9(_0x32e2cb0f, _0xe9a23cbc) if _0x7123a699 is not None))
        return (int(_0x32e2cb0f),)

    def _0xf3be43ed(self, _0x42aefbae):
        (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x42aefbae)
        if _0x7123a699 is not None:
            self._0x01aa0845.add(_0x825031bd(_0x32e2cb0f, _0x7123a699))
            return
        _0xaa6f6d62 = self._0x94b57abb.get(_0x32e2cb0f)
        if _0xaa6f6d62:
            for _0x5a2a8eb6 in _0xaa6f6d62:
                self._0x01aa0845.add(_0x825031bd(_0x32e2cb0f, _0x5a2a8eb6))
            return
        self._0x01aa0845.add(int(_0x32e2cb0f))

    def _0xcf1a7d5f(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is not None and _0xe9a23cbc._0x7123a699 == 0:
            return None
        _0x12fba141 = self._0x94b57abb.get(_0x32e2cb0f)
        if _0x12fba141:
            for _0x65afdfb4 in _0x12fba141:
                if _0x65afdfb4 is not None:
                    return int(_0x65afdfb4)
            if None in _0x12fba141:
                return None
        _0x686090eb = _0x825031bd(_0x32e2cb0f, 0)
        _0x8d777f38 = self.data or {}
        if _0x686090eb in self._0xdedd8ef4 or _0x686090eb in _0x8d777f38:
            return 0
        if int(_0x32e2cb0f) in self._0xdedd8ef4 or int(_0x32e2cb0f) in _0x8d777f38:
            return None
        if _0xe9a23cbc is not None and _0xe9a23cbc._0x7123a699 > 0:
            return 0
        return None

    def _0xeb7db913(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None or not self._0x86b41222(_0x32e2cb0f):
            return ()
        if _0xe9a23cbc._0x7123a699 > 0:
            _0x42bd4c08 = _0x32e2cb0f in self._0x3a3a4684
            _0x6fa93254 = [_0x7123a699 for _0x7123a699 in self._0xcddc3a51(_0x32e2cb0f, _0x42bd4c08=_0x42bd4c08) if _0x7123a699 is not None and (not self._0x649a2aaa(_0x32e2cb0f, _0x7123a699))]
            _0xbeb4220c = []
            _0x738a3e3a = set()
            for _0x7123a699 in _0x6fa93254:
                _0x143c875b = int(_0x7123a699)
                if _0x143c875b in _0x738a3e3a:
                    continue
                _0x738a3e3a.add(_0x143c875b)
                _0xbeb4220c.append(_0x143c875b)
            return tuple((_0x825031bd(_0x32e2cb0f, _0x7123a699) for _0x7123a699 in _0xbeb4220c))
        if not self._0xe2e1241d(_0x32e2cb0f):
            return ()
        return (int(_0x32e2cb0f),)

    def _0xf5fadddf(self):
        _0x98fb7916 = set()
        for (_0x32e2cb0f, _0xe9a23cbc) in self._0x77ad7fd7.items():
            if not _0xe9a23cbc.entity_registry_enabled_default:
                continue
            _0x98fb7916.update(self._0xeb7db913(_0x32e2cb0f))
        for (_0xef7c876f, _0x756bb351) in self._0x3522077d.items():
            if _0x756bb351._0x500f1c43 and _0x756bb351.entity_registry_enabled_default:
                _0x98fb7916.add(_0xef7c876f)
        return _0x98fb7916

    def _0x7f68e801(self):
        if self._0x25cb3c49 is None:
            return None
        _0xa7e02e9f = {int(_0x3c6e0b8a[0] if isinstance(_0x3c6e0b8a, tuple) else _0x3c6e0b8a) for _0x3c6e0b8a in self._0xaaf9910f}
        return {int(_0x32e2cb0f): dict(_0xa4ade155) for (_0x32e2cb0f, _0xa4ade155) in self._0x25cb3c49.items() if int(_0x32e2cb0f) not in self._0xd05acf0b and int(_0x32e2cb0f) not in _0xa7e02e9f}

    def _0x1ead0057(self, _0x32e2cb0f, _0x7123a699=None):
        _0xd1f82b6b = int(_0x32e2cb0f)
        _0x40c41b7f = _0x7123a699
        if _0x40c41b7f is None:
            _0x40c41b7f = self._0xcf1a7d5f(_0xd1f82b6b)
        return _0x825031bd(_0xd1f82b6b, _0x40c41b7f)

    def _0x8dc7742e(self, *, _0x60810dad):
        if self._0x084706dd is None or not self._0x3a821fc7:
            return False
        if _0x60810dad and self._0xd4252973 is None:
            return False
        return self._0xd8c19966.is_set()

    async def _0xb317e247(self, _0x418c5509, _0xf7235a61, *, _0x60810dad, _0x90272dda=15.0):
        if not self.poll_enabled:
            raise RuntimeError(f"{_0x418c5509}{_0xd14e4b1f('20756e617661696c61626c6520626563617573652074686520636f6e6e656374696f6e20737769746368206973206f6666')}")
        if not self._0x8dc7742e(_0x60810dad=_0x60810dad):
            try:
                await asyncio.wait_for(self._0xd8c19966.wait(), timeout=_0x90272dda)
            except asyncio.TimeoutError as _0x56bd7107:
                raise RuntimeError(f"{_0xd14e4b1f('50657273697374656e7420424c452073657373696f6e206e6f7420726561647920666f7220')}{_0x418c5509}") from _0x56bd7107
        if not self._0x8dc7742e(_0x60810dad=_0x60810dad):
            raise RuntimeError(f"{_0xd14e4b1f('50657273697374656e7420424c452073657373696f6e20756e617661696c61626c6520666f7220')}{_0x418c5509}")
        return await _0xf7235a61()

    async def _0x56c3a97b(self, _0x32e2cb0f, _0x7123a699=None):
        _0x884d9804 = self._0x1ead0057(_0x32e2cb0f, _0x7123a699)
        (_0xcc383da8, _0x40c41b7f) = _0x726b25f9(_0x884d9804)
        return await self._0xb317e247(f"{_0xd14e4b1f('726561642064705f69643d')}{_0xcc383da8}{_0xd14e4b1f('20696e7374616e63653d')}{_0x40c41b7f}", lambda : self._0xd4252973.read(_0xcc383da8, instance=_0x40c41b7f), _0x60810dad=True)

    async def _0x97956325(self, _0x32e2cb0f, _0x2063c160, _0x7123a699=None):
        _0x884d9804 = self._0x1ead0057(_0x32e2cb0f, _0x7123a699)
        (_0xcc383da8, _0x40c41b7f) = _0x726b25f9(_0x884d9804)
        await self._0xb317e247(f"{_0xd14e4b1f('77726974652064705f69643d')}{_0xcc383da8}{_0xd14e4b1f('20696e7374616e63653d')}{_0x40c41b7f}", lambda : self._0xd4252973.write(_0xcc383da8, _0x2063c160, instance=_0x40c41b7f), _0x60810dad=True)
        return _0x884d9804

    async def _0xf49209e0(self, _0x42aefbae):
        _0xa1031145 = await self._0xb317e247(f"{_0xd14e4b1f('6e6f746966792d656e61626c65207461726765743d')}{_0x42aefbae}", lambda : self._0xd4252973.enable_notification([_0x42aefbae]), _0x60810dad=True)
        return (_0x42aefbae, _0xa1031145)

    async def _0x7a63f2eb(self, _0x42aefbae, _0x90272dda=None):
        (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x42aefbae)
        _0xc11b5658 = 30.0 if _0x90272dda is None else max(1.0, float(_0x90272dda))
        _0xdcf3e36e = await self._0xb317e247(f"{_0xd14e4b1f('6e6f746966792d72656164207461726765743d')}{_0x42aefbae}", lambda : self._0xd4252973.get_notification_frame(_0x32e2cb0f, instance=_0x7123a699, timeout=_0x90272dda), _0x60810dad=True, _0x90272dda=_0xc11b5658)
        return (_0x42aefbae, _0xdcf3e36e)

    def _0xa1aaa9f2(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None or not _0xe9a23cbc._0x500f1c43:
            return None
        return _0xd14e4b1f('6e6f74696679') if _0xe9a23cbc._0x09f821ba and _0xe9a23cbc._0xd706b7c5 else _0xd14e4b1f('706f6c6c')

    def _0x5eb74917(self, _0x958b30d4):
        (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x958b30d4)
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None or not _0xe9a23cbc._0x500f1c43:
            return None
        if not _0xe9a23cbc._0x09f821ba or not _0xe9a23cbc._0xd706b7c5:
            return _0xd14e4b1f('706f6c6c')
        _0x42aefbae = _0x825031bd(_0x32e2cb0f, _0x7123a699)
        return _0xd14e4b1f('6e6f74696679') if _0x42aefbae in self._0x01aa0845 else _0xd14e4b1f('706f6c6c')

    def _0x351f8a4d(self, _0x958b30d4):
        return self._0x4250c6b6.get(_0x958b30d4)

    @property
    def _0x3a3a4684(self):
        if self._0x25cb3c49 is None:
            return set()
        _0x42bd4c08 = {int(_0x32e2cb0f) for _0x32e2cb0f in self._0x25cb3c49.keys() if not self._0xc97399be(int(_0x32e2cb0f)) and int(_0x32e2cb0f) not in self._0xd05acf0b}
        _0x42bd4c08.update((int(_0x32e2cb0f) for _0x32e2cb0f in self._0xa6f36771 if not self._0xc97399be(int(_0x32e2cb0f))))
        return _0x42bd4c08

    @property
    def _0xe856d8fe(self):
        return self._0x77ad7fd7

    def _0xf1645e71(self, _0x32e2cb0f):
        if _0x32e2cb0f is None:
            return None
        return self._0x77ad7fd7.get(int(_0x32e2cb0f))

    @property
    def _0x8dc7eed5(self):
        return self._0x3522077d

    @property
    def _0xfb7124c4(self):
        return self._0x84f90afc

    @property
    def _0x0f7bd6f1(self):
        return self._0x93b9730d

    async def _0xba139b66(self, _0x266e0d3d):
        _0x10cd395c = _0x266e0d3d.get_services()
        if not _0x10cd395c:
            return
        self._0x3522077d = _0x4c284fb2(_0x10cd395c)
        _0x92098b4c = set(self._0x3522077d)
        self._0x93b9730d = {_0xef7c876f: _0x2063c160 for (_0xef7c876f, _0x2063c160) in self._0x93b9730d.items() if _0xef7c876f in _0x92098b4c}
        self._0x84f90afc = {_0xef7c876f: _0x2063c160 for (_0xef7c876f, _0x2063c160) in self._0x84f90afc.items() if _0xef7c876f in _0x92098b4c}
        _0x98fb7916 = self._0xc2a94238()
        for (_0xef7c876f, _0x756bb351) in self._0x3522077d.items():
            if not _0x756bb351._0x500f1c43:
                continue
            if _0x98fb7916 is not None and _0xef7c876f not in _0x98fb7916:
                continue
            try:
                _0x7f6f2cd1 = await _0x266e0d3d.read_characteristic(_0xef7c876f)
            except Exception as _0x56bd7107:
                continue
            self._0x93b9730d[_0xef7c876f] = _0x7f6f2cd1
            self._0x84f90afc[_0xef7c876f] = _0xd3278554(_0x756bb351, _0x7f6f2cd1)
        self._0x696cd6fe(0.0)

    def _0x19eb0e64(self, _0x958b30d4):
        if self._0xc97399be(_0x958b30d4):
            return False
        return not self._0xfc17d6bb(_0x958b30d4)

    def _0x86b41222(self, _0x32e2cb0f):
        if self._0xc97399be(int(_0x32e2cb0f)):
            return False
        return int(_0x32e2cb0f) not in self._0x05ecc105

    def _0xe2e1241d(self, _0x32e2cb0f):
        _0x42aefbae = int(_0x32e2cb0f)
        if not self._0x86b41222(_0x42aefbae):
            return False
        _0x686090eb = _0x825031bd(_0x42aefbae, 0)
        _0x8d777f38 = self.data or {}
        if _0x686090eb in _0x8d777f38:
            return False
        if _0x686090eb in self._0xdedd8ef4:
            return False
        return True

    def _0x60391626(self, _0x2063c160):
        if _0x2063c160 is None:
            return False
        if isinstance(_0x2063c160, str) and (not _0x2063c160.strip()):
            return False
        return True

    def _0x1d0c6f37(self, _0x8d777f38, _0x11593456=None):
        _0xc44387b4 = self._0xdedd8ef4 if _0x11593456 is None else _0x11593456
        _0x34a2b396 = {}
        for (_0x3c6e0b8a, _0x2063c160) in _0x8d777f38.items():
            if not self._0x60391626(_0x2063c160):
                _0xc44387b4.pop(_0x3c6e0b8a, None)
                continue
            if self._0xfc17d6bb(_0x3c6e0b8a):
                _0xc44387b4.pop(_0x3c6e0b8a, None)
                continue
            _0x34a2b396[_0x3c6e0b8a] = _0x2063c160
        _0xe9a64b1c = {int(_0x3c6e0b8a[0]) for _0x3c6e0b8a in _0x34a2b396 if isinstance(_0x3c6e0b8a, tuple) and len(_0x3c6e0b8a) == 2 and (int(_0x3c6e0b8a[1]) == 0)}
        for _0x32e2cb0f in _0xe9a64b1c:
            _0xeef79ba5 = int(_0x32e2cb0f)
            _0xb07286eb = False
            if _0xeef79ba5 in _0x34a2b396:
                _0x34a2b396.pop(_0xeef79ba5, None)
                _0xb07286eb = True
            if _0xeef79ba5 in _0xc44387b4:
                _0xc44387b4.pop(_0xeef79ba5, None)
                _0xb07286eb = True
            if _0xb07286eb or _0xeef79ba5 in self._0x94b57abb:
                self._0x01fa193e(_0x32e2cb0f, None)
        return (_0x34a2b396, _0x11593456)

    def _0xf1874205(self, _0x8d777f38, _0x32e2cb0f, _0x7123a699):
        _0xf1c23cc9 = {_0x825031bd(_0x32e2cb0f, _0x7123a699)}
        if _0x7123a699 in (None, 0):
            _0xf1c23cc9.add(int(_0x32e2cb0f))
            _0xf1c23cc9.add(_0x825031bd(_0x32e2cb0f, 0))
        for _0x3c6e0b8a in _0xf1c23cc9:
            _0x8d777f38.pop(_0x3c6e0b8a, None)
            self._0xdedd8ef4.pop(_0x3c6e0b8a, None)
            self._0x4250c6b6.pop(_0x3c6e0b8a, None)

    def _0x6f60f3b2(self, _0xc59247c8, _0xfe558db1):
        _0x0b54c559 = dict(self.data) if self.data else {}
        for _0x884d9804 in _0xfe558db1:
            (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x884d9804)
            self._0xf1874205(_0x0b54c559, _0x32e2cb0f, _0x7123a699)
        _0x0b54c559.update(_0xc59247c8)
        (_0x0b54c559, _) = self._0x1d0c6f37(_0x0b54c559)
        return _0x0b54c559

    def _0xbc542398(self, _0xd939aaf7):
        _0x691d502c = []
        for (_0x958b30d4, _0x2063c160) in (self.data or {}).items():
            if not self._0x60391626(_0x2063c160):
                continue
            if not self._0x19eb0e64(_0x958b30d4):
                continue
            if not isinstance(_0x958b30d4, tuple) and (not self._0xe2e1241d(_0x958b30d4)):
                continue
            _0x32e2cb0f = int(_0x958b30d4[0] if isinstance(_0x958b30d4, tuple) else _0x958b30d4)
            _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
            if _0xe9a23cbc is None:
                continue
            if self._0x512d0b0d(_0x32e2cb0f) != _0xd939aaf7:
                continue
            _0x691d502c.append(_0x958b30d4)
        return tuple(_0x691d502c)

    def _0x512d0b0d(self, _0x32e2cb0f):
        _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None:
            return _0xc9ed32a4._0x696b0310
        return _0xe9a23cbc.preferred_kind

    def _0x7248158e(self, _0x266e0d3d):
        if _0x266e0d3d is None or _0x266e0d3d.client is None:
            return False
        try:
            return bool(_0x266e0d3d.client.is_connected)
        except Exception:
            return False

    @property
    def _0x3a821fc7(self):
        return self._0x7248158e(self._0x084706dd)

    def _0x6fe1e009(self, _0xd2e16d3f):
        if hasattr(self, _0xd14e4b1f('6173796e635f7365745f7570646174655f696e74657276616c')):
            self.async_set_update_interval(_0xd2e16d3f)
        else:
            self.update_interval = _0xd2e16d3f

    def _0xfa4ed030(self, _0x14f802e1, *, _0xaa9f73ee=20):
        _0xd6662047 = []
        _0x6dacddc1 = [_0x3c6e0b8a for _0x3c6e0b8a in _0x14f802e1 if not isinstance(_0x3c6e0b8a, str)]
        for _0x3c6e0b8a in sorted(_0x6dacddc1, key=_0x9e46b199)[:_0xaa9f73ee]:
            (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x3c6e0b8a)
            _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
            _0xd304ba20 = _0xe9a23cbc.key if _0xe9a23cbc is not None else str(_0x32e2cb0f)
            if _0x7123a699 is None:
                _0xd6662047.append(_0xd304ba20)
            else:
                _0xd6662047.append(f"{_0xd304ba20}{_0xd14e4b1f('3a')}{_0x7123a699}")
        _0x2626772c = _0xaa9f73ee - len(_0xd6662047)
        if _0x2626772c > 0:
            for _0xef7c876f in sorted((_0x3c6e0b8a for _0x3c6e0b8a in _0x14f802e1 if isinstance(_0x3c6e0b8a, str)))[:_0x2626772c]:
                _0x756bb351 = self._0x3522077d.get(_0xef7c876f)
                _0xd6662047.append(f"{_0xd14e4b1f('676174743a')}{(_0x756bb351.key if _0x756bb351 is not None else _0xef7c876f)}")
        return _0xd6662047

    def _0xd46304b0(self):
        self._0x3147b7f8(_0xd14e4b1f('537461747573207570646174653a20706f6c6c5f656e61626c65643d257320626c655f636f6e6e65637465643d25732070657273697374656e745f72656164793d257320696e746567726174696f6e5f72656164793d2573206c6173745f726566726573685f636f6d706c6574653d257320646174615f6b6579733d2564'), self.poll_enabled, self._0x3a821fc7, self._0x8dc7742e(_0x60810dad=False), self._0xd92c6474, self._0xabcb4e1a, len(self.data or {}))
        self.async_update_listeners()

    def _0x20c07364(self, _0x2063c160):
        if self._0x73d4c228 == _0x2063c160:
            return
        self._0x73d4c228 = _0x2063c160
        self._0xd46304b0()

    def _0x7dc2142f(self, _0x185336ab):
        self._0x3147b7f8(_0xd14e4b1f('5265667265736820737563636573733a20726566726573685f636f6d706c6574653d257320646174615f6b6579733d2564'), _0x185336ab, len(self.data or {}))
        self._0xabcb4e1a = _0x185336ab
        self._0x20c07364(_0x185336ab)

    def _0x4b8f2e4e(self):
        self._0x3147b7f8(_0xd14e4b1f('52656672657368206661696c7572653a20626c655f636f6e6e65637465643d25732070657273697374656e745f72656164793d257320646174615f6b6579733d2564'), self._0x3a821fc7, self._0x8dc7742e(_0x60810dad=False), len(self.data or {}))
        self._0xabcb4e1a = False
        self._0x20c07364(False)

    def _0xc07eb575(self, _0x8d777f38, *, _0x52f1ba45=None, _0x1cb60fd5=False):
        if self._0xbb786552:
            return
        _0xff8a6061 = self.data or {}
        _0xf362a929 = set(_0xff8a6061)
        _0x8f5eec92 = set(_0x8d777f38)
        _0x4284fcde = _0xf362a929 - _0x8f5eec92
        _0x8486e27d = _0x8f5eec92 - _0xf362a929
        if _0x4284fcde or _0x8486e27d:
            self._0x3147b7f8(_0xd14e4b1f('5075626c697368696e672072756e74696d6520646174613a206b6579735f6265666f72653d2564206b6579735f61667465723d25642061646465643d25642064726f707065643d25642061646465645f73616d706c653d25732064726f707065645f73616d706c653d2573'), len(_0xf362a929), len(_0x8f5eec92), len(_0x8486e27d), len(_0x4284fcde), self._0xfa4ed030(_0x8486e27d), self._0xfa4ed030(_0x4284fcde))
        else:
            self._0x3147b7f8(_0xd14e4b1f('5075626c697368696e672072756e74696d6520646174613a206b6579735f6265666f72653d2564206b6579735f61667465723d2564206e6f206b6579736574206368616e6765'), len(_0xf362a929), len(_0x8f5eec92))
        if _0x1cb60fd5:
            self.data = _0x8d777f38
            if not self._0xbe3450d2:
                self._0xbe3450d2 = True

                async def _0x363c8dcd():
                    try:
                        await asyncio.sleep(self._0x39779d0f)
                        self._0xbe3450d2 = False
                        self.async_set_updated_data(self.data)
                        self._0x72dfe5d1()
                    except asyncio.CancelledError:
                        pass
                self._0x878b4eb8 = self.hass.async_create_task(_0x363c8dcd())
        else:
            self.async_set_updated_data(_0x8d777f38)
            self._0x72dfe5d1()
        if _0x52f1ba45 is not None:
            self._0x696cd6fe(_0x52f1ba45)

    def _0xd7644488(self, _0x924a8cee):
        self._0xe77f8e52.append(_0x924a8cee)

    def _0x72dfe5d1(self):
        if not self._0xe77f8e52:
            return
        for _0x924a8cee in tuple(self._0xe77f8e52):
            try:
                _0x924a8cee()
            except Exception as _0x56bd7107:
                pass

    def _0x1ac0a4ae(self, _0x69080cee):
        _0xe2ad9856 = f"{self._device_id}{_0xd14e4b1f('5f67656e657269635f')}"
        if _0x69080cee.startswith(_0xe2ad9856):
            _0x321c3cf4 = _0x69080cee[len(_0xe2ad9856):]
            _0x7123a699 = None
            if _0xd14e4b1f('5f696e7374616e63655f') in _0x321c3cf4:
                (_0x6e384ad7, _0xad382bdf) = _0x321c3cf4.split(_0xd14e4b1f('5f696e7374616e63655f'), 1)
                try:
                    _0x7123a699 = int(_0xad382bdf)
                except ValueError:
                    pass
                _0x3c6e0b8a = _0x6e384ad7
            else:
                _0x3c6e0b8a = _0x321c3cf4
            for (_0x32e2cb0f, _0xe9a23cbc) in self._0x77ad7fd7.items():
                if _0xe9a23cbc.key == _0x3c6e0b8a:
                    return _0x825031bd(_0x32e2cb0f, _0x7123a699)
            return None
        _0xb7b8ccd2 = f"{self._device_id}{_0xd14e4b1f('5f676174745f')}"
        if _0x69080cee.startswith(_0xb7b8ccd2):
            _0x3c6e0b8a = _0x69080cee[len(_0xb7b8ccd2):]
            for (_0xef7c876f, _0x756bb351) in self._0x3522077d.items():
                if _0x756bb351.key == _0x3c6e0b8a:
                    return _0xef7c876f
            return None
        return None

    def _0xc2a94238(self):
        try:
            _0xf9fb410d = er.async_get(self.hass)
            _0x5fce916b = er.async_entries_for_config_entry(_0xf9fb410d, self._0x5f3f26ad.entry_id)
            if _0x5fce916b:
                _0xe0c40454 = False
                _0x98fb7916 = set()
                for _0x1043bfc7 in _0x5fce916b:
                    _0x1747dbff = _0x1043bfc7.unique_id.startswith(f"{self._device_id}{_0xd14e4b1f('5f67656e657269635f')}")
                    _0x17f388a5 = _0x1043bfc7.unique_id.startswith(f"{self._device_id}{_0xd14e4b1f('5f676174745f')}")
                    if _0x1747dbff or _0x17f388a5:
                        _0xe0c40454 = True
                        if _0x1043bfc7.disabled_by is None:
                            _0x958b30d4 = self._0x1ac0a4ae(_0x1043bfc7.unique_id)
                            if _0x958b30d4 is not None:
                                _0x98fb7916.add(_0x958b30d4)
                if _0xe0c40454:
                    return _0x98fb7916
            _0xb79064a1 = self._0xf5fadddf()
            return _0xb79064a1 or None
        except Exception as _0x54d54a12:
            return None

    async def _0x8219d935(self):
        if not self._0x0104f66a:
            return
        _0x234a9b6b = set()
        for _0x958b30d4 in self.data or {}:
            (_0x32e2cb0f, _) = _0x726b25f9(_0x958b30d4)
            _0xe9a23cbc = self._0xf1645e71(_0x32e2cb0f)
            if _0xe9a23cbc is not None and (not _0xe9a23cbc.entity_registry_enabled_default) and self._0x19eb0e64(_0x958b30d4):
                _0x234a9b6b.add(_0x958b30d4)
        for (_0xef7c876f, _0x756bb351) in self._0x3522077d.items():
            if _0x756bb351._0x500f1c43 and (not _0x756bb351.entity_registry_enabled_default) and (_0xef7c876f in self._0x93b9730d or _0xef7c876f in self._0x84f90afc):
                _0x234a9b6b.add(_0xef7c876f)
        _0xf9fb410d = er.async_get(self.hass)
        _0x665d96b5 = []
        _0xf3a3393e = set()
        for _ in range(20):
            _0x665d96b5 = []
            _0xf3a3393e = set()
            for _0xe03ed967 in er.async_entries_for_config_entry(_0xf9fb410d, self._0x5f3f26ad.entry_id):
                _0x958b30d4 = self._0x1ac0a4ae(_0xe03ed967.unique_id)
                if _0x958b30d4 is None:
                    continue
                _0x665d96b5.append((_0xe03ed967, _0x958b30d4))
                _0xf3a3393e.add(_0x958b30d4)
            if _0x234a9b6b.issubset(_0xf3a3393e):
                break
            await asyncio.sleep(0.05)
        self._0xa1de6604 = True
        try:
            for (_0xe03ed967, _0x958b30d4) in _0x665d96b5:
                if _0x958b30d4 not in _0x234a9b6b or _0xe03ed967.disabled_by is not None:
                    continue
                _0xf9fb410d.async_update_entity(_0xe03ed967.entity_id, disabled_by=er.RegistryEntryDisabler.INTEGRATION)
        finally:
            self._0xa1de6604 = False
            self._0x0104f66a = False
        _0x45b532d8 = _0x234a9b6b - _0xf3a3393e
        if _0x45b532d8:
            pass

    @callback
    def _0x616f970c(self, _0x41196390):
        if self._0xbb786552 or self._0x80c14035 or self._0x5eda439f or self._0xa1de6604:
            return
        _0xdffc4713 = _0x41196390.data.get(_0xd14e4b1f('656e746974795f6964'))
        if not _0xdffc4713:
            return
        _0x418c5509 = _0x41196390.data.get(_0xd14e4b1f('616374696f6e'))
        if _0x418c5509 != _0xd14e4b1f('757064617465'):
            return
        _0xe03ed967 = er.async_get(self.hass).async_get(_0xdffc4713)
        if _0xe03ed967 is None or _0xe03ed967.config_entry_id != self._0x5f3f26ad.entry_id:
            return
        self._0x3147b7f8(_0xd14e4b1f('456e7469747920726567697374727920757064617465206576656e742072656365697665642028616374696f6e3d25732c20656e746974795f69643d257329'), _0x418c5509, _0xdffc4713)
        if self._0x49464da6 is not None and (not self._0x49464da6.done()):
            self._0x49464da6.cancel()
        self._0x49464da6 = self.hass.async_create_task(self._0x2483df2a())

    @device_log_context
    async def _0x2483df2a(self):
        if not self._0x23c6e6a5 or self._0x5eda439f:
            return
        async with self._0x5d231dfe:
            if self._0x084706dd is None or not self._0x3a821fc7:
                return
            if self._0xc2d0990a and self._0xd4252973 is None:
                return
            self._0x3147b7f8(_0xd14e4b1f('50726f63657373696e67207265676973747279207570646174657320746f2061646a7573742061637469766520424c4520706f6c6c696e672f6e6f74696669636174696f6e73'))
            _0x98fb7916 = self._0xc2a94238()
            if _0x98fb7916 is None:
                return
            _0x001cc4f0 = set()
            for _0x32e2cb0f in self._0x77ad7fd7:
                for _0x654432d6 in self._0x27940332(_0x32e2cb0f):
                    if _0x654432d6 in _0x98fb7916:
                        _0x001cc4f0.add(_0x654432d6)
            _0xb463d4cc = _0x001cc4f0 - self._0x01aa0845
            _0x099f90b8 = self._0x01aa0845 - _0x001cc4f0
            if _0xb463d4cc:
                _0xcb982542 = []
                for _0x654432d6 in sorted(_0xb463d4cc, key=_0x9e46b199):
                    (_0xa4d554f5, _0x87f1e7b0) = _0x726b25f9(_0x654432d6)
                    try:
                        (_0x3ec5d083, _0xa1031145) = await self._0xf49209e0(_0x654432d6)
                        if _0x3ec5d083 in _0xa1031145:
                            _0xcb982542.append(_0x3ec5d083)
                    except Exception as _0x2d83211f:
                        pass
                for _0x654432d6 in _0xcb982542:
                    self._0xf3be43ed(_0x654432d6)
                    _0x478f3a4c = asyncio.create_task(self._0x4007296a(_0x654432d6))
                    self._0x5d1bb011.append(_0x478f3a4c)
                    self._0xd3a0bb01[_0x478f3a4c] = _0x654432d6
            if _0x099f90b8:
                try:
                    _0x075ae3d2 = await self._0xb317e247(f"{_0xd14e4b1f('6e6f746966792d64697361626c6520746172676574733d')}{list(_0x099f90b8)}", lambda : self._0xd4252973.disable_notification(list(_0x099f90b8)), _0x60810dad=True)
                except Exception as _0x8f7f04e1:
                    pass
                _0xeba5d264 = [_0x478f3a4c for (_0x478f3a4c, _0x654432d6) in list(self._0xd3a0bb01.items()) if _0x654432d6 in _0x099f90b8]
                for _0x478f3a4c in _0xeba5d264:
                    _0x654432d6 = self._0xd3a0bb01.get(_0x478f3a4c)
                    _0x478f3a4c.cancel()
                    self._0xd3a0bb01.pop(_0x478f3a4c, None)
                    if _0x478f3a4c in self._0x5d1bb011:
                        self._0x5d1bb011.remove(_0x478f3a4c)
                for _0x654432d6 in _0x099f90b8:
                    self._0x01aa0845.discard(_0x654432d6)
            _0x510543e3 = [_0x8ce4b16b for _0x8ce4b16b in _0x98fb7916 if not isinstance(_0x8ce4b16b, str) and _0x8ce4b16b not in (self.data or {}) and (self._0xa1aaa9f2(_0x726b25f9(_0x8ce4b16b)[0]) in (_0xd14e4b1f('706f6c6c'), _0xd14e4b1f('6e6f74696679')))]
            if _0x510543e3:
                try:
                    (_0xa9f0a3a6, _) = await self._0xb317e247(f"{_0xd14e4b1f('6d756c74692d7265616420')}{len(_0x510543e3)}{_0xd14e4b1f('206e65776c7920656e61626c65642074617267657473')}", lambda : self._0xd4252973.read_many(_0x510543e3, timeout=self._0xf3e35bdf), _0x60810dad=True, _0x90272dda=self._0xf3e35bdf + 5.0)
                    _0x70179363 = dict(self.data) if self.data else {}
                    for (_0x884d9804, _0x37dc56b4) in _0xa9f0a3a6.items():
                        (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x884d9804)
                        _0xad054584 = self._0x18ad59bd(_0x32e2cb0f, _0x37dc56b4)
                        _0x958b30d4 = _0x825031bd(_0x32e2cb0f, _0x7123a699)
                        if self._0x60391626(_0xad054584):
                            self._0xdedd8ef4[_0x958b30d4] = _0x37dc56b4
                            self._0x4250c6b6[_0x958b30d4] = _0xd14e4b1f('706f6c6c')
                            _0x70179363[_0x958b30d4] = _0xad054584
                    (_0x70179363, _) = self._0x1d0c6f37(_0x70179363)
                    self._0xc07eb575(_0x70179363)
                except Exception as _0x56bd7107:
                    pass
            if self._0xb605ddfc:
                try:
                    await self._0xba139b66(self._0x084706dd)
                    self._0xc07eb575(self.data or {})
                except Exception as _0x56bd7107:
                    pass

    def _0x255a5598(self):
        self._0x4b8f2e4e()
        self._0xd8c19966.clear()
        self._0x01aa0845.clear()
        self._0xcbec47bb = False
        self._0x9ff434a9 = {}
        self._0xb8223521 = set()

    def _0x4af2a93e(self):
        if not self._0x5d1bb011:
            return
        _0xc6d3ff56 = []
        _0xe6d6f918 = []
        for _0x478f3a4c in self._0x5d1bb011:
            if _0x478f3a4c.done():
                _0x1da6b67b = self._0xd3a0bb01.pop(_0x478f3a4c, None)
                if _0x1da6b67b is not None:
                    _0xd517b272 = None
                    try:
                        _0xd517b272 = _0x478f3a4c.exception()
                    except (asyncio.CancelledError, asyncio.InvalidStateError):
                        pass
                    if _0xd517b272 is not None:
                        if self._0x3a821fc7:
                            _0x4bcc5e3b = self._0x9ff434a9.get(_0x1da6b67b, 0) + 1
                            self._0x9ff434a9[_0x1da6b67b] = _0x4bcc5e3b
                            (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x1da6b67b)
                            if _0x4bcc5e3b >= 3:
                                self._0xb8223521.add(_0x1da6b67b)
                                if _0x7123a699 is None:
                                    pass
                                continue
                            elif _0x7123a699 is None:
                                pass
                    if _0x1da6b67b not in self._0xb8223521:
                        _0xc6d3ff56.append(_0x1da6b67b)
                continue
            _0xe6d6f918.append(_0x478f3a4c)
        self._0x5d1bb011 = _0xe6d6f918
        if not _0xc6d3ff56 or not self.poll_enabled or (not self._0x3a821fc7) or (self._0xd4252973 is None):
            return
        for _0x1da6b67b in sorted(_0xc6d3ff56, key=_0x9e46b199):
            (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x1da6b67b)
            if _0x7123a699 is None:
                self._0x3147b7f8(_0xd14e4b1f('52657374617274696e67206e6f74696669636174696f6e206c697374656e657220666f722044704964202564'), _0x32e2cb0f)
            else:
                self._0x3147b7f8(_0xd14e4b1f('52657374617274696e67206e6f74696669636174696f6e206c697374656e657220666f72204470496420256420696e7374616e63653d2564'), _0x32e2cb0f, _0x7123a699)
            _0x478f3a4c = asyncio.create_task(self._0x4007296a(_0x1da6b67b))
            self._0x5d1bb011.append(_0x478f3a4c)
            self._0xd3a0bb01[_0x478f3a4c] = _0x1da6b67b

    def _0x0e8f8f97(self, _0x266e0d3d, _0x06aa6fa8, *_0x3d7902a3):
        if _0x266e0d3d is not self._0x084706dd:
            return
        if _0x06aa6fa8:
            self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420636f6e6e6563746f72207265706f7274656420636f6e6e6563746564207374617465'))
            self._0xd46304b0()
            return
        self._0x4b8f2e4e()
        if not self.poll_enabled:
            self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e6563746f7220646973636f6e6e6563746564207768696c6520636f6e6e656374696f6e20737769746368206973206f6666'))
            self._0xd46304b0()
            return
        self._0xd46304b0()

    @device_log_context
    async def _0x111bbd40(self):
        async with self._0xf6b7615e:
            if self._0xbb786552 or self._0x80c14035:
                return
            self.poll_enabled = True
            self._0xe8e1c9b0 = False
            self._0xe86ce9bc.set()
            self._0x6fe1e009(self._0x5755254e)
            self._0xb0ae159e()
            self._0xd46304b0()

    @device_log_context
    async def _0x30ffb15e(self):
        async with self._0xf6b7615e:
            self.poll_enabled = False
            self._0xe86ce9bc.clear()
            self._0x6fe1e009(None)
            self._0x4b8f2e4e()
            _0x01e2cd23 = self._0x49464da6
            self._0x49464da6 = None
            if _0x01e2cd23 is not None:
                _0x01e2cd23.cancel()
                await asyncio.gather(_0x01e2cd23, return_exceptions=True)
            _0x329e2707 = self._0xe68baedb
            self._0xe68baedb = None
            if _0x329e2707 is not None:
                _0x329e2707.cancel()
                await asyncio.gather(_0x329e2707, return_exceptions=True)
            async with self._0xadbbed2f:
                await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('636f6e6e656374696f6e20737769746368207475726e6564206f6666'))

    @device_log_context
    async def _0xbeabd378(self):
        await self._0xf6b7615e.acquire()
        if self._0xbb786552 or self._0x80c14035:
            self._0xf6b7615e.release()
            return False
        try:
            self._0x5eda439f = True
            self._0x6fe1e009(None)
            self._0x3147b7f8(_0xd14e4b1f('50617573696e6720636f6f7264696e61746f7220424c4520616374697669747920666f72206578636c757369766520636f6e6e656374696f6e2074657374'))
            _0x01e2cd23 = self._0x49464da6
            self._0x49464da6 = None
            if _0x01e2cd23 is not None:
                _0x01e2cd23.cancel()
                await asyncio.gather(_0x01e2cd23, return_exceptions=True)
            _0x329e2707 = self._0xe68baedb
            self._0xe68baedb = None
            if _0x329e2707 is not None:
                _0x329e2707.cancel()
                await asyncio.gather(_0x329e2707, return_exceptions=True)
            async with self._0xadbbed2f:
                await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('6578636c7573697665206f7074696f6e7320666c6f7720636f6e6e656374696f6e2074657374'))
            self._0x3147b7f8(_0xd14e4b1f('436f6f7264696e61746f7220424c452061637469766974792070617573656420666f72206578636c757369766520636f6e6e656374696f6e2074657374'))
            return True
        except BaseException:
            self._0x5eda439f = False
            if self.poll_enabled and (not self._0xbb786552) and (not self._0x80c14035):
                self._0x6fe1e009(self._0x5755254e)
                self._0xb0ae159e()
            self._0xf6b7615e.release()
            raise

    @device_log_context
    async def _0xdb22ea9d(self, *, _0x0ac3398d, _0xad5cd0c1):
        if not _0x0ac3398d:
            return
        try:
            if _0xad5cd0c1 and self.poll_enabled and (not self._0xbb786552) and (not self._0x80c14035):
                self._0x5eda439f = False
                self._0xe8e1c9b0 = False
                self._0x6fe1e009(self._0x5755254e)
                self._0xb0ae159e()
                self._0x3147b7f8(_0xd14e4b1f('436f6f7264696e61746f7220424c4520616374697669747920726573756d656420616674657220636f6e6e656374696f6e2074657374'))
            else:
                self._0x3147b7f8(_0xd14e4b1f('436f6f7264696e61746f7220424c45206163746976697479206c6566742073746f707065642070656e64696e6720636f6e66696720656e7472792072656c6f6164'))
            self._0xd46304b0()
        finally:
            self._0xf6b7615e.release()

    @device_log_context
    async def _async_update_data(self):
        if self._0xbb786552 or self._0x80c14035:
            return self.data or {}
        if self._0x5eda439f:
            self._0x3147b7f8(_0xd14e4b1f('506f6c6c696e6720736b6970706564206265636175736520424c452061637469766974792069732070617573656420666f72206120636f6e6e656374696f6e2074657374'))
            return self.data or {}
        if not self.poll_enabled:
            return self.data or {}
        async with self._0xadbbed2f:
            if self._0x5eda439f:
                self._0x3147b7f8(_0xd14e4b1f('506f6c6c696e6720736b69707065642061667465722077616974696e6720666f7220424c45206c6f636b2062656361757365206120636f6e6e656374696f6e20746573742070617573652073746172746564'))
                return self.data or {}
            if self._0x8dc7742e(_0x60810dad=self._0xc2d0990a):
                self._0x3147b7f8(_0xd14e4b1f('506f6c6c207573696e67206163746976652070657273697374656e7420424c4520636f6e6e656374696f6e20287573655f64706964733d25732c207573655f676174743d257329'), self._0xc2d0990a, self._0xb605ddfc)
                try:
                    if self._0xc2d0990a:
                        (_0x8d777f38, _0x185336ab) = await self._0x60aa9737(_0x27d707fd=True)
                        self._0x3147b7f8(_0xd14e4b1f('4450494420706f6c6c207265667265736820636f6d706c6574656e6573733a202573'), _0x185336ab)
                        self._0x7dc2142f(_0x185336ab)
                        return _0x8d777f38
                    if self._0xb605ddfc:
                        await self._0xba139b66(self._0x084706dd)
                        self._0x7dc2142f(True)
                        return self.data or {}
                except Exception as _0x56bd7107:
                    if not self._0x3a821fc7:
                        self._0x4b8f2e4e()
                        await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('706f6c6c206166746572207265616c20646973636f6e6e656374'))
                        return self.data or {}
                    return self.data or {}
            self._0x3147b7f8(_0xd14e4b1f('506f6c6c20736b69707065642062656361757365206e6f2070657273697374656e7420424c452073657373696f6e206973207265616479207965742028636f6e6e6563746f723d25732c20636f6e6e65637465643d25732c20636c69656e743d257329'), self._0x084706dd is not None, self._0x3a821fc7, self._0xd4252973 is not None)
            return self.data or {}

    async def _0x60aa9737(self, *, _0x27d707fd):
        if self._0xb605ddfc and self._0x084706dd is not None:
            await self._0xba139b66(self._0x084706dd)
        if not self._0xcbec47bb and 763 in self._0x25cb3c49 and (270 in self._0x25cb3c49):
            try:
                _0xa13d898b = await self._0x56c3a97b(763)
                _0x3457e9f9 = int.from_bytes(_0xa13d898b, byteorder=_0xd14e4b1f('6c6974746c65'))
                _0x0c52488c = self._0x57023259()
                _0x47af5c12 = int(time.time())
                _0xa3ffeaa9 = _0x47af5c12 + _0x0c52488c
                if abs(_0x3457e9f9 - _0xa3ffeaa9) > 60:
                    await self._0x97956325(270, _0x47af5c12.to_bytes(4, byteorder=_0xd14e4b1f('6c6974746c65')))
                self._0xcbec47bb = True
            except Exception as _0xd1ef682e:
                pass
        _0x8d777f38 = {}
        _0xde5eac3b = self._0x3a3a4684
        if not self._0x68eea019:
            _0x9b504c43 = set(_0xde5eac3b)
            if self._0x96ffac89 == _0x5223e47e:
                _0x9b504c43.update(self._0x63735d9e)
            self._0x99bc22f6(_0x9b504c43, _0xde5eac3b)
        else:
            _0x9b504c43 = set(self._0x94b57abb)
        self._0x3147b7f8(_0xd14e4b1f('445049442072656672657368207374617274696e6720776974682025642063616e646964617465733a202573'), len(_0x9b504c43), sorted(_0x9b504c43))
        _0xeb156fad = {}
        _0x433b0376 = []
        _0x98fb7916 = self._0xc2a94238() if _0x27d707fd else None
        for _0x32e2cb0f in sorted(_0x9b504c43):
            _0x869fad40 = getattr(_0x32e2cb0f, _0xd14e4b1f('6e616d65'), str(_0x32e2cb0f))
            _0x6478e51f = self._0xd8ace7ec(_0x32e2cb0f, _0x42bd4c08=_0x32e2cb0f in _0xde5eac3b)
            self._0x3147b7f8(_0xd14e4b1f('4450494420726566726573682072656164696e672064705f69643d2573206e616d653d2573206164647265737365733d2573'), _0x32e2cb0f, _0x869fad40, _0x6478e51f)
            for _0x884d9804 in _0x6478e51f:
                if _0x884d9804 in _0xeb156fad:
                    continue
                if _0x98fb7916 is not None and _0x884d9804 not in _0x98fb7916:
                    continue
                _0x433b0376.append(_0x884d9804)
                _0xeb156fad[_0x884d9804] = _0x32e2cb0f
        self._0x3147b7f8(_0xd14e4b1f('44504944207265667265736820657870616e64656420746f202564206164647265737365732077697468206368756e6b5f73697a653d25642074696d656f75743d252e316673'), len(_0x433b0376), self._0x57274421, self._0xf3e35bdf)
        _0x185336ab = True
        _0xfe558db1 = set()
        _0xb9ac76a9 = set()
        for _0x50d739f3 in _0xc9e514d3(_0x433b0376, self._0x57274421):
            self._0x3147b7f8(_0xd14e4b1f('4450494420726566726573682062617463682072656164696e6720256420616464726573736573'), len(_0x50d739f3))
            _0xfe558db1.update(_0x50d739f3)
            (_0xa9f0a3a6, _0x07213a01) = await self._0xb317e247(f"{_0xd14e4b1f('6d756c74692d7265616420')}{len(_0x50d739f3)}{_0xd14e4b1f('2074617267657473')}", lambda _0x50d739f3=_0x50d739f3: self._0xd4252973.read_many(_0x50d739f3, timeout=self._0xf3e35bdf), _0x60810dad=True, _0x90272dda=self._0xf3e35bdf + 5.0)
            for (_0x884d9804, _0x37dc56b4) in _0xa9f0a3a6.items():
                (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x884d9804)
                _0xb9ac76a9.add(_0x32e2cb0f)
                _0x869fad40 = getattr(_0x32e2cb0f, _0xd14e4b1f('6e616d65'), str(_0x32e2cb0f))
                _0xad054584 = self._0x18ad59bd(_0x32e2cb0f, _0x37dc56b4)
                _0x958b30d4 = _0x825031bd(_0x32e2cb0f, _0x7123a699)
                if not self._0x60391626(_0xad054584):
                    self._0xdedd8ef4.pop(_0x958b30d4, None)
                    self._0x4250c6b6.pop(_0x958b30d4, None)
                    self._0x01fa193e(_0x32e2cb0f, _0x7123a699)
                    continue
                _0xa0bf7556 = self.data or {}
                _0x426ea53d = _0xa0bf7556.get(_0x958b30d4, _0x8a9cbaca)
                if _0x426ea53d is not _0x8a9cbaca and _0x426ea53d == _0xad054584:
                    _0x8d777f38[_0x958b30d4] = _0x426ea53d
                    continue
                self._0xdedd8ef4[_0x958b30d4] = _0x37dc56b4
                self._0x4250c6b6[_0x958b30d4] = _0xd14e4b1f('706f6c6c')
                _0x8d777f38[_0x958b30d4] = _0xad054584
                self._0x3147b7f8(_0xd14e4b1f('44504944207265667265736820737563636573732064705f69643d2573206e616d653d257320696e7374616e63653d2573206465636f6465643d2572'), _0x32e2cb0f, _0x869fad40, _0x7123a699, _0xad054584)
            for (_0x884d9804, _0x54d54a12) in _0x07213a01.items():
                (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x884d9804)
                _0x869fad40 = getattr(_0x32e2cb0f, _0xd14e4b1f('6e616d65'), str(_0x32e2cb0f))
                self._0x3147b7f8(_0xd14e4b1f('445049442072656672657368206661696c65642064705f69643d2573206e616d653d257320696e7374616e63653d2573206572726f723d2573'), _0x32e2cb0f, _0x869fad40, _0x7123a699, _0x54d54a12)
                if self._0x94c69b93(_0x54d54a12):
                    self._0x01fa193e(_0x32e2cb0f, _0x7123a699)
                else:
                    if not self._0x4c068da5(_0x54d54a12):
                        _0xb9ac76a9.add(_0x32e2cb0f)
                    _0x185336ab = False
        for _0x32e2cb0f in sorted(_0x9b504c43):
            _0x214ae76e = self._0x94b57abb.get(_0x32e2cb0f, ())
            if _0x214ae76e and _0x32e2cb0f in _0xb9ac76a9 and (_0x32e2cb0f not in _0xde5eac3b):
                self._0xa6f36771.add(_0x32e2cb0f)
                self._0x8c009663(_0x32e2cb0f)
                self._0x8f41c896 = True
                _0x869fad40 = getattr(_0x32e2cb0f, _0xd14e4b1f('6e616d65'), str(_0x32e2cb0f))
                self._0x3147b7f8(_0xd14e4b1f('44504944207265667265736820646973636f7665726564206e6f6e2d696e76656e746f72792064705f69643d2573206e616d653d2573'), _0x32e2cb0f, _0x869fad40)
        self._0x76e5bb59()
        if self._0x96ffac89 == _0x5223e47e and _0x185336ab and (not self._0x68eea019):
            self._0x68eea019 = True
            self._0x8f41c896 = True
        (_0x8d777f38, _) = self._0x1d0c6f37(_0x8d777f38)
        _0x8d777f38 = self._0x6f60f3b2(_0x8d777f38, _0xfe558db1)
        _0xa0bf7556 = self.data or {}
        if _0xa0bf7556 and _0x8d777f38 == _0xa0bf7556:
            _0x8d777f38 = _0xa0bf7556
        self._0x3147b7f8(_0xd14e4b1f('44504944207265667265736820636f6d706c657465642077697468202564206465636f6465642064617461706f696e7473206163726f737320256420617474656d70746564206164647265737365733b206d65726765642072756e74696d65206b6579733d2564'), len(_0x8d777f38), len(_0xfe558db1), len(_0x8d777f38))
        await self._0x9bca487c()
        self._0x696cd6fe(0.0)
        return (_0x8d777f38, _0x185336ab)

    async def _0x77e0443f(self):
        while True:
            try:
                if not self.poll_enabled:
                    if self._0x084706dd is not None:
                        await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('636f6e6e656374696f6e20737769746368207475726e6564206f6666'))
                    await self._0xe86ce9bc.wait()
                    continue
                if self._0x084706dd is not None:
                    if not self._0x3a821fc7:
                        self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e656374696f6e206973206e6f206c6f6e67657220616c6976652c207265636f6e6e656374696e67'))
                        await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('7265616c20424c4520646973636f6e6e65637420646574656374656420627920636f6e6e656374696f6e206c6f6f70'))
                    elif self._0xc2d0990a and self._0x5d1bb011 and any((_0xe358efa4.done() for _0xe358efa4 in self._0x5d1bb011)):
                        self._0x3147b7f8(_0xd14e4b1f('4f6e65206f72206d6f7265206e6f74696669636174696f6e206c697374656e6572732073746f7070656420776974686f757420424c4520646973636f6e6e6563743b2072657374617274696e672066696e6973686564207461736b73'))
                        self._0x4af2a93e()
                    else:
                        await asyncio.sleep(1.0)
                    continue
                self._0x3147b7f8(_0xd14e4b1f('417474656d7074696e6720746f2065737461626c6973682070657273697374656e7420424c4520636f6e6e656374696f6e20746f204765626572697420546f696c6574'))
                async with self._0xadbbed2f:
                    _0x266e0d3d = self._0x231b3f6f()
                    _0x266e0d3d.connection_status_changed_handlers += self._0x0e8f8f97
                    try:
                        await _0x266e0d3d.connect_async(self._device_id)
                        self._0x084706dd = _0x266e0d3d
                        self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e656374696f6e207472616e73706f72742065737461626c6973686564'))
                        if self._0xe8e1c9b0:
                            self._0xe8e1c9b0 = False
                        self._0xd46304b0()
                        if self._0xc2d0990a:
                            self._0x3147b7f8(_0xd14e4b1f('4172656e64692073656375726974792068616e647368616b6520636f6e6669726d65642c206372656174696e6720426c65323020636c69656e74'))
                            _0x62608e08 = await self._0xdf782ed6(_0x266e0d3d)
                            self._0xd4252973 = _0x62608e08
                            self._0xd8c19966.set()
                            self._0xd46304b0()
                            self._0x3147b7f8(_0xd14e4b1f('426c65323020636c69656e742072656164792c207374617274696e6720696e697469616c2072656672657368'))
                            (_0x8d777f38, _0x185336ab) = await self._0x60aa9737(_0x27d707fd=False)
                            self._0x3147b7f8(_0xd14e4b1f('496e697469616c207265667265736820636f6d706c657465642c2072656365697665642025642064617461706f696e7473'), len(_0x8d777f38))
                            self._0xc07eb575(_0x8d777f38)
                            self._0x3147b7f8(_0xd14e4b1f('496e697469616c2070657273697374656e742044504944207265667265736820636f6d706c6574656e6573733a202573'), _0x185336ab)
                            await self._0x8219d935()
                            _0x98fb7916 = self._0xc2a94238()
                            _0x909fe0f6 = sorted({_0x42aefbae for _0x32e2cb0f in self._0x77ad7fd7 for _0x42aefbae in self._0x27940332(_0x32e2cb0f) if _0x98fb7916 is None or _0x42aefbae in _0x98fb7916}, key=_0x9e46b199)
                            self._0x3147b7f8(_0xd14e4b1f('5374617274696e67206e6f74696669636174696f6e20737562736372697074696f6e7320666f722025642064705f696473'), len(_0x909fe0f6))
                            _0xcb982542 = []
                            for _0x654432d6 in _0x909fe0f6:
                                (_0xa4d554f5, _0x87f1e7b0) = _0x726b25f9(_0x654432d6)
                                try:
                                    if _0x87f1e7b0 is None:
                                        self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e20737562736372697074696f6e20617474656d707420666f722044704964202564'), _0xa4d554f5)
                                    else:
                                        self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e20737562736372697074696f6e20617474656d707420666f72204470496420256420696e7374616e63653d2564'), _0xa4d554f5, _0x87f1e7b0)
                                    (_0x3ec5d083, _0xa1031145) = await self._0xf49209e0(_0x654432d6)
                                    if _0x3ec5d083 in _0xa1031145:
                                        _0xcb982542.append(_0x3ec5d083)
                                    elif _0x87f1e7b0 is None:
                                        self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e20737562736372697074696f6e2072656a65637465642062792064657669636520666f722044704964202564'), _0xa4d554f5)
                                    else:
                                        self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e20737562736372697074696f6e2072656a65637465642062792064657669636520666f72204470496420256420696e7374616e63653d2564'), _0xa4d554f5, _0x87f1e7b0)
                                except Exception as _0x2d83211f:
                                    if _0x87f1e7b0 is None:
                                        pass
                            for _0x654432d6 in _0xcb982542:
                                self._0xf3be43ed(_0x654432d6)
                                _0x478f3a4c = asyncio.create_task(self._0x4007296a(_0x654432d6))
                                self._0x5d1bb011.append(_0x478f3a4c)
                                self._0xd3a0bb01[_0x478f3a4c] = _0x654432d6
                            self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e656374696f6e2072656164792c207375627363726962656420746f2025642f2564206e6f74696669636174696f6e733a202573'), len(_0xcb982542), len(_0x909fe0f6), _0xcb982542)
                            self._0x7dc2142f(_0x185336ab)
                        else:
                            if self._0xb605ddfc:
                                self._0x3147b7f8(_0xd14e4b1f('5374617274696e6720474154542d6f6e6c7920696e697469616c2072656672657368'))
                                await self._0xba139b66(_0x266e0d3d)
                                self._0x3147b7f8(_0xd14e4b1f('474154542d6f6e6c7920696e697469616c207265667265736820636f6d706c657465642c207265616420256420636861726163746572697374696373'), len(self._0x84f90afc))
                            self._0xd4252973 = None
                            self._0xd8c19966.set()
                            self._0xc07eb575(self.data or {})
                            await self._0x8219d935()
                            self._0x7dc2142f(True)
                            self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e656374696f6e20726561647920696e202573206d6f646520776974686f757420426c653230206e6f74696669636174696f6e73'), self._0x44904414)
                    except asyncio.CancelledError:
                        try:
                            _0x266e0d3d.connection_status_changed_handlers -= self._0x0e8f8f97
                        except Exception:
                            pass
                        if self._0x084706dd is not _0x266e0d3d:
                            try:
                                await _0x266e0d3d.disconnect()
                            except Exception:
                                pass
                        raise
                    except Exception:
                        _0x266e0d3d.connection_status_changed_handlers -= self._0x0e8f8f97
                        try:
                            await _0x266e0d3d.disconnect()
                        except Exception:
                            pass
                        raise
            except Exception as _0x56bd7107:
                self._0x4b8f2e4e()
                if not self._0xe8e1c9b0:
                    self._0xe8e1c9b0 = True
                await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('636f6e6e656374696f6e206c6f6f702065737461626c6973682f7265636f766572206661696c757265'))
                await asyncio.sleep(10.0)

    async def _0x4007296a(self, _0x1da6b67b):
        (_0x32e2cb0f, _0x1801071a) = _0x726b25f9(_0x1da6b67b)
        try:
            if _0x1801071a is None:
                self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e206c697374656e6572207374617274656420666f722044704964202564'), _0x32e2cb0f)
            else:
                self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e206c697374656e6572207374617274656420666f72204470496420256420696e7374616e63653d2564'), _0x32e2cb0f, _0x1801071a)
            while True:
                (_, _0xdcf3e36e) = await self._0x7a63f2eb(_0x1da6b67b, _0x90272dda=None)
                (_, _0x7123a699, _0x3262d48d) = _0xbefb508d(_0xdcf3e36e, 1)
                _0x37dc56b4 = _0xdcf3e36e[_0x3262d48d:]
                _0xad054584 = self._0x18ad59bd(_0x32e2cb0f, _0x37dc56b4)
                if _0x7123a699 is None:
                    self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e2072656365697665643a2044704964202564202d3e202572'), _0x32e2cb0f, _0xad054584)
                else:
                    self._0x3147b7f8(_0xd14e4b1f('4e6f74696669636174696f6e2072656365697665643a204470496420256420696e7374616e63653d2564202d3e202572'), _0x32e2cb0f, _0x7123a699, _0xad054584)
                _0x70179363 = dict(self.data) if self.data else {}
                _0x958b30d4 = _0x1da6b67b
                if not self._0x60391626(_0xad054584):
                    self._0xdedd8ef4.pop(_0x958b30d4, None)
                    self._0x4250c6b6.pop(_0x958b30d4, None)
                    _0x70179363.pop(_0x958b30d4, None)
                    self._0x01fa193e(_0x32e2cb0f, _0x1801071a)
                else:
                    _0x426ea53d = _0x70179363.get(_0x958b30d4, _0x8a9cbaca)
                    if _0x426ea53d is not _0x8a9cbaca and _0x426ea53d == _0xad054584:
                        continue
                    self._0xdedd8ef4[_0x958b30d4] = _0x37dc56b4
                    self._0x4250c6b6[_0x958b30d4] = _0xd14e4b1f('6e6f74696679')
                    _0x70179363[_0x958b30d4] = _0xad054584
                (_0x70179363, _) = self._0x1d0c6f37(_0x70179363)
                self._0xc07eb575(_0x70179363, _0x52f1ba45=_0x5452b02e, _0x1cb60fd5=True)
        except asyncio.CancelledError:
            pass
        except Exception as _0x54d54a12:
            if _0x1801071a is None:
                pass
            if not self._0x3a821fc7:
                self._0x4b8f2e4e()
                self._0xd46304b0()

    async def _0x74dbe0ea(self, _0x40bea8d6=_0xd14e4b1f('756e737065636966696564')):
        self._0x255a5598()
        self._0x3147b7f8(_0xd14e4b1f('436c65616e696e672075702070657273697374656e7420424c4520636f6e6e656374696f6e2073746174652028726561736f6e3d257329'), _0x40bea8d6)
        for _0x478f3a4c in self._0x5d1bb011:
            _0x478f3a4c.cancel()
        if self._0x5d1bb011:
            await asyncio.gather(*self._0x5d1bb011, return_exceptions=True)
            self._0x5d1bb011.clear()
        self._0xd3a0bb01.clear()
        self._0xd4252973 = None
        if self._0x084706dd is not None:
            try:
                self._0x084706dd.connection_status_changed_handlers -= self._0x0e8f8f97
            except Exception:
                pass
            try:
                await self._0x084706dd.disconnect()
            except Exception:
                pass
            self._0x084706dd = None
        self._0x3147b7f8(_0xd14e4b1f('50657273697374656e7420424c4520636f6e6e656374696f6e20737461746520636c65616e65642075702028726561736f6e3d257329'), _0x40bea8d6)
        self._0xd46304b0()

    async def _0x848ba6b6(self, _0x958b30d4, _0x2063c160):
        (_0x32e2cb0f, _0x7123a699) = _0x726b25f9(_0x958b30d4)
        await self._0x175d2343(_0x32e2cb0f, _0x2063c160, _0x7123a699=_0x7123a699)

    async def _0x175d2343(self, _0x32e2cb0f, _0x2063c160, _0x7123a699=None):
        _0x653515c6 = self._0x0a23c6b4(_0x32e2cb0f, _0x2063c160, _0x7123a699=_0x7123a699)
        await self._0xf09e5941(_0x32e2cb0f, _0x653515c6, _0x7123a699=_0x7123a699, _0x065806cf=_0x2063c160)

    async def _0x3da39fe5(self, _0x32e2cb0f, _0x7f6f2cd1, _0x7123a699=None, _0x065806cf=_0x8a9cbaca):
        await self._0xf09e5941(_0x32e2cb0f, _0x7f6f2cd1, _0x7123a699=_0x7123a699, _0x065806cf=_0x065806cf)

    @device_log_context
    async def _0xf09e5941(self, _0x32e2cb0f, _0x653515c6, _0x7123a699=None, _0x065806cf=_0x8a9cbaca):
        if self._0xbb786552 or self._0x80c14035:
            raise UpdateFailed(_0xd14e4b1f('496e746567726174696f6e206973207368757474696e6720646f776e'))
        if self._0x5eda439f:
            raise UpdateFailed(_0xd14e4b1f('424c452061637469766974792069732074656d706f726172696c792070617573656420666f72206120636f6e6e656374696f6e2074657374'))
        if not self.poll_enabled:
            raise UpdateFailed(_0xd14e4b1f('436f6e6e656374696f6e20737769746368206973206f66663b20424c4520636f6e6e656374696f6e2069732066756c6c792072656c656173656420616e6420777269746573206172652064697361626c6564'))
        if not self._0x8dc7742e(_0x60810dad=True):
            try:
                await asyncio.wait_for(self._0xd8c19966.wait(), timeout=15.0)
            except asyncio.TimeoutError as _0x56bd7107:
                raise UpdateFailed(_0xd14e4b1f('50657273697374656e7420424c452073657373696f6e206e6f7420726561647920666f72207772697465')) from _0x56bd7107
        async with self._0xadbbed2f:
            if self._0xbb786552 or self._0x80c14035:
                raise UpdateFailed(_0xd14e4b1f('496e746567726174696f6e2073746172746564207368757474696e6720646f776e207768696c652077616974696e6720746f207772697465'))
            if self._0x5eda439f:
                raise UpdateFailed(_0xd14e4b1f('424c4520616374697669747920626563616d6520706175736564207768696c652077616974696e6720746f207772697465'))
            try:
                _0x7e35ea5c = await self._0x97956325(_0x32e2cb0f, _0x653515c6, _0x7123a699=_0x7123a699)
                self._0x69266e31(_0x7e35ea5c, _0x653515c6, _0x065806cf)
            except Exception as _0x56bd7107:
                self._0x4b8f2e4e()
                if not self._0x3a821fc7:
                    await self._0x74dbe0ea(_0x40bea8d6=f"{_0xd14e4b1f('7772697465206166746572207265616c20646973636f6e6e6563742064705f69643d')}{_0x32e2cb0f}")
                raise UpdateFailed(f"{_0xd14e4b1f('4661696c656420746f207772697465204470496420')}{_0x32e2cb0f}{_0xd14e4b1f('3a20')}{_0x56bd7107}") from _0x56bd7107

    def _0x69266e31(self, _0x958b30d4, _0x653515c6, _0x065806cf):
        if _0x065806cf is _0x8a9cbaca:
            return
        _0x70179363 = dict(self.data) if self.data else {}
        self._0xdedd8ef4[_0x958b30d4] = _0x653515c6
        self._0x4250c6b6[_0x958b30d4] = _0xd14e4b1f('7772697465')
        _0x70179363[_0x958b30d4] = _0x065806cf
        (_0x70179363, _) = self._0x1d0c6f37(_0x70179363)
        self._0xc07eb575(_0x70179363, _0x52f1ba45=_0xb98f4261)

    @device_log_context
    async def _0x29c17b19(self):
        self._0x80c14035 = True
        async with self._0xf6b7615e:
            await self._0x2928c4b4()

    async def _0x2928c4b4(self):
        self._0xbb786552 = True
        self._0x5eda439f = False
        if self._0x878b4eb8 is not None:
            self._0x878b4eb8.cancel()
            try:
                await self._0x878b4eb8
            except asyncio.CancelledError:
                pass
            self._0x878b4eb8 = None
        if self._0x49464da6 is not None:
            self._0x49464da6.cancel()
            try:
                await self._0x49464da6
            except asyncio.CancelledError:
                pass
            self._0x49464da6 = None
        if self._0xe68baedb is not None:
            self._0xe68baedb.cancel()
            try:
                await self._0xe68baedb
            except asyncio.CancelledError:
                pass
        if self._0xb41ecae5 is not None:
            self._0xb41ecae5.cancel()
            try:
                await self._0xb41ecae5
            except asyncio.CancelledError:
                pass
            self._0xe68baedb = None
            self._0xb41ecae5 = None
        try:
            await self._0x9308b7eb()
        except Exception as _0x56bd7107:
            pass
        if self._0x2ce69584:
            self._0x2ce69584()
            self._0x2ce69584 = None
        async with self._0xadbbed2f:
            await self._0x74dbe0ea(_0x40bea8d6=_0xd14e4b1f('696e746567726174696f6e2073687574646f776e'))