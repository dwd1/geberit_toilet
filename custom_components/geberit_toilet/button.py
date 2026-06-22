from __future__ import annotations
from dataclasses import dataclass
import logging
from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import UpdateFailed
from . import GeberitToiletConfigEntry
from .entity import GeberitToiletEntity
from .metadata import EntityKind
_LOGGER = logging.getLogger(__name__)

@dataclass(frozen=True)
class GeberitToiletButtonDescription(ButtonEntityDescription):
    action_key: str | None = None
BUTTON_TYPES: tuple[GeberitToiletButtonDescription, ...] = (GeberitToiletButtonDescription(key='create_report', translation_key='create_report', action_key='create_report', icon='mdi:file-document-plus-outline'), GeberitToiletButtonDescription(key='compare_reports', translation_key='compare_reports', action_key='compare_reports', icon='mdi:file-compare'), GeberitToiletButtonDescription(key='clear_reports', translation_key='clear_reports', action_key='clear_reports', icon='mdi:file-remove-outline'), GeberitToiletButtonDescription(key='clear_differences', translation_key='clear_differences', action_key='clear_differences', icon='mdi:file-document-remove-outline'))

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = entry.runtime_data
    entities: list[ButtonEntity] = [GeberitToiletDiagnosticButton(coordinator, entry, desc) for desc in BUTTON_TYPES]
    for (dp_id, meta) in coordinator.dp_metadata.items():
        if not coordinator.should_expose_dp_id_as_entity(dp_id):
            continue
        if meta.hidden or meta.preferred_kind != EntityKind.BUTTON:
            continue
        if dp_id in coordinator.supported_dp_ids:
            entities.append(GeberitToiletGenericButton(coordinator, entry, dp_id))
    async_add_entities(entities)

class GeberitToiletGenericButton(GeberitToiletEntity, ButtonEntity):

    def __init__(self, coordinator, entry: GeberitToiletConfigEntry, dp_id: int) -> None:
        super().__init__(coordinator, entry)
        self._dp_id = dp_id
        self._meta = coordinator.get_dp_metadata(dp_id)
        self._attr_unique_id = f'{self._device_id}_generic_{self._meta.key}'
        self._attr_name = self.coordinator.localize_metadata_name(self._meta)
        self._attr_entity_category = self._meta.entity_category
        self._attr_entity_registry_enabled_default = self._meta.entity_registry_enabled_default

    @property
    def extra_state_attributes(self) -> dict[str, object]:
        return self._metadata_attributes(self._dp_id)

    async def async_press(self) -> None:
        await self.coordinator.async_write_dp(self._dp_id, True)
        await self.coordinator.async_request_refresh()

class GeberitToiletDiagnosticButton(GeberitToiletEntity, ButtonEntity):
    entity_description: GeberitToiletButtonDescription

    def __init__(self, coordinator, entry: GeberitToiletConfigEntry, description: GeberitToiletButtonDescription) -> None:
        super().__init__(coordinator, entry)
        self.entity_description = description
        self._attr_unique_id = f'{self._device_id}_{description.key}'

    @property
    def available(self) -> bool:
        if self.entity_description.action_key == 'compare_reports':
            return len(self.coordinator.report_files) >= 2
        return True

    async def async_press(self) -> None:
        action = self.entity_description.action_key
        try:
            if action == 'create_report':
                path = await self.coordinator.async_create_report()
                _LOGGER.info('Created Geberit Toilet report: %s', path)
                return
            if action == 'compare_reports':
                path = await self.coordinator.async_compare_selected_reports()
                _LOGGER.info('Created Geberit Toilet report differences: %s', path)
                return
            if action == 'clear_reports':
                deleted = await self.coordinator.async_clear_reports()
                _LOGGER.info('Deleted %d Geberit Toilet report file(s)', deleted)
                return
            if action == 'clear_differences':
                deleted = await self.coordinator.async_clear_differences()
                _LOGGER.info('Deleted %d Geberit Toilet difference file(s)', deleted)
                return
        except ValueError as err:
            raise UpdateFailed(str(err)) from err
        raise UpdateFailed(f'Unsupported diagnostic action: {action}')
