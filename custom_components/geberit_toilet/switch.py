from __future__ import annotations
from typing import Any
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .metadata import EntityKind

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[SwitchEntity] = []
    entities.append(GeberitToiletConnectionSwitch(coordinator, entry))
    for (dp_id, meta) in coordinator.dp_metadata.items():
        if not coordinator.should_expose_dp_id_as_entity(dp_id):
            continue
        if meta.hidden or meta.preferred_kind != EntityKind.SWITCH:
            continue
        if coordinator.data and coordinator.data.get(dp_id) is not None:
            entities.append(GeberitToiletGenericSwitch(coordinator, entry, dp_id))
    async_add_entities(entities)

class GeberitToiletConnectionSwitch(GeberitToiletEntity, SwitchEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{self._device_id}_connection'
        self._attr_translation_key = 'connection'
        self._attr_icon = 'mdi:bluetooth-connect'

    @property
    def is_on(self) -> bool:
        return self.coordinator.poll_enabled

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self.coordinator.async_enable_connection()
        self.async_write_ha_state()
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self.coordinator.async_disable_connection()
        self.async_write_ha_state()

class GeberitToiletGenericSwitch(GeberitToiletEntity, SwitchEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, dp_id: int) -> None:
        super().__init__(coordinator, entry)
        self._dp_id = dp_id
        self._meta = coordinator.get_dp_metadata(dp_id)
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta)

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        if not data or self._dp_id not in data:
            return None
        return bool(data[self._dp_id])

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        return self._metadata_attributes(self._dp_id)

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self.coordinator.async_write_dp(self._dp_id, True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self.coordinator.async_write_dp(self._dp_id, False)
