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
from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
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

def _0xff3a2f1a(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    for _0xf5e638cc in (_0x225d8b6c(_0xc4312c2a, _0x1043bfc7), _0xc16ed144(_0xc4312c2a, _0x1043bfc7)):
        if _0xf5e638cc.unique_id in _0x133edd70:
            continue
        _0x133edd70.add(_0xf5e638cc.unique_id)
        _0x07214c67.append(_0xf5e638cc)
    if _0xc4312c2a._0x1a94487b:
        for _0x958b30d4 in _0xc4312c2a._0xbc542398(_0xc9ed32a4._0x9dc7bd04):
            _0xf5e638cc = _0x9a198cfa(_0xc4312c2a, _0x1043bfc7, _0x958b30d4)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0xff3a2f1a(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0x225d8b6c(_0x23fa9765, BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY
    _attr_translation_key = _0xd14e4b1f('626c655f636f6e6e656374696f6e')
    _attr_icon = _0xd14e4b1f('6d64693a626c7565746f6f74682d636f6e6e656374')
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f626c655f636f6e6e656374696f6e')}"

    @property
    def is_on(self):
        return self.coordinator._0x3a821fc7

    @property
    def extra_state_attributes(self):
        return self._0xc5fbb88f()

class _0xc16ed144(_0x23fa9765, BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_translation_key = _0xd14e4b1f('696e746567726174696f6e5f7265616479')
    _attr_icon = _0xd14e4b1f('6d64693a636865636b2d636972636c652d6f75746c696e65')
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator, entry):
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f696e746567726174696f6e5f7265616479')}"

    @property
    def is_on(self):
        return self.coordinator._0xd92c6474

    @property
    def extra_state_attributes(self):
        return self._0xc5fbb88f()

class _0x9a198cfa(_0x01e56675, BinarySensorEntity):

    def __init__(self, coordinator, entry, data_key):
        super().__init__(coordinator, entry, data_key)
        self._attr_device_class = self._meta._0xe84e5b08