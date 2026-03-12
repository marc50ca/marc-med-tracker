# Changelog

All notable changes to Marc Med Tracker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-02-21

### Added
- **NEW SERVICE**: `update_stock` - Manually set current pill count
  - Useful for physical inventory counts
  - Correcting calculation errors
  - Accounting for lost/dropped pills
- **NEW SERVICE**: `update_doctor` - Change prescribing doctor name
- **Daily Dose Tracking**: Red/green buttons for tracking doses
  - Morning Pills tracker
  - Lunch Pills tracker
  - Evening Pills tracker
  - Morning Puffer tracker
  - Evening Puffer tracker
  - Automatic midnight reset
- **Detailed Information Panels**: Complete medication details dashboards
- **Event System**: Events fired for stock updates and doctor changes
- **Comprehensive Documentation**:
  - UPDATE_STOCK_GUIDE.md - Stock management guide
  - UPDATE_DOCTOR_GUIDE.md - Doctor update guide
  - DOSE_TRACKING_GUIDE.md - Daily tracking guide
  - DETAILS_PANEL_GUIDE.md - Dashboard setup
  - TROUBLESHOOTING.md - Common issues and solutions
  - COMPATIBILITY.md - Version compatibility matrix
  - UPGRADE_NOTES.md - Migration instructions

### Changed
- **BREAKING**: Renamed from `med_tracker` to `marc_med_tracker`
  - Domain: `med_tracker` → `marc_med_tracker`
  - Entity prefix: `med_` → `marc_med_`
  - Service prefix: `med_tracker.*` → `marc_med_tracker.*`
- **Updated for Home Assistant 2024.1.0+**:
  - Modern type hints (`dict[str, Any]` instead of `Dict[str, Any]`)
  - Added `from __future__ import annotations`
  - Updated imports to use `ConfigType` and `DiscoveryInfoType`
  - Added `_attr_has_entity_name = False` to entities
  - Changed IoT class from `local_polling` to `calculated`
- **Platform loading**: Fixed to work with YAML configuration
- **Sensor names**: Changed from "Med X" to "Marc Med X"

### Fixed
- Platform discovery for YAML-based configuration
- Import errors with Home Assistant 2025.2+
- Service registration in async_setup

### Deprecated
- None

### Removed
- None

### Security
- None

## [1.0.0] - 2025-01-15

### Added
- Initial release
- Basic medication tracking
- Inventory management
- Refill tracking
- Service calls: `take_dose`, `refill`, `update_refills`
- Sensor platform for medication inventory
- Configuration via YAML
- Automated stock calculations
- Status indicators (OK, LOW, CRITICAL, OUT_OF_STOCK)

---

## Version History Summary

| Version | Date | Key Features |
|---------|------|--------------|
| 2.0.0 | 2025-02-21 | Stock updates, doctor changes, daily tracking, HA 2025.2 support |
| 1.0.0 | 2025-01-15 | Initial release with basic tracking |

---

## Migration Guide

### From 1.0.0 to 2.0.0

**Entity ID Changes:**
```yaml
# Old:
sensor.med_aspirin
binary_sensor.med_morning

# New:
sensor.marc_med_aspirin
binary_sensor.marc_med_morning
```

**Service Changes:**
```yaml
# Old:
service: med_tracker.take_dose

# New:
service: marc_med_tracker.take_dose
```

**Configuration Changes:**
```yaml
# Old:
med_tracker:
  medications: [...]

# New:
marc_med_tracker:
  medications: [...]
```

**Action Required:**
1. Update `configuration.yaml` - change `med_tracker:` to `marc_med_tracker:`
2. Update all automations - replace `med_tracker.` with `marc_med_tracker.`
3. Update dashboard cards - replace `med_` with `marc_med_` in entity IDs
4. Restart Home Assistant

**Data Migration:**
- All medication data is preserved
- Stock counts carry over automatically
- No manual data migration needed

See [UPGRADE_NOTES.md](UPGRADE_NOTES.md) for detailed instructions.

---

## Upcoming Features (Planned)

### v2.1.0
- [ ] Config flow support (UI configuration)
- [ ] Medication categories/tags
- [ ] Multiple daily schedules (AM/PM variations)
- [ ] Medication interaction warnings
- [ ] Photo support for pill identification
- [ ] Barcode scanning integration

### v2.2.0
- [ ] Calendar integration for refill dates
- [ ] Shopping list integration
- [ ] Medication history graphs
- [ ] Adherence statistics
- [ ] Export medication records
- [ ] Multi-language support

### v3.0.0
- [ ] Full config flow migration
- [ ] Cloud sync support (optional)
- [ ] Mobile app companion
- [ ] Advanced reporting
- [ ] Integration with pharmacy APIs
- [ ] Health app integration

---

## Support

For issues, questions, or feature requests:
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Review [closed issues](https://github.com/yourusername/marc-med-tracker/issues?q=is%3Aissue+is%3Aclosed)
- Open a [new issue](https://github.com/yourusername/marc-med-tracker/issues/new)

---

## Contributors

Thank you to all contributors who have helped make Marc Med Tracker better!

<!-- Add contributors here -->

---

[2.0.0]: https://github.com/yourusername/marc-med-tracker/releases/tag/v2.0.0
[1.0.0]: https://github.com/yourusername/marc-med-tracker/releases/tag/v1.0.0
