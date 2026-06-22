DEVICE_TYPES = {
    255: {
        "name": "Platform",
    },
    254: {
        "name": "Urinal",
        "variants": {
            0: "IR Control",
            1: "IR Control SASO",
            2: "UPC Exposed (Battery)",
            3: "UPC Exposed (Mains)",
            4: "Integrated",
            5: "Integrated SASO",
            6: "UPC Exposed (BMS)",
            7: "UPC Concealed",
        },
    },
    253: {
        "name": "Lavatory Tap",
        "variants": {
            0: "Hytronic",
            1: "Hytronic (US)",
            2: "Hytronic (US Watersaver)",
            3: "Hytronic (US Hygiene)",
            4: "Etronic 40 (US)",
            5: "Etronic 40 (US Watersaver)",
            6: "Etronic 80 (US)",
            7: "ELR (US)",
            8: "Hytronic (US BMS)",
            9: "Hytronic (US BMS Watersaver)",
            10: "Hytronic (US BMS Hygiene)",
            11: "Etronic 40 (US BMS)",
            12: "Etronic 40 (US BMS Watersaver)",
            13: "Etronic 80 (US BMS)",
            14: "Piave/Brenta",
            15: "Piave/Brenta (Deck)",
            16: "Piave/Brenta (Wall)",
        },
    },
    252: {
        "name": "DuoFresh",
        "variants": {
            0: "Manual",
            1: "Automatic",
        },
    },
    251: {
        "name": "Converter",
        "variants": {
            0: "Urinal",
            1: "Duofix",
        },
    },
    250: {
        "name": "AquaClean",
        "variants": {
            0: "Unknown",
            1: "Mera Floorstanding",
            2: "Mera Classic",
            3: "Mera Comfort",
            4: "Tuma Classic",
            5: "Tuma Comfort",
            6: "Sela",
            7: "WST Testset",
            8: "WST",
        },
    },
    249: {
        "name": "WC Flush Control",
        "variants": {
            0: "Automatic",
            1: "Wired",
            2: "Wireless",
            3: "Wired Typ 290",
            4: "Wired Omega",
            5: "Hygiene",
            6: "Automatic Sigma80",
        },
    },
    248: {
        "name": "AquaClean (Legacy)",
        "variants": {
            0: "Unknown",
            1: "Mera Floorstanding",
            2: "Mera Classic",
            3: "Mera Comfort",
            4: "Tuma Classic",
            5: "Tuma Comfort",
            6: "Sela",
            7: "WST Testset",
            8: "WST",
        },
    },
    247: {
        "name": "Sanitary Flush Unit",
    },
    246: {
        "name": "Smart Sensor",
    },
    245: {
        "name": "Gateway",
    },
    244: {
        "name": "Mirror Cabinet",
        "variants": {
            0: "ONE",
            1: "ONE (Heated)",
        },
    },
    243: {
        "name": "Illuminated Mirror",
        "variants": {
            0: "ONE",
        },
    },
    242: {
        "name": "Washbasin Cabinet",
        "variants": {
            0: "ONE",
        },
    },
    241: {
        "name": "Shelf Unit",
        "variants": {
            0: "ONE",
        },
    },
}


def get_model_name(series_id: int | None, variant_id: int | None) -> str:
    if not isinstance(series_id, int):
        return "Geberit Toilet"

    device_info = DEVICE_TYPES.get(series_id)
    if not device_info:
        return f"Geberit Series {series_id}"

    series_name = device_info["name"]
    if not isinstance(variant_id, int):
        return f"Geberit {series_name}"

    variant_name = device_info.get("variants", {}).get(variant_id)
    if not variant_name:
        return f"Geberit {series_name} (v{variant_id})"

    if variant_name == "ONE":
        return f"Geberit ONE {series_name}"
    if variant_name == "ONE (Heated)":
        return f"Geberit ONE {series_name} (Heated)"
    return f"Geberit {series_name} ({variant_name})"
