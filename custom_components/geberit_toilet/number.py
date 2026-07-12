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
import logging
from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import _0xa14eb14e
from .const import _0x042bca9f
from .entity import _0x02109a59, _0x6531dd07
from .metadata import _0xc9ed32a4
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x2c2ed43e = 0

def _0x54bcf9f5(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    if _0xc4312c2a._0x1a94487b:
        for _0x958b30d4 in _0xc4312c2a._0xbc542398(_0xc9ed32a4._0x34f55eca):
            _0xf5e638cc = _0x80f26440(_0xc4312c2a, _0x1043bfc7, _0x958b30d4)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0x54bcf9f5(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0x80f26440(_0x02109a59, NumberEntity):

    def __init__(self, coordinator, entry, data_key):
        super().__init__(coordinator, entry, data_key)
        self._attr_native_min_value = float(self._meta._0x56dda363 or 0)
        self._attr_native_max_value = float(self._meta._0xc6a35ba1 if self._meta._0xc6a35ba1 is not None else 100)
        self._attr_native_step = 1.0

    @property
    def native_value(self):
        _0x3a6d0284 = self._0x510ef47b()
        return float(_0x3a6d0284) if _0x3a6d0284 is not None else None

    async def async_set_native_value(self, value):
        await self.coordinator._0x848ba6b6(self._data_key, int(value))