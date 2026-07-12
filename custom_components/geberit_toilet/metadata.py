from __future__ import annotations
from .protocol import _0x27401bf3, _0x340e827c

def _0xd14e4b1f(h):
    return bytes.fromhex(h).decode('utf-8')
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import PERCENTAGE, UnitOfTime
from homeassistant.helpers.entity import EntityCategory
from .const import _0x847653f3
from .DpId import DpId
from .catalog import _0xb7aa207c
from .config_helpers import _0x34b55d2a

def _0x20567fc5(_0x3931108d, _0x56dda363, _0xc6a35ba1, _0x93da65a9):
    if _0x93da65a9:
        return _0x93da65a9
    if _0x3931108d == _0x340e827c._0x471c4cee:
        return (_0xd14e4b1f('6f6666'), _0xd14e4b1f('6f6e'), _0xd14e4b1f('6175746f'))
    if _0x3931108d == _0x340e827c._0xcf20423e and _0x56dda363 is not None and (_0xc6a35ba1 is not None):
        return tuple((str(_0x2063c160) for _0x2063c160 in range(_0x56dda363, _0xc6a35ba1 + 1)))
    return ()

def _0x73e4bf98(_0x3931108d, _0xb140af3d, _0x500f1c43, _0xc83e24cd, _0x93da65a9):
    if _0xb140af3d in (_0x27401bf3._0xee97be03, _0x27401bf3._0x922337c3):
        return _0xc9ed32a4._0x57b35198
    if _0x3931108d in (_0x340e827c._0xcf20423e, _0x340e827c._0x471c4cee) and _0xc83e24cd and _0x93da65a9:
        return _0xc9ed32a4._0x63225f19
    if _0x3931108d in (_0x340e827c._0x6ce976e8, _0x340e827c._0x084c8428):
        if _0xc83e24cd:
            return _0xc9ed32a4._0x4239f063
        if _0x500f1c43:
            return _0xc9ed32a4._0x9dc7bd04
    if _0xc83e24cd and _0x3931108d not in (None, _0x340e827c._0x27118326, _0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
        return _0xc9ed32a4._0x34f55eca
    if _0x500f1c43:
        return _0xc9ed32a4._0x72700b6a
    return _0xc9ed32a4._0x696b0310

class _0xc9ed32a4(str, Enum):
    _0x72700b6a = _0xd14e4b1f('73656e736f72')
    _0x9dc7bd04 = _0xd14e4b1f('62696e6172795f73656e736f72')
    _0x34f55eca = _0xd14e4b1f('6e756d626572')
    _0x63225f19 = _0xd14e4b1f('73656c656374')
    _0x4239f063 = _0xd14e4b1f('737769746368')
    _0x57b35198 = _0xd14e4b1f('627574746f6e')
    _0x696b0310 = _0xd14e4b1f('756e6b6e6f776e')
_0x58b529d0: frozenset[int] = frozenset(_0x847653f3)
_0x27d94169: dict[int, dict[str, Any]] = {int(382): {_0xd14e4b1f('6f7074696f6e73'): [_0xd14e4b1f('626c7565'), _0xd14e4b1f('74757271756f697365'), _0xd14e4b1f('6d6167656e7461'), _0xd14e4b1f('6f72616e6765'), _0xd14e4b1f('79656c6c6f77'), _0xd14e4b1f('726564'), _0xd14e4b1f('7768697465')]}, int(62): {_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): False}, int(63): {_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): False}, int(83): {_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): False}, int(153): {_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): False}, int(373): {_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74'): False}}
_0x9fcb580e: dict[int, dict[int, tuple[str, ...]]] = {int(17): {0: (_0xd14e4b1f('62617474657279'), _0xd14e4b1f('6d61696e7320737570706c79'))}, int(23): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'), _0xd14e4b1f('4175746f'))}, int(24): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(25): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(26): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(34): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(37): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(39): {0: (_0xd14e4b1f('302028667265736829'), _0xd14e4b1f('31'), _0xd14e4b1f('32'), _0xd14e4b1f('33'), _0xd14e4b1f('342028776f726e206f757429'))}, int(44): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'), _0xd14e4b1f('4175746f'))}, int(45): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(46): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(47): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(55): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(58): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(62): {0: (_0xd14e4b1f('45786563757465'),)}, int(63): {0: (_0xd14e4b1f('45786563757465'),)}, int(71): {0: (_0xd14e4b1f('45786563757465'),)}, int(72): {0: (_0xd14e4b1f('436c6f736564'), _0xd14e4b1f('4f70656e6564'), _0xd14e4b1f('556e646566696e6564'))}, int(77): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'), _0xd14e4b1f('32'))}, int(78): {0: (_0xd14e4b1f('535444'), _0xd14e4b1f('4357'), _0xd14e4b1f('4f4646'))}, int(83): {0: (_0xd14e4b1f('45786563757465'),), 1: (_0xd14e4b1f('53544d20626f6f746c6f61646572'), _0xd14e4b1f('4765626572697420626f6f746c6f61646572'))}, int(85): {0: (_0xd14e4b1f('45786563757465'),)}, int(89): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('52656164'), _0xd14e4b1f('526561642f5772697465'))}, int(95): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(112): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(114): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(115): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(118): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(119): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(120): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e')), 1: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(121): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(123): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(125): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(126): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e')), 1: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(127): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(129): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(130): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e')), 1: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(137): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(140): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(141): {0: (_0xd14e4b1f('45786563757465'),)}, int(143): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(150): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(151): {0: (_0xd14e4b1f('45786563757465'),)}, int(152): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('72756e6e696e67'), _0xd14e4b1f('7375636365737366756c'), _0xd14e4b1f('6661696c6564'))}, int(153): {0: (_0xd14e4b1f('45786563757465'),)}, int(160): {0: (_0xd14e4b1f('6f6666'), _0xd14e4b1f('6175746f'), _0xd14e4b1f('64796e616d6963')), 1: (_0xd14e4b1f('6f6666'), _0xd14e4b1f('737461746963'), _0xd14e4b1f('64796e616d6963'), _0xd14e4b1f('6175746f'))}, int(161): {0: (_0xd14e4b1f('6e6f20646574656374696f6e'), _0xd14e4b1f('737461746963'), _0xd14e4b1f('64796e616d6963'))}, int(162): {0: (_0xd14e4b1f('6f6666'), _0xd14e4b1f('6175746f'), _0xd14e4b1f('64796e616d6963')), 1: (_0xd14e4b1f('6f6666'), _0xd14e4b1f('737461746963'), _0xd14e4b1f('64796e616d6963'), _0xd14e4b1f('6175746f'))}, int(163): {0: (_0xd14e4b1f('6e6f20646574656374696f6e'), _0xd14e4b1f('737461746963'), _0xd14e4b1f('64796e616d6963'))}, int(164): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(165): {0: (_0xd14e4b1f('6e6f74206465746563746564'), _0xd14e4b1f('6465746563746564'))}, int(167): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('72756e6e696e67'), _0xd14e4b1f('756e696e697469616c697a6564'))}, int(172): {0: (_0xd14e4b1f('45786563757465'),)}, int(173): {0: (_0xd14e4b1f('636c6f736564'), _0xd14e4b1f('6f70656e'))}, int(174): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('72756e6e696e67'))}, int(176): {0: (_0xd14e4b1f('45786563757465'),)}, int(180): {0: (_0xd14e4b1f('6e6f726d616c'), _0xd14e4b1f('77617465722d736176696e67')), 1: (_0xd14e4b1f('6e6f726d616c'), _0xd14e4b1f('7363727562'), _0xd14e4b1f('6d65746572696e67'), _0xd14e4b1f('77617465722d736176696e67'), _0xd14e4b1f('68616e6477617368'), _0xd14e4b1f('766f6c756d65'))}, int(183): {0: (_0xd14e4b1f('72656c6561736564'), _0xd14e4b1f('70726573736564')), 1: (_0xd14e4b1f('72656c6561736564'), _0xd14e4b1f('70726573736564')), 2: (_0xd14e4b1f('72656c6561736564'), _0xd14e4b1f('70726573736564'))}, int(184): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(185): {0: (_0xd14e4b1f('7374616e646172642031'), _0xd14e4b1f('7374616e646172642032'), _0xd14e4b1f('7374616e646172642033'), _0xd14e4b1f('637573746f6d'))}, int(191): {0: (_0xd14e4b1f('45786563757465'),)}, int(202): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(203): {0: (_0xd14e4b1f('696e616374697665202868696768207261746529'), _0xd14e4b1f('61637469766520286c6f77207261746529'))}, int(205): {0: (_0xd14e4b1f('6575726f7065'), _0xd14e4b1f('757361'))}, int(206): {0: (_0xd14e4b1f('313120746f203134206d6d'), _0xd14e4b1f('313620746f203139206d6d'), _0xd14e4b1f('323120746f203234206d6d'), _0xd14e4b1f('323620746f203239206d6d'), _0xd14e4b1f('333120746f203333206d6d'))}, int(213): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(216): {0: (_0xd14e4b1f('322078'), _0xd14e4b1f('382078'), _0xd14e4b1f('33322078'), _0xd14e4b1f('3132382078'))}, int(219): {0: (_0xd14e4b1f('322078'), _0xd14e4b1f('382078'), _0xd14e4b1f('33322078'), _0xd14e4b1f('3132382078'))}, int(222): {0: (_0xd14e4b1f('322078'), _0xd14e4b1f('382078'), _0xd14e4b1f('33322078'), _0xd14e4b1f('3132382078'))}, int(235): {0: (_0xd14e4b1f('3134206c2f6d696e'), _0xd14e4b1f('39206c2f6d696e'))}, int(272): {0: (_0xd14e4b1f('7374616e646172642031'), _0xd14e4b1f('7374616e646172642032'), _0xd14e4b1f('7374616e646172642033'), _0xd14e4b1f('7374616e646172642034'), _0xd14e4b1f('637573746f6d'))}, int(279): {0: (_0xd14e4b1f('31333030206d6c2f6d696e'), _0xd14e4b1f('31393030206d6c2f6d696e'), _0xd14e4b1f('33383030206d6c2f6d696e'), _0xd14e4b1f('35303030206d6c2f6d696e'), _0xd14e4b1f('637573746f6d')), 1: (_0xd14e4b1f('31333030206d6c2f6d696e'), _0xd14e4b1f('31393030206d6c2f6d696e'), _0xd14e4b1f('33383030206d6c2f6d696e'), _0xd14e4b1f('36303030206d6c2f6d696e'), _0xd14e4b1f('637573746f6d')), 2: (_0xd14e4b1f('39206c2f6d696e'), _0xd14e4b1f('3134206c2f6d696e'), _0xd14e4b1f('3138206c2f6d696e'), _0xd14e4b1f('637573746f6d'))}, int(281): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(282): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(283): {0: (_0xd14e4b1f('7374616e64617264'), _0xd14e4b1f('6175746f'), _0xd14e4b1f('68696768207265666c656374697665'))}, int(284): {0: (_0xd14e4b1f('73686f7274'), _0xd14e4b1f('6d656469756d'), _0xd14e4b1f('6c6f6e67'))}, int(285): {0: (_0xd14e4b1f('55736572'), _0xd14e4b1f('48616e64'), _0xd14e4b1f('50726573656e6365'))}, int(300): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(301): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(315): {0: (_0xd14e4b1f('372c35206c2f6d696e'), _0xd14e4b1f('36206c2f6d696e'), _0xd14e4b1f('342c35206c2f6d696e'), _0xd14e4b1f('637573746f6d'), _0xd14e4b1f('34'))}, int(327): {0: (_0xd14e4b1f('427574746f6e'), _0xd14e4b1f('537769746368'))}, int(328): {0: (_0xd14e4b1f('4e6f726d616c206f7065726174696f6e'), _0xd14e4b1f('3056'), _0xd14e4b1f('332e3956'), _0xd14e4b1f('342e3556')), 1: (_0xd14e4b1f('4e6f726d616c206f7065726174696f6e'), _0xd14e4b1f('3056'), _0xd14e4b1f('313256')), 2: (_0xd14e4b1f('4e6f726d616c206f7065726174696f6e'), _0xd14e4b1f('3056'), _0xd14e4b1f('3556287374616e64627929'), _0xd14e4b1f('313256'))}, int(330): {0: (_0xd14e4b1f('4e6f726d616c206f7065726174696f6e'), _0xd14e4b1f('4f6666'), _0xd14e4b1f('436f6c6f722031'), _0xd14e4b1f('436f6c6f722032'), _0xd14e4b1f('426f7468')), 1: (_0xd14e4b1f('4e6f726d616c206f7065726174696f6e'), _0xd14e4b1f('4f6666'), _0xd14e4b1f('436f6c6f722031'), _0xd14e4b1f('436f6c6f722032'), _0xd14e4b1f('426f7468'))}, int(342): {0: (_0xd14e4b1f('45786563757465'),)}, int(344): {0: (_0xd14e4b1f('4f7269656e746174696f6e204d6f6f64'), _0xd14e4b1f('43616e646c65204d6f6f64'), _0xd14e4b1f('5374616e64617264204d6f6f64'), _0xd14e4b1f('576f726b204d6f6f64'))}, int(346): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(349): {0: (_0xd14e4b1f('4f7269656e746174696f6e204d6f6f64'), _0xd14e4b1f('43616e646c65204d6f6f64'), _0xd14e4b1f('5374616e64617264204d6f6f64'), _0xd14e4b1f('576f726b204d6f6f64'))}, int(352): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(353): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(355): {0: (_0xd14e4b1f('3056'), _0xd14e4b1f('332e3956'), _0xd14e4b1f('342e3556')), 1: (_0xd14e4b1f('3056'), _0xd14e4b1f('313256')), 2: (_0xd14e4b1f('3056'), _0xd14e4b1f('3556287374616e64627929'), _0xd14e4b1f('313256'))}, int(356): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(357): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(358): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(359): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(360): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(361): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(362): {0: (_0xd14e4b1f('363020636d'), _0xd14e4b1f('373520636d'), _0xd14e4b1f('393020636d'), _0xd14e4b1f('31303520636d'), _0xd14e4b1f('31323020636d'), _0xd14e4b1f('31333520636d'), _0xd14e4b1f('31353020636d'))}, int(363): {0: (_0xd14e4b1f('4869676820506f776572203839332e3335372f382f392e30302e30'), _0xd14e4b1f('4c6f7720506f776572203839332e3336312f322f332e30302e30'))}, int(368): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(372): {0: (_0xd14e4b1f('57616974466f72557365'), _0xd14e4b1f('5573616765'), _0xd14e4b1f('576169744166746572557365'), _0xd14e4b1f('466c757368696e67'), _0xd14e4b1f('466c7573684f76657272756e'), _0xd14e4b1f('576169744166746572466c757368'), _0xd14e4b1f('556e75736564'), _0xd14e4b1f('556e75736564'), _0xd14e4b1f('556e75736564'), _0xd14e4b1f('556e75736564'), _0xd14e4b1f('466c7573684c6f636b6564'), _0xd14e4b1f('466c757368426c6f636b6564'), _0xd14e4b1f('466c757368496e74657276616c'))}, int(373): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(380): {0: (_0xd14e4b1f('4e6f74204465746563746564'), _0xd14e4b1f('4465746563746564'))}, int(381): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(382): {0: (_0xd14e4b1f('726f74'), _0xd14e4b1f('677275656e'), _0xd14e4b1f('626c6175'), _0xd14e4b1f('33'))}, int(383): {0: (_0xd14e4b1f('4c696768746d6f6465206f6666'), _0xd14e4b1f('4c696768746d6f6465206f6e'), _0xd14e4b1f('4c696768746d6f64652064796e616d6963'))}, int(384): {0: (_0xd14e4b1f('426c7565'), _0xd14e4b1f('4379616e'), _0xd14e4b1f('4d6167656e7461'), _0xd14e4b1f('4f72616e6765'), _0xd14e4b1f('59656c6c6f77'))}, int(387): {0: (_0xd14e4b1f('73656872206e6168'), _0xd14e4b1f('6e6168'), _0xd14e4b1f('6e6f726d616c'), _0xd14e4b1f('6665726e'), _0xd14e4b1f('73656872206665726e'))}, int(388): {0: (_0xd14e4b1f('73656872206e6168'), _0xd14e4b1f('6e6168'), _0xd14e4b1f('6e6f726d616c'), _0xd14e4b1f('6665726e'), _0xd14e4b1f('73656872206665726e'))}, int(396): {0: (_0xd14e4b1f('6c6f77506f776572'), _0xd14e4b1f('6d6964506f776572'), _0xd14e4b1f('68696768506f776572'))}, int(397): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('72756e6e696e67'))}, int(398): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('72756e6e696e67'))}, int(399): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(545): {0: (_0xd14e4b1f('69646c65'), _0xd14e4b1f('636f6e6e656374696e67'))}, int(548): {0: (_0xd14e4b1f('4f6666'), _0xd14e4b1f('4f6e'))}, int(32518): {0: (_0xd14e4b1f('456e756d2030'), _0xd14e4b1f('456e756d2031'), _0xd14e4b1f('456e756d2032'), _0xd14e4b1f('456e756d2033')), 1: (_0xd14e4b1f('456e756d2030'), _0xd14e4b1f('456e756d2031'), _0xd14e4b1f('456e756d2032'), _0xd14e4b1f('456e756d2033'), _0xd14e4b1f('456e756d2034'), _0xd14e4b1f('456e756d2035'))}, int(32529): {0: (_0xd14e4b1f('4f444f55525f45585452414354494f4e'), _0xd14e4b1f('4f5249454e544154494f4e5f4c49474854'), _0xd14e4b1f('5553455f574954485f464c555348'), _0xd14e4b1f('464c5553485f574954484f55545f555345'), _0xd14e4b1f('5553455f46465f4155544f4d41544943'), _0xd14e4b1f('5553455f46465f4d414e55414c'), _0xd14e4b1f('494e54455256414c5f464c5553484553'), _0xd14e4b1f('5553455f50465f4d414e55414c'), _0xd14e4b1f('46554c4c5f464c5553484553'), _0xd14e4b1f('5553455f574954484f55545f464c555348'), _0xd14e4b1f('504f5745525f4f4e5f464c5553484553'), _0xd14e4b1f('3131'), _0xd14e4b1f('3132'), _0xd14e4b1f('3133'), _0xd14e4b1f('3134'), _0xd14e4b1f('3135'), _0xd14e4b1f('3136'), _0xd14e4b1f('3137'), _0xd14e4b1f('3138'), _0xd14e4b1f('3139'), _0xd14e4b1f('3230'))}, int(32530): {0: (_0xd14e4b1f('45786563757465'),)}}

