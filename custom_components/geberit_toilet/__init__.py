from __future__ import annotations

def _geberit_get_disabled_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL + 1)
    logger.propagate = False
    logger.disabled = True
    return logger

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')
import asyncio
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from .config_helpers import _0x36ddd560
from .const import _0x2dd4cb7c, _0xbf7c9959, _0xdce4d7c5, _0x042bca9f, _0x2d39b37a
from .coordinator import _0x0409f5bf
from .log_helpers import async_remove_file_logging, configure_logging, log_config_summary, reset_device_log_context, set_device_log_context, silence_package_logging
from .metadata import _0xdcc10bc1
_LOGGER = _geberit_get_disabled_logger(__name__)
_0xa14eb14e = ConfigEntry[_0x0409f5bf]
_0x4bd8d48d = cv.config_entry_only_config_schema(_0xbf7c9959)
if not _0x042bca9f:
    silence_package_logging()

async def async_setup(hass, config):
    return True

def _0x458703c5(_0x1043bfc7, _0xc4312c2a):
    _0x3a8e4c06 = {**_0x1043bfc7.data, **_0x1043bfc7.options}
    log_config_summary(_0x3a8e4c06, include_targets=_0xc4312c2a._0x361c3e6d, exclude_targets=_0xc4312c2a._0x87b637aa, prefix=_0xd14e4b1f('436f6e66696720656e7472792073756d6d617279'))

async def async_setup_entry(hass, entry):
    _0x2b482023 = set_device_log_context(entry.data.get(_0xd14e4b1f('6465766963655f6964')))
    try:
        await configure_logging(hass, entry.data.get(_0xd14e4b1f('6465766963655f6964')))
        return await _0x6150f04b(hass, entry)
    except (asyncio.CancelledError, Exception):
        _0xc4312c2a = getattr(entry, _0xd14e4b1f('72756e74696d655f64617461'), None)
        if _0xc4312c2a is not None:
            try:
                await _0xc4312c2a._0x29c17b19()
            except Exception as _0x629d4431:
                pass
        await async_remove_file_logging(hass, entry.data.get(_0xd14e4b1f('6465766963655f6964')))
        raise
    finally:
        reset_device_log_context(_0x2b482023)

async def _0x6150f04b(_0x055cfe9f, _0x1043bfc7):
    if _0x042bca9f:
        pass
    _0xffee96f8 = dict(_0x1043bfc7.data)
    _0xc0690d61 = bool(_0xffee96f8.get(_0xdce4d7c5, False))
    _0xde9aba00 = dict(_0x1043bfc7.options)
    if _0x2dd4cb7c in _0xffee96f8:
        _0x33cbe2b5 = _0x36ddd560(_0xffee96f8.get(_0x2dd4cb7c))
        if _0x33cbe2b5 != _0xffee96f8.get(_0x2dd4cb7c):
            _0xffee96f8[_0x2dd4cb7c] = _0x33cbe2b5
    if _0x2dd4cb7c in _0xde9aba00:
        _0xbec9fa74 = _0x36ddd560(_0xde9aba00.get(_0x2dd4cb7c))
        if _0xbec9fa74 != _0xde9aba00.get(_0x2dd4cb7c):
            _0xde9aba00[_0x2dd4cb7c] = _0xbec9fa74
    if _0xffee96f8 != dict(_0x1043bfc7.data) or _0xde9aba00 != dict(_0x1043bfc7.options):
        _0x055cfe9f.config_entries.async_update_entry(_0x1043bfc7, data=_0xffee96f8, options=_0xde9aba00)
    _0xc4312c2a = _0x0409f5bf(_0x055cfe9f, _0x1043bfc7)
    _0x1043bfc7.runtime_data = _0xc4312c2a
    _0x458703c5(_0x1043bfc7, _0xc4312c2a)
    _0xc4312c2a._0xa67a8c65(await _0x055cfe9f.async_add_executor_job(_0xdcc10bc1, _0x055cfe9f.config.language or _0xd14e4b1f('656e')))
    await _0xc4312c2a._0xaf0e34c6()
    await _0xc4312c2a._0xc75f438a()
    _0xc4312c2a._0x0104f66a = _0xc0690d61
    if not _0xc4312c2a._0xc5f8f30d:
        try:
            await _0xc4312c2a._0x4691f650()
        except Exception as _0x56bd7107:
            raise ConfigEntryNotReady(f"{_0xd14e4b1f('4661696c656420746f207072696d65204765626572697420546f696c657420656e74697479206d6574616461746120647572696e672073657475703a20')}{_0x56bd7107}") from _0x56bd7107
    if _0xc0690d61:
        _0x53749c2e = dict(_0x1043bfc7.data)
        _0x53749c2e.pop(_0xdce4d7c5, None)
        _0x055cfe9f.config_entries.async_update_entry(_0x1043bfc7, data=_0x53749c2e)
    await _0xc4312c2a._0x009a3261()
    await _0x055cfe9f.config_entries.async_forward_entry_setups(_0x1043bfc7, _0x2d39b37a)
    _0xc4312c2a._0x23c6e6a5 = True
    _0xc4312c2a._0xb0ae159e()
    _0x1043bfc7.async_on_unload(_0x1043bfc7.add_update_listener(_0x38af84d9))
    return True

