# Geberit Toilet for Home Assistant

This custom integration connects Home Assistant directly to compatible Geberit BLE devices that expose the same protocol family.

The long-term goal is to provide a broad Geberit integration that can handle many different toilets and related Geberit BLE-capable devices, with whatever functions each model and firmware version actually supports.

Its purpose is simple:

- monitor what the device reports;
- expose supported settings, controls and sensors in Home Assistant;
- discover as much useful device data as possible from the device itself;
- adapt to different model-specific capabilities instead of assuming one fixed feature set;
- help with diagnostics and reverse-engineering by collecting and comparing value reports.

## What This Integration Does

This integration is built to expose the real Geberit BLE feature surface, not just a small hand-picked subset.

The codebase is prepared for a wide Geberit device family, including product lines such as DuoFresh, AquaClean, WC flush control systems, urinals, lavatory taps, sanitary flush units, smart sensors, converters, gateways and Geberit One mirror / cabinet style devices.

Depending on the exact model and firmware, it can discover and control features such as:

- device identity, model, variant, serial numbers, production dates, firmware versions and other low-level system information;
- odour extraction functions including fan speed, mode, override control, follow-up timing, filter operating data, filter lifetime, filter installation / replacement state and related error reporting;
- orientation or comfort lighting including brightness, mode, color, follow-up timing, ambient-light dependent behavior, proximity-dependent behavior and manual override;
- proximity, motion, ambient light, distance, amplitude, radar and other detection-related values used by different Geberit platforms;
- flush-control and water-management features such as manual flush, automatic flush, interval flush, hybrid mode, purging flush, empty-pipe routines, cleaning mode, water-saving mode, metering mode, actuator / valve status and related diagnostics;
- maintenance and service data including watchdog counters, fatal error counts, RTC state, operation timers, flash erase counters, calibration values, self-test status and internal statistic counters;
- direct device control actions such as locate, restart, reset and other firmware-exposed commands when available.

In other words, the goal is not just to create Home Assistant entities, but to turn as much as possible into something usable, inspectable and automatable.

Not every Geberit device exposes the same capabilities. The integration is designed to discover what your specific hardware and firmware actually support and then expose that real capability set instead of pretending every device behaves like one fixed product.

## Key Features & Smart Functions

To make the integration user-friendly and robust, several smart features are built-in:

### 1. Human-Readable Settings (No Raw Numbers)
Thanks to decompiled metadata mappings, dropdown menus and selection entities do not show raw numeric enum codes.
Options for toilet flushing modes, orientation light modes or odour extraction modes display clean, descriptive labels in the Home Assistant UI.

### 2. Automated Time & Clock Synchronization
Geberit units have an internal Real-Time Clock (RTC).
To prevent time drift, the integration automatically monitors the Geberit device's clock skew. If the drift exceeds 60 seconds, it uses timezone and DST offsets to calculate and write the correct local time back to the device, keeping your toilet's clock perfectly in sync.

### 3. Real-Time Push Notifications
Critical sensor states and events are pushed instantly from the Geberit device to Home Assistant over the active BLE connection. This allows near-instant updates for:
- Motion / presence detection (e.g., orientation light and odour sensors)
- Ambient light changes and user distance/proximity tracking
- Instant status feedback for the odour extraction fan and orientation light status

### 5. Disabled Actions & Sensors
To ensure a clean dashboard, prevent accidental triggers, and optimize database usage, certain entities are created as **disabled by default**:
- **Risky System Actions**: Potentially disruptive actions (such as factory reset, restart or bootloader commands) are disabled to avoid accidental triggers. Please note that these advanced functions and buttons are experimental and have not been tested by the developer.
- **High-Frequency Telemetry**: Read-only sensors reporting values in seconds (such as operation time counters) are disabled by default to prevent the Home Assistant recorder database from being flooded with frequent updates, reducing database writes and saving storage space.

You can easily enable any of these entities at any time in the Home Assistant entity settings.

## Startup Behavior

After the integration is added for the first time, do not expect every entity to appear immediately.

The integration may need a few seconds to connect, identify the device, determine its supported functionality and let Home Assistant create the corresponding entities.

The same applies after Home Assistant restarts.

After a restart, entities may already exist in Home Assistant, but their live values can still need a few seconds to refresh again from the device.

## Installation

### HACS

1. Open HACS.
2. Add this repository as a custom repository.
3. Select the **Integration** category.
4. In HACS, open **Geberit Toilet**.
5. Click **Download**.
6. Restart Home Assistant.
7. Open **Settings** -> **Devices & Services**.
8. Add **Geberit Toilet**.

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

### Notifications Debounce Delay

The time in seconds that the integration waits to group multiple incoming push notifications together before publishing them to Home Assistant. 

For example, when multiple parameters update simultaneously (e.g., motion detection triggers fan, light, and distance changes), this debounce window aggregates the updates to reduce Home Assistant state changes and prevent UI stutter.

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

In Geberit's BLE protocol, these data points are usually referred to as **DPIDs** (data-point identifiers). A DPID is simply the numeric identifier of a value, setting, counter, state or command exposed by the device.

