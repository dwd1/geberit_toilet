from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorEntityDescription, SensorStateClass
from homeassistant.const import PERCENTAGE, UnitOfElectricPotential
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .metadata import EntityKind, metadata_value_to_native
from .protocol.DpId import DpId
from .protocol.DpType import DpType
from .protocol.GattIdentifiers import RuntimeGattCharacteristic

@dataclass(frozen=True)
class GeberitToiletSensorDescription(SensorEntityDescription):
    dp_id: DpId | tuple[DpId, int] | None = None
    value_fn: Callable[[Any], Any] | None = None

def safe_hex(val: Any) -> str | None:
    if val is None:
        return None
    if isinstance(val, bytes):
        return val.hex().upper()
    try:
        return hex(int(val))[2:].upper()
    except (ValueError, TypeError):
        return str(val)
SENSOR_TYPES: tuple[GeberitToiletSensorDescription, ...] = (GeberitToiletSensorDescription(key='battery_level', dp_id=DpId.DP_BATTERY_LEVEL, native_unit_of_measurement=PERCENTAGE, device_class=SensorDeviceClass.BATTERY, state_class=SensorStateClass.MEASUREMENT), GeberitToiletSensorDescription(key='supply_voltage', dp_id=DpId.DP_SUPPLY_VOLTAGE, native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, value_fn=lambda x: x / 1000.0 if x is not None else None), GeberitToiletSensorDescription(key='distance', dp_id=DpId.DP_SENSOR_DISTANCE_STATUS, native_unit_of_measurement='mm', state_class=SensorStateClass.MEASUREMENT), GeberitToiletSensorDescription(key='idc_id_hash', dp_id=DpId.DP_IDC_ID_HASH, value_fn=safe_hex))

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[SensorEntity] = []
    claimed_data_keys = {desc.dp_id for desc in SENSOR_TYPES if desc.dp_id is not None}
    data = coordinator.data or {}
    for desc in SENSOR_TYPES:
        if desc.dp_id is None or not coordinator.should_expose_data_key_as_entity(desc.dp_id):
            continue
        if data.get(desc.dp_id) is not None:
            entities.append(GeberitToiletSensor(coordinator, entry, desc))
    for (data_key, value) in data.items():
        if value is None or data_key in claimed_data_keys:
            continue
        if not coordinator.should_expose_data_key_as_entity(data_key):
            continue
        dp_id = int(data_key[0] if isinstance(data_key, tuple) else data_key)
        meta = coordinator.dp_metadata.get(dp_id)
        if meta is None or meta.hidden or meta.preferred_kind != EntityKind.SENSOR:
            continue
        entities.append(GeberitToiletGenericSensor(coordinator, entry, data_key))
    for (uuid, runtime_char) in coordinator.gatt_characteristics.items():
        if runtime_char.hidden or not runtime_char.readable:
            continue
        if uuid not in coordinator.gatt_raw_values:
            continue
        entities.append(GeberitToiletGattSensor(coordinator, entry, runtime_char))
    async_add_entities(entities)

class GeberitToiletSensor(GeberitToiletEntity, SensorEntity):
    entity_description: GeberitToiletSensorDescription

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, description: GeberitToiletSensorDescription) -> None:
        super().__init__(coordinator, entry)
        self.entity_description = description
        self._attr_unique_id = f'{self._device_id}_{description.key}'
        self._attr_name = self._metadata_display_name(description.dp_id)

    @property
    def native_value(self) -> Any:
        data = self.coordinator.data
        if not data or self.entity_description.dp_id not in data:
            return None
        val = data[self.entity_description.dp_id]
        if self.entity_description.value_fn:
            return self.entity_description.value_fn(val)
        return val

class GeberitToiletGenericSensor(GeberitToiletEntity, SensorEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, data_key: int | tuple[int, int]) -> None:
        super().__init__(coordinator, entry)
        self._data_key = data_key
        self._dp_id = int(data_key[0] if isinstance(data_key, tuple) else data_key)
        self._instance = data_key[1] if isinstance(data_key, tuple) else None
        self._meta = coordinator.get_dp_metadata(self._dp_id)
        suffix = '' if self._instance is None else f'_instance_{self._instance}'
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}{suffix}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta) if self._instance is None else f'{self.coordinator.localize_metadata_name(self._meta)} Instance {self._instance}'
        self._attr_device_class = self._meta.sensor_device_class
        self._attr_native_unit_of_measurement = self._meta.unit
        self._attr_state_class = self._meta.sensor_state_class
        self._attr_entity_category = self._meta.entity_category
        self._attr_entity_registry_enabled_default = self._meta.entity_registry_enabled_default
        if self._meta.datatype in (DpType.Seconds, DpType.Minutes, DpType.Hours, DpType.Percent, DpType.Permill, DpType.Signed, DpType.Counter, DpType.MilliSeconds):
            self._attr_suggested_display_precision = 0

    @property
    def native_value(self) -> Any:
        data = self.coordinator.data
        if not data or self._data_key not in data:
            return None
        return metadata_value_to_native(self._meta, data[self._data_key])

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        attrs = self._metadata_attributes(self._dp_id)
        if self._instance is not None:
            attrs['data_instance'] = self._instance
        return attrs

class GeberitToiletGattSensor(GeberitToiletEntity, SensorEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, runtime_char: RuntimeGattCharacteristic) -> None:
        super().__init__(coordinator, entry)
        self._runtime_char = runtime_char
        self._attr_unique_id = f'{self._device_id}_gatt_{runtime_char.key}'
        self._attr_name = runtime_char.name
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_entity_registry_enabled_default = runtime_char.entity_registry_enabled_default
        if runtime_char.decoder == 'uint16_le':
            self._attr_suggested_display_precision = 0

    @property
    def native_value(self) -> Any:
        return self.coordinator.gatt_decoded_values.get(self._runtime_char.uuid)

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        raw_value = self.coordinator.gatt_raw_values.get(self._runtime_char.uuid)
        attrs: dict[str, object] = {'gatt_uuid': self._runtime_char.uuid, 'gatt_service_uuid': self._runtime_char.service_uuid, 'gatt_service_name': self._runtime_char.service_name, 'gatt_key': self._runtime_char.key, 'gatt_source': self._runtime_char.source, 'gatt_properties': list(self._runtime_char.properties), 'gatt_readable': self._runtime_char.readable, 'gatt_writable': self._runtime_char.writable, 'gatt_notifiable': self._runtime_char.notifiable, 'gatt_indicatable': self._runtime_char.indicatable}
        if raw_value is not None:
            attrs['gatt_raw_hex'] = raw_value.hex()
        if self._runtime_char.descriptors:
            attrs['gatt_descriptors'] = list(self._runtime_char.descriptors)
        return attrs
