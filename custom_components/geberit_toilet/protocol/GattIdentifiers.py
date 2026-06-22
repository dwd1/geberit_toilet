from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from ..const import BLUETOOTH_SIG_BASE_SUFFIX, GAP_SERVICE_UUID, GATT_SERVICE_UUID, DIS_SERVICE_UUID, STANDARD_GEBERIT_SERVICE_UUID, LEGACY_ADVERTISEMENT_UUID, VARIANT_A_DISCOVERY_SERVICE_UUID, VARIANT_A_DATA_SERVICE_UUID, VARIANT_A_VENDOR_SERVICE_UUID, OTA_ST_SERVICE_UUID

@dataclass(frozen=True)
class KnownGattCharacteristic:
    uuid: str
    key: str
    name: str
    service_uuid: str
    source: str
    decoder: str = 'hex'
    entity_registry_enabled_default: bool = True
    hidden: bool = False

@dataclass(frozen=True)
class KnownGattService:
    uuid: str
    key: str
    name: str
    source: str

@dataclass(frozen=True)
class RuntimeGattCharacteristic:
    uuid: str
    service_uuid: str
    service_name: str
    key: str
    name: str
    source: str
    decoder: str
    properties: tuple[str, ...]
    descriptors: tuple[str, ...]
    readable: bool
    writable: bool
    notifiable: bool
    indicatable: bool
    entity_registry_enabled_default: bool
    hidden: bool
