# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Marc Med Tracker v2.1.1** — A Home Assistant custom integration (HACS) for medication tracking, health metrics from Apple Health, and iPhone notifications. The target repository is `marc50ca/marc-med-tracker` on GitHub.

## Development Commands

```bash
make install       # Install dependencies (homeassistant, voluptuous, black, ruff, pytest)
make test          # Run tests (pytest tests/)
make lint          # ruff + black --check + isort --check
make format        # black + isort (auto-fix)
make validate      # Validate manifest.json, services.yaml, Python syntax
make release       # Build marc-med-tracker.zip for distribution
```

Run a single test file: `pytest tests/test_calculations.py -v`

**Note:** The Makefile's `lint`/`format`/`validate` targets reference `marc_med_tracker/` (a subdirectory), but the integration Python files (`__init__.py`, `sensor.py`, `binary_sensor.py`) currently live in the repo root. Adjust paths if running those targets directly.

## Deployment Context

This is a **Home Assistant custom integration**, not a standalone app. Code runs inside Home Assistant's Python environment. Configuration is YAML-based. There is no local build/test pipeline — all validation is done against a running Home Assistant instance or via the GitHub Actions workflows in `.github/workflows/`.

The integration files (`__init__.py`, `sensor.py`, `binary_sensor.py`, etc.) are placed in Home Assistant's `custom_components/marc_med_tracker/` directory.

## Architecture

The integration has two layers:

1. **Integration layer** (`__init__.py`, `sensor.py`, `binary_sensor.py`, `services.yaml`, `manifest.json`) — standard Home Assistant custom component structure. Binary sensors have a known loading issue; the workaround is manual template sensors defined in `examples/manual_binary_sensors.yaml`.

2. **Configuration layer** (`examples/`) — YAML files the user copies into their Home Assistant configuration. These are not executed by the integration itself; they use Home Assistant's built-in `template`, `input_boolean`, `input_number`, `automation`, and `script` platforms.

## Key Domain Rules

- **Blood glucose units: mmol/L** (Canadian standard). Never use mg/dL. Fasting target: 4.0–7.0 mmol/L; post-meal: 5.0–10.0 mmol/L.
- **A1C formula:** `A1C (%) = (avg_mmol_L × 0.555) + 2.59`
- **Spironolactone dose:** 0.5 tablet of a 60mg pill = 30mg actual dose.
- **Zenhale:** 1 puff twice daily; must include "rinse mouth" reminder.
- **Metformin:** 2 tablets per dose, twice daily (4 tablets/day).
- **iPhone notifications:** `notify.mobile_app_marcs_iphone_14` at 9:30, 14:30, 19:30.

## Medications (8 total)

| Medication | Dose | Time | Prescriber | Initial Stock |
|---|---|---|---|---|
| Metformin 500mg | 2 tabs | morning + lunch | NP T. Wakefield | 360 |
| Jardiance 40mg | 1 tab | evening | NP T. Wakefield | 90 |
| Candesartan 16mg | 1 tab | morning | NP T. Wakefield | 90 |
| Rosuvastatin 10mg | 1 tab | morning | NP T. Wakefield | 90 |
| Pantoprazole 40mg | 1 tab | morning | NP T. Wakefield | 90 |
| Bisoprolol 2.5mg | 1 tab | morning | Dr. K. Ducet | 90 |
| Spironolactone 60mg | 0.5 tab | morning | Dr. K. Ducet | 45 |
| Zenhale 100/6mcg | 1 puff | morning + evening | Dr. K. Safka | 200 doses |

Refill dates: NP T. Wakefield → March 25, 2026; Dr. K. Ducet & Dr. K. Safka → February 1, 2026.

## Known Issues

- **Binary sensors won't load** from the integration itself (root cause unknown). Workaround: use `examples/manual_binary_sensors.yaml` with modern `template:` syntax (not legacy `platform: template`).
- **Dashboard YAML** must be installed card-by-card via the manual card editor — pasting the full view YAML causes "Expected an array value, but received: undefined".
- **Markdown card averages** require `content: >` (not `content: |`) for HTML rendering.

## Apple Health Sensors

Prefix for all sensors: `hae.marchealthsync_`. Total: 33 sensors across blood glucose (1), cardiovascular (10), sleep (7), weight (3), activity (12). Sensors within each section are alphabetically sorted. The excluded sensors are `hae.marchealthsync_sleep_analysis_sleep` (duplicate) and `hae.marchealthsync_environment_audio_exposure`.

## YAML Conventions

- All example YAML must be validated for zero syntax errors before delivery.
- Use modern Home Assistant template syntax throughout.
- Automation IDs follow the pattern `marc_med_<description>`.
- Stock alert thresholds: LOW ≤ 7 days supply, CRITICAL ≤ 3 days (DND bypass), OUT_OF_STOCK (3 urgent alerts).
