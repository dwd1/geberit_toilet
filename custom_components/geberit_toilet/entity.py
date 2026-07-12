from __future__ import annotations
from .protocol import _0x77301576, _0x4da742b9

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
import logging
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from . import _0xa14eb14e
from .const import _0xcff93a68, _0xbf7c9959
from .coordinator import _0x0409f5bf, _0x726b25f9
from .device_types import _0x5e1748ef
from .DpId import DpId
_LOGGER = _geberit_get_disabled_logger(__name__)

def _0x6531dd07(_0xc4312c2a, _0x60b92ca7, _0x91e3a7ff):
    _0x133edd70 = set()

    def _0x05baa0a4():
        _0x07214c67 = _0x91e3a7ff(_0x133edd70)
        if _0x07214c67:
            _0x60b92ca7(_0x07214c67)
        return _0x07214c67
    _0x7fdc5ec2 = _0x05baa0a4()
    _0xc4312c2a._0xd7644488(_0x05baa0a4)
    return _0x7fdc5ec2

class _0x23fa9765(CoordinatorEntity[_0x0409f5bf]):
    _attr_has_entity_name = True
    _0x40adab5a = _0xd14e4b1f('5468697320697320616e20696e7465726e616c20656e74697479206f6620746865204765626572697420546f696c657420696e746567726174696f6e2e')

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._0x5f3f26ad = entry
        self._device_id = entry.data[_0xcff93a68]
        self._0x94bf2e69 = None

    @property
    def available(self):
        if self.unique_id in (f"{self._device_id}{_0xd14e4b1f('5f636f6e6e656374696f6e')}", f"{self._device_id}{_0xd14e4b1f('5f626c655f636f6e6e656374696f6e')}", f"{self._device_id}{_0xd14e4b1f('5f696e746567726174696f6e5f7265616479')}"):
            return super().available
        return self.coordinator._0x3a821fc7 and super().available

    @property
    def entity_category(self):
        if hasattr(self, _0xd14e4b1f('5f617474725f656e746974795f63617465676f7279')):
            return self._attr_entity_category
        if getattr(self, _0xd14e4b1f('656e746974795f6465736372697074696f6e'), None) is not None:
            return self.entity_description.entity_category
        if hasattr(self, _0xd14e4b1f('5f6d657461')) and self._meta is not None:
            return self._meta.entity_category
        return None

    @property
    def device_info(self):
        _0xa08cee2d = self.coordinator._0xf096db62(0)
        _0x444abb90 = self.coordinator._0xf096db62(1)
        _0x20f35e63 = _0x5e1748ef(_0xa08cee2d, _0x444abb90)
        _0xb068931c = _0x20f35e63
        _0x4450a055 = getattr(dr, _0xd14e4b1f('434f4e4e454354494f4e5f424c5545544f4f5448'), _0xd14e4b1f('626c7565746f6f7468'))
        return DeviceInfo(identifiers={(_0xbf7c9959, self._device_id)}, connections={(_0x4450a055, self._device_id)}, name=_0xb068931c, manufacturer=_0xd14e4b1f('47656265726974'), model=_0x20f35e63)

    def _0x6323b8d8(self, _0x32e2cb0f, _0x958b30d4=None):
        _0xe9a23cbc = self.coordinator._0xf1645e71(_0x32e2cb0f)
        if _0xe9a23cbc is None:
            return {}
        _0x425ce871 = {_0xd14e4b1f('64705f6964'): int(_0xe9a23cbc._0x32e2cb0f), _0xd14e4b1f('64705f6b6579'): _0xe9a23cbc.key, _0xd14e4b1f('64705f6461746174797065'): _0x4da742b9(_0xe9a23cbc._0x3931108d) if _0xe9a23cbc._0x3931108d is not None else None, _0xd14e4b1f('64705f6265686176696f72'): _0x77301576(_0xe9a23cbc._0xb140af3d) if _0xe9a23cbc._0xb140af3d is not None else None, _0xd14e4b1f('64705f7265616461626c65'): _0xe9a23cbc._0x500f1c43, _0xd14e4b1f('64705f7772697461626c65'): _0xe9a23cbc._0xc83e24cd, _0xd14e4b1f('64705f6e6f7469666961626c65'): _0xe9a23cbc._0x09f821ba, _0xd14e4b1f('64705f7570646174655f6d6f6465'): self.coordinator._0x5eb74917(_0x958b30d4) if _0x958b30d4 is not None else self.coordinator._0xa1aaa9f2(_0xe9a23cbc._0x32e2cb0f), _0xd14e4b1f('64705f6d696e'): _0xe9a23cbc._0x56dda363, _0xd14e4b1f('64705f6d6178'): _0xe9a23cbc._0xc6a35ba1, _0xd14e4b1f('64705f76657273696f6e'): _0xe9a23cbc._0x2af72f10, _0xd14e4b1f('64705f696e7374616e6365'): _0xe9a23cbc._0x7123a699}
        if _0xe9a23cbc._0x67daf92c:
            _0x425ce871[_0xd14e4b1f('64705f6465736372697074696f6e')] = _0xe9a23cbc._0x67daf92c
        _0x7f4be311 = self.coordinator._0x7f4be311
        if _0x7f4be311 is not None:
            _0x425ce871[_0xd14e4b1f('70726f66696c655f6b6579')] = _0x7f4be311
        _0x5d002cd2 = self.coordinator._0x971a9022(_0xe9a23cbc.key)
        if _0x5d002cd2 is not None:
            _0x425ce871[_0xd14e4b1f('64705f656e61626c65645f696e5f70726f66696c65')] = _0x5d002cd2
        if _0xe9a23cbc.options:
            _0x425ce871[_0xd14e4b1f('64705f6f7074696f6e73')] = list(_0xe9a23cbc.options)
        return _0x425ce871

    def _0x582d160d(self, _0x32e2cb0f, _0x7123a699):
        if _0x7123a699 != 0 or _0x32e2cb0f is None:
            return False
        _0x42aefbae = int(_0x32e2cb0f)
        _0x2c51de0c = []
        for _0x958b30d4 in self.coordinator.data or {}:
            (_0xd3fd2d82, _) = _0x726b25f9(_0x958b30d4)
            if _0xd3fd2d82 != _0x42aefbae:
                continue
            _0x2c51de0c.append(_0x958b30d4)
        if len(_0x2c51de0c) != 1:
            return False
        _0x9ba024ca = _0x2c51de0c[0]
        (_, _0x58e8d35a) = _0x726b25f9(_0x9ba024ca)
        return _0x58e8d35a == 0

    def _0xe2c147a6(self, _0x32e2cb0f, _0x7123a699=None):
        _0xe9a23cbc = self.coordinator._0xf1645e71(_0x32e2cb0f)
        _0xb068931c = self.coordinator._0xf1dfc2fd(_0xe9a23cbc)
        if _0xb068931c is None or _0x7123a699 is None or self._0x582d160d(_0x32e2cb0f, _0x7123a699):
            return _0xb068931c
        if _0xe9a23cbc and _0xe9a23cbc._0x4ad9a0ea and (_0x7123a699 < len(_0xe9a23cbc._0x4ad9a0ea)):
            _0x6a2622a0 = _0xe9a23cbc._0x4ad9a0ea[_0x7123a699]
            if _0x6a2622a0:
                return f"{_0xb068931c}{_0xd14e4b1f('20')}{_0x6a2622a0}"
        return f"{_0xb068931c}{_0xd14e4b1f('20496e7374616e636520')}{_0x7123a699}"

    def _0xc5fbb88f(self):
        return {_0xd14e4b1f('696e746567726174696f6e5f656e746974795f6e6f7465'): self._0x40adab5a}

    def _0x258252c1(self):
        _0x958b30d4 = getattr(self, _0xd14e4b1f('5f646174615f6b6579'), None)
        if _0x958b30d4 is not None:
            return str(_0x958b30d4)
        _0x756bb351 = getattr(self, _0xd14e4b1f('5f72756e74696d655f63686172'), None)
        if _0x756bb351 is not None:
            return f"{_0xd14e4b1f('676174743a')}{_0x756bb351.key}"
        _0x69080cee = getattr(self, _0xd14e4b1f('756e697175655f6964'), None)
        return str(_0x69080cee)

    def _0xf5299cc6(self):
        for _0x2b9331d0 in (_0xd14e4b1f('6e61746976655f76616c7565'), _0xd14e4b1f('69735f6f6e'), _0xd14e4b1f('63757272656e745f6f7074696f6e')):
            if not hasattr(type(self), _0x2b9331d0):
                continue
            try:
                _0x2063c160 = getattr(self, _0x2b9331d0)
            except Exception as _0x56bd7107:
                return f"{_0xd14e4b1f('3c6572726f722072656164696e6720')}{_0x2b9331d0}{_0xd14e4b1f('3a20')}{_0x56bd7107}{_0xd14e4b1f('3e')}"
            return repr(_0x2063c160)
        return _0xd14e4b1f('3c6e6f2d73746174652d70726f70657274793e')

    def _0x48ddd378(self):
        _0x958b30d4 = getattr(self, _0xd14e4b1f('5f646174615f6b6579'), None)
        if _0x958b30d4 is not None:
            if not self.coordinator.data:
                return _0xd14e4b1f('636f6f7264696e61746f722e6461746120697320656d707479')
            if _0x958b30d4 not in self.coordinator.data:
                return f"{_0xd14e4b1f('64617461206b6579206d697373696e672066726f6d20636f6f7264696e61746f722e646174613a20')}{_0x958b30d4}"
            return _0xd14e4b1f('73746174652070726f7065727479207265736f6c76656420746f204e6f6e65')
        _0x756bb351 = getattr(self, _0xd14e4b1f('5f72756e74696d655f63686172'), None)
        if _0x756bb351 is not None:
            if _0x756bb351.uuid not in self.coordinator._0x0f7bd6f1 and _0x756bb351.uuid not in self.coordinator._0xfb7124c4:
                return f"{_0xd14e4b1f('67617474206b6579206d697373696e673a20')}{_0x756bb351.key}"
            return _0xd14e4b1f('676174742073746174652070726f7065727479207265736f6c76656420746f204e6f6e65')
        if self.unique_id == f"{self._device_id}{_0xd14e4b1f('5f626c655f636f6e6e656374696f6e')}":
            return f"{_0xd14e4b1f('626c655f636f6e6e65637465643d')}{self.coordinator._0x3a821fc7}"
        if self.unique_id == f"{self._device_id}{_0xd14e4b1f('5f696e746567726174696f6e5f7265616479')}":
            return f"{_0xd14e4b1f('696e746567726174696f6e5f72656164793d')}{self.coordinator._0xd92c6474}{_0xd14e4b1f('20706f6c6c5f656e61626c65643d')}{self.coordinator.poll_enabled}{_0xd14e4b1f('20626c655f636f6e6e65637465643d')}{self.coordinator._0x3a821fc7}"
        return _0xd14e4b1f('656e74697479207265706f7274656420756e617661696c61626c65')

    def _0x4b800a5d(self):
        try:
            _0xe4894ca1 = bool(self.available)
        except Exception as _0x56bd7107:
            return
        if _0xe4894ca1:
            _0x951da6b7 = self._0xf5299cc6()
        else:
            _0x951da6b7 = self._0x48ddd378()
        _0xac201fd2 = (_0xe4894ca1, _0x951da6b7)
        if _0xac201fd2 == self._0x94bf2e69:
            return
        self._0x94bf2e69 = _0xac201fd2

    def _handle_coordinator_update(self):
        self._0x4b800a5d()
        super()._handle_coordinator_update()

