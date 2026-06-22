# Geberit Toilet for Home Assistant

This custom integration connects Home Assistant directly to compatible Geberit BLE devices that expose the same protocol family.

The long-term goal is to provide a broad Geberit integration that can handle many different toilets and related Geberit BLE-capable devices, with whatever functions each model and firmware version actually supports.

Its purpose is simple:

- monitor what the device reports;
- expose supported settings and controls in Home Assistant;
- discover as much useful device data as possible from the device itself;
- adapt to different model-specific capabilities instead of assuming one fixed feature set;
- help with diagnostics and reverse-engineering by collecting and comparing value reports.

## What This Integration Does

This integration is built to expose the real Geberit BLE feature surface, not just a small hand-picked subset.

The codebase is prepared for a wide Geberit device family, including product lines such as DuoFresh, AquaClean, WC flush control systems, urinals, lavatory taps, sanitary flush units, smart sensors, converters, gateways, and Geberit ONE mirror / cabinet style devices.

Depending on the exact model and firmware, it can discover and control features such as:

- device identity, model, variant, serial numbers, production dates, firmware versions, PCB metadata, wireless stack details, and other low-level system information;
- odour extraction functions including fan speed, mode, override control, follow-up timing, filter operating data, filter lifetime, filter installation / replacement state, and related error reporting;
- orientation or comfort lighting including brightness, mode, color, follow-up timing, ambient-light dependent behavior, proximity-dependent behavior, and manual override;
- proximity, motion, ambient light, distance, amplitude, Doppler radar, and other detection-related values used by different Geberit platforms;
- flush-control and water-management features such as manual flush, automatic flush, interval flush, hybrid mode, purging flush, empty-pipe routines, cleaning mode, water-saving mode, metering mode, actuator / valve status, and related diagnostics;
- maintenance and service data including watchdog counters, fatal error counts, RTC state, operation timers, flash erase counters, calibration values, self-test status, and internal statistic counters;
- direct device control actions such as locate, restart, reset, and other firmware-exposed commands when available.

In other words, the goal is not just to create Home Assistant entities, but to turn as much of the reverse-engineered Geberit BLE protocol as possible into something usable, inspectable, and automatable.

Not every Geberit device exposes the same capabilities. The integration is designed to discover what your specific hardware and firmware actually support, and then expose that real capability set instead of pretending every device behaves like one fixed product.

## Installation

### HACS

1. Open HACS.
2. Add this repository as a custom repository.
3. Select the **Integration** category.
4. Install **Geberit Toilet**.
5. Restart Home Assistant.
6. Open **Settings** -> **Devices & Services**.
7. Add **Geberit Toilet**.

### Manual

1. Copy the `geberit_toilet` folder into your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Open **Settings** -> **Devices & Services**.
4. Add **Geberit Toilet**.

## Setup Flow

During setup, the integration asks for a few basic settings.

### BLE MAC Address

This is the Bluetooth MAC address of the Geberit device you want to connect to.

If Home Assistant discovers the device automatically, this is already known and you usually do not need to enter it manually.

### Pairing PIN

If your device is protected by a PIN, enter it here.

If your device does not require a PIN, this can be left empty.

### Use ESPHome Bluetooth Proxy

Enable this if Home Assistant should talk to the Geberit device through an ESPHome Bluetooth proxy instead of the local Bluetooth adapter.

If this is disabled, the integration uses the Bluetooth adapter on the Home Assistant host directly.

### Poll Interval

This is how often Home Assistant actively asks the device for values that are not pushed by notifications.

Smaller values mean faster updates but more BLE traffic.

Larger values reduce traffic but make some values update more slowly.

### Communication Mode

This controls which transport layer the integration actively uses after connecting.

#### DPIDs

This uses the Ble20 / Arendi-secured DPID protocol only.

Use this if your goal is to expose and explore the Geberit data-point layer.

This is the default mode.

#### GATT

This uses only known plain GATT characteristics.

Use this if you want to avoid the DPID path entirely and only work with values available through standard BLE characteristic access.

#### Both

This enables both paths together.

Use this if you want the widest possible coverage from one config entry.

### Requested Data Scope

This controls how aggressively the integration tries to discover and read data points.

In Geberit's BLE protocol, these data points are usually referred to as **DPIDs** (data-point identifiers). A DPID is simply the numeric identifier of a value, setting, counter, state, or command exposed by the device.


> **Known DPID reference**
>
> You can see the currently known reverse-engineered Geberit Ble20 DPID constant list here:
>
> ```text
> protocol/DpId.py
> ```

#### Only inventory

This is the safer and more normal mode.

The integration reads:

- what the device officially reports in its own inventory.

#### All known DPIDs (adding can be slow)

This is the aggressive discovery mode.

The integration tries to read all DPIDs currently known to the codebase, even if your device does not advertise them in inventory.

Use this if your goal is deep discovery, diagnostics, or finding hidden model-specific values.

### Use include DPID list

The include list adds extra DPIDs on top of the selected base scope.

That means:

- in **Only inventory** mode, it adds extra requested DPIDs beyond the device inventory;
- in **All known DPIDs** mode, it can still be used to keep a custom include list together with the config entry.

If enabled, the integration loads the default include list from:

```text
include_dpids.txt
```

and shows it in a dedicated setup step.

### Use exclude DPID list

The exclude list does **not** stop those DPIDs from being read.

Instead, excluded DPIDs:

