from __future__ import annotations
from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .entity import GeberitToiletEntity
from .metadata import EntityKind
from .protocol.DpId import DpId
CLAIMED_HIGH_LEVEL_DP_IDS = {int(DpId.DP_ODOUR_EXTRACTION_FAN), int(DpId.DP_ODOUR_EXTRACTION_SET_FAN), int(DpId.DP_ORIENTATION_LIGHT_LED), int(DpId.DP_ORIENTATION_LIGHT_SET_LED)}

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[NumberEntity] = []
    for (dp_id, meta) in coordinator.dp_metadata.items():
        if not coordinator.should_expose_dp_id_as_entity(dp_id):
            continue
        if dp_id in CLAIMED_HIGH_LEVEL_DP_IDS:
            continue
        if meta.hidden or meta.preferred_kind != EntityKind.NUMBER:
            continue
        if coordinator.data and coordinator.data.get(dp_id) is not None:
            entities.append(GeberitToiletGenericNumber(coordinator, entry, dp_id))
    async_add_entities(entities)

class GeberitToiletGenericNumber(GeberitToiletEntity, NumberEntity):

    def __init__(self, coordinator, entry: GeberitToiletConfigEntry, dp_id: int) -> None:
        super().__init__(coordinator, entry)
        self._dp_id = dp_id
        self._meta = coordinator.get_dp_metadata(dp_id)
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta)
        self._attr_entity_category = self._meta.entity_category
        self._attr_entity_registry_enabled_default = self._meta.entity_registry_enabled_default
        self._attr_native_min_value = float(self._meta.min_value or 0)
        self._attr_native_max_value = float(self._meta.max_value if self._meta.max_value is not None else 100)
        self._attr_native_step = 1.0

    @property
    def native_value(self) -> float | None:
        data = self.coordinator.data
        if not data or self._dp_id not in data:
            return None
        val = data[self._dp_id]
        return float(val) if val is not None else None

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        return self._metadata_attributes(self._dp_id)

    async def async_set_native_value(self, value: float) -> None:
        await self.coordinator.async_write_dp(self._dp_id, int(value))
