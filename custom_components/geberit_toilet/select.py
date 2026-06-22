from __future__ import annotations
from dataclasses import dataclass
import logging
from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from . import GeberitToiletConfigEntry
from .coordinator import GeberitToiletCoordinator
from .entity import GeberitToiletEntity
from .metadata import EntityKind
from .protocol.DpId import DpId
from .protocol.DpType import DpType
_LOGGER = logging.getLogger(__name__)

@dataclass(frozen=True)
class GeberitToiletSelectDescription(SelectEntityDescription):
    dp_id: DpId | None = None
    action_key: str | None = None
SELECT_TYPES: tuple[GeberitToiletSelectDescription, ...] = (GeberitToiletSelectDescription(key='report_left', translation_key='report_left', action_key='report_left', icon='mdi:file-document-outline'), GeberitToiletSelectDescription(key='report_right', translation_key='report_right', action_key='report_right', icon='mdi:file-document-outline'))

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[SelectEntity] = []
    for desc in SELECT_TYPES:
        if desc.action_key is not None:
            entities.append(GeberitToiletReportSelect(coordinator, entry, desc))
    if coordinator._inventory:
        for (dp_id, meta) in coordinator.dp_metadata.items():
            if not coordinator.should_expose_dp_id_as_entity(dp_id):
                continue
            if meta.hidden or meta.preferred_kind != EntityKind.SELECT:
                continue
            options = meta.options_for_select()
            if options:
                entities.append(GeberitToiletGenericSelect(coordinator, entry, dp_id, list(options)))
    async_add_entities(entities)

class GeberitToiletGenericSelect(GeberitToiletEntity, SelectEntity):

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, dp_id: int, options: list[str]) -> None:
        super().__init__(coordinator, entry)
        self._dp_id = dp_id
        self._meta = coordinator.get_dp_metadata(dp_id)
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta)
        self._attr_options = options

    @property
    def current_option(self) -> str | None:
        data = self.coordinator.data
        if not data or self._dp_id not in data:
            return None
        val = data[self._dp_id]
        if val is None:
            return None
        try:
            idx = int(val)
        except (TypeError, ValueError):
            return None
        if 0 <= idx < len(self._attr_options):
            return self._attr_options[idx]
        option = str(idx)
        return option if option in self._attr_options else None

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        return self._metadata_attributes(self._dp_id)

    async def async_select_option(self, option: str) -> None:
        if option not in self._attr_options:
            raise ValueError(f'Invalid option: {option}')
        if self._meta.options or self._meta.datatype == DpType.OffOnAuto:
            value = self._attr_options.index(option)
        else:
            value = int(option)
        await self.coordinator.async_write_dp(self._dp_id, value)

class GeberitToiletReportSelect(GeberitToiletEntity, SelectEntity):
    entity_description: GeberitToiletSelectDescription

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry, description: GeberitToiletSelectDescription) -> None:
        super().__init__(coordinator, entry)
        self.entity_description = description
        self._attr_unique_id = f'{self._device_id}_{description.key}'

    @property
    def options(self) -> list[str]:
        if self.entity_description.action_key == 'report_left':
            return self.coordinator.report_files_left
        return self.coordinator.report_files_right

    @property
    def current_option(self) -> str | None:
        if self.entity_description.action_key == 'report_left':
            return self.coordinator.selected_report_left
        return self.coordinator.selected_report_right

    @property
    def available(self) -> bool:
        return len(self.options) > 0

    async def async_select_option(self, option: str) -> None:
        if option not in self.options:
            raise ValueError(f'Invalid report file: {option}')
        if self.entity_description.action_key == 'report_left':
            await self.coordinator.async_select_report_left(option)
        else:
            await self.coordinator.async_select_report_right(option)
        _LOGGER.debug('Selected %s report file: %s', self.entity_description.action_key, option)
