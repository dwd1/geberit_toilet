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
from .config_helpers import _0x34b55d2a, _0x36ddd560, _0x1f4fdd89
from .const import _0xbf7c9959, _0xcff93a68, _0xc9d4372f, _0xcfc35486, _0xc83ac5c7, _0xdf46d1bc, _0xa9d4a173, _0x0e947c32, _0xb8a5e944, _0x2dd4cb7c, _0xe4b27365, _0x2cbe1305, _0x378188b4, _0xb11e8fce, _0x7180920c, _0xb5df4305, _0x5f76d50a, _0xe4204fbd, _0x3c717acb, _0xf2330fa3, _0x3d99575a, _0x98513e7d, _0xdd09b7d5, _0xb40494b3, _0xdce4d7c5, _0x011c5d45, _0xc880a522, _0x8b0c8ba7, _0x5223e47e, _0x9755795a
from .device_types import _0x5e1748ef
from .log_helpers import configure_logging, log_config_summary, reset_device_log_context, set_device_log_context
_LOGGER = _geberit_get_disabled_logger(__name__)

class _0x80ddd4bd(Exception):
    pass

class _0xa39aaf87(Exception):
    pass
_0x39d66235 = selector.NumberSelector(selector.NumberSelectorConfig(min=0, max=100, mode=selector.NumberSelectorMode.BOX))

def _0x9acd0884(_0xee244119):
    return bool(_0xee244119 and _0xee244119.get(_0x0e947c32) is True)

def _0x71f7658b(_0x435ed7e9):
    _0xd6fe1d0b = Path(__file__).with_name(_0x435ed7e9)
    try:
        return _0xd6fe1d0b.read_text(encoding=_0xd14e4b1f('7574662d38')).strip()
    except OSError:
        return ''

async def _0x51b0110e(_0x055cfe9f, _0x435ed7e9):
    return await _0x055cfe9f.async_add_executor_job(_0x71f7658b, _0x435ed7e9)

def _0x150bfb83(_0x426ea53d, _0x3fa9857c):
    if isinstance(_0x426ea53d, str) and _0x426ea53d.strip():
        return _0x426ea53d
    return _0x3fa9857c

def _0xc072f2c9(_0x1a483b47):
    return _0x1a483b47 != _0xc880a522

def _0xc18cee6d(_0x9379346c, _0x36a88093, _0xd980de70=''):
    import re
    _0xd5d3db17 = None
    if _0x36a88093:
        _0xf3334ac9 = _0x36a88093.advertisement
        if _0xf3334ac9 and 1538 in _0xf3334ac9.manufacturer_data:
            _0x41de38d7 = _0xf3334ac9.manufacturer_data[1538]
            if len(_0x41de38d7) >= 3:
                _0xa08cee2d = _0x41de38d7[1]
                _0x444abb90 = _0x41de38d7[2]
                _0xd5d3db17 = f"{_0x5e1748ef(_0xa08cee2d, _0x444abb90)}{_0xd14e4b1f('2028')}{_0x9379346c}{_0xd14e4b1f('29')}"
        if not _0xd5d3db17:
            _0xa9f1da21 = _0xd980de70 or _0x36a88093.name or ''
            if _0xa9f1da21:
                _0xe3cc92c1 = re.search(_0xd14e4b1f('476562657269745c732b285c642b29'), _0xa9f1da21, re.IGNORECASE)
                if _0xe3cc92c1:
                    _0xa08cee2d = int(_0xe3cc92c1.group(1))
                    _0xd5d3db17 = f"{_0x5e1748ef(_0xa08cee2d, None)}{_0xd14e4b1f('2028')}{_0x9379346c}{_0xd14e4b1f('29')}"
                elif _0xd14e4b1f('64756f6672657368') in _0xa9f1da21.lower():
                    _0xd5d3db17 = f"{_0xd14e4b1f('476562657269742044756f46726573682028')}{_0x9379346c}{_0xd14e4b1f('29')}"
                elif _0xd14e4b1f('61717561636c65616e') in _0xa9f1da21.lower():
                    _0xd5d3db17 = f"{_0xd14e4b1f('476562657269742041717561436c65616e2028')}{_0x9379346c}{_0xd14e4b1f('29')}"
                elif _0xd14e4b1f('7572696e616c') in _0xa9f1da21.lower():
                    _0xd5d3db17 = f"{_0xd14e4b1f('47656265726974205572696e616c2028')}{_0x9379346c}{_0xd14e4b1f('29')}"
    if not _0xd5d3db17:
        _0xd5d3db17 = f"{_0xd14e4b1f('4765626572697420546f696c65742028')}{_0x9379346c}{_0xd14e4b1f('29')}"
    return _0xd5d3db17

