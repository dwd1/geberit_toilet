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
import logging
from typing import Any
from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorStateClass
from homeassistant.const import SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import _0xa14eb14e
from .const import _0x042bca9f
from .coordinator import _0x0409f5bf
from .entity import _0x02109a59, _0x23fa9765, _0x6531dd07
from .metadata import _0xc9ed32a4, _0x18c49331
from .protocol import _0x80bb1bf9
_LOGGER = _geberit_get_disabled_logger(__name__)
_0x2c2ed43e = 0

def _0x3c310977(_0xc4312c2a, _0x1043bfc7, _0x133edd70):
    _0x07214c67 = []
    if _0xc4312c2a._0x1a94487b:
        for _0x958b30d4 in _0xc4312c2a._0xbc542398(_0xc9ed32a4._0x72700b6a):
            _0xf5e638cc = _0xd362eeba(_0xc4312c2a, _0x1043bfc7, _0x958b30d4)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    if _0xc4312c2a._0xd90bbd0e:
        for (_0xef7c876f, _0x756bb351) in _0xc4312c2a._0x8dc7eed5.items():
            if not _0x756bb351._0x500f1c43:
                continue
            if _0xef7c876f not in _0xc4312c2a._0x0f7bd6f1 and _0xef7c876f not in _0xc4312c2a._0xfb7124c4:
                continue
            _0xf5e638cc = _0x7e046145(_0xc4312c2a, _0x1043bfc7, _0x756bb351)
            if _0xf5e638cc.unique_id in _0x133edd70:
                continue
            _0x133edd70.add(_0xf5e638cc.unique_id)
            _0x07214c67.append(_0xf5e638cc)
    _0x41d50f6f = _0x37748bdc(_0xc4312c2a, _0x1043bfc7)
    if _0x41d50f6f.unique_id not in _0x133edd70:
        _0x133edd70.add(_0x41d50f6f.unique_id)
        _0x07214c67.append(_0x41d50f6f)
    if _0xc4312c2a._0x1a77b829:
        _0xb9477b69 = _0xf6bfce9e(_0xc4312c2a, _0x1043bfc7)
        if _0xb9477b69.unique_id not in _0x133edd70:
            _0x133edd70.add(_0xb9477b69.unique_id)
            _0x07214c67.append(_0xb9477b69)
    return _0x07214c67

async def async_setup_entry(hass, entry, async_add_entities):
    _0xc4312c2a = entry.runtime_data
    _0x07214c67 = _0x6531dd07(_0xc4312c2a, async_add_entities, lambda known_unique_ids: _0x3c310977(_0xc4312c2a, entry, known_unique_ids))
    if _0x042bca9f:
        pass

class _0xd362eeba(_0x02109a59, SensorEntity):

    def __init__(self, coordinator, entry, data_key):
        super().__init__(coordinator, entry, data_key)
        self._attr_device_class = self._meta.sensor_device_class
        self._attr_native_unit_of_measurement = self._meta.unit
        self._attr_state_class = self._meta.sensor_state_class
        if self._meta._0x3931108d in (_0x340e827c._0x8f19a8c7, _0x340e827c._0xf670ea66, _0x340e827c._0x6a7e7316, _0x340e827c._0xadaaee4b, _0x340e827c._0xc442a6c2, _0x340e827c._0x71fed0c3, _0x340e827c._0x64d12922, _0x340e827c._0x127d04b8):
            self._attr_suggested_display_precision = 0

    @property
    def native_value(self):
        return _0x18c49331(self._meta, self._0x510ef47b(), _0x2716a391=self.coordinator._0x57023259())

