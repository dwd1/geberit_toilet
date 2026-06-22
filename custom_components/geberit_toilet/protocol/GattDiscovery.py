from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from ..const import BLUETOOTH_SIG_BASE_SUFFIX, STANDARD_GEBERIT_SERVICE_UUID

GEBERIT_SERVICE_UUID = STANDARD_GEBERIT_SERVICE_UUID
_PROP_WRITE = 4
_PROP_WRITE_NO_RESP = 8
_PROP_NOTIFY = 16

@dataclass
class GattProfile:
    is_standard: bool
    svc_uuid: str
    write_uuids: List[str] = field(default_factory=list)
    notify_uuids: List[str] = field(default_factory=list)
    dis_info: dict | None = None
    arendi_handshake_done: bool = False

def _has_write(char) -> bool:
    props = char.properties
    if isinstance(props, int):
        return bool(props & (_PROP_WRITE | _PROP_WRITE_NO_RESP))
    if isinstance(props, (list, tuple)):
        return any((p in props for p in ('write', 'write-without-response')))
    return False

def _has_notify(char) -> bool:
    props = char.properties
    if isinstance(props, int):
        return bool(props & _PROP_NOTIFY)
    if isinstance(props, (list, tuple)):
        return 'notify' in props
    return False

def classify_services(services_iterable) -> GattProfile:
    try:
        services = list(services_iterable)
    except Exception:
        return GattProfile(is_standard=True, svc_uuid=GEBERIT_SERVICE_UUID)
    for svc in services:
        if svc.uuid.lower() == GEBERIT_SERVICE_UUID:
            return GattProfile(is_standard=True, svc_uuid=GEBERIT_SERVICE_UUID)
    for svc in services:
        svc_uuid = svc.uuid.lower()
        is_std_svc = svc_uuid.endswith(BLUETOOTH_SIG_BASE_SUFFIX) and svc_uuid.startswith('0000')
        has_vendor_chars = any((not (c.uuid.lower().endswith(BLUETOOTH_SIG_BASE_SUFFIX) and c.uuid.lower().startswith('0000')) for c in svc.characteristics))
        if is_std_svc and (not has_vendor_chars):
            continue
        write_uuids: list[str] = []
        notify_uuids: list[str] = []
        seen_handles: set = set()
        for char in svc.characteristics:
            handle = getattr(char, 'handle', None)
            if _has_write(char) and handle not in seen_handles:
                if handle is not None:
                    seen_handles.add(handle)
                write_uuids.append(char.uuid)
            if _has_notify(char):
                notify_uuids.append(char.uuid)
        if write_uuids and notify_uuids:
            return GattProfile(is_standard=False, svc_uuid=svc_uuid, write_uuids=write_uuids, notify_uuids=notify_uuids)
    return GattProfile(is_standard=False, svc_uuid='unknown')

def probe_gatt_profile(client) -> GattProfile:
    try:
        services = client.services
    except Exception:
        return GattProfile(is_standard=True, svc_uuid=GEBERIT_SERVICE_UUID)
    return classify_services(services)