def _0x003b1125(_0xee244119, *, _0x9379346c, _0xa4a918a4=None):
    _0x593616de = _0xa4a918a4 or {}
    _0x8b92a895 = _0xee244119.get(_0x5f76d50a, _0x593616de.get(_0x5f76d50a, False))
    _0x7cde80a8 = _0x593616de.get(_0xcfc35486) or ''
    _0x116c6dd6 = _0x593616de.get(_0xc83ac5c7, _0x3c717acb)
    _0xccac6dc1 = _0x593616de.get(_0xdf46d1bc) or ''
    if not _0x8b92a895:
        _0x7cde80a8 = ''
        _0x116c6dd6 = _0x3c717acb
        _0xccac6dc1 = ''
    _0x8a6f5038 = _0xee244119[_0xc9d4372f] if _0xc9d4372f in _0xee244119 else _0x593616de.get(_0xc9d4372f)
    return {**({_0xcff93a68: _0x9379346c} if _0x9379346c is not None else {_0xcff93a68: _0xee244119[_0xcff93a68]}), _0xc9d4372f: _0x8a6f5038 or '', _0xe4204fbd: _0xee244119.get(_0xe4204fbd, _0x593616de.get(_0xe4204fbd, _0x98513e7d)), _0xa9d4a173: _0xee244119.get(_0xa9d4a173, _0x593616de.get(_0xa9d4a173, _0xf2330fa3)), _0xb8a5e944: _0xee244119.get(_0xb8a5e944, _0x593616de.get(_0xb8a5e944, _0x9755795a)), _0x2dd4cb7c: _0xee244119.get(_0x2dd4cb7c, _0x593616de.get(_0x2dd4cb7c, _0x011c5d45)), _0x7180920c: _0xee244119.get(_0x7180920c, _0x593616de.get(_0x7180920c, _0x3d99575a)), _0xb5df4305: _0xee244119.get(_0xb5df4305, _0x593616de.get(_0xb5df4305, False)), _0xe4b27365: _0xee244119.get(_0xe4b27365, _0x593616de.get(_0xe4b27365, True)), _0x2cbe1305: _0xee244119.get(_0x2cbe1305, _0x593616de.get(_0x2cbe1305, True)), _0x378188b4: _0x593616de.get(_0x378188b4) or '', _0xb11e8fce: _0x593616de.get(_0xb11e8fce) or '', _0x5f76d50a: _0x8b92a895, _0xcfc35486: _0x7cde80a8, _0xc83ac5c7: _0x116c6dd6, _0xdf46d1bc: _0xccac6dc1}