KNOWN_GATT_SERVICES: dict[str, KnownGattService] = {GAP_SERVICE_UUID: KnownGattService(uuid=GAP_SERVICE_UUID, key='gap', name='Generic Access', source='Bluetooth SIG'), GATT_SERVICE_UUID: KnownGattService(uuid=GATT_SERVICE_UUID, key='gatt', name='Generic Attribute', source='Bluetooth SIG'), DIS_SERVICE_UUID: KnownGattService(uuid=DIS_SERVICE_UUID, key='device_information', name='Device Information', source='Bluetooth SIG'), STANDARD_GEBERIT_SERVICE_UUID: KnownGattService(uuid=STANDARD_GEBERIT_SERVICE_UUID, key='geberit_standard_data', name='Geberit Standard Data Channel', source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct'), VARIANT_A_VENDOR_SERVICE_UUID: KnownGattService(uuid=VARIANT_A_VENDOR_SERVICE_UUID, key='geberit_vendor_service_a', name='Geberit Vendor Service A', source='Geberit.ComLib.Bluetooth.Ble20Product / Geberit.OTA.Library'), VARIANT_A_DATA_SERVICE_UUID: KnownGattService(uuid=VARIANT_A_DATA_SERVICE_UUID, key='geberit_variant_a_data', name='Geberit Variant A Data Channel', source='Geberit.ComLib.Bluetooth.Ble20Product'), OTA_ST_SERVICE_UUID: KnownGattService(uuid=OTA_ST_SERVICE_UUID, key='geberit_ota_st', name='Geberit OTA ST Service', source='Geberit.OTA.Library')}
KNOWN_GATT_CHARACTERISTICS: dict[str, KnownGattCharacteristic] = {'00002a00-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a00-0000-1000-8000-00805f9b34fb', key='gap_device_name', name='GATT Device Name', service_uuid=GAP_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a01-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a01-0000-1000-8000-00805f9b34fb', key='gap_appearance', name='GATT Appearance', service_uuid=GAP_SERVICE_UUID, source='Bluetooth SIG', decoder='uint16_le'), '00002a04-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a04-0000-1000-8000-00805f9b34fb', key='gap_preferred_connection_parameters', name='Preferred Connection Parameters', service_uuid=GAP_SERVICE_UUID, source='Bluetooth SIG', decoder='hex'), '00002a05-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a05-0000-1000-8000-00805f9b34fb', key='gatt_service_changed', name='Service Changed', service_uuid=GATT_SERVICE_UUID, source='Bluetooth SIG', entity_registry_enabled_default=False, hidden=True), '00002a24-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a24-0000-1000-8000-00805f9b34fb', key='dis_model_number', name='DIS Model Number', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a25-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a25-0000-1000-8000-00805f9b34fb', key='dis_serial_number', name='DIS Serial Number', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a26-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a26-0000-1000-8000-00805f9b34fb', key='dis_firmware_revision', name='DIS Firmware Revision', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a27-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a27-0000-1000-8000-00805f9b34fb', key='dis_hardware_revision', name='DIS Hardware Revision', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a28-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a28-0000-1000-8000-00805f9b34fb', key='dis_software_revision', name='DIS Software Revision', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '00002a29-0000-1000-8000-00805f9b34fb': KnownGattCharacteristic(uuid='00002a29-0000-1000-8000-00805f9b34fb', key='dis_manufacturer_name', name='DIS Manufacturer Name', service_uuid=DIS_SERVICE_UUID, source='Bluetooth SIG', decoder='utf8'), '3334429d-90f3-4c41-a02d-5cb3a13e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a13e0000', key='standard_write_0', name='Standard Write 0', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a23e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a23e0000', key='standard_write_1', name='Standard Write 1', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a33e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a33e0000', key='standard_write_2', name='Standard Write 2', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a43e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a43e0000', key='standard_write_3', name='Standard Write 3', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a53e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a53e0000', key='standard_notify_0', name='Standard Notify 0', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a63e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a63e0000', key='standard_notify_1', name='Standard Notify 1', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a73e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a73e0000', key='standard_notify_2', name='Standard Notify 2', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '3334429d-90f3-4c41-a02d-5cb3a83e0000': KnownGattCharacteristic(uuid='3334429d-90f3-4c41-a02d-5cb3a83e0000', key='standard_notify_3', name='Standard Notify 3', service_uuid=STANDARD_GEBERIT_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Legacy.AquaCleanProduct', entity_registry_enabled_default=False, hidden=True), '559eb101-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb101-2390-11e8-b467-0ed5f89f718b', key='variant_a_ota_request', name='Variant A OTA Request', service_uuid=VARIANT_A_VENDOR_SERVICE_UUID, source='Geberit.OTA.Library / Geberit.ComLib.Bluetooth.Ble20Product', entity_registry_enabled_default=False, hidden=True), '559eb110-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb110-2390-11e8-b467-0ed5f89f718b', key='variant_a_system_info', name='Variant A System Info', service_uuid=VARIANT_A_VENDOR_SERVICE_UUID, source='Geberit.OTA.Library / Geberit.ComLib.Bluetooth.Ble20Product', decoder='hex'), '559eb120-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb120-2390-11e8-b467-0ed5f89f718b', key='variant_a_ota_control', name='Variant A OTA Control', service_uuid=VARIANT_A_VENDOR_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '559eb121-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb121-2390-11e8-b467-0ed5f89f718b', key='variant_a_ota_confirmation', name='Variant A OTA Confirmation', service_uuid=VARIANT_A_VENDOR_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '559eb122-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb122-2390-11e8-b467-0ed5f89f718b', key='variant_a_ota_data', name='Variant A OTA Data', service_uuid=VARIANT_A_VENDOR_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '559eb001-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb001-2390-11e8-b467-0ed5f89f718b', key='variant_a_write_0', name='Variant A Write 0', service_uuid=VARIANT_A_DATA_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Ble20Product', entity_registry_enabled_default=False, hidden=True), '559eb002-2390-11e8-b467-0ed5f89f718b': KnownGattCharacteristic(uuid='559eb002-2390-11e8-b467-0ed5f89f718b', key='variant_a_notify_0', name='Variant A Notify 0', service_uuid=VARIANT_A_DATA_SERVICE_UUID, source='Geberit.ComLib.Bluetooth.Ble20Product', entity_registry_enabled_default=False, hidden=True), '0000fe11-8e22-4541-9d4c-21edae82ed19': KnownGattCharacteristic(uuid='0000fe11-8e22-4541-9d4c-21edae82ed19', key='ota_st_request', name='OTA ST Request', service_uuid=OTA_ST_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '0000fe22-8e22-4541-9d4c-21edae82ed19': KnownGattCharacteristic(uuid='0000fe22-8e22-4541-9d4c-21edae82ed19', key='ota_st_control', name='OTA ST Control', service_uuid=OTA_ST_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '0000fe23-8e22-4541-9d4c-21edae82ed19': KnownGattCharacteristic(uuid='0000fe23-8e22-4541-9d4c-21edae82ed19', key='ota_st_confirmation', name='OTA ST Confirmation', service_uuid=OTA_ST_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True), '0000fe24-8e22-4541-9d4c-21edae82ed19': KnownGattCharacteristic(uuid='0000fe24-8e22-4541-9d4c-21edae82ed19', key='ota_st_data', name='OTA ST Data', service_uuid=OTA_ST_SERVICE_UUID, source='Geberit.OTA.Library', entity_registry_enabled_default=False, hidden=True)}
KNOWN_DISCOVERY_SERVICE_UUIDS: tuple[str, ...] = ('3334429d-90f3-4c41-a02d-5cb3a03e0000', '00003ea0-0000-1000-8000-00805f9b34fb', '559eb000-2390-11e8-b467-0ed5f89f718b', '0000fd48-0000-1000-8000-00805f9b34fb', '559eb100-2390-11e8-b467-0ed5f89f718b')

