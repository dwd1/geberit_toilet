from __future__ import annotations
from typing import Any
from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .protocol.DpId import DpId

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    if coordinator._inventory and DpId.DP_ODOUR_EXTRACTION_FAN in coordinator._inventory and coordinator.should_expose_dp_id_as_entity(DpId.DP_ODOUR_EXTRACTION_FAN):
        async_add_entities([GeberitToiletFan(coordinator, entry)])

class GeberitToiletFan(GeberitToiletEntity, FanEntity):
    _attr_supported_features = FanEntityFeature.SET_SPEED | FanEntityFeature.TURN_ON | FanEntityFeature.TURN_OFF

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{self._device_id}_fan'
        self._attr_name = self._metadata_display_name(DpId.DP_ODOUR_EXTRACTION_FAN)

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        if not data:
            return None
        return (data.get(DpId.DP_ODOUR_EXTRACTION_FAN) or 0) > 0

    @property
    def percentage(self) -> int | None:
        data = self.coordinator.data
        if not data:
            return None
        return data.get(DpId.DP_ODOUR_EXTRACTION_FAN)

    async def async_turn_on(self, percentage: int | None=None, preset_mode: str | None=None, **kwargs: Any) -> None:
        if percentage is not None:
            await self.async_set_percentage(percentage)
        else:
            await self.coordinator.async_write_dp(DpId.DP_ODOUR_EXTRACTION_FAN_OVERRIDE, True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self.coordinator.async_write_dp(DpId.DP_ODOUR_EXTRACTION_FAN_OVERRIDE, False)

    async def async_set_percentage(self, percentage: int) -> None:
        await self.coordinator.async_write_dp(DpId.DP_ODOUR_EXTRACTION_SET_FAN, percentage)