def _0x3e7c6362(*, _0xf29764bc, _0x7a0448fc, _0x23d03c88, _0x2ddf6db4, _0xa4a918a4=None):
    _0x593616de = _0xa4a918a4 or {}
    _0xc9550d5f = {}
    if _0x23d03c88:
        _0xc9550d5f[vol.Required(_0xcff93a68, default=_0x593616de.get(_0xcff93a68, ''))] = cv.string
    _0xc9550d5f[vol.Optional(_0xc9d4372f, default=_0x593616de.get(_0xc9d4372f) or '')] = cv.string
    _0xc9550d5f[vol.Optional(_0x5f76d50a, default=_0x593616de.get(_0x5f76d50a, False))] = cv.boolean
    _0xc9550d5f[vol.Optional(_0xe4204fbd, default=_0x593616de.get(_0xe4204fbd, _0x98513e7d))] = vol.All(vol.Coerce(float), vol.Range(min=0.25, max=60.0))
    _0xc9550d5f[vol.Optional(_0xa9d4a173, default=_0x593616de.get(_0xa9d4a173, _0xf2330fa3))] = vol.All(int, vol.Range(min=5, max=3600))
    _0xc9550d5f[vol.Required(_0x2dd4cb7c, default=_0x593616de.get(_0x2dd4cb7c, _0x011c5d45))] = vol.In(_0xf29764bc)
    _0xc9550d5f[vol.Required(_0xb8a5e944, default=_0x593616de.get(_0xb8a5e944, _0x9755795a))] = vol.In(_0x7a0448fc)
    _0xc9550d5f[vol.Optional(_0x7180920c, default=_0x593616de.get(_0x7180920c, _0x3d99575a))] = _0x39d66235
    _0xc9550d5f[vol.Optional(_0xb5df4305, default=_0x593616de.get(_0xb5df4305, False))] = cv.boolean
    _0xc9550d5f[vol.Optional(_0xe4b27365, default=_0x593616de.get(_0xe4b27365, True))] = cv.boolean
    _0xc9550d5f[vol.Optional(_0x2cbe1305, default=_0x593616de.get(_0x2cbe1305, True))] = cv.boolean
    if _0x2ddf6db4:
        _0xc9550d5f[vol.Required(_0x0e947c32, default=_0x593616de.get(_0x0e947c32, False))] = cv.boolean
    return vol.Schema(_0xc9550d5f)

def _0x15ef227a(_0xa4a918a4=None):
    _0x593616de = _0xa4a918a4 or {}
    return vol.Schema({vol.Required(_0xcfc35486, default=_0x593616de.get(_0xcfc35486) or ''): cv.string, vol.Optional(_0xc83ac5c7, default=_0x593616de.get(_0xc83ac5c7, _0x3c717acb)): cv.port, vol.Optional(_0xdf46d1bc, default=_0x593616de.get(_0xdf46d1bc) or ''): cv.string})

def _0xee0141a1(_0x42aefbae, _0xee244119):
    _0x42aefbae.update({_0x5f76d50a: True, _0xcfc35486: _0xee244119[_0xcfc35486], _0xc83ac5c7: _0xee244119.get(_0xc83ac5c7, _0x3c717acb), _0xdf46d1bc: _0xee244119.get(_0xdf46d1bc) or ''})

async def _0xa718beae(_0x055cfe9f):
    _0x321c3cf4 = await _0x055cfe9f.async_add_executor_job(_0x34b55d2a, _0x055cfe9f.config.language or _0xd14e4b1f('656e'))
    _0x93da65a9 = _0x321c3cf4.get(_0xd14e4b1f('73656c6563746f72'), {}).get(_0xd14e4b1f('726571756573745f646174615f6d6f6465'), {}).get(_0xd14e4b1f('6f7074696f6e73'), {})
    return {_0x9755795a: _0x93da65a9.get(_0x9755795a, _0xd14e4b1f('4f6e6c7920696e76656e746f7279')), _0x5223e47e: _0x93da65a9.get(_0x5223e47e, _0xd14e4b1f('416c6c206b6e6f776e204450494473'))}

async def _0x765a5b14(_0x055cfe9f):
    _0x321c3cf4 = await _0x055cfe9f.async_add_executor_job(_0x34b55d2a, _0x055cfe9f.config.language or _0xd14e4b1f('656e'))
    _0x93da65a9 = _0x321c3cf4.get(_0xd14e4b1f('73656c6563746f72'), {}).get(_0xd14e4b1f('636f6d6d756e69636174696f6e5f6d6f6465'), {}).get(_0xd14e4b1f('6f7074696f6e73'), {})
    return {_0x011c5d45: _0x93da65a9.get(_0x011c5d45, _0xd14e4b1f('4450494473')), _0xc880a522: _0x93da65a9.get(_0xc880a522, _0xd14e4b1f('47415454')), _0x8b0c8ba7: _0x93da65a9.get(_0x8b0c8ba7, _0xd14e4b1f('426f7468'))}

