from __future__ import annotations
from .protocol import _0x27401bf3

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')
from dataclasses import dataclass
from typing import Any
from .catalog_data import _0x18a56bc1, _0x9f2dbf92, _0xd73f810a
from .DpId import DpId

@dataclass(frozen=True)
class _0xc8d6f455:
    _0xa68071d3: str
    _0x2af72f10: int
    _0x6fa93254: int
    _0x3931108d: int
    _0x56dda363: int
    _0xc6a35ba1: int
    _0xb140af3d: str
    _0x67daf92c: str = ''
    _0x4ad9a0ea: list[str] | None = None
    _0xc80e6e0d: bool = False

def _0xaab9449c(_0xa68071d3):
    try:
        return int(DpId[str(_0xa68071d3)])
    except (KeyError, ValueError):
        return None

def _0xe942bd4d(_0xa08cee2d):
    if _0xa08cee2d == 252:
        return _0xd14e4b1f('47414d')
    if _0xa08cee2d == 244:
        return _0xd14e4b1f('4d694361')
    return None

def _0x47e82895(_0xa08cee2d, _0x444abb90):
    if not isinstance(_0xa08cee2d, int) or not isinstance(_0x444abb90, int):
        return None
    _0x3c6e0b8a = f"{_0xa08cee2d}{_0xd14e4b1f('3a')}{_0x444abb90}"
    return _0x3c6e0b8a if _0x3c6e0b8a in _0xd73f810a else None

def _0xd7cd945d(_0xa08cee2d, _0x444abb90):
    _0x7f4be311 = _0x47e82895(_0xa08cee2d, _0x444abb90)
    if _0x7f4be311 is not None:
        return set(_0xd73f810a[_0x7f4be311])
    _0x22711bea = _0xe942bd4d(_0xa08cee2d)
    if _0x22711bea is not None:
        return set(_0x9f2dbf92.get(_0x22711bea, {}))
    return None

def _0x4df13a38(_0xa08cee2d):
    _0x22711bea = _0xe942bd4d(_0xa08cee2d)
    if _0x22711bea is None:
        return {}
    return dict(_0x9f2dbf92.get(_0x22711bea, {}))

def _0xb9659644(_0xa68071d3):
    return tuple((_0xc8d6f455(_0xa68071d3=_0xa68071d3, **_0x1043bfc7) for _0x1043bfc7 in _0x18a56bc1.get(_0xa68071d3, ()) if isinstance(_0x1043bfc7, dict)))

def _0xb7aa207c(_0xa68071d3, *, _0x2af72f10, _0x6fa93254):
    _0xbef2e239 = _0xb9659644(_0xa68071d3)
    if not _0xbef2e239:
        return None

    def score(item):
        return (int(_0x2af72f10 is not None and item._0x2af72f10 == _0x2af72f10), int(_0x6fa93254 is not None and item._0x6fa93254 == _0x6fa93254), int(item._0x2af72f10 == 0), -item._0x2af72f10)
    return max(_0xbef2e239, key=score)

def _0xabe76933(_0xa08cee2d, _0x444abb90):
    _0xccba6b12 = _0xd7cd945d(_0xa08cee2d, _0x444abb90)
    if not _0xccba6b12:
        return {}
    _0x3369638f = _0x4df13a38(_0xa08cee2d)
    _0x7a1eabc3 = {}
    for _0xa68071d3 in sorted(_0xccba6b12):
        _0x32e2cb0f = _0xaab9449c(_0xa68071d3)
        if _0x32e2cb0f is None:
            continue
        _0x30618b3b = _0xb7aa207c(_0xa68071d3, _0x2af72f10=_0x3369638f.get(_0xa68071d3), _0x6fa93254=None)
        if _0x30618b3b is None:
            _0x7a1eabc3[_0x32e2cb0f] = {_0xd14e4b1f('6b6579'): _0xa68071d3.lower().removeprefix(_0xd14e4b1f('64705f')), _0xd14e4b1f('696e7374616e6365'): 0, _0xd14e4b1f('76657273696f6e'): _0x3369638f.get(_0xa68071d3, 0), _0xd14e4b1f('6461746174797065'): None, _0xd14e4b1f('6d696e5f73'): None, _0xd14e4b1f('6d61785f73'): None, _0xd14e4b1f('6d696e5f75'): None, _0xd14e4b1f('6d61785f75'): None, _0xd14e4b1f('69735f696e7465726e616c'): False, _0xd14e4b1f('6265686176696f72'): None}
            continue
        _0x7a1eabc3[_0x32e2cb0f] = {_0xd14e4b1f('6b6579'): _0xa68071d3.lower().removeprefix(_0xd14e4b1f('64705f')), _0xd14e4b1f('696e7374616e6365'): _0x30618b3b._0x6fa93254, _0xd14e4b1f('76657273696f6e'): _0x30618b3b._0x2af72f10, _0xd14e4b1f('6461746174797065'): _0x30618b3b._0x3931108d, _0xd14e4b1f('6d696e5f73'): _0x30618b3b._0x56dda363, _0xd14e4b1f('6d61785f73'): _0x30618b3b._0xc6a35ba1, _0xd14e4b1f('6d696e5f75'): _0x30618b3b._0x56dda363, _0xd14e4b1f('6d61785f75'): _0x30618b3b._0xc6a35ba1, _0xd14e4b1f('69735f696e7465726e616c'): False, _0xd14e4b1f('6265686176696f72'): int(_0x27401bf3[_0x30618b3b._0xb140af3d])}
    return _0x7a1eabc3

def _0x44eacae4(_0xc3f62fb2, _0xbb5e9d49):
    _0xd33b2d33 = {int(_0x32e2cb0f): dict(_0x1043bfc7) for (_0x32e2cb0f, _0x1043bfc7) in _0xc3f62fb2.items()}
    if not _0xbb5e9d49:
        return _0xd33b2d33
    for (_0x06e1a2e9, _0xbe0a189d) in _0xbb5e9d49.items():
        _0x32e2cb0f = int(_0x06e1a2e9)
        _0xb466859d = dict(_0xbe0a189d)
        if _0x32e2cb0f not in _0xd33b2d33:
            _0xd33b2d33[_0x32e2cb0f] = _0xb466859d
            continue
        _0x6eed7d60 = dict(_0xd33b2d33[_0x32e2cb0f])
        for _0x73f329f1 in (_0xd14e4b1f('696e7374616e6365'), _0xd14e4b1f('6461746174797065'), _0xd14e4b1f('6265686176696f72'), _0xd14e4b1f('6d696e5f73'), _0xd14e4b1f('6d61785f73'), _0xd14e4b1f('6d696e5f75'), _0xd14e4b1f('6d61785f75'), _0xd14e4b1f('69735f696e7465726e616c')):
            if _0xb466859d.get(_0x73f329f1) is not None:
                _0x6eed7d60[_0x73f329f1] = _0xb466859d[_0x73f329f1]
        if _0xb466859d.get(_0xd14e4b1f('76657273696f6e')) is not None:
            _0x6eed7d60[_0xd14e4b1f('76657273696f6e')] = _0xb466859d[_0xd14e4b1f('76657273696f6e')]
            _0x6eed7d60[_0xd14e4b1f('7265706f727465645f76657273696f6e')] = _0xb466859d[_0xd14e4b1f('76657273696f6e')]
        _0xd33b2d33[_0x32e2cb0f] = _0x6eed7d60
    return _0xd33b2d33