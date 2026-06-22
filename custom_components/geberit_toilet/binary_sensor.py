from __future__ import annotations
from datetime import timedelta
from typing import Any
from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .metadata import EntityKind

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[BinarySensorEntity] = []
    entities.append(GeberitToiletConnectionSensor(coordinator, entry))
    entities.append(GeberitToiletIntegrationReadySensor(coordinator, entry))
    for (dp_id, meta) in coordinator.dp_metadata.items():
        if not coordinator.should_expose_dp_id_as_entity(dp_id):
            continue
        if meta.hidden or meta.preferred_kind != EntityKind.BINARY_SENSOR:
            continue
        if coordinator.data and coordinator.data.get(dp_id) is not None:
            entities.append(GeberitToiletGenericBinarySensor(coordinator, entry, dp_id))
    async_add_entities(entities)

class GeberitToiletConnectionSensor(GeberitToiletEntity, BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY
    _attr_translation_key = 'ble_connection'
    _attr_icon = 'mdi:bluetooth-connect'

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{self._device_id}_ble_connection'
        self._last_state: bool | None = None
        self._unsub_timer: Any = None

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._unsub_timer = async_track_time_interval(self.hass, self._check_connection_state, timedelta(seconds=2))

    async def async_will_remove_from_hass(self) -> None:
        if self._unsub_timer:
            self._unsub_timer()
            self._unsub_timer = None

    @callback
    def _check_connection_state(self, _now=None) -> None:
        current = self.coordinator.ble_connected
        if current != self._last_state:
            self._last_state = current
            self.async_write_ha_state()

    @property
    def is_on(self) -> bool:
        return self.coordinator.ble_connected


class GeberitToiletIntegrationReadySensor(GeberitToiletEntity, BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_translation_key = 'integration_ready'
    _attr_icon = 'mdi:check-circle-outline'

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{self._device_id}_integration_ready'

    @property
    def is_on(self) -> bool:
        return self.coordinator.integration_ready

class GeberitToiletGenericBinarySensor(GeberitToiletEntity, BinarySensorEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, dp_id: int) -> None:
        super().__init__(coordinator, entry)
        self._dp_id = dp_id
        self._meta = coordinator.get_dp_metadata(dp_id)
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta)
        self._attr_device_class = self._meta.binary_sensor_device_class

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        if not data or self._dp_id not in data:
            return None
        return bool(data[self._dp_id])

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        return self._metadata_attributes(self._dp_id)