class _0x02109a59(_0x23fa9765):

    def __init__(self, coordinator, entry, data_key):
        self._data_key = data_key
        (self._0x762585fe, self._0x5694d766) = _0x726b25f9(data_key)
        self._meta = coordinator._0xf1645e71(self._0x762585fe)
        if self._meta is None:
            raise ValueError(f"{_0xd14e4b1f('4d697373696e67206d6574616461746120666f72204470496420')}{self._0x762585fe}")
        self._attr_entity_category = self._meta.entity_category
        self._attr_entity_registry_enabled_default = self._meta.entity_registry_enabled_default
        super().__init__(coordinator, entry)
        _0x4ec1b477 = '' if self._0x5694d766 is None else f"{_0xd14e4b1f('5f696e7374616e63655f')}{self._0x5694d766}"
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f67656e657269635f')}{self._meta.key}{_0x4ec1b477}"
        self._attr_name = self._0xe2c147a6(self._0x762585fe, self._0x5694d766)

    def _0x510ef47b(self):
        if not self.coordinator.data:
            return None
        if self._0x5694d766 is None:
            return self.coordinator._0xf096db62(self._0x762585fe)
        return self.coordinator.data.get(self._data_key)

    @property
    def extra_state_attributes(self):
        _0x425ce871 = self._0x6323b8d8(self._0x762585fe, self._data_key)
        _0x425ce871[_0xd14e4b1f('64705f6c6173745f7570646174655f736f75726365')] = self.coordinator._0x351f8a4d(self._data_key)
        if self._0x5694d766 is not None:
            _0x425ce871[_0xd14e4b1f('646174615f696e7374616e6365')] = self._0x5694d766
        return _0x425ce871

class _0x01e56675(_0x02109a59):

    @property
    def is_on(self):
        _0x2063c160 = self._0x510ef47b()
        return bool(_0x2063c160) if _0x2063c160 is not None else None

    async def async_update(self):
        pass