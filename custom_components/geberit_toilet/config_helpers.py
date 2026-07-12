from __future__ import annotations

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')
import json
from pathlib import Path
import re
from .const import _0x8b0c8ba7, _0x011c5d45, _0xc880a522

def _0x34b55d2a(_0x8512ae7d):
    _0x85ee095b = Path(__file__).with_name(_0xd14e4b1f('7472616e736c6174696f6e73'))
    for _0x65afdfb4 in (_0x8512ae7d, _0xd14e4b1f('656e')):
        _0xd6fe1d0b = _0x85ee095b / f"{_0x65afdfb4}{_0xd14e4b1f('2e6a736f6e')}"
        try:
            return json.loads(_0xd6fe1d0b.read_text(encoding=_0xd14e4b1f('7574662d38')))
        except (OSError, json.JSONDecodeError):
            continue
    return {}

def _0x1f4fdd89(_0x2063c160):
    if not _0x2063c160:
        return []
    _0xaa6f6d62 = []
    _0xd5b4a9a5 = set()
    for _0x6438c669 in _0x2063c160.splitlines():
        _0x9a0364b9 = _0x6438c669.split(_0xd14e4b1f('23'), 1)[0].strip()
        if not _0x9a0364b9:
            continue
        for _0x94a08da1 in re.split(_0xd14e4b1f('5b5c732c3b5d2b'), _0x9a0364b9):
            if not _0x94a08da1:
                continue
            _0x5ffc3ec8 = re.fullmatch(_0xd14e4b1f('285c642b295b5c2e3a5d285c642b29'), _0x94a08da1)
            if _0x5ffc3ec8:
                _0x42aefbae = (int(_0x5ffc3ec8.group(1), 10), int(_0x5ffc3ec8.group(2), 10))
            else:
                try:
                    _0x42aefbae = int(_0x94a08da1, 10)
                except ValueError:
                    continue
            if _0x42aefbae not in _0xd5b4a9a5:
                _0xd5b4a9a5.add(_0x42aefbae)
                _0xaa6f6d62.append(_0x42aefbae)
    return _0xaa6f6d62

def _0x36ddd560(_0x2063c160):
    if _0x2063c160 in (_0x011c5d45, _0xc880a522, _0x8b0c8ba7):
        return _0x2063c160
    return _0x011c5d45