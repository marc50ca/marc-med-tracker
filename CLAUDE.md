# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Marc Med Tracker v2.1.1** — A Home Assistant custom integration (HACS) for medication tracking, health metrics from Apple Health, and iPhone notifications. GitHub: `marc50ca/marc-med-tracker`.

## Development Commands

```bash
make install       # Install dependencies (homeassistant, voluptuous, black, ruff, pytest)
make test          # Run tests (pytest tests/)
make release       # Build marc-med-tracker.zip for distribution
```

Run a single test: `pytest tests/test_calculations.py -v`

**Makefile path mismatch (blocker):** `lint`, `format`, and `validate` targets all reference `marc_med_tracker/` (a subdirectory that doesn't exist) — the Python files live in the repo root. Run these directly instead:

```bash
ruff check .                  # lint
black --check .                # format check
python scripts/validate_manifest.py
python scripts/validate_services.py
python -m py_compile __init__.py sensor.py binary_sensor.py
```

## Deployment

Integration files go in HA's `custom_components/marc_med_tracker/`. The `examples/` directory contains YAML for the user to copy into their HA config — it is not loaded by the integration itself.

## Known Bugs in Source

### 1. Indentation error in `__init__.py` — affects all service handlers
Every `await store.async_save(...)` block has misaligned indentation: the code that fires the HA bus event and logs is outdented to the function body level rather than staying inside the `if` block. This means `hass.bus.async_fire(...)` and `_LOGGER.info(...)` execute even when the medication is not found. Affects: `handle_take_dose`, `handle_refill`, `handle_update_refills`, `handle_update_doctor`, `handle_update_stock`.

### 2. Schema rejects fractional `pills_per_dose`
`MEDICATION_SCHEMA` defines `pills_per_dose` as `cv.positive_int`, but Spironolactone uses `0.5`. This causes a voluptuous validation error on HA restart. Change to `vol.Coerce(float)` with a range validator.

### 3. Stock resets on HA restart
On `async_setup`, stored data is loaded then **overwritten** by recalculated stock (`initial_stock - days_elapsed × daily_rate`). Any stock changes made via `update_stock` or `take_dose` services are lost on restart. Stored data needs to take precedence over the calculated fallback.

## Architecture

Two layers:

1. **Integration layer** — `__init__.py` (setup + services), `sensor.py` (stock sensors), `binary_sensor.py` (dose-due sensors). Uses HA's `Store` helper to persist state to `.storage/marc_med_tracker.medications`.

2. **Configuration layer** — `examples/` YAML files the user copies into their HA config using built-in `template`, `input_boolean`, `automation`, and `script` platforms.

### Medication ID derivation
`med_id = name.lower().replace(" ", "_")` — used as the dict key in storage, the service `medication_id` parameter, and the sensor entity ID suffix (`sensor.marc_med_{med_id}`).

### Dose tracking vs stock tracking
These are separate systems:
- **Stock tracking**: `current_stock` integer in the medications dict, modified by `take_dose`, `refill`, `update_stock` services.
- **Dose tracking**: `check_off_dose` / `uncheck_dose` services toggle `input_boolean.marc_med_{dose_id}_helper` entities. Valid `dose_id` values: `morning`, `lunch`, `evening`, `morning_puffer`, `evening_puffer`. These helpers must be created manually in HA config — they are not created by the integration.

### Sensor status thresholds
`_get_status()` in `sensor.py`: `OUT_OF_STOCK` (0 pills) → `CRITICAL` (≤3 days) → `LOW` (≤7 days) → `NO_REFILLS_LEFT` (≤14 days + 0 refills) → `OK`.

### Binary sensor workaround
Binary sensors defined in `binary_sensor.py` fail to load (root cause unknown). Use `examples/manual_binary_sensors.yaml` with modern `template:` syntax instead of `platform: template`.

## Key Domain Rules

- **Blood glucose: mmol/L** (Canadian standard, never mg/dL). Fasting target: 4.0–7.0; post-meal: 5.0–10.0.
- **A1C formula:** `(avg_mmol_L × 0.555) + 2.59`
- **Spironolactone:** 0.5 tablet of 60mg = 30mg actual dose.
- **Zenhale:** 1 puff twice daily; always include rinse-mouth reminder.
- **Metformin:** 2 tablets × 2 daily = 4 tablets/day.
- **Notifications:** `notify.mobile_app_marcs_iphone_14` at 9:30, 14:30, 19:30.

## Medications (8 total)

| Medication | Dose | Schedule | Prescriber | Initial Stock |
|---|---|---|---|---|
| Metformin 500mg | 2 tabs | morning + lunch | NP T. Wakefield | 360 |
| Jardiance 40mg | 1 tab | evening | NP T. Wakefield | 90 |
| Candesartan 16mg | 1 tab | morning | NP T. Wakefield | 90 |
| Rosuvastatin 10mg | 1 tab | morning | NP T. Wakefield | 90 |
| Pantoprazole 40mg | 1 tab | morning | NP T. Wakefield | 90 |
| Bisoprolol 2.5mg | 1 tab | morning | Dr. K. Ducet | 90 |
| Spironolactone 60mg | 0.5 tab | morning | Dr. K. Ducet | 45 |
| Zenhale 100/6mcg | 1 puff | morning + evening | Dr. K. Safka | 200 doses |

Refill dates: NP T. Wakefield → 2026-03-25; Dr. K. Ducet & Dr. K. Safka → 2026-02-01.

## Apple Health Sensors

Prefix: `hae.marchealthsync_`. Total 33 sensors: blood glucose (1), cardiovascular (10), sleep (7), weight (3), activity (12). Excluded: `_sleep_analysis_sleep` (duplicate), `_environment_audio_exposure`.

## YAML Conventions

- Automation IDs: `marc_med_<description>`
- Dashboard YAML must be installed card-by-card via the manual card editor — pasting a full view YAML fails with "Expected an array value, but received: undefined"
- Markdown card averages require `content: >` (not `content: |`) for HTML rendering
- Stock alert thresholds: LOW ≤ 7 days, CRITICAL ≤ 3 days (DND bypass), OUT_OF_STOCK (3 urgent alerts)
