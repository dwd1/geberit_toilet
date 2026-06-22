from __future__ import annotations
import asyncio
import json
import logging
from pathlib import Path
from typing import Any
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv
from homeassistant.components import bluetooth
from homeassistant.helpers import selector
from .config_helpers import normalize_communication_mode
from .const import DOMAIN, CONF_DEVICE_ID, CONF_PIN, CONF_ESPHOME_HOST, CONF_ESPHOME_PORT, CONF_NOISE_PSK, CONF_POLL_INTERVAL, CONF_ACCEPT_RISK, CONF_REQUEST_DATA_MODE, CONF_COMMUNICATION_MODE, CONF_USE_INCLUDE_DPID_LIST, CONF_USE_EXCLUDE_DPID_LIST, CONF_INCLUDE_DPIDS, CONF_EXCLUDE_DPIDS, CONF_MAX_INSTANCES_PER_DPID_GROUP, CONF_EXPOSE_LARGE_INSTANCE_GROUPS, CONF_USE_ESPHOME_PROXY, DEFAULT_ESPHOME_PORT, DEFAULT_POLL_INTERVAL, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP, INCLUDE_DPIDS_FILENAME, EXCLUDE_DPIDS_FILENAME, COMMUNICATION_MODE_DPIDS, COMMUNICATION_MODE_GATT, COMMUNICATION_MODE_BOTH, REQUEST_DATA_MODE_ALL_KNOWN, REQUEST_DATA_MODE_INVENTORY_ONLY
from .device_types import get_model_name
_LOGGER = logging.getLogger(__name__)

class CannotConnect(Exception):
    pass

class InvalidAuth(Exception):
    pass
MAX_INSTANCES_SELECTOR = selector.NumberSelector(selector.NumberSelectorConfig(min=0, max=100, mode=selector.NumberSelectorMode.BOX))

def _risk_acknowledged(user_input: dict | None) -> bool:
    return bool(user_input and user_input.get(CONF_ACCEPT_RISK) is True)

def _load_default_dpid_text_sync(filename: str) -> str:
    path = Path(__file__).with_name(filename)
    try:
        return path.read_text(encoding='utf-8').strip()
    except OSError:
        return ''

async def _async_load_default_dpid_text(hass: HomeAssistant, filename: str) -> str:
    return await hass.async_add_executor_job(_load_default_dpid_text_sync, filename)

def _effective_dpid_text(current_value: Any, fallback_value: str) -> str:
    if isinstance(current_value, str) and current_value.strip():
        return current_value
    return fallback_value


def _uses_dpid_lists(communication_mode: str | None) -> bool:
    return communication_mode != COMMUNICATION_MODE_GATT

def _load_translation_lookup_sync(language: str) -> dict[str, Any]:
    for candidate in (language, 'en'):
        path = Path(__file__).with_name('translations') / f'{candidate}.json'
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            continue
    return {}

async def _async_request_data_mode_options(hass: HomeAssistant) -> dict[str, str]:
    payload = await hass.async_add_executor_job(_load_translation_lookup_sync, hass.config.language or 'en')
    options = payload.get('lookup', {}).get('request_data_mode_options', {})
    return {REQUEST_DATA_MODE_INVENTORY_ONLY: options.get(REQUEST_DATA_MODE_INVENTORY_ONLY, 'Only inventory'), REQUEST_DATA_MODE_ALL_KNOWN: options.get(REQUEST_DATA_MODE_ALL_KNOWN, 'All known DPIDs')}

async def _async_communication_mode_options(hass: HomeAssistant) -> dict[str, str]:
    payload = await hass.async_add_executor_job(_load_translation_lookup_sync, hass.config.language or 'en')
    options = payload.get('lookup', {}).get('communication_mode_options', {})
    return {
        COMMUNICATION_MODE_DPIDS: options.get(COMMUNICATION_MODE_DPIDS, 'DPIDs'),
        COMMUNICATION_MODE_GATT: options.get(COMMUNICATION_MODE_GATT, 'GATT'),
        COMMUNICATION_MODE_BOTH: options.get(COMMUNICATION_MODE_BOTH, 'Both'),
    }

