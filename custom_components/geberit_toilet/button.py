from __future__ import annotations

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
from dataclasses import dataclass
import logging
from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import UpdateFailed
from . import _0xa14eb14e
from .const import _0x042bca9f
from homeassistant.helpers.entity import EntityCategory
from .entity import _0x23fa9765, _0x6531dd07
from .metadata import _0xc9ed32a4
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x2c2ed43e = 0

@dataclass(frozen=True)
class _0x2cf30a00(ButtonEntityDescription):
    _0x261c7c15: str | None = None
_0xcac93ab3: tuple[_0x2cf30a00, ...] = (_0x2cf30a00(key=_0xd14e4b1f('6372656174655f7265706f7274'), translation_key=_0xd14e4b1f('6372656174655f7265706f7274'), _0x261c7c15=_0xd14e4b1f('6372656174655f7265706f7274'), icon=_0xd14e4b1f('6d64693a66696c652d646f63756d656e742d706c75732d6f75746c696e65')), _0x2cf30a00(key=_0xd14e4b1f('636f6d706172655f7265706f727473'), translation_key=_0xd14e4b1f('636f6d706172655f7265706f727473'), _0x261c7c15=_0xd14e4b1f('636f6d706172655f7265706f727473'), icon=_0xd14e4b1f('6d64693a66696c652d636f6d70617265')), _0x2cf30a00(key=_0xd14e4b1f('636c6561725f7265706f727473'), translation_key=_0xd14e4b1f('636c6561725f7265706f727473'), _0x261c7c15=_0xd14e4b1f('636c6561725f7265706f727473'), icon=_0xd14e4b1f('6d64693a66696c652d72656d6f76652d6f75746c696e65')), _0x2cf30a00(key=_0xd14e4b1f('636c6561725f646966666572656e636573'), translation_key=_0xd14e4b1f('636c6561725f646966666572656e636573'), _0x261c7c15=_0xd14e4b1f('636c6561725f646966666572656e636573'), icon=_0xd14e4b1f('6d64693a66696c652d646f63756d656e742d72656d6f76652d6f75746c696e65')))

def _0x30cc8bfa(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    for _0x1dee80c7 in _0xcac93ab3:
        _0xf5e638cc = _0xd6799119(_0xc4312c2a, _0x1043bfc7, _0x1dee80c7)
        if _0xf5e638cc.unique_id in _0x133edd70:
            continue
        _0x133edd70.add(_0xf5e638cc.unique_id)
        _0x07214c67.append(_0xf5e638cc)
    if _0xc4312c2a._0x1a94487b:
        for _0x32e2cb0f in _0xc4312c2a._0xe856d8fe:
            if not _0xc4312c2a._0x86b41222(_0x32e2cb0f):
                continue
            if _0xc4312c2a._0x512d0b0d(_0x32e2cb0f) != _0xc9ed32a4._0x57b35198:
                continue
            if _0x32e2cb0f not in _0xc4312c2a._0x3a3a4684:
                continue
            _0xf5e638cc = _0xbeda6769(_0xc4312c2a, _0x1043bfc7, _0x32e2cb0f)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0x30cc8bfa(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0xbeda6769(_0x23fa9765, ButtonEntity):

    def __init__(self, coordinator, entry, dp_id):
        self._0x762585fe = dp_id
        self._meta = coordinator._0xf1645e71(dp_id)
        self._0x5694d766 = 0 if self._meta._0x7123a699 > 0 else None
        self._attr_entity_category = self._meta.entity_category
        self._attr_entity_registry_enabled_default = self._meta.entity_registry_enabled_default
        super().__init__(coordinator, entry)
        _0x4ec1b477 = '' if self._0x5694d766 is None else f"{_0xd14e4b1f('5f696e7374616e63655f')}{self._0x5694d766}"
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f67656e657269635f')}{self._meta.key}{_0x4ec1b477}"
        self._attr_name = self._0xe2c147a6(self._0x762585fe, self._0x5694d766)

    @property
    def extra_state_attributes(self):
        _0x958b30d4 = self._0x762585fe if self._0x5694d766 is None else (self._0x762585fe, self._0x5694d766)
        _0x425ce871 = self._0x6323b8d8(self._0x762585fe, _0x958b30d4)
        if self._0x5694d766 is not None:
            _0x425ce871[_0xd14e4b1f('646174615f696e7374616e6365')] = self._0x5694d766
        return _0x425ce871

    async def async_press(self):
        _0x321c3cf4 = self.coordinator._0x16390971(self._0x762585fe, _0x7123a699=self._0x5694d766)
        await self.coordinator._0x3da39fe5(self._0x762585fe, _0x321c3cf4, _0x7123a699=self._0x5694d766)
        await self.coordinator.async_request_refresh()

class _0xd6799119(_0x23fa9765, ButtonEntity):
    entity_description: _0x2cf30a00

    def __init__(self, coordinator, entry, description):
        self.entity_description = description
        self._attr_entity_category = EntityCategory.CONFIG
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f')}{description.key}"

    @property
    def available(self):
        if self.entity_description._0x261c7c15 == _0xd14e4b1f('636f6d706172655f7265706f727473'):
            return len(self.coordinator._0x26e0440e) >= 2
        return True

    @property
    def extra_state_attributes(self):
        return self._0xc5fbb88f()

    async def async_press(self):
        _0x418c5509 = self.entity_description._0x261c7c15
        try:
            if _0x418c5509 == _0xd14e4b1f('6372656174655f7265706f7274'):
                _0xd6fe1d0b = await self.coordinator._0x9d135782()
                return
            if _0x418c5509 == _0xd14e4b1f('636f6d706172655f7265706f727473'):
                _0xd6fe1d0b = await self.coordinator._0xf9668b85()
                return
            if _0x418c5509 == _0xd14e4b1f('636c6561725f7265706f727473'):
                _0xda602f0b = await self.coordinator._0x6ab718b4()
                return
            if _0x418c5509 == _0xd14e4b1f('636c6561725f646966666572656e636573'):
                _0xda602f0b = await self.coordinator._0x6e4869fd()
                return
        except ValueError as _0x56bd7107:
            raise UpdateFailed(str(_0x56bd7107)) from _0x56bd7107
        raise UpdateFailed(f"{_0xd14e4b1f('556e737570706f7274656420646961676e6f7374696320616374696f6e3a20')}{_0x418c5509}")