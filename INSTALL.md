# Marc Med Tracker — Complete Setup Guide

Marc's production installation guide. Covers integration install, all HA configuration (helpers, scripts, automations), dashboard, and notifications. Replaces the fragmented docs/ files as the authoritative setup reference.

---

## 1. Integration Installation

### Via HACS (recommended)

1. **HACS → Integrations → Explore & Download**
2. Search "Marc Med Tracker" → Download
3. Restart Home Assistant

### Manual install

```bash
cp -r marc_med_tracker/ /config/custom_components/
```

Restart Home Assistant after copying.

---

## 2. Medication Configuration

Add to `/config/configuration.yaml`:

```yaml
marc_med_tracker:
  medications:
    - name: "Metformin 500mg"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "500mg"
      doses_per_day: 2
      pills_per_dose: 2
      initial_stock: 360

    - name: "Jardiance 40mg"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "40mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90

    - name: "Candesartan 16mg"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "16mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90

    - name: "Rosuvastatin 10mg"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "10mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90

    - name: "Pantoprazole 40mg"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "40mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90

    - name: "Bisoprolol 2.5mg"
      prescribing_doctor: "Dr. K. Ducet"
      refills_left: 3
      last_refilled: "2026-02-01"
      strength: "2.5mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90

    - name: "Spironolactone 60mg"
      prescribing_doctor: "Dr. K. Ducet"
      refills_left: 3
      last_refilled: "2026-02-01"
      strength: "60mg"
      doses_per_day: 1
      pills_per_dose: 0.5
      initial_stock: 45

    - name: "Zenhale Inhaler"
      prescribing_doctor: "Dr. K. Safka"
      refills_left: 3
      last_refilled: "2026-02-01"
      strength: "100/6mcg"
      doses_per_day: 2
      pills_per_dose: 1
      initial_stock: 200
```

> **Spironolactone note:** `pills_per_dose: 0.5` requires the schema fix in `__init__.py` (change `cv.positive_int` → `vol.Coerce(float)` for `pills_per_dose`). Without this fix HA will reject the config on restart.

---

## 3. Input Helpers (Stock Update Inputs)

Add to the `input_number:` block in `/config/configuration.yaml`:

```yaml
input_number:
  med_stock_metformin:
    name: "Metformin - New Stock"
    min: 0
    max: 400
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_jardiance:
    name: "Jardiance - New Stock"
    min: 0
    max: 200
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_candesartan:
    name: "Candesartan - New Stock"
    min: 0
    max: 200
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_rosuvastatin:
    name: "Rosuvastatin - New Stock"
    min: 0
    max: 200
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_pantoprazole:
    name: "Pantoprazole - New Stock"
    min: 0
    max: 200
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_bisoprolol:
    name: "Bisoprolol - New Stock"
    min: 0
    max: 200
    step: 1
    unit_of_measurement: "pills"
    icon: mdi:pill
    mode: box

  med_stock_spironolactone:
    name: "Spironolactone - New Stock (tablets)"
    min: 0
    max: 100
    step: 0.5
    unit_of_measurement: "tablets"
    icon: mdi:pill-multiple
    mode: box

  med_stock_zenhale:
    name: "Zenhale - New Stock"
    min: 0
    max: 250
    step: 1
    unit_of_measurement: "puffs"
    icon: mdi:spray
    mode: box
```

---

## 4. Dose Tracking Helpers

The dose-tracking buttons (`check_off_dose` / `uncheck_dose`) toggle these helpers. They must be created manually:

```yaml
input_boolean:
  marc_med_morning_helper:
    name: "Morning Pills Taken"
    icon: mdi:weather-sunset-up

  marc_med_morning_puffer_helper:
    name: "Morning Puffer Taken"
    icon: mdi:spray

  marc_med_lunch_helper:
    name: "Lunch Pills Taken"
    icon: mdi:weather-sunny

  marc_med_evening_helper:
    name: "Evening Pills Taken"
    icon: mdi:weather-sunset-down

  marc_med_evening_puffer_helper:
    name: "Evening Puffer Taken"
    icon: mdi:spray
```

Valid `dose_id` values for services: `morning`, `lunch`, `evening`, `morning_puffer`, `evening_puffer`.

