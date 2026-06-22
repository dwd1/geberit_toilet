from __future__ import annotations

import re

from .const import (
    COMMUNICATION_MODE_BOTH,
    COMMUNICATION_MODE_DPIDS,
    COMMUNICATION_MODE_GATT,
)


def parse_dpid_list(value: str | None) -> list[int]:
    if not value:
        return []

    dp_ids: list[int] = []
    seen: set[int] = set()

    for line in value.splitlines():
        content = line.split("#", 1)[0].strip()
        if not content:
            continue

        for token in re.split(r"[\s,;]+", content):
            if not token:
                continue

            try:
                dp_id = int(token, 10)
            except ValueError:
                continue

            if dp_id not in seen:
                seen.add(dp_id)
                dp_ids.append(dp_id)

    return dp_ids


def normalize_communication_mode(value: str | None) -> str:
    if value in (
        COMMUNICATION_MODE_DPIDS,
        COMMUNICATION_MODE_GATT,
        COMMUNICATION_MODE_BOTH,
    ):
        return value
    return COMMUNICATION_MODE_DPIDS
