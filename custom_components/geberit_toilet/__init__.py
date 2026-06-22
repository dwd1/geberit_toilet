from __future__ import annotations
import asyncio
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .config_helpers import normalize_communication_mode
from .const import (
    CONF_COMMUNICATION_MODE,
    DOMAIN,
    PLATFORMS,
)
from .coordinator import GeberitToiletCoordinator
from .metadata import load_metadata_name_translations_sync
_LOGGER = logging.getLogger(__name__)
GeberitToiletConfigEntry = ConfigEntry[GeberitToiletCoordinator]

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry) -> bool:
    _LOGGER.info('Setting up Geberit Toilet integration')
    normalized_data = dict(entry.data)
    normalized_options = dict(entry.options)
    if CONF_COMMUNICATION_MODE in normalized_data:
        data_mode = normalize_communication_mode(normalized_data.get(CONF_COMMUNICATION_MODE))
        if data_mode != normalized_data.get(CONF_COMMUNICATION_MODE):
            normalized_data[CONF_COMMUNICATION_MODE] = data_mode
    if CONF_COMMUNICATION_MODE in normalized_options:
        options_mode = normalize_communication_mode(normalized_options.get(CONF_COMMUNICATION_MODE))
        if options_mode != normalized_options.get(CONF_COMMUNICATION_MODE):
            normalized_options[CONF_COMMUNICATION_MODE] = options_mode
    if normalized_data != dict(entry.data) or normalized_options != dict(entry.options):
        hass.config_entries.async_update_entry(
            entry,
            data=normalized_data,
            options=normalized_options,
        )
    coordinator = GeberitToiletCoordinator(hass, entry)
    coordinator.set_metadata_name_translations(await hass.async_add_executor_job(load_metadata_name_translations_sync, hass.config.language or 'en'))
    await coordinator.async_load_discovery_cache()
    await asyncio.sleep(2.0)
    await coordinator.async_config_entry_first_refresh()
    await coordinator.async_refresh_report_catalog()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(_async_options_updated))
    return True

async def _async_options_updated(hass: HomeAssistant, entry: GeberitToiletConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass: HomeAssistant, entry: GeberitToiletConfigEntry) -> bool:
    coordinator = entry.runtime_data
    if coordinator:
        await coordinator.async_close()
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
