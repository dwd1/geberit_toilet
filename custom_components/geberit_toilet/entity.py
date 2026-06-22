from __future__ import annotations
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from . import GeberitToiletConfigEntry
from .const import CONF_DEVICE_ID, DOMAIN
from .coordinator import GeberitToiletCoordinator
from .device_types import get_model_name
from .protocol.DpId import DpId

class GeberitToiletEntity(CoordinatorEntity[GeberitToiletCoordinator]):
    _attr_has_entity_name = True

    def __init__(self, coordinator: GeberitToiletCoordinator, entry: GeberitToiletConfigEntry) -> None:
        super().__init__(coordinator)
        self._entry = entry
        self._device_id = entry.data[CONF_DEVICE_ID]

    @property
    def device_info(self) -> DeviceInfo:
        data = self.coordinator.data or {}
        series_id = data.get(DpId.DP_DEVICE_SERIES)
        variant_id = data.get(DpId.DP_DEVICE_VARIANT)
        model = get_model_name(series_id, variant_id)
        name = model

        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            connections={(dr.CONNECTION_NETWORK_MAC, self._device_id)},
            name=name,
            manufacturer='Geberit',
            model=model,
        )

    def _metadata_attributes(self, dp_id: int | DpId | None) -> dict[str, object]:
        meta = self.coordinator.get_dp_metadata(dp_id)
        if meta is None:
            return {}
        attrs: dict[str, object] = {'dp_id': int(meta.dp_id), 'dp_key': meta.key, 'dp_datatype': meta.datatype.name if meta.datatype else None, 'dp_behavior': meta.behavior.name if meta.behavior else None, 'dp_readable': meta.readable, 'dp_writable': meta.writable, 'dp_notifiable': meta.notifiable, 'dp_min': meta.min_value, 'dp_max': meta.max_value, 'dp_version': meta.version, 'dp_instance': meta.instance}
        if meta.options:
            attrs['dp_options'] = list(meta.options)
        return attrs

    def _metadata_display_name(self, dp_id: int | DpId | None) -> str | None:
        return self.coordinator.localize_metadata_name(self.coordinator.get_dp_metadata(dp_id))
