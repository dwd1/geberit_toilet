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
from typing import Any
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import _0xa14eb14e
from .const import _0x042bca9f
from homeassistant.helpers.entity import EntityCategory
from .coordinator import _0x0409f5bf
from .entity import _0x01e56675, _0x23fa9765, _0x6531dd07
from .metadata import _0xc9ed32a4
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x2c2ed43e = 0

def _0xeaa6a933(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    _0xf5e638cc = _0x6779657f(_0xc4312c2a, _0x1043bfc7)
    if _0xf5e638cc.unique_id not in _0x133edd70:
        _0x133edd70.add(_0xf5e638cc.unique_id)
        _0x07214c67.append(_0xf5e638cc)
    if _0xc4312c2a._0x1a94487b:
        for _0x958b30d4 in _0xc4312c2a._0xbc542398(_0xc9ed32a4._0x4239f063):
            _0xf5e638cc = _0x4fe06c7b(_0xc4312c2a, _0x1043bfc7, _0x958b30d4)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0xeaa6a933(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0x6779657f(_0x23fa9765, SwitchEntity):
    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f636f6e6e656374696f6e')}"
        self._attr_translation_key = _0xd14e4b1f('626c655f636f6e6e656374696f6e')
        self._attr_icon = _0xd14e4b1f('6d64693a626c7565746f6f74682d636f6e6e656374')

    @property
    def is_on(self):
        return self.coordinator.poll_enabled

    async def async_turn_on(self, **kwargs):
        await self.coordinator._0x111bbd40()
        self.async_write_ha_state()
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        await self.coordinator._0x30ffb15e()
        self.async_write_ha_state()

    @property
    def extra_state_attributes(self):
        return self._0xc5fbb88f()

class _0x4fe06c7b(_0x01e56675, SwitchEntity):

    def __init__(self, coordinator, entry, data_key):
        super().__init__(coordinator, entry, data_key)

    async def async_turn_on(self, **kwargs):
        await self.coordinator._0x848ba6b6(self._data_key, True)

    async def async_turn_off(self, **kwargs):
        await self.coordinator._0x848ba6b6(self._data_key, False)