def _0xdcc10bc1(_0x8512ae7d):
    _0x321c3cf4 = _0x34b55d2a(_0x8512ae7d)
    _0xd58c8b05 = _0x321c3cf4.get(_0xd14e4b1f('73656c6563746f72'), {})
    _0xa8998c31 = _0xd58c8b05.get(_0xd14e4b1f('6d657461646174615f6e616d6573'), {})
    return {str(_0x3c6e0b8a): str(_0x2063c160) for (_0x3c6e0b8a, _0x2063c160) in _0xa8998c31.items() if _0x2063c160}

@dataclass(frozen=True)
class _0xfb98c9d8:
    _0x32e2cb0f: int
    name: str
    key: str
    _0x3931108d: _0x340e827c | None
    _0xb140af3d: _0x27401bf3 | None
    _0x56dda363: int | None
    _0xc6a35ba1: int | None
    _0x500f1c43: bool
    _0xc83e24cd: bool
    _0x09f821ba: bool
    _0x7123a699: int
    _0x2af72f10: int
    options: tuple[str, ...] = ()
    _0xe84e5b08: BinarySensorDeviceClass | None = None
    _0x662f707d: bool = False
    entity_category: EntityCategory | None = None
    entity_registry_enabled_default: bool = True
    _0xd706b7c5: bool = True
    _0x67daf92c: str = ''
    _0x4ad9a0ea: tuple[str, ...] = ()

    @property
    def unit(self):
        if self._0x3931108d == _0x340e827c._0x8f19a8c7:
            return UnitOfTime.SECONDS
        if self._0x3931108d == _0x340e827c._0xf670ea66:
            return UnitOfTime.MINUTES
        if self._0x3931108d == _0x340e827c._0x6a7e7316:
            return UnitOfTime.HOURS
        if self._0x3931108d == _0x340e827c._0xadaaee4b:
            return PERCENTAGE
        if self._0x3931108d == _0x340e827c._0xc442a6c2:
            return _0xd14e4b1f('7065726d696c6c65')
        return None

    @property
    def sensor_device_class(self):
        if self._0x3931108d in (_0x340e827c._0x8f19a8c7, _0x340e827c._0xf670ea66, _0x340e827c._0x6a7e7316):
            return SensorDeviceClass.DURATION
        if self._0x3931108d in (_0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
            return SensorDeviceClass.TIMESTAMP
        if self._0x3931108d == _0x340e827c._0xadaaee4b:
            return None
        return None

    @property
    def sensor_state_class(self):
        if self._0x3931108d in (_0x340e827c._0x8f19a8c7, _0x340e827c._0xf670ea66, _0x340e827c._0x6a7e7316, _0x340e827c._0xadaaee4b, _0x340e827c._0xc442a6c2, _0x340e827c._0x71fed0c3, _0x340e827c._0x64d12922):
            return SensorStateClass.MEASUREMENT
        return None

    @property
    def preferred_kind(self):
        return _0x73e4bf98(self._0x3931108d, self._0xb140af3d, self._0x500f1c43, self._0xc83e24cd, self.options_for_select())

    def options_for_select(self):
        return _0x20567fc5(self._0x3931108d, self._0x56dda363, self._0xc6a35ba1, self.options)

def _0x84320d2b(_0x2063c160):
    try:
        return _0x340e827c(int(_0x2063c160))
    except (TypeError, ValueError):
        return None

def _0xf552722e(_0x2063c160):
    try:
        return _0x27401bf3(int(_0x2063c160))
    except (TypeError, ValueError):
        return None

def _0xd484feef(_0x32e2cb0f):
    try:
        _0x6ea1fd1b = DpId(_0x32e2cb0f)
        return _0x6ea1fd1b.name.lower().removeprefix(_0xd14e4b1f('64705f'))
    except ValueError:
        return f"{_0xd14e4b1f('647069645f')}{_0x32e2cb0f}"

def _0x91b2b639(_0x3c6e0b8a):
    return _0x3c6e0b8a.replace(_0xd14e4b1f('5f'), _0xd14e4b1f('20')).title()

def _0x9839fddd(_0x2063c160, _0xc21f969b=0):
    try:
        if _0x2063c160 is None:
            return _0xc21f969b
        return int(_0x2063c160)
    except (TypeError, ValueError):
        return _0xc21f969b

def _0x39b4dc45(_0x2063c160):
    if _0x2063c160 is None:
        return None
    if isinstance(_0x2063c160, bool):
        return _0x2063c160
    if isinstance(_0x2063c160, (int, float)):
        return bool(_0x2063c160)
    if isinstance(_0x2063c160, str):
        _0x14f42e76 = _0x2063c160.strip().lower()
        if _0x14f42e76 in {_0xd14e4b1f('31'), _0xd14e4b1f('74727565'), _0xd14e4b1f('796573'), _0xd14e4b1f('6f6e')}:
            return True
        if _0x14f42e76 in {_0xd14e4b1f('30'), _0xd14e4b1f('66616c7365'), _0xd14e4b1f('6e6f'), _0xd14e4b1f('6f6666')}:
            return False
    return None

def _0xd316edcb(_0x3c6e0b8a, _0x3931108d, _0xb140af3d):
    if _0x3931108d not in (_0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
        return True
    if _0xb140af3d != _0x27401bf3._0xec53a8c4:
        return True
    _0xb95fd33c = _0x3c6e0b8a.lower()
    _0x2d45a8a8 = (_0xd14e4b1f('74696d65'), _0xd14e4b1f('636c6f636b'), _0xd14e4b1f('727463'), _0xd14e4b1f('6c6f63616c'), _0xd14e4b1f('757463'))
    if not any((_0x94a08da1 in _0xb95fd33c for _0x94a08da1 in _0x2d45a8a8)):
        return True
    _0xbd8c87fa = (_0xd14e4b1f('6261636b7570'), _0xd14e4b1f('696e7374616c6c6174696f6e'), _0xd14e4b1f('70726f64756374696f6e'), _0xd14e4b1f('6368616e67655f6f766572'), _0xd14e4b1f('6d6f6d656e74'), _0xd14e4b1f('74696d657374616d70'), _0xd14e4b1f('64617465'))
    if any((_0x94a08da1 in _0xb95fd33c for _0x94a08da1 in _0xbd8c87fa)):
        return True
    return False

def _0x79ac0181(_0x3c6e0b8a, _0x3931108d, _0xb140af3d):
    if _0x3931108d not in (_0x340e827c._0x6ce976e8, _0x340e827c._0x084c8428):
        return None
    if _0xb140af3d not in (_0x27401bf3._0x4059b025, _0x27401bf3._0xec53a8c4, _0x27401bf3._0x5208b345, _0x27401bf3._0x56f0605c):
        return None
    _0xb95fd33c = _0x3c6e0b8a.lower()
    if _0xd14e4b1f('646f6f72') in _0xb95fd33c:
        return BinarySensorDeviceClass.DOOR
    if _0xd14e4b1f('706f7765725f737570706c79') in _0xb95fd33c or _0xb95fd33c == _0xd14e4b1f('706f7765725f737570706c79'):
        return BinarySensorDeviceClass.PLUG
    if _0xd14e4b1f('73656e736f725f6d6f7665') in _0xb95fd33c or _0xd14e4b1f('6d6f74696f6e') in _0xb95fd33c:
        return BinarySensorDeviceClass.MOTION
    if any((_0x94a08da1 in _0xb95fd33c for _0x94a08da1 in (_0xd14e4b1f('6572726f72'), _0xd14e4b1f('6661756c74'), _0xd14e4b1f('616c61726d'), _0xd14e4b1f('6368616e6765'), _0xd14e4b1f('64697361626c6564')))):
        return BinarySensorDeviceClass.PROBLEM
    return None

def _0x3d83b33a(_0x3c6e0b8a, _0x3931108d, _0xb140af3d, _0xd939aaf7):
    if _0xb140af3d in (_0x27401bf3._0xee97be03, _0x27401bf3._0x922337c3):
        return None
    if _0xd939aaf7 not in (_0xc9ed32a4._0x72700b6a, _0xc9ed32a4._0x9dc7bd04):
        return None
    if _0x3931108d in (_0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
        return EntityCategory.DIAGNOSTIC
    _0xb95fd33c = _0x3c6e0b8a.lower()
    _0x89759e12 = _0xb95fd33c.split(_0xd14e4b1f('5f'))
    _0xc07da09d = {_0xd14e4b1f('6970'), _0xd14e4b1f('69707634'), _0xd14e4b1f('69707636'), _0xd14e4b1f('6d6163'), _0xd14e4b1f('756964'), _0xd14e4b1f('6964')}
    if any((_0xf1290186 in _0xc07da09d for _0xf1290186 in _0x89759e12)):
        return EntityCategory.DIAGNOSTIC
    _0xfdfa2417 = (_0xd14e4b1f('73657269616c'), _0xd14e4b1f('76657273696f6e'), _0xd14e4b1f('70726f64756374696f6e'), _0xd14e4b1f('696e7374616c6c6174696f6e'), _0xd14e4b1f('736170'), _0xd14e4b1f('7761746368646f67'), _0xd14e4b1f('666174616c'), _0xd14e4b1f('71756172747a'), _0xd14e4b1f('67627573'), _0xd14e4b1f('696463'), _0xd14e4b1f('68617368'), _0xd14e4b1f('6c6f61646572'), _0xd14e4b1f('776972656c6573735f737461636b'), _0xd14e4b1f('737461746973746963'), _0xd14e4b1f('636f756e746572'), _0xd14e4b1f('6261636b7570'), _0xd14e4b1f('727463'), _0xd14e4b1f('6f6666736574'), _0xd14e4b1f('72657365727665'), _0xd14e4b1f('696e666f726d6174696f6e'), _0xd14e4b1f('736572696573'), _0xd14e4b1f('76617269616e74'), _0xd14e4b1f('736563726574'), _0xd14e4b1f('6d6f6d656e74'), _0xd14e4b1f('6e756d626572'), _0xd14e4b1f('61646472657373'), _0xd14e4b1f('7a6f6e65'))
    if any((any((_0x94a08da1 in _0xc47d1870 for _0xc47d1870 in _0x89759e12)) for _0x94a08da1 in _0xfdfa2417)):
        return EntityCategory.DIAGNOSTIC
    return None

def _0x64a7c4d5(_0x7a1eabc3):
    if not _0x7a1eabc3:
        return {}
    _0x9f81f3c0 = {}
    for (_0x06e1a2e9, _0xa4ade155) in _0x7a1eabc3.items():
        _0x32e2cb0f = int(_0x06e1a2e9)
        _0xe3b3f566 = _0x27d94169.get(_0x32e2cb0f, {})
        _0x4ea76ebf = _0x9839fddd(_0xa4ade155.get(_0xd14e4b1f('76657273696f6e')), 0)
        _0x93da65a9 = _0xe3b3f566.get(_0xd14e4b1f('6f7074696f6e73'))
        if not _0x93da65a9:
            _0x93da65a9 = _0x9fcb580e.get(_0x32e2cb0f, {}).get(_0x4ea76ebf)
        if not _0x93da65a9:
            _0x93da65a9 = _0x9fcb580e.get(_0x32e2cb0f, {}).get(0, ())
        _0x3c6e0b8a = str(_0xa4ade155.get(_0xd14e4b1f('6b6579')) or _0xe3b3f566.get(_0xd14e4b1f('6b6579')) or _0xd484feef(_0x32e2cb0f))
        _0xa68071d3 = _0x3c6e0b8a.upper()
        if not _0xa68071d3.startswith(_0xd14e4b1f('44505f')):
            _0xa68071d3 = f"{_0xd14e4b1f('44505f')}{_0xa68071d3}"
        _0xe5c6ed4b = _0xb7aa207c(_0xa68071d3, _0x2af72f10=_0xa4ade155.get(_0xd14e4b1f('76657273696f6e')), _0x6fa93254=_0xa4ade155.get(_0xd14e4b1f('696e7374616e6365')))
        _0x3931108d = _0x84320d2b(_0xa4ade155.get(_0xd14e4b1f('6461746174797065')))
        _0xab1999dc = _0x3931108d in (None, _0x340e827c._0x92e592d9)
        if _0xab1999dc and _0xe5c6ed4b is not None:
            _0x3931108d = _0x84320d2b(_0xe5c6ed4b._0x3931108d)
        _0xb140af3d = _0xf552722e(_0xa4ade155.get(_0xd14e4b1f('6265686176696f72')))
        if (_0xb140af3d is None or _0xab1999dc) and _0xe5c6ed4b is not None:
            _0xb140af3d = getattr(_0x27401bf3, _0xe5c6ed4b._0xb140af3d, None)
        _0x56dda363 = _0xa4ade155.get(_0xd14e4b1f('6d696e5f73'))
        _0xc6a35ba1 = _0xa4ade155.get(_0xd14e4b1f('6d61785f73'))
        if _0x3931108d not in (_0x340e827c._0x71fed0c3, _0x340e827c._0x27118326, _0x340e827c._0x95cc683e, _0x340e827c._0x3b3e62b3):
            _0x56dda363 = _0xa4ade155.get(_0xd14e4b1f('6d696e5f75'))
            _0xc6a35ba1 = _0xa4ade155.get(_0xd14e4b1f('6d61785f75'))
        if (_0x56dda363 is None or _0xab1999dc) and _0xe5c6ed4b is not None:
            _0x56dda363 = _0xe5c6ed4b._0x56dda363
        if (_0xc6a35ba1 is None or _0xab1999dc) and _0xe5c6ed4b is not None:
            _0xc6a35ba1 = _0xe5c6ed4b._0xc6a35ba1
        _0x500f1c43 = _0x39b4dc45(_0xa4ade155.get(_0xd14e4b1f('7265616461626c65')))
        if _0x500f1c43 is None:
            _0x500f1c43 = _0x39b4dc45(_0xe3b3f566.get(_0xd14e4b1f('7265616461626c65')))
        if _0x500f1c43 is None:
            _0x500f1c43 = _0xb140af3d in (_0x27401bf3._0x4059b025, _0x27401bf3._0xec53a8c4, _0x27401bf3._0x5208b345, _0x27401bf3._0x56f0605c)
        _0xc83e24cd = _0x39b4dc45(_0xa4ade155.get(_0xd14e4b1f('7772697461626c65')))
        if _0xc83e24cd is None:
            _0xc83e24cd = _0x39b4dc45(_0xe3b3f566.get(_0xd14e4b1f('7772697461626c65')))
        if _0xc83e24cd is None:
            _0xc83e24cd = _0xb140af3d in (_0x27401bf3._0xee97be03, _0x27401bf3._0x5208b345, _0x27401bf3._0x922337c3)
        _0x09f821ba = _0x39b4dc45(_0xa4ade155.get(_0xd14e4b1f('6e6f7469666961626c65')))
        if _0x09f821ba is None:
            _0x09f821ba = _0xb140af3d == _0x27401bf3._0xec53a8c4
        _0x106847c9 = _0xa4ade155.get(_0xd14e4b1f('6d657461646174615f6e616d65')) or _0xa4ade155.get(_0xd14e4b1f('6e616d65'))
        if _0x106847c9 is not None:
            _0x106847c9 = str(_0x106847c9).strip()
        if not _0x106847c9:
            _0x106847c9 = _0xe3b3f566.get(_0xd14e4b1f('6e616d65')) or _0x91b2b639(_0x3c6e0b8a)
        _0xe9faac4e = _0xe3b3f566.get(_0xd14e4b1f('656e746974795f63617465676f7279'))
        _0x98a8fb82 = _0xe5c6ed4b._0x67daf92c if _0xe5c6ed4b is not None else ''
        _0xa6e9ffec = tuple(_0xe5c6ed4b._0x4ad9a0ea or []) if _0xe5c6ed4b is not None else ()
        _0xe28636b8 = tuple(_0x93da65a9 or ())
        _0xeb4112b6 = _0x20567fc5(_0x3931108d, int(_0x56dda363) if _0x56dda363 is not None else None, int(_0xc6a35ba1) if _0xc6a35ba1 is not None else None, _0xe28636b8)
        _0xd939aaf7 = _0x73e4bf98(_0x3931108d, _0xb140af3d, _0x500f1c43, _0xc83e24cd, _0xeb4112b6)
        if _0xe9faac4e is None:
            _0xe9faac4e = _0x3d83b33a(_0x3c6e0b8a, _0x3931108d, _0xb140af3d, _0xd939aaf7)
        if _0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74') in _0xe3b3f566:
            _0x8840caf4 = bool(_0xe3b3f566[_0xd14e4b1f('656e746974795f72656769737472795f656e61626c65645f64656661756c74')])
        elif _0x3931108d == _0x340e827c._0x8f19a8c7 and _0xd939aaf7 in (_0xc9ed32a4._0x72700b6a, _0xc9ed32a4._0x9dc7bd04):
            _0x8840caf4 = False
        else:
            _0x8840caf4 = not (_0xe5c6ed4b._0xc80e6e0d if _0xe5c6ed4b is not None else False)
        _0x9f81f3c0[_0x32e2cb0f] = _0xfb98c9d8(_0x32e2cb0f=_0x32e2cb0f, name=_0x106847c9, key=_0x3c6e0b8a, _0x3931108d=_0x3931108d, _0xb140af3d=_0xb140af3d, _0x56dda363=int(_0x56dda363) if _0x56dda363 is not None else None, _0xc6a35ba1=int(_0xc6a35ba1) if _0xc6a35ba1 is not None else None, _0x500f1c43=_0x500f1c43, _0xc83e24cd=_0xc83e24cd, _0x09f821ba=_0x09f821ba, _0x7123a699=_0x9839fddd(_0xa4ade155.get(_0xd14e4b1f('696e7374616e6365')), 0), _0x2af72f10=_0x9839fddd(_0xa4ade155.get(_0xd14e4b1f('76657273696f6e')), 0), options=tuple(_0x93da65a9 or ()), _0xe84e5b08=_0xe3b3f566.get(_0xd14e4b1f('62696e6172795f73656e736f725f6465766963655f636c617373'), _0x79ac0181(_0x3c6e0b8a, _0x3931108d, _0xb140af3d)), _0x662f707d=_0x32e2cb0f in _0x58b529d0 or bool(_0xe3b3f566.get(_0xd14e4b1f('68696464656e'), False)), entity_category=_0xe9faac4e, entity_registry_enabled_default=_0x8840caf4, _0xd706b7c5=bool(_0xe3b3f566.get(_0xd14e4b1f('7375627363726962655f6e6f74696669636174696f6e73'), _0xd316edcb(_0x3c6e0b8a, _0x3931108d, _0xb140af3d))), _0x67daf92c=_0x98a8fb82, _0x4ad9a0ea=_0xa6e9ffec)
    return _0x9f81f3c0

def _0x18c49331(_0xe9a23cbc, _0x2063c160, _0x2716a391=0):
    if _0x2063c160 is None:
        return None
    if _0xe9a23cbc._0x3931108d == _0x340e827c._0x95cc683e:
        try:
            return datetime.fromtimestamp(int(_0x2063c160), timezone.utc)
        except (TypeError, ValueError, OverflowError):
            return None
    if _0xe9a23cbc._0x3931108d == _0x340e827c._0x3b3e62b3:
        try:
            return datetime.fromtimestamp(int(_0x2063c160) - int(_0x2716a391), timezone.utc)
        except (TypeError, ValueError, OverflowError):
            return None
    if _0xe9a23cbc._0x3931108d == _0x340e827c._0xcf20423e and _0xe9a23cbc.options:
        try:
            _0x7f9bec28 = int(_0x2063c160)
        except (TypeError, ValueError):
            return _0x2063c160
        if 0 <= _0x7f9bec28 < len(_0xe9a23cbc.options):
            return _0xe9a23cbc.options[_0x7f9bec28]
    return _0x2063c160