async def _0x2d19f223(_0x9379346c, _0x7cde80a8, _0x116c6dd6, _0xccac6dc1, _0x8a6f5038, _0x1a483b47, _0x055cfe9f):
    from .protocol import _0xabcea1bc
    from .protocol import _0x6e2f7964
    _0x925cc8d2 = _0x055cfe9f if not _0x7cde80a8 else None
    _0x266e0d3d = _0xabcea1bc(_0x7cde80a8, _0x116c6dd6, _0xccac6dc1, hass=_0x925cc8d2)
    try:
        await _0x266e0d3d.connect_async(_0x9379346c)
        if _0x1a483b47 == _0xc880a522:
            return True
        if not _0x266e0d3d.arendi_handshake_done:
            raise _0x80ddd4bd(_0xd14e4b1f('4172656e64692073656375726974792068616e647368616b65206661696c65642e'))
        _0x62608e08 = _0x6e2f7964(_0x266e0d3d)
        _0x545f7f57 = await _0x62608e08.inventory()
        _0x69cd8955 = await _0x62608e08.capabilities()
        await _0x62608e08.event_storage_inventory(_0x69cd8955)
        try:
            await _0x62608e08.join(pin=_0x8a6f5038, inv=_0x545f7f57)
        except IOError as _0xe1671797:
            if _0xd14e4b1f('50494e') in str(_0xe1671797):
                raise _0xa39aaf87(str(_0xe1671797)) from _0xe1671797
            raise _0x80ddd4bd(str(_0xe1671797)) from _0xe1671797
        return True
    except _0x80ddd4bd:
        raise
    except _0xa39aaf87:
        raise
    except Exception as _0xe1671797:
        raise _0x80ddd4bd(str(_0xe1671797)) from _0xe1671797
    finally:
        try:
            await _0x266e0d3d.disconnect()
        except Exception:
            pass

def _0x8bc3f269(_0xee244119):
    return {**_0xee244119, _0xcff93a68: _0xee244119[_0xcff93a68].strip().upper(), _0xcfc35486: (_0xee244119.get(_0xcfc35486) or '').strip() or None, _0xdf46d1bc: (_0xee244119.get(_0xdf46d1bc) or '').strip() or None, _0xc9d4372f: (_0xee244119.get(_0xc9d4372f) or '').strip() or None, _0x2dd4cb7c: _0x36ddd560(_0xee244119.get(_0x2dd4cb7c))}

def _0x247f441c(_0x3a8e4c06):
    _0x8b92a895 = bool(_0x3a8e4c06.get(_0x5f76d50a) or _0x3a8e4c06.get(_0xcfc35486))
    return ((_0x3a8e4c06.get(_0xcff93a68) or '').strip().upper(), _0x8b92a895, (_0x3a8e4c06.get(_0xcfc35486) or '').strip().casefold() if _0x8b92a895 else '', int(_0x3a8e4c06.get(_0xc83ac5c7) or _0x3c717acb) if _0x8b92a895 else _0x3c717acb, (_0x3a8e4c06.get(_0xdf46d1bc) or '').strip() if _0x8b92a895 else '', (_0x3a8e4c06.get(_0xc9d4372f) or '').strip(), _0x36ddd560(_0x3a8e4c06.get(_0x2dd4cb7c)))

def _0x55ea693a(_0x055cfe9f, _0x9379346c):
    _0x36a88093 = bluetooth.async_last_service_info(_0x055cfe9f, _0x9379346c, connectable=False)
    _0xd5d3db17 = _0xc18cee6d(_0x9379346c, _0x36a88093)
    return _0xd5d3db17