- can still be read from the device;
- can still appear in value reports and comparisons;
- do not create Home Assistant entities automatically.

If enabled, the integration loads the default exclude list from:

```text
exclude_dpids.txt
```

and shows it in a dedicated setup step.

### Maximum instances per DPID group to expose automatically

Some DPIDs are available not just once, but as a group of indexed instance values.

Examples:

- a single DPID may expose instance `0` and `1`;
- another may expose a much larger block such as `0` through `19`.

This setting controls when those instance groups are turned into Home Assistant entities automatically.

How it works:

- the integration still reads all discovered values;
- reports and diffs can still contain all discovered values;
- this limit only controls automatic entity creation for grouped instance values.

If the number of discovered instances for one DPID is at or below this limit, the integration exposes them automatically as entities.

Default: `5`

### Expose DPID groups above maximum instance limit

If this option is disabled, large instance groups stay available for reports and diagnostics, but do not automatically create large numbers of Home Assistant entities.

If this option is enabled, those larger groups are exposed as entities too.

Use this if you want the most complete possible entity surface, even when a DPID exposes many indexed values.

### ESPHome Proxy Settings

If **Use ESPHome Bluetooth Proxy** is enabled, there is an extra setup step for:

- ESPHome host or IP;
- ESPHome API port;
- optional Noise PSK.

### Include DPID List

This step appears when **Use include DPID list** is enabled.

Here you can enter numeric DPIDs that should be included in reads in addition to the selected base scope.

Useful details:

- one or more decimal DPID values per line are supported;
- inline `#` comments are supported;
- the default content is loaded from `include_dpids.txt`;
- editing the text in the setup flow changes what this config entry will request.

### Exclude DPID List

This step appears when **Use exclude DPID list** is enabled.

Here you can enter numeric DPIDs that should remain readable and reportable, but should not create Home Assistant entities.

Useful details:

- one or more decimal DPID values per line are supported;
- inline `#` comments are supported;
- the default content is loaded from `exclude_dpids.txt`;
- editing the text in the setup flow changes what this config entry will hide from entity creation.

## BLE Connection Switch

The integration exposes a **BLE Connection** switch.

When this switch is turned off:

- the BLE connection is released;
- polling stops;
- notification listeners stop;
- reads stop;
- writes stop.

This is useful if you want to temporarily use the official Geberit app, because the device typically allows only one active connection at a time.

When the switch is turned on again, the integration reconnects and resumes normal operation.

## Notifications vs Polling

Some values are pushed immediately by the device through BLE notifications.

Other values are only refreshed during polling.

That means:

- some entities react almost instantly;
- some entities update on the next poll cycle.

This is normal and depends on how the device exposes that specific value.

## Diagnostic Reports

The integration includes built-in reporting tools to help you see what the device is exposing and what changed after you modified settings in the official app or elsewhere.

### Create value report

This button creates a JSON snapshot of the current integration state.

The report includes:

- currently known entity states;
- entity attributes;
- decoded DPID values;
- raw hex values where available;
- instance information for instance-based DPIDs;
- configured include DPIDs;
- configured exclude DPIDs;
- discovered non-inventory DPIDs.

Reports are stored here:

```text
/config/geberit_toilet/reports/
```

### Compare report A / Compare report B

These two select entities let you choose which two saved reports should be compared.

### Compare two reports

This button compares the currently selected **A** and **B** reports and creates a human-readable text diff.

The diff highlights:

- added values;
- removed values;
- changed decoded values;
- changed raw values;
- changed entity states;
- changed entity attributes.

Diff files are stored here:

```text
/config/geberit_toilet/differences/
```

### Clear reports

Deletes all saved JSON reports from:

```text
/config/geberit_toilet/reports/
```

### Clear compared differences

Deletes all saved diff text files from:

```text
/config/geberit_toilet/differences/
```

## Practical Example

If you want to see what the official Geberit app changes:

1. Create a value report.
2. Turn the integration **BLE Connection** switch off.
3. Connect with the official app and change something.
4. Disconnect the official app.
5. Turn the integration **BLE Connection** switch back on.
6. Create another value report.
7. Select the older report as **A** and the newer report as **B**.
8. Press **Compare two reports**.

This is usually much more useful than manually checking dozens of entities one by one.

## Notes

- The integration intentionally blocks known-dangerous DPIDs such as bootloader start commands.
- Some values may be model-specific, firmware-specific, undocumented, or noisy.
- Some timestamp-like values may update very frequently on certain models.
- The number of created entities can vary significantly between devices and discovery modes.

## Use At Your Own Risk

This integration is unofficial and experimental.

It may read and write values that were never intended by Geberit to be changed through Home Assistant. Some commands or values may be poorly documented, device-specific, unsupported by your exact model, or simply unsafe to experiment with.

You use this integration entirely at your own risk.

The developer of this integration accepts no responsibility if a bad write, unsupported command, firmware quirk, or unexpected device behavior causes malfunctions, data loss, unstable behavior, service issues, or even hardware damage to your toilet or related device.

If you are not comfortable with that, do not use this integration.

## Disclaimer

This project is not affiliated with, authorized by, endorsed by, maintained by, or otherwise connected to Geberit.

All product names, trademarks, and brands belong to their respective owners.

## Donate

If you found this integration useful, consider supporting its continued development.

Support helps me spend more time improving compatibility, adding features, and pushing the reverse-engineering work further.

https://buymeacoffee.com/dwdhu

![Buy Me a Coffee QR code](buymeacoffee.png)