> **Known DPID reference**
>
> You can see the currently known reverse-engineered Geberit DPID constant list in DpId.py file.

#### Only inventory

This is the default and more normal mode.

The integration reads:

- what the device officially reports in its own inventory.

#### All known DPIDs

This is the aggressive discovery mode.

The integration tries to read all DPIDs currently known to the codebase, even if your device does not advertise them in inventory.

Use this if your goal is deep discovery, diagnostics or finding hidden model-specific values and settings.

### Use include DPID list

The include list adds extra read targets on top of the selected base scope.

That means:

- in **Only inventory** mode, it adds extra requested DPIDs or DPID instances beyond the device inventory;
- in **All known DPIDs** mode, it can still be used to keep a custom include list together with the config entry.
- if you specify a concrete instance such as `405.2`, that specific DPID instance is added as an explicit read target.

If enabled, the integration loads the default include list from:

```text
include_dpids.txt
```

and shows it in a dedicated setup step.

### Use exclude DPID list

The exclude list removes DPID or DPID instance targets from the integration's active read and expose target set.

Instead, excluded DPIDs:

- are skipped during the integration's target-building and read process;
- do not create Home Assistant entities automatically;
- can still exist in older saved reports if they were collected before you excluded them.

If enabled, the integration loads the default exclude list from:

```text
exclude_dpids.txt
```

and shows it in a dedicated setup step.

### Maximum instances per DPID group to expose automatically

Some DPIDs are available not just once, but as a group of indexed instance values.

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

Here you can enter numeric DPIDs or DPID instances that should be included in reads in addition to the selected base scope.

Useful details:

- one or more decimal DPID values per line are supported;
- instance-specific includes can be written as `DPID.INSTANCE`, for example `405.2`;
- inline `#` comments are supported;
- the default content is loaded from `include_dpids.txt`;
- editing the text in the setup flow changes what this config entry will request during its discovery / read target build.

### Exclude DPID List

This step appears when **Use exclude DPID list** is enabled.

Here you can enter numeric DPIDs or DPID instances that should be removed from this config entry's read and entity target set.

Useful details:

- one or more decimal DPID values per line are supported;
- instance-specific excludes can be written as `DPID.INSTANCE`, for example `405.2`;
- inline `#` comments are supported;
- the default content is loaded from `exclude_dpids.txt`;
- editing the text in the setup flow changes what this config entry will skip during discovery / reads and therefore also not expose as entities.

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

## Integration Ready Sensor

The integration also exposes an **Integration Ready** binary sensor.

This sensor tells you whether the BLE connection is currently up and the integration is actually ready for use.

This is especially useful:

- after Home Assistant restarts;
- after intentionally disconnecting the integration;
- after accidental disconnects caused by range, interference, adapter issues or other BLE problems.

The sensor turns on only when the integration has successfully re-established the BLE connection and completed a real live refresh in the current Home Assistant session.

If it is off, the integration may still be starting up, reconnecting or waiting to recover from a dropped connection.

While this sensor is off, the individual entities can still continue to show cached values from the previous successful connection.

That means a dropped or intentionally released connection does not immediately clear every entity state.

Use **Integration Ready** to see whether the currently visible values are backed by a live active connection or are still the last cached values from an earlier one.

## Notifications vs Polling

Some values are pushed immediately by the device through BLE notifications.

Other values are only refreshed during polling.

That means:

- some entities react almost instantly;
- some entities update on the next poll cycle.

This is normal and depends on how the device exposes that specific value.

## Diagnostic Reports

The integration includes built-in reporting tools to help you see what the device is exposing and what changed after you modified settings in the official Geberit app or elsewhere.

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

- Some values may be model-specific, firmware-specific, undocumented or noisy.
- Some timestamp-like values may update very frequently on certain models.
- The number of created entities can vary significantly between devices and discovery modes.
- Parts of the communication layer and device-specific behavior are also obfuscated in Geberit's own original software. To respect and preserve that same business logic boundary, the integration keeps the relevant protocol implementation areas obfuscated as well.

## Use At Your Own Risk

This integration is unofficial and experimental.

It may read and write values that were never intended by Geberit to be changed through Home Assistant.

Some commands or values may be poorly documented, device-specific, unsupported by your exact model or simply unsafe to experiment with.

You use this integration entirely at your own risk.

The developer of this integration accepts no responsibility if a bad write, unsupported command, firmware quirk or unexpected device behavior causes malfunctions, data loss, unstable behavior, service issues or even hardware damage to your toilet or related device.

If you are not comfortable with that, do not use this integration.

## Disclaimer

This project is not affiliated with, authorized by, endorsed by, maintained by or otherwise connected to Geberit.

All product names, trademarks and brands belong to their respective owners.

## Donate

If you found this integration useful, consider supporting its continued development.

Support helps me spend more time improving compatibility, adding features and pushing the reverse-engineering work further.

https://buymeacoffee.com/dwdhu

![Buy Me a Coffee QR code](buymeacoffee.png)
