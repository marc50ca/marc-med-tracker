# Changelog

All notable changes to Marc Med Tracker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.1] - 2026-03-30

### Fixed
- **Corrected Zenhale Inhaler Prescriber**: Changed from Dr. K. Ducet to Dr. K. Safka
- Configuration now shows 3 prescribers: NP T. Wakefield, Dr. K. Ducet, Dr. K. Safka
- Updated all documentation to reflect correct prescriber information

---

## [2.1.0] - 2026-03-29

### Added

#### Complete Health Tracking Dashboard
- **Blood Sugar Section** with automatic A1C calculator
  - Tracks total test count since April 30, 2026
  - Calculates average glucose level
  - Auto-calculates estimated A1C when 21+ readings available
  - Formula: (Average + 2.9) / 1.59
  - Progress indicator showing tests needed for A1C

- **Cardio-Vascular Section** with gauges and graphs
  - Blood pressure gauges (systolic & diastolic) with color zones
  - Heart rate and resting heart rate tracking
  - O2 saturation monitoring
  - 7-day trend graphs for BP and heart rate

- **Sleep Tracking Section**
  - Total sleep duration
  - Core sleep hours
  - Deep sleep hours
  - Awake hours tracking
  - Flights climbed
  - 7-day sleep quality graph

- **Activity Tracking Section**
  - Steps and distance tracking
  - Active calories burned
  - Exercise time monitoring
  - Stand time tracking
  - Walking speed
  - Body mass tracking
  - 7-day activity trend graphs

#### Dashboard Improvements
- Shortcut button for main dashboard (`shortcut_button.yaml`)
- 29 total cards organized in 6 major sections
- All health metrics show current value + 7-day history
- Color-coded gauges with safe/warning/danger zones

#### Documentation
- `DASHBOARD_INSTALLATION.md` - Complete step-by-step guide
- Fixed "Expected an array value" error instructions
- Video tutorial steps included
- Troubleshooting for all common errors

### Changed
- Dashboard now includes health tracking alongside medications
- Total card count increased from 13 to 29
- Dashboard file size optimized for faster loading

### Fixed
- Dashboard installation error ("Expected an array value")
- Corrected YAML structure for view format
- Clear instructions to DELETE existing YAML before pasting

---

## [2.0.0] - 2026-03-28

### Added

#### Core Medication Tracking
- **8 Medication Configuration**
  - Metformin 500mg (2 tablets, twice daily)
  - Jardiance 40mg (1 tablet, evening)
  - Candesartan 16mg (1 tablet, morning)
  - Rosuvastatin 10mg (1 tablet, morning)
  - Pantoprazole 40mg (1 tablet, morning)
  - Bisoprolol 2.5mg (1 tablet, morning)
  - Spironolactone 60mg (0.5 tablet, morning)
  - Zenhale Inhaler (1-2 puffs, twice daily)

- **Prescriber Organization**
  - NP T. Wakefield (5 medications)
  - Dr. K. Ducet (3 medications)
  - Last refilled dates: March 25 & February 1, 2026

#### iPhone Notifications (19 Automations)
- **Timed Reminders**
  - 9:30 AM - Morning medications
  - 2:30 PM - Lunch medications
  - 7:30 PM - Evening medications

- **Features**
  - Actionable buttons (Mark as Taken / Snooze 15 min)
  - Critical alerts bypass Do Not Disturb
  - Daily summary at 10:00 PM
  - Weekly refill check (Sunday 6:00 PM)
  - Perfect adherence celebration

- **Stock Alerts**
  - Low stock warning (≤7 days)
  - Critical alert (≤3 days) - bypasses DND
  - Out of stock - 3 urgent alerts

#### Dashboard
- Daily medication schedule with red/green buttons
- Progress percentage tracker
- Medication inventory by prescriber
- Active alerts with color coding
- 30-day refill calendar
- Quick statistics summary

#### Documentation
- `QUICK_START.md` - 15-minute setup guide
- `MEDICATION_SCHEDULE.md` - Daily schedule reference
- `NOTIFICATION_SETUP.md` - iPhone notification guide
- `NOTIFICATION_REFERENCE.md` - Quick reference card
- Complete example configurations

### Changed
- Repository structure to HACS-compliant format
- Integration files moved to repository root
- `content_in_root: true` in hacs.json

### Technical
- Integration validates with zero errors
- All YAML files syntax-checked
- Automation file: 19 automations validated
- Configuration file: 8 medications validated

---

## [1.0.0] - Initial Development

### Added
- Basic medication tracking integration
- Sensor platform for inventory
- Binary sensor platform for daily tracking
- 7 core services
- YAML configuration support
- Basic documentation

---

## Versioning Guide

### Version Number Format: MAJOR.MINOR.PATCH

**MAJOR** version (X.0.0):
- Incompatible API changes
- Major feature overhaul
- Breaking changes requiring user action

**MINOR** version (2.X.0):
- New features added
- Backwards compatible
- New functionality that doesn't break existing setups

**PATCH** version (2.1.X):
- Bug fixes
- Documentation updates
- Minor improvements
- Backwards compatible

---

## Upgrade Notes

### From 2.0.0 to 2.1.0

**No breaking changes** - fully backwards compatible

**New Features:**
- Health tracking sections (optional)
- Shortcut button for main dashboard

**Action Required:**
- None - existing installations continue to work
- To use new features: Update dashboard using new `complete_dashboard.yaml`

**Health Sensors:**
If you don't have health sensors configured, the health sections will show "unavailable" but medication tracking continues to work normally.

---

## Coming Soon (Planned Features)

### Version 2.2.0 (Planned)
- [ ] Config flow (UI-based configuration)
- [ ] Lovelace card for medication details
- [ ] Multiple user support
- [ ] Custom refill reminder times per medication

### Version 2.3.0 (Planned)
- [ ] Medication interaction warnings
- [ ] Doctor appointment tracking
- [ ] Prescription renewal reminders
- [ ] Insurance coverage tracking

### Version 3.0.0 (Future)
- [ ] Mobile app integration
- [ ] Barcode scanning for medications
- [ ] Photo upload for pills
- [ ] AI-powered medication identification

---

## Support & Feedback

- **Bug Reports**: GitHub Issues
- **Feature Requests**: GitHub Issues with "enhancement" label
- **Questions**: GitHub Discussions
- **Documentation**: See `docs/` folder

---

## Links

- **GitHub**: https://github.com/marc50ca/marc-med-tracker
- **HACS**: Install via custom repository
- **Documentation**: https://github.com/marc50ca/marc-med-tracker/tree/main/docs
- **Examples**: https://github.com/marc50ca/marc-med-tracker/tree/main/examples