async def _test_connection(device_id: str, esphome_host: str | None, esphome_port: int, noise_psk: str | None, pin: str | None, communication_mode: str, hass: HomeAssistant) -> bool:
    from .protocol.BluetoothLeConnector import BluetoothLeConnector
    from .protocol.Ble20Client import Ble20Client
    ha = hass if not esphome_host else None
    connector = BluetoothLeConnector(esphome_host, esphome_port, noise_psk, hass=ha)
    try:
        await connector.connect_async(device_id)
        if communication_mode == COMMUNICATION_MODE_GATT:
            return True
        if not connector.arendi_handshake_done:
            raise CannotConnect('Arendi security handshake failed.')
        client = Ble20Client(connector)
        inv = await client.inventory()
        caps = await client.capabilities()
        await client.event_storage_inventory(caps)
        try:
            await client.join(pin=pin, inv=inv)
        except IOError as e:
            if 'PIN' in str(e):
                raise InvalidAuth(str(e)) from e
            raise CannotConnect(str(e)) from e
        return True
    except CannotConnect:
        raise
    except InvalidAuth:
        raise
    except Exception as e:
        raise CannotConnect(str(e)) from e
    finally:
        try:
            await connector.disconnect()
        except Exception:
            pass

def _normalise(user_input: dict) -> dict:
    return {
        **user_input,
        CONF_DEVICE_ID: user_input[CONF_DEVICE_ID].strip().upper(),
        CONF_ESPHOME_HOST: user_input.get(CONF_ESPHOME_HOST, '').strip() or None,
        CONF_NOISE_PSK: user_input.get(CONF_NOISE_PSK, '').strip() or None,
        CONF_PIN: user_input.get(CONF_PIN, '').strip() or None,
        CONF_COMMUNICATION_MODE: normalize_communication_mode(
            user_input.get(CONF_COMMUNICATION_MODE)
        ),
    }

def _get_device_title(hass: HomeAssistant, device_id: str) -> str:
    import re
    title = None
    discovery_info = bluetooth.async_last_service_info(hass, device_id, connectable=False)
    _LOGGER.debug('Resolving title for BLE device %s. Discovery info: %s', device_id, discovery_info)
    if discovery_info:
        if discovery_info.advertisement and 1538 in discovery_info.advertisement.manufacturer_data:
            mdata = discovery_info.advertisement.manufacturer_data[1538]
            if len(mdata) >= 3:
                series_id = mdata[1]
                variant_id = mdata[2]
                title = f'{get_model_name(series_id, variant_id)} ({device_id})'
        if not title and discovery_info.name:
            adv_name = discovery_info.name
            match = re.search('Geberit\\s+(\\d+)', adv_name, re.IGNORECASE)
            if match:
                series_id = int(match.group(1))
                title = f'{get_model_name(series_id, None)} ({device_id})'
            elif 'duofresh' in adv_name.lower():
                title = f'Geberit DuoFresh ({device_id})'
            elif 'aquaclean' in adv_name.lower():
                title = f'Geberit AquaClean ({device_id})'
            elif 'urinal' in adv_name.lower():
                title = f'Geberit Urinal ({device_id})'
    if not title:
        title = f'Geberit Toilet ({device_id})'
    _LOGGER.debug('Resolved title to: %s', title)
    return title

class GeberitToiletConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    _discovered_device_id: str | None = None
    _user_inputs: dict[str, Any] = {}

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> GeberitToiletOptionsFlow:
        return GeberitToiletOptionsFlow(config_entry)

    async def _async_finish_create_entry(self) -> FlowResult:
        normalized = _normalise(self._user_inputs)
        if not self._discovered_device_id:
            device_id = normalized[CONF_DEVICE_ID]
            await self.async_set_unique_id(device_id)
            self._abort_if_unique_id_configured()
        try:
            await _test_connection(device_id=normalized[CONF_DEVICE_ID], esphome_host=normalized[CONF_ESPHOME_HOST], esphome_port=normalized[CONF_ESPHOME_PORT], noise_psk=normalized[CONF_NOISE_PSK], pin=normalized[CONF_PIN], communication_mode=normalized[CONF_COMMUNICATION_MODE], hass=self.hass)
        except InvalidAuth as err:
            _LOGGER.error('Authentication failed during connection test: %s', err)
            raise
        except Exception as err:
            _LOGGER.error('Connection test failed: %s', err)
            raise CannotConnect(str(err)) from err
        title = self.context.get('title_placeholders', {}).get('name')
        if not title:
            title = _get_device_title(self.hass, normalized[CONF_DEVICE_ID])
        return self.async_create_entry(title=title, data=normalized)

    async def _async_continue_after_connection_step(self) -> FlowResult:
        if not _uses_dpid_lists(self._user_inputs.get(CONF_COMMUNICATION_MODE)):
            self._user_inputs[CONF_USE_INCLUDE_DPID_LIST] = False
            self._user_inputs[CONF_USE_EXCLUDE_DPID_LIST] = False
            self._user_inputs[CONF_INCLUDE_DPIDS] = ''
            self._user_inputs[CONF_EXCLUDE_DPIDS] = ''
            try:
                return await self._async_finish_create_entry()
            except InvalidAuth:
                return await self._show_current_connection_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_connection_step('cannot_connect')
        if self._user_inputs.get(CONF_USE_INCLUDE_DPID_LIST):
            return await self.async_step_include_dpids()
        if self._user_inputs.get(CONF_USE_EXCLUDE_DPID_LIST):
            return await self.async_step_exclude_dpids()
        try:
            return await self._async_finish_create_entry()
        except InvalidAuth:
            return await self._show_current_connection_step('invalid_auth')
        except CannotConnect:
            return await self._show_current_connection_step('cannot_connect')

    async def _show_current_connection_step(self, base_error: str | None=None) -> FlowResult:
        if self._user_inputs.get(CONF_USE_ESPHOME_PROXY):
            return await self.async_step_esphome({'_show_errors_only': True, 'base_error': base_error})
        if self._discovered_device_id:
            return await self.async_step_bluetooth_confirm({'_show_errors_only': True, 'base_error': base_error})
        return await self.async_step_user({'_show_errors_only': True, 'base_error': base_error})

    async def async_step_bluetooth(self, discovery_info: bluetooth.BluetoothServiceInfoBleak) -> FlowResult:
        import re
        device_id = discovery_info.address.upper()
        await self.async_set_unique_id(device_id)
        self._abort_if_unique_id_configured()
        title = None
        adv_name = discovery_info.name or ''
        _LOGGER.debug('Bluetooth discovery triggered: address=%s, name=%r, uuids=%r, manufacturer_data=%r, service_data=%r', device_id, adv_name, discovery_info.advertisement.service_uuids, discovery_info.advertisement.manufacturer_data, discovery_info.advertisement.service_data)
        if 1538 in discovery_info.advertisement.manufacturer_data:
            mdata = discovery_info.advertisement.manufacturer_data[1538]
            if len(mdata) >= 3:
                series_id = mdata[1]
                variant_id = mdata[2]
                title = f'{get_model_name(series_id, variant_id)} ({device_id})'
        if not title and adv_name:
            match = re.search('Geberit\\s+(\\d+)', adv_name, re.IGNORECASE)
            if match:
                series_id = int(match.group(1))
                title = f'{get_model_name(series_id, None)} ({device_id})'
            elif 'duofresh' in adv_name.lower():
                title = f'Geberit DuoFresh ({device_id})'
            elif 'aquaclean' in adv_name.lower():
                title = f'Geberit AquaClean ({device_id})'
            elif 'urinal' in adv_name.lower():
                title = f'Geberit Urinal ({device_id})'
        if not title:
            title = f'Geberit Toilet ({device_id})'
        self.context['title_placeholders'] = {'name': title}
        self._discovered_device_id = device_id
        return await self.async_step_bluetooth_confirm()

    async def async_step_bluetooth_confirm(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        request_data_mode_options = await _async_request_data_mode_options(self.hass)
        communication_mode_options = await _async_communication_mode_options(self.hass)
        if user_input and user_input.get('_show_errors_only'):
            errors['base'] = user_input['base_error']
            user_input = None
        if user_input is not None:
            if not _risk_acknowledged(user_input):
                errors['base'] = 'risk_ack_required'
            else:
                self._user_inputs = {CONF_DEVICE_ID: self._discovered_device_id, CONF_PIN: user_input.get(CONF_PIN, ''), CONF_POLL_INTERVAL: user_input.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL), CONF_REQUEST_DATA_MODE: user_input.get(CONF_REQUEST_DATA_MODE, REQUEST_DATA_MODE_INVENTORY_ONLY), CONF_COMMUNICATION_MODE: user_input.get(CONF_COMMUNICATION_MODE, COMMUNICATION_MODE_DPIDS), CONF_MAX_INSTANCES_PER_DPID_GROUP: user_input.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP), CONF_EXPOSE_LARGE_INSTANCE_GROUPS: user_input.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, False), CONF_USE_INCLUDE_DPID_LIST: user_input.get(CONF_USE_INCLUDE_DPID_LIST, True), CONF_USE_EXCLUDE_DPID_LIST: user_input.get(CONF_USE_EXCLUDE_DPID_LIST, True), CONF_INCLUDE_DPIDS: '', CONF_EXCLUDE_DPIDS: '', CONF_USE_ESPHOME_PROXY: user_input.get(CONF_USE_ESPHOME_PROXY, False), CONF_ESPHOME_HOST: '', CONF_ESPHOME_PORT: DEFAULT_ESPHOME_PORT, CONF_NOISE_PSK: ''}
                if user_input.get(CONF_USE_ESPHOME_PROXY):
                    return await self.async_step_esphome()
                return await self._async_continue_after_connection_step()
        schema = vol.Schema({vol.Optional(CONF_PIN, default=''): cv.string, vol.Optional(CONF_USE_ESPHOME_PROXY, default=False): cv.boolean, vol.Optional(CONF_POLL_INTERVAL, default=DEFAULT_POLL_INTERVAL): vol.All(int, vol.Range(min=5, max=3600)), vol.Required(CONF_COMMUNICATION_MODE, default=COMMUNICATION_MODE_DPIDS): vol.In(communication_mode_options), vol.Required(CONF_REQUEST_DATA_MODE, default=REQUEST_DATA_MODE_INVENTORY_ONLY): vol.In(request_data_mode_options), vol.Optional(CONF_MAX_INSTANCES_PER_DPID_GROUP, default=DEFAULT_MAX_INSTANCES_PER_DPID_GROUP): MAX_INSTANCES_SELECTOR, vol.Optional(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, default=False): cv.boolean, vol.Optional(CONF_USE_INCLUDE_DPID_LIST, default=True): cv.boolean, vol.Optional(CONF_USE_EXCLUDE_DPID_LIST, default=True): cv.boolean, vol.Required(CONF_ACCEPT_RISK, default=False): cv.boolean})
        return self.async_show_form(step_id='bluetooth_confirm', data_schema=schema, errors=errors)

    async def async_step_user(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        request_data_mode_options = await _async_request_data_mode_options(self.hass)
        communication_mode_options = await _async_communication_mode_options(self.hass)
        if user_input and user_input.get('_show_errors_only'):
            errors['base'] = user_input['base_error']
            user_input = None
        if user_input is not None:
            if not _risk_acknowledged(user_input):
                errors['base'] = 'risk_ack_required'
            else:
                self._user_inputs = {CONF_DEVICE_ID: user_input[CONF_DEVICE_ID], CONF_PIN: user_input.get(CONF_PIN, ''), CONF_POLL_INTERVAL: user_input.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL), CONF_REQUEST_DATA_MODE: user_input.get(CONF_REQUEST_DATA_MODE, REQUEST_DATA_MODE_INVENTORY_ONLY), CONF_COMMUNICATION_MODE: user_input.get(CONF_COMMUNICATION_MODE, COMMUNICATION_MODE_DPIDS), CONF_MAX_INSTANCES_PER_DPID_GROUP: user_input.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP), CONF_EXPOSE_LARGE_INSTANCE_GROUPS: user_input.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, False), CONF_USE_INCLUDE_DPID_LIST: user_input.get(CONF_USE_INCLUDE_DPID_LIST, True), CONF_USE_EXCLUDE_DPID_LIST: user_input.get(CONF_USE_EXCLUDE_DPID_LIST, True), CONF_INCLUDE_DPIDS: '', CONF_EXCLUDE_DPIDS: '', CONF_USE_ESPHOME_PROXY: user_input.get(CONF_USE_ESPHOME_PROXY, False), CONF_ESPHOME_HOST: '', CONF_ESPHOME_PORT: DEFAULT_ESPHOME_PORT, CONF_NOISE_PSK: ''}
                if user_input.get(CONF_USE_ESPHOME_PROXY):
                    return await self.async_step_esphome()
                return await self._async_continue_after_connection_step()
        schema = vol.Schema({vol.Required(CONF_DEVICE_ID, default=''): cv.string, vol.Optional(CONF_PIN, default=''): cv.string, vol.Optional(CONF_USE_ESPHOME_PROXY, default=False): cv.boolean, vol.Optional(CONF_POLL_INTERVAL, default=DEFAULT_POLL_INTERVAL): vol.All(int, vol.Range(min=5, max=3600)), vol.Required(CONF_COMMUNICATION_MODE, default=COMMUNICATION_MODE_DPIDS): vol.In(communication_mode_options), vol.Required(CONF_REQUEST_DATA_MODE, default=REQUEST_DATA_MODE_INVENTORY_ONLY): vol.In(request_data_mode_options), vol.Optional(CONF_MAX_INSTANCES_PER_DPID_GROUP, default=DEFAULT_MAX_INSTANCES_PER_DPID_GROUP): MAX_INSTANCES_SELECTOR, vol.Optional(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, default=False): cv.boolean, vol.Optional(CONF_USE_INCLUDE_DPID_LIST, default=True): cv.boolean, vol.Optional(CONF_USE_EXCLUDE_DPID_LIST, default=True): cv.boolean, vol.Required(CONF_ACCEPT_RISK, default=False): cv.boolean})
        return self.async_show_form(step_id='user', data_schema=schema, errors=errors)

    async def async_step_esphome(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        if user_input and user_input.get('_show_errors_only'):
            errors['base'] = user_input['base_error']
            user_input = None
        if user_input is not None:
            self._user_inputs.update({CONF_USE_ESPHOME_PROXY: True, CONF_ESPHOME_HOST: user_input[CONF_ESPHOME_HOST], CONF_ESPHOME_PORT: user_input.get(CONF_ESPHOME_PORT, DEFAULT_ESPHOME_PORT), CONF_NOISE_PSK: user_input.get(CONF_NOISE_PSK, '')})
            return await self._async_continue_after_connection_step()
        schema = vol.Schema({vol.Required(CONF_ESPHOME_HOST, default=''): cv.string, vol.Optional(CONF_ESPHOME_PORT, default=DEFAULT_ESPHOME_PORT): cv.port, vol.Optional(CONF_NOISE_PSK, default=''): cv.string})
        return self.async_show_form(step_id='esphome', data_schema=schema, errors=errors)

    async def async_step_include_dpids(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        default_include_text = await _async_load_default_dpid_text(self.hass, INCLUDE_DPIDS_FILENAME)
        if user_input is not None:
            self._user_inputs[CONF_INCLUDE_DPIDS] = user_input.get(CONF_INCLUDE_DPIDS, '').strip()
            if self._user_inputs.get(CONF_USE_EXCLUDE_DPID_LIST):
                return await self.async_step_exclude_dpids()
            try:
                return await self._async_finish_create_entry()
            except InvalidAuth:
                return await self._show_current_connection_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_connection_step('cannot_connect')
        schema = vol.Schema({vol.Optional(CONF_INCLUDE_DPIDS, default=_effective_dpid_text(self._user_inputs.get(CONF_INCLUDE_DPIDS), default_include_text)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id='include_dpids', data_schema=schema, errors=errors)

    async def async_step_exclude_dpids(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        default_exclude_text = await _async_load_default_dpid_text(self.hass, EXCLUDE_DPIDS_FILENAME)
        if user_input is not None:
            self._user_inputs[CONF_EXCLUDE_DPIDS] = user_input.get(CONF_EXCLUDE_DPIDS, '').strip()
            try:
                return await self._async_finish_create_entry()
            except InvalidAuth:
                return await self._show_current_connection_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_connection_step('cannot_connect')
        schema = vol.Schema({vol.Optional(CONF_EXCLUDE_DPIDS, default=_effective_dpid_text(self._user_inputs.get(CONF_EXCLUDE_DPIDS), default_exclude_text)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id='exclude_dpids', data_schema=schema, errors=errors)

class GeberitToiletOptionsFlow(config_entries.OptionsFlow):
    _user_inputs: dict[str, Any] = {}

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry
        self._user_inputs = {}

    async def _async_finish_options_entry(self) -> FlowResult:
        device_id = self.config_entry.data[CONF_DEVICE_ID]
        normalized = _normalise({CONF_DEVICE_ID: device_id, **self._user_inputs})
        try:
            await _test_connection(device_id=device_id, esphome_host=normalized[CONF_ESPHOME_HOST], esphome_port=normalized[CONF_ESPHOME_PORT], noise_psk=normalized[CONF_NOISE_PSK], pin=normalized[CONF_PIN], communication_mode=normalized[CONF_COMMUNICATION_MODE], hass=self.hass)
        except InvalidAuth as err:
            _LOGGER.error('Authentication failed during connection test: %s', err)
            raise
        except Exception as err:
            _LOGGER.error('Connection test failed: %s', err)
            raise CannotConnect(str(err)) from err
        return self.async_create_entry(title='', data=normalized)

    async def _async_continue_after_options_connection_step(self) -> FlowResult:
        if not _uses_dpid_lists(self._user_inputs.get(CONF_COMMUNICATION_MODE)):
            self._user_inputs[CONF_USE_INCLUDE_DPID_LIST] = False
            self._user_inputs[CONF_USE_EXCLUDE_DPID_LIST] = False
            self._user_inputs[CONF_INCLUDE_DPIDS] = ''
            self._user_inputs[CONF_EXCLUDE_DPIDS] = ''
            try:
                return await self._async_finish_options_entry()
            except InvalidAuth:
                return await self._show_current_options_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_options_step('cannot_connect')
        if self._user_inputs.get(CONF_USE_INCLUDE_DPID_LIST):
            return await self.async_step_include_dpids()
        if self._user_inputs.get(CONF_USE_EXCLUDE_DPID_LIST):
            return await self.async_step_exclude_dpids()
        try:
            return await self._async_finish_options_entry()
        except InvalidAuth:
            return await self._show_current_options_step('invalid_auth')
        except CannotConnect:
            return await self._show_current_options_step('cannot_connect')

    async def _show_current_options_step(self, base_error: str | None=None) -> FlowResult:
        if self._user_inputs.get(CONF_USE_ESPHOME_PROXY):
            return await self.async_step_esphome({'_show_errors_only': True, 'base_error': base_error})
        return await self.async_step_init({'_show_errors_only': True, 'base_error': base_error})

    async def async_step_init(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        conf = {**self.config_entry.data, **self.config_entry.options}
        request_data_mode_options = await _async_request_data_mode_options(self.hass)
        communication_mode_options = await _async_communication_mode_options(self.hass)
        if user_input and user_input.get('_show_errors_only'):
            errors['base'] = user_input['base_error']
            user_input = None
        if user_input is not None:
            self._user_inputs = {CONF_PIN: user_input.get(CONF_PIN, ''), CONF_POLL_INTERVAL: user_input.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL), CONF_REQUEST_DATA_MODE: user_input.get(CONF_REQUEST_DATA_MODE, conf.get(CONF_REQUEST_DATA_MODE, REQUEST_DATA_MODE_INVENTORY_ONLY)), CONF_COMMUNICATION_MODE: user_input.get(CONF_COMMUNICATION_MODE, conf.get(CONF_COMMUNICATION_MODE, COMMUNICATION_MODE_DPIDS)), CONF_MAX_INSTANCES_PER_DPID_GROUP: user_input.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, conf.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP)), CONF_EXPOSE_LARGE_INSTANCE_GROUPS: user_input.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, conf.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, False)), CONF_USE_INCLUDE_DPID_LIST: user_input.get(CONF_USE_INCLUDE_DPID_LIST, conf.get(CONF_USE_INCLUDE_DPID_LIST, True)), CONF_USE_EXCLUDE_DPID_LIST: user_input.get(CONF_USE_EXCLUDE_DPID_LIST, conf.get(CONF_USE_EXCLUDE_DPID_LIST, True)), CONF_INCLUDE_DPIDS: conf.get(CONF_INCLUDE_DPIDS, ''), CONF_EXCLUDE_DPIDS: conf.get(CONF_EXCLUDE_DPIDS, ''), CONF_USE_ESPHOME_PROXY: user_input.get(CONF_USE_ESPHOME_PROXY, False), CONF_ESPHOME_HOST: '', CONF_ESPHOME_PORT: DEFAULT_ESPHOME_PORT, CONF_NOISE_PSK: ''}
            if user_input.get(CONF_USE_ESPHOME_PROXY):
                return await self.async_step_esphome()
            return await self._async_continue_after_options_connection_step()
        has_proxy = bool(conf.get(CONF_ESPHOME_HOST))
        schema = vol.Schema({vol.Optional(CONF_PIN, default=conf.get(CONF_PIN) or ''): cv.string, vol.Optional(CONF_USE_ESPHOME_PROXY, default=has_proxy): cv.boolean, vol.Optional(CONF_POLL_INTERVAL, default=conf.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL)): vol.All(int, vol.Range(min=5, max=3600)), vol.Required(CONF_COMMUNICATION_MODE, default=conf.get(CONF_COMMUNICATION_MODE, COMMUNICATION_MODE_DPIDS)): vol.In(communication_mode_options), vol.Required(CONF_REQUEST_DATA_MODE, default=conf.get(CONF_REQUEST_DATA_MODE, REQUEST_DATA_MODE_INVENTORY_ONLY)): vol.In(request_data_mode_options), vol.Optional(CONF_MAX_INSTANCES_PER_DPID_GROUP, default=conf.get(CONF_MAX_INSTANCES_PER_DPID_GROUP, DEFAULT_MAX_INSTANCES_PER_DPID_GROUP)): MAX_INSTANCES_SELECTOR, vol.Optional(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, default=conf.get(CONF_EXPOSE_LARGE_INSTANCE_GROUPS, False)): cv.boolean, vol.Optional(CONF_USE_INCLUDE_DPID_LIST, default=conf.get(CONF_USE_INCLUDE_DPID_LIST, True)): cv.boolean, vol.Optional(CONF_USE_EXCLUDE_DPID_LIST, default=conf.get(CONF_USE_EXCLUDE_DPID_LIST, True)): cv.boolean})
        return self.async_show_form(step_id='init', data_schema=schema, errors=errors)

    async def async_step_esphome(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        conf = {**self.config_entry.data, **self.config_entry.options}
        if user_input and user_input.get('_show_errors_only'):
            errors['base'] = user_input['base_error']
            user_input = None
        if user_input is not None:
            self._user_inputs.update({CONF_USE_ESPHOME_PROXY: True, CONF_ESPHOME_HOST: user_input[CONF_ESPHOME_HOST], CONF_ESPHOME_PORT: user_input.get(CONF_ESPHOME_PORT, DEFAULT_ESPHOME_PORT), CONF_NOISE_PSK: user_input.get(CONF_NOISE_PSK, '')})
            return await self._async_continue_after_options_connection_step()
        schema = vol.Schema({vol.Required(CONF_ESPHOME_HOST, default=conf.get(CONF_ESPHOME_HOST) or ''): cv.string, vol.Optional(CONF_ESPHOME_PORT, default=conf.get(CONF_ESPHOME_PORT, DEFAULT_ESPHOME_PORT)): cv.port, vol.Optional(CONF_NOISE_PSK, default=conf.get(CONF_NOISE_PSK) or ''): cv.string})
        return self.async_show_form(step_id='esphome', data_schema=schema, errors=errors)

    async def async_step_include_dpids(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        conf = {**self.config_entry.data, **self.config_entry.options}
        default_include_text = await _async_load_default_dpid_text(self.hass, INCLUDE_DPIDS_FILENAME)
        if user_input is not None:
            self._user_inputs[CONF_INCLUDE_DPIDS] = user_input.get(CONF_INCLUDE_DPIDS, '').strip()
            if self._user_inputs.get(CONF_USE_EXCLUDE_DPID_LIST):
                return await self.async_step_exclude_dpids()
            try:
                return await self._async_finish_options_entry()
            except InvalidAuth:
                return await self._show_current_options_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_options_step('cannot_connect')
        schema = vol.Schema({vol.Optional(CONF_INCLUDE_DPIDS, default=_effective_dpid_text(self._user_inputs.get(CONF_INCLUDE_DPIDS), conf.get(CONF_INCLUDE_DPIDS) or default_include_text)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id='include_dpids', data_schema=schema, errors=errors)

    async def async_step_exclude_dpids(self, user_input: dict | None=None) -> FlowResult:
        errors = {}
        conf = {**self.config_entry.data, **self.config_entry.options}
        default_exclude_text = await _async_load_default_dpid_text(self.hass, EXCLUDE_DPIDS_FILENAME)
        if user_input is not None:
            self._user_inputs[CONF_EXCLUDE_DPIDS] = user_input.get(CONF_EXCLUDE_DPIDS, '').strip()
            try:
                return await self._async_finish_options_entry()
            except InvalidAuth:
                return await self._show_current_options_step('invalid_auth')
            except CannotConnect:
                return await self._show_current_options_step('cannot_connect')
        schema = vol.Schema({vol.Optional(CONF_EXCLUDE_DPIDS, default=_effective_dpid_text(self._user_inputs.get(CONF_EXCLUDE_DPIDS), conf.get(CONF_EXCLUDE_DPIDS) or default_exclude_text)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id='exclude_dpids', data_schema=schema, errors=errors)
