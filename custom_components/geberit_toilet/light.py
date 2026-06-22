from __future__ import annotations
from typing import Any
from homeassistant.components.light import ATTR_BRIGHTNESS, ColorMode, LightEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .protocol.DpId import DpId

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    if coordinator._inventory:
        if DpId.DP_ORIENTATION_LIGHT_LED in coordinator._inventory and coordinator.should_expose_dp_id_as_entity(DpId.DP_ORIENTATION_LIGHT_LED) or (DpId.DP_ORIENTATION_LIGHT_LED_OVERRIDE in coordinator._inventory and coordinator.should_expose_dp_id_as_entity(DpId.DP_ORIENTATION_LIGHT_LED_OVERRIDE)) or (DpId.DP_ORIENTATION_LIGHT_MODE in coordinator._inventory and coordinator.should_expose_dp_id_as_entity(DpId.DP_ORIENTATION_LIGHT_MODE)):
            async_add_entities([GeberitToiletLight(coordinator, entry)])

class GeberitToiletLight(GeberitToiletEntity, LightEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator, entry)
        self._attr_unique_id = f'{self._device_id}_light'
        self._attr_name = self._metadata_display_name(DpId.DP_ORIENTATION_LIGHT_LED)
        self._use_brightness = DpId.DP_ORIENTATION_LIGHT_LED in coordinator._inventory
        if self._use_brightness:
            self._attr_color_mode = ColorMode.BRIGHTNESS
            self._attr_supported_color_modes = {ColorMode.BRIGHTNESS}
        else:
            self._attr_color_mode = ColorMode.ONOFF
            self._attr_supported_color_modes = {ColorMode.ONOFF}

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        if not data:
            return None
        if self._use_brightness:
            return (data.get(DpId.DP_ORIENTATION_LIGHT_LED) or 0) > 0
        else:
            return bool(data.get(DpId.DP_ORIENTATION_LIGHT_LED_OVERRIDE))

    @property
    def brightness(self) -> int | None:
        if not self._use_brightness:
            return None
        data = self.coordinator.data
        if not data:
            return None
        pct = data.get(DpId.DP_ORIENTATION_LIGHT_LED) or 0
        return int(pct * 255 / 100)

    async def async_turn_on(self, **kwargs: Any) -> None:
        if self._use_brightness and ATTR_BRIGHTNESS in kwargs:
            pct = int(kwargs[ATTR_BRIGHTNESS] * 100 / 255)
            await self.coordinator.async_write_dp(DpId.DP_ORIENTATION_LIGHT_SET_LED, pct)
        else:
            await self.coordinator.async_write_dp(DpId.DP_ORIENTATION_LIGHT_LED_OVERRIDE, True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self.coordinator.async_write_dp(DpId.DP_ORIENTATION_LIGHT_LED_OVERRIDE, False)