class _0x289c12de(config_entries.ConfigFlow, domain=_0xbf7c9959):
    _0x021321e8 = 1
    _0x99a75560: str | None = None
    _0x8d8a52d3: dict[str, Any] = {}

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return _0xdbf65a70(config_entry)

    async def _0x9dc14bba(self):
        _0x14f42e76 = _0x8bc3f269(self._0x8d8a52d3)
        _0x9379346c = _0x14f42e76[_0xcff93a68]
        _0x2b482023 = set_device_log_context(_0x9379346c)
        try:
            await configure_logging(self.hass, _0x9379346c)
            log_config_summary(_0x14f42e76, include_targets=set(_0x1f4fdd89(_0x14f42e76.get(_0x378188b4))) if _0x14f42e76.get(_0xe4b27365) else set(), exclude_targets=set(_0x1f4fdd89(_0x14f42e76.get(_0xb11e8fce))) if _0x14f42e76.get(_0x2cbe1305) else set(), prefix=_0xd14e4b1f('436f6e66696720666c6f772073756d6d617279'))
            if not self._0x99a75560:
                await self.async_set_unique_id(_0x9379346c)
                self._abort_if_unique_id_configured()
            try:
                await _0x2d19f223(_0x9379346c=_0x9379346c, _0x7cde80a8=_0x14f42e76[_0xcfc35486], _0x116c6dd6=_0x14f42e76[_0xc83ac5c7], _0xccac6dc1=_0x14f42e76[_0xdf46d1bc], _0x8a6f5038=_0x14f42e76[_0xc9d4372f], _0x1a483b47=_0x14f42e76[_0x2dd4cb7c], _0x055cfe9f=self.hass)
            except _0xa39aaf87 as _0x56bd7107:
                raise
            except Exception as _0x56bd7107:
                raise _0x80ddd4bd(str(_0x56bd7107)) from _0x56bd7107
        finally:
            reset_device_log_context(_0x2b482023)
        _0xd5d3db17 = self.context.get(_0xd14e4b1f('7469746c655f706c616365686f6c64657273'), {}).get(_0xd14e4b1f('6e616d65'))
        if not _0xd5d3db17:
            _0xd5d3db17 = _0x55ea693a(self.hass, _0x14f42e76[_0xcff93a68])
        _0x14f42e76[_0xdce4d7c5] = True
        return self.async_create_entry(title=_0xd5d3db17, data=_0x14f42e76)

    async def _0xcccfa959(self):
        if not _0xc072f2c9(self._0x8d8a52d3.get(_0x2dd4cb7c)):
            self._0x8d8a52d3[_0xe4b27365] = False
            self._0x8d8a52d3[_0x2cbe1305] = False
            self._0x8d8a52d3[_0x378188b4] = ''
            self._0x8d8a52d3[_0xb11e8fce] = ''
            try:
                return await self._0x9dc14bba()
            except _0xa39aaf87:
                return await self._0xe60931c6(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xe60931c6(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        if self._0x8d8a52d3.get(_0xe4b27365):
            return await self.async_step_include_dpids()
        if self._0x8d8a52d3.get(_0x2cbe1305):
            return await self.async_step_exclude_dpids()
        try:
            return await self._0x9dc14bba()
        except _0xa39aaf87:
            return await self._0xe60931c6(_0xd14e4b1f('696e76616c69645f61757468'))
        except _0x80ddd4bd:
            return await self._0xe60931c6(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))

    async def _0xe60931c6(self, _0x42a92ade=None):
        if self._0x8d8a52d3.get(_0x5f76d50a):
            return await self.async_step_esphome({_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79'): True, _0xd14e4b1f('626173655f6572726f72'): _0x42a92ade})
        if self._0x99a75560:
            return await self.async_step_bluetooth_confirm({_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79'): True, _0xd14e4b1f('626173655f6572726f72'): _0x42a92ade})
        return await self.async_step_user({_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79'): True, _0xd14e4b1f('626173655f6572726f72'): _0x42a92ade})

    async def async_step_bluetooth(self, discovery_info):
        _0x9379346c = discovery_info.address.upper()
        await self.async_set_unique_id(_0x9379346c)
        self._abort_if_unique_id_configured()
        _0xd980de70 = discovery_info.name or ''
        _0xd5d3db17 = _0xc18cee6d(_0x9379346c, discovery_info, _0xd980de70)
        self.context[_0xd14e4b1f('7469746c655f706c616365686f6c64657273')] = {_0xd14e4b1f('6e616d65'): _0xd5d3db17}
        self._0x99a75560 = _0x9379346c
        return await self.async_step_bluetooth_confirm()

    async def async_step_bluetooth_confirm(self, user_input=None):
        _0x07213a01 = {}
        _0x7a0448fc = await _0xa718beae(self.hass)
        _0xf29764bc = await _0x765a5b14(self.hass)
        if user_input and user_input.get(_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79')):
            _0x07213a01[_0xd14e4b1f('62617365')] = user_input[_0xd14e4b1f('626173655f6572726f72')]
            user_input = None
        if user_input is not None:
            if not _0x9acd0884(user_input):
                _0x07213a01[_0xd14e4b1f('62617365')] = _0xd14e4b1f('7269736b5f61636b5f7265717569726564')
            else:
                self._0x8d8a52d3 = _0x003b1125(user_input, _0x9379346c=self._0x99a75560)
                if user_input.get(_0x5f76d50a):
                    return await self.async_step_esphome()
                return await self._0xcccfa959()
        _0xc9550d5f = _0x3e7c6362(_0xf29764bc=_0xf29764bc, _0x7a0448fc=_0x7a0448fc, _0x23d03c88=False, _0x2ddf6db4=True)
        return self.async_show_form(step_id=_0xd14e4b1f('626c7565746f6f74685f636f6e6669726d'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_user(self, user_input=None):
        _0x07213a01 = {}
        _0x7a0448fc = await _0xa718beae(self.hass)
        _0xf29764bc = await _0x765a5b14(self.hass)
        if user_input and user_input.get(_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79')):
            _0x07213a01[_0xd14e4b1f('62617365')] = user_input[_0xd14e4b1f('626173655f6572726f72')]
            user_input = None
        if user_input is not None:
            if not _0x9acd0884(user_input):
                _0x07213a01[_0xd14e4b1f('62617365')] = _0xd14e4b1f('7269736b5f61636b5f7265717569726564')
            else:
                self._0x8d8a52d3 = _0x003b1125(user_input, _0x9379346c=None)
                if user_input.get(_0x5f76d50a):
                    return await self.async_step_esphome()
                return await self._0xcccfa959()
        _0xc9550d5f = _0x3e7c6362(_0xf29764bc=_0xf29764bc, _0x7a0448fc=_0x7a0448fc, _0x23d03c88=True, _0x2ddf6db4=True)
        return self.async_show_form(step_id=_0xd14e4b1f('75736572'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_esphome(self, user_input=None):
        _0x07213a01 = {}
        if user_input and user_input.get(_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79')):
            _0x07213a01[_0xd14e4b1f('62617365')] = user_input[_0xd14e4b1f('626173655f6572726f72')]
            user_input = None
        if user_input is not None:
            _0xee0141a1(self._0x8d8a52d3, user_input)
            return await self._0xcccfa959()
        _0xc9550d5f = _0x15ef227a()
        return self.async_show_form(step_id=_0xd14e4b1f('657370686f6d65'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_include_dpids(self, user_input=None):
        _0x07213a01 = {}
        _0x16d3c9fc = await _0x51b0110e(self.hass, _0xdd09b7d5)
        if user_input is not None:
            self._0x8d8a52d3[_0x378188b4] = (user_input.get(_0x378188b4) or '').strip()
            if self._0x8d8a52d3.get(_0x2cbe1305):
                return await self.async_step_exclude_dpids()
            try:
                return await self._0x9dc14bba()
            except _0xa39aaf87:
                return await self._0xe60931c6(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xe60931c6(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        _0xc9550d5f = vol.Schema({vol.Optional(_0x378188b4, default=_0x150bfb83(self._0x8d8a52d3.get(_0x378188b4), _0x16d3c9fc)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id=_0xd14e4b1f('696e636c7564655f6470696473'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_exclude_dpids(self, user_input=None):
        _0x07213a01 = {}
        _0x14aa863f = await _0x51b0110e(self.hass, _0xb40494b3)
        if user_input is not None:
            self._0x8d8a52d3[_0xb11e8fce] = (user_input.get(_0xb11e8fce) or '').strip()
            try:
                return await self._0x9dc14bba()
            except _0xa39aaf87:
                return await self._0xe60931c6(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xe60931c6(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        _0xc9550d5f = vol.Schema({vol.Optional(_0xb11e8fce, default=_0x150bfb83(self._0x8d8a52d3.get(_0xb11e8fce), _0x14aa863f)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id=_0xd14e4b1f('6578636c7564655f6470696473'), data_schema=_0xc9550d5f, errors=_0x07213a01)

class _0xdbf65a70(config_entries.OptionsFlow):
    _0x8d8a52d3: dict[str, Any] = {}

    def __init__(self, config_entry):
        self._0x8d8a52d3 = {}
        try:
            self.config_entry = config_entry
        except AttributeError:
            pass

    async def _0xd70d0a10(self):
        _0x9379346c = self.config_entry.data[_0xcff93a68]
        _0x14f42e76 = _0x8bc3f269({_0xcff93a68: _0x9379346c, **self._0x8d8a52d3})
        _0x30bff3ef = {**self.config_entry.data, **self.config_entry.options}
        _0xe0a605b2 = _0x247f441c(_0x14f42e76) != _0x247f441c(_0x30bff3ef)
        _0xc4312c2a = getattr(self.config_entry, _0xd14e4b1f('72756e74696d655f64617461'), None)
        _0x0ac3398d = False
        _0x18ce0f79 = False
        _0x2b482023 = set_device_log_context(_0x9379346c)
        try:
            await configure_logging(self.hass, _0x9379346c)
            if _0xe0a605b2:
                if _0xc4312c2a is not None and _0xc4312c2a.poll_enabled:
                    _0x0ac3398d = await _0xc4312c2a._0xbeabd378()
                try:
                    await _0x2d19f223(_0x9379346c=_0x9379346c, _0x7cde80a8=_0x14f42e76[_0xcfc35486], _0x116c6dd6=_0x14f42e76[_0xc83ac5c7], _0xccac6dc1=_0x14f42e76[_0xdf46d1bc], _0x8a6f5038=_0x14f42e76[_0xc9d4372f], _0x1a483b47=_0x14f42e76[_0x2dd4cb7c], _0x055cfe9f=self.hass)
                except _0xa39aaf87 as _0x56bd7107:
                    raise
                except Exception as _0x56bd7107:
                    raise _0x80ddd4bd(str(_0x56bd7107)) from _0x56bd7107
            _0xb4a88417 = self.async_create_entry(title='', data=_0x14f42e76)
            _0x18ce0f79 = True
            return _0xb4a88417
        finally:
            if _0xc4312c2a is not None:
                await _0xc4312c2a._0xdb22ea9d(_0x0ac3398d=_0x0ac3398d, _0xad5cd0c1=not _0x18ce0f79)
            reset_device_log_context(_0x2b482023)

    async def _0xe71a86d4(self):
        if not _0xc072f2c9(self._0x8d8a52d3.get(_0x2dd4cb7c)):
            self._0x8d8a52d3[_0xe4b27365] = False
            self._0x8d8a52d3[_0x2cbe1305] = False
            self._0x8d8a52d3[_0x378188b4] = ''
            self._0x8d8a52d3[_0xb11e8fce] = ''
            try:
                return await self._0xd70d0a10()
            except _0xa39aaf87:
                return await self._0xb0da7c1d(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xb0da7c1d(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        if self._0x8d8a52d3.get(_0xe4b27365):
            return await self.async_step_include_dpids()
        if self._0x8d8a52d3.get(_0x2cbe1305):
            return await self.async_step_exclude_dpids()
        try:
            return await self._0xd70d0a10()
        except _0xa39aaf87:
            return await self._0xb0da7c1d(_0xd14e4b1f('696e76616c69645f61757468'))
        except _0x80ddd4bd:
            return await self._0xb0da7c1d(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))

    async def _0xb0da7c1d(self, _0x42a92ade=None):
        if self._0x8d8a52d3.get(_0x5f76d50a):
            return await self.async_step_esphome({_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79'): True, _0xd14e4b1f('626173655f6572726f72'): _0x42a92ade})
        return await self.async_step_init({_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79'): True, _0xd14e4b1f('626173655f6572726f72'): _0x42a92ade})

    async def async_step_init(self, user_input=None):
        _0x07213a01 = {}
        _0x3a8e4c06 = {**self.config_entry.data, **self.config_entry.options}
        _0x7a0448fc = await _0xa718beae(self.hass)
        _0xf29764bc = await _0x765a5b14(self.hass)
        if user_input and user_input.get(_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79')):
            _0x07213a01[_0xd14e4b1f('62617365')] = user_input[_0xd14e4b1f('626173655f6572726f72')]
            user_input = None
        if user_input is not None:
            _0x9379346c = self.config_entry.data[_0xcff93a68]
            self._0x8d8a52d3 = _0x003b1125(user_input, _0x9379346c=_0x9379346c, _0xa4a918a4=_0x3a8e4c06)
            if user_input.get(_0x5f76d50a):
                return await self.async_step_esphome()
            return await self._0xe71a86d4()
        _0x6afc6a20 = bool(_0x3a8e4c06.get(_0xcfc35486))
        _0xc9550d5f = _0x3e7c6362(_0xf29764bc=_0xf29764bc, _0x7a0448fc=_0x7a0448fc, _0x23d03c88=False, _0x2ddf6db4=False, _0xa4a918a4={**_0x3a8e4c06, _0x5f76d50a: _0x6afc6a20})
        return self.async_show_form(step_id=_0xd14e4b1f('696e6974'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_esphome(self, user_input=None):
        _0x07213a01 = {}
        _0x3a8e4c06 = {**self.config_entry.data, **self.config_entry.options}
        if user_input and user_input.get(_0xd14e4b1f('5f73686f775f6572726f72735f6f6e6c79')):
            _0x07213a01[_0xd14e4b1f('62617365')] = user_input[_0xd14e4b1f('626173655f6572726f72')]
            user_input = None
        if user_input is not None:
            _0xee0141a1(self._0x8d8a52d3, user_input)
            return await self._0xe71a86d4()
        _0xc9550d5f = _0x15ef227a(_0x3a8e4c06)
        return self.async_show_form(step_id=_0xd14e4b1f('657370686f6d65'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_include_dpids(self, user_input=None):
        _0x07213a01 = {}
        _0x3a8e4c06 = {**self.config_entry.data, **self.config_entry.options}
        _0x16d3c9fc = await _0x51b0110e(self.hass, _0xdd09b7d5)
        if user_input is not None:
            self._0x8d8a52d3[_0x378188b4] = (user_input.get(_0x378188b4) or '').strip()
            if self._0x8d8a52d3.get(_0x2cbe1305):
                return await self.async_step_exclude_dpids()
            try:
                return await self._0xd70d0a10()
            except _0xa39aaf87:
                return await self._0xb0da7c1d(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xb0da7c1d(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        _0xc9550d5f = vol.Schema({vol.Optional(_0x378188b4, default=_0x150bfb83(self._0x8d8a52d3.get(_0x378188b4), _0x3a8e4c06.get(_0x378188b4) or _0x16d3c9fc)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id=_0xd14e4b1f('696e636c7564655f6470696473'), data_schema=_0xc9550d5f, errors=_0x07213a01)

    async def async_step_exclude_dpids(self, user_input=None):
        _0x07213a01 = {}
        _0x3a8e4c06 = {**self.config_entry.data, **self.config_entry.options}
        _0x14aa863f = await _0x51b0110e(self.hass, _0xb40494b3)
        if user_input is not None:
            self._0x8d8a52d3[_0xb11e8fce] = (user_input.get(_0xb11e8fce) or '').strip()
            try:
                return await self._0xd70d0a10()
            except _0xa39aaf87:
                return await self._0xb0da7c1d(_0xd14e4b1f('696e76616c69645f61757468'))
            except _0x80ddd4bd:
                return await self._0xb0da7c1d(_0xd14e4b1f('63616e6e6f745f636f6e6e656374'))
        _0xc9550d5f = vol.Schema({vol.Optional(_0xb11e8fce, default=_0x150bfb83(self._0x8d8a52d3.get(_0xb11e8fce), _0x3a8e4c06.get(_0xb11e8fce) or _0x14aa863f)): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.TEXT, multiline=True))})
        return self.async_show_form(step_id=_0xd14e4b1f('6578636c7564655f6470696473'), data_schema=_0xc9550d5f, errors=_0x07213a01)