class _0x7e046145(_0x23fa9765, SensorEntity):

    def __init__(self, coordinator, entry, runtime_char):
        self._runtime_char = runtime_char
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_entity_registry_enabled_default = runtime_char.entity_registry_enabled_default
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f676174745f')}{runtime_char.key}"
        self._attr_name = runtime_char.name
        if runtime_char._0x3a6bdba8 == _0xd14e4b1f('75696e7431365f6c65'):
            self._attr_suggested_display_precision = 0

    @property
    def native_value(self):
        return self.coordinator._0xfb7124c4.get(self._runtime_char.uuid)

    @property
    def extra_state_attributes(self):
        _0x7f6f2cd1 = self.coordinator._0x0f7bd6f1.get(self._runtime_char.uuid)
        _0x425ce871 = {_0xd14e4b1f('676174745f75756964'): self._runtime_char.uuid, _0xd14e4b1f('676174745f736572766963655f75756964'): self._runtime_char._0x10c1ecca, _0xd14e4b1f('676174745f736572766963655f6e616d65'): self._runtime_char._0xd505dfd5, _0xd14e4b1f('676174745f6b6579'): self._runtime_char.key, _0xd14e4b1f('676174745f736f75726365'): self._runtime_char._0x36cd38f4, _0xd14e4b1f('676174745f70726f70657274696573'): list(self._runtime_char.properties), _0xd14e4b1f('676174745f7265616461626c65'): self._runtime_char._0x500f1c43, _0xd14e4b1f('676174745f7772697461626c65'): self._runtime_char._0xc83e24cd, _0xd14e4b1f('676174745f6e6f7469666961626c65'): self._runtime_char._0x09f821ba, _0xd14e4b1f('676174745f696e646963617461626c65'): self._runtime_char._0xdecb0dc3}
        if _0x7f6f2cd1 is not None:
            _0x425ce871[_0xd14e4b1f('676174745f7261775f686578')] = _0x7f6f2cd1.hex()
        if self._runtime_char.descriptors:
            _0x425ce871[_0xd14e4b1f('676174745f64657363726970746f7273')] = list(self._runtime_char.descriptors)
        return _0x425ce871

class _0x37748bdc(_0x23fa9765, SensorEntity):

    def __init__(self, coordinator, entry):
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_entity_registry_enabled_default = True
        self._attr_device_class = SensorDeviceClass.SIGNAL_STRENGTH
        self._attr_native_unit_of_measurement = SIGNAL_STRENGTH_DECIBELS_MILLIWATT
        self._attr_state_class = SensorStateClass.MEASUREMENT
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f626c655f72737369')}"
        self._attr_name = _0xd14e4b1f('424c452052535349')
        _0x8082663a = self._device_id.replace(_0xd14e4b1f('3a'), _0xd14e4b1f('5f')).lower()
        self.entity_id = f"{_0xd14e4b1f('73656e736f722e676562657269745f746f696c65745f')}{_0x8082663a}{_0xd14e4b1f('5f626c655f72737369')}"

    @property
    def native_value(self):
        return self.coordinator._0x9ddac438

class _0xf6bfce9e(_0x23fa9765, SensorEntity):

    def __init__(self, coordinator, entry):
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_entity_registry_enabled_default = True
        self._attr_device_class = SensorDeviceClass.SIGNAL_STRENGTH
        self._attr_native_unit_of_measurement = SIGNAL_STRENGTH_DECIBELS_MILLIWATT
        self._attr_state_class = SensorStateClass.MEASUREMENT
        super().__init__(coordinator, entry)
        self._attr_unique_id = f"{self._device_id}{_0xd14e4b1f('5f657370686f6d655f776966695f72737369')}"
        self._attr_name = _0xd14e4b1f('455350486f6d6520576946692052535349')
        _0x8082663a = self._device_id.replace(_0xd14e4b1f('3a'), _0xd14e4b1f('5f')).lower()
        self.entity_id = f"{_0xd14e4b1f('73656e736f722e676562657269745f746f696c65745f')}{_0x8082663a}{_0xd14e4b1f('5f657370686f6d655f776966695f72737369')}"

    @property
    def native_value(self):
        return self.coordinator._0x70b8e2d2