---

## 5. Scripts

Add to `/config/scripts.yaml`:

```yaml
# Save NP T. Wakefield medications (5 meds)
med_update_wakefield_stock:
  alias: "Update NP T. Wakefield Medications"
  sequence:
    - action: marc_med_tracker.update_stock
      data:
        medication_id: metformin
        pills: "{{ states('input_number.med_stock_metformin') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: jardiance
        pills: "{{ states('input_number.med_stock_jardiance') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: candesartan
        pills: "{{ states('input_number.med_stock_candesartan') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: rosuvastatin
        pills: "{{ states('input_number.med_stock_rosuvastatin') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: pantoprazole
        pills: "{{ states('input_number.med_stock_pantoprazole') | int }}"

# Save Dr. K. Ducet medications (Bisoprolol + Spironolactone)
med_update_ducet_stock:
  alias: "Update Dr. K. Ducet Medications"
  sequence:
    - action: marc_med_tracker.update_stock
      data:
        medication_id: bisoprolol
        pills: "{{ states('input_number.med_stock_bisoprolol') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: spironolactone
        pills: "{{ states('input_number.med_stock_spironolactone') | float }}"

# Save Dr. K. Safka medications (Zenhale)
med_update_safka_stock:
  alias: "Update Dr. K. Safka Medications"
  sequence:
    - action: marc_med_tracker.update_stock
      data:
        medication_id: zenhale_inhaler
        pills: "{{ states('input_number.med_stock_zenhale') | int }}"

# Save all medications at once
med_update_all_stock:
  alias: "Update All Medication Stock"
  sequence:
    - action: marc_med_tracker.update_stock
      data:
        medication_id: metformin
        pills: "{{ states('input_number.med_stock_metformin') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: jardiance
        pills: "{{ states('input_number.med_stock_jardiance') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: candesartan
        pills: "{{ states('input_number.med_stock_candesartan') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: rosuvastatin
        pills: "{{ states('input_number.med_stock_rosuvastatin') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: pantoprazole
        pills: "{{ states('input_number.med_stock_pantoprazole') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: bisoprolol
        pills: "{{ states('input_number.med_stock_bisoprolol') | int }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: spironolactone
        pills: "{{ states('input_number.med_stock_spironolactone') | float }}"
    - action: marc_med_tracker.update_stock
      data:
        medication_id: zenhale_inhaler
        pills: "{{ states('input_number.med_stock_zenhale') | int }}"
```

---

## 6. Notifications

Medication reminder automations fire at 09:30, 14:30, and 19:30 via:

```yaml
notify.mobile_app_marcs_iphone_14
```

Dose IDs for notification automations:

| Time  | dose_id          | Medications                                    |
|-------|------------------|------------------------------------------------|
| 09:30 | `morning`        | Metformin, Candesartan, Rosuvastatin, Pantoprazole, Bisoprolol, Spironolactone |
| 09:30 | `morning_puffer` | Zenhale (rinse mouth after use)               |
| 14:30 | `lunch`          | Metformin (2nd dose)                          |
| 19:30 | `evening`        | Jardiance                                     |
| 19:30 | `evening_puffer` | Zenhale                                       |

See `examples/automations_with_notifications.yaml` for full automation YAML.

---

## 7. Dashboard — Meds & Health

Dashboard stored in `.storage/lovelace.marc_s_meds_health`. Add cards via the manual card editor (paste each card individually — pasting a full view fails with "Expected an array value").

### Stock display (read-only)

```yaml
type: entities
title: "💊 NP T. Wakefield"
state_color: true
entities:
  - entity: sensor.marc_med_metformin
    name: Metformin 500mg
  - entity: sensor.marc_med_jardiance
    name: Jardiance 40mg
  - entity: sensor.marc_med_candesartan
    name: Candesartan 16mg
  - entity: sensor.marc_med_rosuvastatin
    name: Rosuvastatin 10mg
  - entity: sensor.marc_med_pantoprazole
    name: Pantoprazole 40mg
```

```yaml
type: entities
title: "❤️ Dr. K. Ducet"
state_color: true
entities:
  - entity: sensor.marc_med_bisoprolol
    name: Bisoprolol 2.5mg
  - entity: sensor.marc_med_spironolactone
    name: "Spironolactone 60mg (half tablet)"
```

