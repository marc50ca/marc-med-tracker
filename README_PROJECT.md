# Marc Med Tracker

> A comprehensive Home Assistant integration for complete medication management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-41BDF5.svg)](https://www.home-assistant.io/)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](CHANGELOG.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/marc-med-tracker/graphs/commit-activity)

## Features at a Glance

- 💊 **Complete Medication Tracking** - Track name, strength, doctor, refills, and more
- 📦 **Smart Inventory** - Automatic calculation of pills remaining
- 🟢 **Daily Dose Buttons** - Red/green visual tracking that resets at midnight
- 📊 **Detailed Panels** - Comprehensive medication information dashboards
- 🔔 **Automated Alerts** - Low stock, critical levels, refill reminders
- 🔄 **7 Service Calls** - Full automation integration
- 📈 **Event Tracking** - Monitor all changes with events
- 🎨 **Custom Theme** - Optimized red/green color scheme

## Quick Start

### Installation (3 minutes)

1. **Download the latest release**
2. **Extract to custom_components:**
   ```bash
   unzip marc-med-tracker.zip
   cp -r marc-med-tracker/marc_med_tracker /config/custom_components/
   ```
3. **Add to configuration.yaml:**
   ```yaml
   marc_med_tracker:
     medications:
       - name: "Aspirin"
         prescribing_doctor: "Dr. Smith"
         refills_left: 3
         last_refilled: "2025-02-20"
         strength: "100mg"
         doses_per_day: 1
         pills_per_dose: 1
         initial_stock: 90
   ```
4. **Restart Home Assistant**

See [docs/INSTALL.md](docs/INSTALL.md) for detailed instructions.

### First Dashboard (2 minutes)

Add this card to your dashboard:

```yaml
type: entities
title: Today's Medications
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning Pills"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening Pills"
    tap_action:
      action: toggle
```

Tap buttons to mark doses as taken. They turn green! ✅

## Documentation

### Getting Started
- 📖 [**README**](README.md) - Main documentation
- 🚀 [**Quick Start**](docs/QUICK_START_BUTTONS.md) - 3-minute setup
- 📦 [**Installation**](docs/INSTALL.md) - Step-by-step guide
- ✨ [**Overview**](OVERVIEW.md) - Feature summary

### Guides
- 💊 [**Dose Tracking**](docs/DOSE_TRACKING_GUIDE.md) - Using red/green buttons
- 📊 [**Details Panel**](docs/DETAILS_PANEL_GUIDE.md) - Information dashboards
- 🩺 [**Update Doctor**](docs/UPDATE_DOCTOR_GUIDE.md) - Change prescribing doctor
- 📦 [**Update Stock**](docs/UPDATE_STOCK_GUIDE.md) - Manual inventory counts

### Reference
- 🔧 [**Troubleshooting**](docs/TROUBLESHOOTING.md) - Common issues
- 📋 [**Compatibility**](docs/COMPATIBILITY.md) - Version requirements
- 🔄 [**Upgrade Notes**](docs/UPGRADE_NOTES.md) - Migration guide
- 📝 [**Changelog**](CHANGELOG.md) - Version history

### Examples
- [Configuration Examples](examples/configuration.yaml.example)
- [Automation Examples](examples/automations.yaml.example)
- [Dashboard Examples](examples/)
- [Theme](examples/marc_med_tracker_theme.yaml)

## What's Included

### 📊 Sensors (Inventory Tracking)
- `sensor.marc_med_{medication}` - Shows pills remaining
- Attributes: doctor, strength, refills, days left, status, etc.
- Auto-calculates based on dosage schedule

### 🔘 Binary Sensors (Daily Tracking)
- `binary_sensor.marc_med_morning` - Morning pills
- `binary_sensor.marc_med_lunch` - Lunch pills
- `binary_sensor.marc_med_evening` - Evening pills
- `binary_sensor.marc_med_morning_puffer` - Morning puffer
- `binary_sensor.marc_med_evening_puffer` - Evening puffer
- Automatically reset at midnight

### ⚙️ Services (7 Total)
1. `take_dose` - Record taking medication
2. `refill` - Log a pharmacy refill
3. `update_refills` - Change refill count
4. `check_off_dose` - Mark daily dose as taken
5. `uncheck_dose` - Unmark if mistake
6. `update_doctor` - Change prescribing doctor
7. `update_stock` - Set exact pill count

### 📱 Example Use Cases

**Daily Tracking:**
```yaml
# Tap button on dashboard → Turns green
# Automatic midnight reset → Back to red
```

**Inventory Management:**
```yaml
service: marc_med_tracker.update_stock
data:
  medication_id: aspirin
  pills: 42  # Physical count
```

**Automation:**
```yaml
automation:
  - alias: "Low Stock Alert"
    trigger:
      - platform: numeric_state
        entity_id: sensor.marc_med_aspirin
        below: 10
    action:
      - service: notify.mobile_app
        data:
          message: "Aspirin running low!"
```

## Screenshots

### Daily Dose Tracker
Red buttons (not taken) turn green when clicked. Auto-resets at midnight.

### Medication Details Panel
Complete information: stock, days remaining, refills, doctor, schedule, alerts.

### Inventory Sensors
Real-time tracking with status indicators (OK, LOW, CRITICAL, OUT_OF_STOCK).

## Requirements

- Home Assistant 2024.1.0 or later
- Python 3.11 or later
- YAML configuration (config flow coming in v2.1)

## Support

- 🐛 [Issue Tracker](https://github.com/yourusername/marc-med-tracker/issues)
- 💬 [Discussions](https://github.com/yourusername/marc-med-tracker/discussions)
- 📖 [Documentation](docs/)
- 🤝 [Contributing](CONTRIBUTING.md)

## Roadmap

See [CHANGELOG.md](CHANGELOG.md) for planned features:
- Config flow support (UI configuration)
- Medication categories
- Calendar integration
- Barcode scanning
- Health app integration

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## Disclaimer

⚠️ **Medical Disclaimer**: This integration is for informational and tracking purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult healthcare professionals regarding your medications.

## Acknowledgments

- Home Assistant community
- All contributors
- You for using Marc Med Tracker!

---

**Made with ❤️ for the Home Assistant community**
