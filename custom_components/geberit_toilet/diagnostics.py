from __future__ import annotations

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')
from typing import Any
from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import _0xc9d4372f, _0xdf46d1bc
from .coordinator import _0x0409f5bf
from .device_types import _0x5e1748ef
_0xcc0cb50e = {_0xc9d4372f, _0xdf46d1bc}

async def async_get_config_entry_diagnostics(hass, entry):
    _0xc4312c2a = entry.runtime_data
    _0xce539e3b = {}
    if _0xc4312c2a.data:
        for (_0x3c6e0b8a, _0x3a6d0284) in _0xc4312c2a.data.items():
            if isinstance(_0x3a6d0284, bytes):
                _0xce539e3b[str(_0x3c6e0b8a)] = _0x3a6d0284.hex()
            else:
                _0xce539e3b[str(_0x3c6e0b8a)] = _0x3a6d0284
    _0x1b6b61d5 = dict(_0xc4312c2a._0x84f90afc)
    _0x14696946 = {_0x8ce4b16b: _0x9e3669d1.hex() for (_0x8ce4b16b, _0x9e3669d1) in _0xc4312c2a._0x93b9730d.items()}
    _0x20f35e63 = _0x5e1748ef(_0xc4312c2a._0x4aec38a9, _0xc4312c2a._0xffe5c0a0)
    _0x444c7cc8 = {_0xd14e4b1f('636f6e6669675f656e747279'): {_0xd14e4b1f('64617461'): async_redact_data(dict(entry.data), _0xcc0cb50e), _0xd14e4b1f('6f7074696f6e73'): async_redact_data(dict(entry.options), _0xcc0cb50e)}, _0xd14e4b1f('636f6f7264696e61746f72'): {_0xd14e4b1f('626c655f636f6e6e6563746564'): _0xc4312c2a._0x3a821fc7, _0xd14e4b1f('696e746567726174696f6e5f7265616479'): _0xc4312c2a._0x73d4c228, _0xd14e4b1f('706f6c6c5f656e61626c6564'): _0xc4312c2a.poll_enabled, _0xd14e4b1f('64657465637465645f7365726965735f6964'): _0xc4312c2a._0x4aec38a9, _0xd14e4b1f('64657465637465645f76617269616e745f6964'): _0xc4312c2a._0xffe5c0a0, _0xd14e4b1f('6d6f64656c'): _0x20f35e63, _0xd14e4b1f('696e76656e746f72795f73697a65'): len(_0xc4312c2a._0x25cb3c49) if _0xc4312c2a._0x25cb3c49 else 0, _0xd14e4b1f('6361706162696c6974696573'): _0xc4312c2a._0x5db8c29c, _0xd14e4b1f('64617461'): _0xce539e3b, _0xd14e4b1f('676174745f6465636f6465645f76616c756573'): _0x1b6b61d5, _0xd14e4b1f('676174745f7261775f76616c756573'): _0x14696946}}
    return _0x444c7cc8