```yaml
type: entities
title: "🫁 Dr. K. Safka"
state_color: true
entities:
  - entity: sensor.marc_med_zenhale_inhaler
    name: Zenhale 100/6mcg
```

### Update Pills on Hand (per-doctor groups with individual save buttons)

```yaml
# NP T. Wakefield group
type: entities
title: "💊 NP T. Wakefield"
entities:
  - entity: input_number.med_stock_metformin
    name: Metformin 500mg
    secondary_info: none
  - entity: input_number.med_stock_jardiance
    name: Jardiance 40mg
    secondary_info: none
  - entity: input_number.med_stock_candesartan
    name: Candesartan 16mg
    secondary_info: none
  - entity: input_number.med_stock_rosuvastatin
    name: Rosuvastatin 10mg
    secondary_info: none
  - entity: input_number.med_stock_pantoprazole
    name: Pantoprazole 40mg
    secondary_info: none
  - type: button
    name: "💾 Save NP Wakefield"
    action_name: Save
    tap_action:
      action: perform-action
      perform_action: script.med_update_wakefield_stock
```

```yaml
# Dr. K. Ducet group
type: entities
title: "❤️ Dr. K. Ducet"
entities:
  - entity: input_number.med_stock_bisoprolol
    name: Bisoprolol 2.5mg
    secondary_info: none
  - entity: input_number.med_stock_spironolactone
    name: "Spironolactone (tablets, ½ per dose = 30mg)"
    icon: mdi:pill-multiple
    secondary_info: none
  - type: button
    name: "💾 Save Dr. Ducet"
    action_name: Save
    tap_action:
      action: perform-action
      perform_action: script.med_update_ducet_stock
```

```yaml
# Dr. K. Safka group (puffs, not pills)
type: entities
title: "🫁 Dr. K. Safka"
entities:
  - entity: input_number.med_stock_zenhale
    name: "Zenhale 100/6mcg (puffs remaining)"
    icon: mdi:spray
    secondary_info: none
  - type: button
    name: "💾 Save Dr. Safka"
    action_name: Save
    tap_action:
      action: perform-action
      perform_action: script.med_update_safka_stock
```

```yaml
# Save All button (updates all 8 medications at once)
type: button
name: "💾 Save All Medications"
icon: mdi:content-save-all
tap_action:
  action: perform-action
  perform_action: script.med_update_all_stock
```

---

## 8. Binary Sensors Workaround

The integration's `binary_sensor.py` fails to load (root cause unknown). Use `examples/manual_binary_sensors.yaml` in your HA config instead — copy the contents into a `template:` block or `packages/`. Uses modern template syntax, not `platform: template`.

---

## 9. Reload After Changes

After editing configuration.yaml:
- **Developer Tools → YAML → Reload All YAML**

After editing scripts.yaml or automations.yaml:
- **Developer Tools → YAML → Reload Scripts / Reload Automations**

After editing the dashboard storage file directly:
- **Hard refresh the browser** (Ctrl+Shift+R)

---

## 10. Known Integration Bugs (v2.1.1)

These are bugs in the source code that need patching before they affect production:

1. **`pills_per_dose` schema (`__init__.py`)** — uses `cv.positive_int`, rejects `0.5` for Spironolactone. Fix: change to `vol.Coerce(float)`.

2. **Stock resets on restart (`__init__.py`)** — `async_setup` overwrites stored stock with a recalculated value. Any `update_stock` or `take_dose` changes are lost on HA restart. Fix: load stored stock first; only use calculated fallback if key is absent.

3. **Service handler indentation (`__init__.py`)** — `hass.bus.async_fire(...)` and `_LOGGER.info(...)` in `handle_take_dose`, `handle_refill`, `handle_update_refills`, `handle_update_doctor`, `handle_update_stock` are outdented to the function body, so they execute even when the medication ID is not found.

4. **Makefile path mismatch** — `lint`, `format`, `validate` targets reference `marc_med_tracker/` subdirectory which doesn't exist. Run directly: `ruff check .`, `black --check .`, `python scripts/validate_manifest.py`.