async def _0x38af84d9(_0x055cfe9f, _0x1043bfc7):
    await _0x055cfe9f.config_entries.async_reload(_0x1043bfc7.entry_id)

async def async_unload_entry(hass, entry):
    _0xad15cfaf = await hass.config_entries.async_unload_platforms(entry, _0x2d39b37a)
    if not _0xad15cfaf:
        return False
    _0xc4312c2a = entry.runtime_data
    if _0xc4312c2a:
        try:
            await _0xc4312c2a._0x29c17b19()
        except Exception as _0x56bd7107:
            pass
    await async_remove_file_logging(hass, entry.data.get(_0xd14e4b1f('6465766963655f6964')))
    return True

async def async_remove_entry(hass, entry):
    from homeassistant.helpers.storage import Store
    from homeassistant.helpers import entity_registry as er
    from .const import _0xbf7c9959, _0x218f0966, _0xeeafb6f6, _0x20db4e1a
    from pathlib import Path
    await async_remove_file_logging(hass, entry.data.get(_0xd14e4b1f('6465766963655f6964')))
    try:
        _0xf9fb410d = er.async_get(hass)
        _0xbd64bdd9 = {_0xe03ed967.entity_id: _0xe03ed967 for _0xe03ed967 in er.async_entries_for_config_entry(_0xf9fb410d, entry.entry_id)}
        _0x9379346c = entry.data.get(_0xd14e4b1f('6465766963655f6964'))
        if _0x9379346c:
            _0x2bbcccca = f"{_0x9379346c}{_0xd14e4b1f('5f')}"
            for _0xe03ed967 in list(_0xf9fb410d.entities.values()):
                if _0xe03ed967.platform != _0xbf7c9959:
                    continue
                if not _0xe03ed967.unique_id.startswith(_0x2bbcccca):
                    continue
                _0xbd64bdd9[_0xe03ed967.entity_id] = _0xe03ed967
        for _0xe03ed967 in _0xbd64bdd9.values():
            _0xf9fb410d.async_remove(_0xe03ed967.entity_id)
        if _0xbd64bdd9:
            pass
    except Exception as _0x56bd7107:
        pass
    try:
        _0x6fd95c57 = Store(hass, 1, f"{_0xbf7c9959}{_0xd14e4b1f('5f')}{entry.entry_id}{_0xd14e4b1f('5f646973636f76657279')}")
        await _0x6fd95c57.async_remove()
    except Exception as _0x56bd7107:
        pass
    try:
        _0x80f9b76d = Store(hass, 1, f"{_0xbf7c9959}{_0xd14e4b1f('5f')}{entry.entry_id}{_0xd14e4b1f('5f7374617465')}")
        await _0x80f9b76d.async_remove()
    except Exception as _0x56bd7107:
        pass
    _0x9379346c = entry.data.get(_0xd14e4b1f('6465766963655f6964'))
    if _0x9379346c:
        _0xb0c82bf0 = _0x9379346c.replace(_0xd14e4b1f('3a'), _0xd14e4b1f('2d')).lower()

        def _0x205e8ce6(_0xa93d0e39, _0x851f5ac9):
            if not _0xa93d0e39.exists() or not _0xa93d0e39.is_dir():
                return
            for _0x97fd815a in _0xa93d0e39.iterdir():
                if _0x97fd815a.is_file() and _0x97fd815a.name.lower().startswith(_0x851f5ac9):
                    try:
                        _0x97fd815a.unlink(missing_ok=True)
                    except Exception as _0x56bd7107:
                        pass
        _0xf38a44f4 = Path(hass.config.path(_0x218f0966))
        _0x650796ba = Path(hass.config.path(_0xeeafb6f6))
        _0x6c75047f = Path(hass.config.path(_0x20db4e1a))
        await hass.async_add_executor_job(_0x205e8ce6, _0xf38a44f4, _0xb0c82bf0)
        await hass.async_add_executor_job(_0x205e8ce6, _0x650796ba, _0xb0c82bf0)
        await hass.async_add_executor_job(_0x205e8ce6, _0x6c75047f, _0xb0c82bf0)