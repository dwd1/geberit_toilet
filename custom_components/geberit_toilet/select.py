from __future__ import annotations
from .protocol import _0x340e827c

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
from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import _0xa14eb14e
from .const import _0x042bca9f
from .coordinator import _0x0409f5bf
from homeassistant.helpers.entity import EntityCategory
from .entity import _0x02109a59, _0x23fa9765, _0x726b25f9, _0x6531dd07
from .metadata import _0xc9ed32a4
from .DpId import DpId
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x2c2ed43e = 0

@dataclass(frozen=True)
class _0xdb9732c9(SelectEntityDescription):
    _0x32e2cb0f: DpId | None = None
    _0x261c7c15: str | None = None
_0x617030d6: tuple[_0xdb9732c9, ...] = (_0xdb9732c9(key=_0xd14e4b1f('7265706f72745f6c656674'), translation_key=_0xd14e4b1f('7265706f72745f6c656674'), _0x261c7c15=_0xd14e4b1f('7265706f72745f6c656674'), icon=_0xd14e4b1f('6d64693a66696c652d646f63756d656e742d6f75746c696e65')), _0xdb9732c9(key=_0xd14e4b1f('7265706f72745f7269676874'), translation_key=_0xd14e4b1f('7265706f72745f7269676874'), _0x261c7c15=_0xd14e4b1f('7265706f72745f7269676874'), icon=_0xd14e4b1f('6d64693a66696c652d646f63756d656e742d6f75746c696e65')))

def _0x492ec201(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    for _0x1dee80c7 in _0x617030d6:
        if _0x1dee80c7._0x261c7c15 is None:
            continue
        _0xf5e638cc = _0xe2417442(_0xc4312c2a, _0x1043bfc7, _0x1dee80c7)
        if _0xf5e638cc.unique_id in _0x133edd70:
            continue
        _0x133edd70.add(_0xf5e638cc.unique_id)
        _0x07214c67.append(_0xf5e638cc)
    if _0xc4312c2a._0x1a94487b:
        for _0x958b30d4 in _0xc4312c2a._0xbc542398(_0xc9ed32a4._0x63225f19):
            (_0x32e2cb0f, _) = _0x726b25f9(_0x958b30d4)
            _0xe9a23cbc = _0xc4312c2a._0xe856d8fe.get(_0x32e2cb0f)
            _0x93da65a9 = _0xe9a23cbc.options_for_select()
            if not _0x93da65a9:
                continue
            _0xf5e638cc = _0x581a2311(_0xc4312c2a, _0x1043bfc7, _0x958b30d4, list(_0x93da65a9))
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0x492ec201(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0x581a2311(_0x02109a59, SelectEntity):

    def __init__(self, coordinator, entry, data_key, options):
        super().__init__(coordinator, entry, data_key)
        self._attr_options = options

    @property
    def current_option(self):
        _0x3a6d0284 = self._0x510ef47b()
        if _0x3a6d0284 is None:
            return None
        try:
            _0x7f9bec28 = int(_0x3a6d0284)
        except (TypeError, ValueError):
            return None
        if 0 <= _0x7f9bec28 < len(self._attr_options):
            return self._attr_options[_0x7f9bec28]
        _0xef3e30e0 = str(_0x7f9bec28)
        return _0xef3e30e0 if _0xef3e30e0 in self._attr_options else None

    async def async_select_option(self, option):
        if option not in self._attr_options:
            raise ValueError(f"{_0xd14e4b1f('496e76616c6964206f7074696f6e3a20')}{option}")
        if self._meta.options or self._meta._0x3931108d == _0x340e827c._0x471c4cee:
            _0x2063c160 = self._attr_options.index(option)
        else:
            _0x2063c160 = int(option)
        await self.coordinator._0x848ba6b6(self._data_key, _0x2063c160)

class _0xe2417442(_0x23fa9765, SelectEntity):
    entity_description: _0xdb9732c9

    def __init__(self, coordinator, entry, description):
        super().__init__(coordinator, entry)
        self.entity_description = description
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f')}{description.key}"

    @property
    def options(self):
        if self.entity_description._0x261c7c15 == _0xd14e4b1f('7265706f72745f6c656674'):
            return self.coordinator._0x94131d13
        return self.coordinator._0x70308f6c

    @property
    def current_option(self):
        if self.entity_description._0x261c7c15 == _0xd14e4b1f('7265706f72745f6c656674'):
            return self.coordinator._0x555427b0
        return self.coordinator._0xfac3be13

    @property
    def available(self):
        return len(self.options) > 0

    @property
    def extra_state_attributes(self):
        return self._0xc5fbb88f()

    async def async_select_option(self, option):
        if option not in self.options:
            raise ValueError(f"{_0xd14e4b1f('496e76616c6964207265706f72742066696c653a20')}{option}")
        if self.entity_description._0x261c7c15 == _0xd14e4b1f('7265706f72745f6c656674'):
            await self.coordinator._0x4fc51951(option)
        else:
            await self.coordinator._0x6060d761(option)