def normalize_uuid(value: Any) -> str:
    return str(value).lower()

def _extract_properties(characteristic: Any) -> tuple[str, ...]:
    props = characteristic.properties
    if isinstance(props, int):
        normalized: list[str] = []
        if props & 2:
            normalized.append('read')
        if props & 4:
            normalized.append('write-without-response')
        if props & 8:
            normalized.append('write')
        if props & 16:
            normalized.append('notify')
        if props & 32:
            normalized.append('indicate')
        return tuple(normalized)
    if isinstance(props, (list, tuple)):
        return tuple((str(prop).lower() for prop in props))
    return ()

def discover_known_gatt_characteristics(services_iterable: Any) -> dict[str, RuntimeGattCharacteristic]:
    discovered: dict[str, RuntimeGattCharacteristic] = {}
    for service in services_iterable:
        service_uuid = normalize_uuid(service.uuid)
        service_meta = KNOWN_GATT_SERVICES.get(service_uuid)
        service_name = service_meta.name if service_meta else f'Service {service_uuid}'
        for characteristic in service.characteristics:
            char_uuid = normalize_uuid(characteristic.uuid)
            known = KNOWN_GATT_CHARACTERISTICS.get(char_uuid)
            if known is None:
                continue
            properties = _extract_properties(characteristic)
            descriptors = tuple((normalize_uuid(desc.uuid) for desc in getattr(characteristic, 'descriptors', ())))
            discovered[char_uuid] = RuntimeGattCharacteristic(uuid=char_uuid, service_uuid=service_uuid, service_name=service_name, key=known.key, name=known.name, source=known.source, decoder=known.decoder, properties=properties, descriptors=descriptors, readable='read' in properties, writable='write' in properties or 'write-without-response' in properties, notifiable='notify' in properties, indicatable='indicate' in properties, entity_registry_enabled_default=known.entity_registry_enabled_default, hidden=known.hidden)
    return discovered

def decode_known_gatt_value(runtime_char: RuntimeGattCharacteristic, raw_value: bytes) -> Any:
    decoder = runtime_char.decoder
    if decoder == 'utf8':
        return raw_value.decode('utf-8', errors='replace').strip('\x00').strip()
    if decoder == 'uint16_le':
        if len(raw_value) >= 2:
            return int.from_bytes(raw_value[:2], byteorder='little', signed=False)
        return None
    return raw_value.hex()
