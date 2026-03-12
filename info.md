[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![hacs](https://img.shields.io/badge/HACS-Default-orange.svg)](https://hacs.xyz)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](https://github.com/yourusername/marc-med-tracker/releases)

# Marc Med Tracker

> Complete medication management for Home Assistant

## Features

💊 **Medication Tracking**
- Track multiple medications with full details
- Automatic inventory calculation
- Smart refill reminders

🟢 **Daily Dose Buttons**  
- Visual red/green buttons
- Tap to mark as taken
- Auto-reset at midnight

📊 **Beautiful Dashboards**
- Modern, professional design
- Color-coded status indicators
- Mobile optimized

🔔 **Automated Alerts**
- Low stock warnings
- Critical level alerts
- Refill reminders

📦 **Inventory Management**
- Automatic stock calculation
- Days remaining tracker
- Refill history

## Quick Start

### 1. Configure Your Medications

Add to `configuration.yaml`:

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

### 2. Restart Home Assistant

### 3. Add Dashboard

Copy one of the example dashboards from the `examples/` folder:
- `dashboard_beautiful_simple.yaml` - Recommended, no custom cards
- `dashboard_beautiful.yaml` - With custom cards
- `dashboard_simple.yaml` - Basic functionality

### 4. Start Tracking!

Tap the red buttons to mark doses as taken. They turn green! ✅

## What You Get

### Sensors (Inventory)
- `sensor.marc_med_aspirin` - Shows pills remaining
- Auto-calculates based on dosage schedule
- Status: OK, LOW, CRITICAL, OUT_OF_STOCK

### Binary Sensors (Daily Tracking)  
- `binary_sensor.marc_med_morning` - Morning pills
- `binary_sensor.marc_med_lunch` - Lunch pills
- `binary_sensor.marc_med_evening` - Evening pills
- `binary_sensor.marc_med_morning_puffer` - Morning puffer
- `binary_sensor.marc_med_evening_puffer` - Evening puffer

### Services (7 Total)
1. `take_dose` - Record taking medication
2. `refill` - Log pharmacy refill
3. `update_refills` - Update refill count
4. `check_off_dose` - Mark daily dose (green button)
5. `uncheck_dose` - Unmark if mistake
6. `update_doctor` - Change prescribing doctor
7. `update_stock` - Set exact pill count

## Screenshots

### Daily Tracker
Beautiful red/green buttons that auto-reset at midnight

### Medication Inventory
Complete details: stock, days remaining, refills, doctor, status

### Active Alerts
Color-coded warnings when action is needed

### Refill Schedule
Visual calendar of upcoming refill dates

## Documentation

📖 [Full Documentation](https://github.com/yourusername/marc-med-tracker)  
🚀 [Quick Start Guide](https://github.com/yourusername/marc-med-tracker/blob/main/docs/QUICK_START_BUTTONS.md)  
🐛 [Troubleshooting](https://github.com/yourusername/marc-med-tracker/blob/main/docs/TROUBLESHOOTING.md)  
📋 [Examples](https://github.com/yourusername/marc-med-tracker/tree/main/examples)

## Support

Having issues? Check the [troubleshooting guide](https://github.com/yourusername/marc-med-tracker/blob/main/docs/TROUBLESHOOTING.md) or [open an issue](https://github.com/yourusername/marc-med-tracker/issues).

## Contributing

Contributions welcome! See [CONTRIBUTING.md](https://github.com/yourusername/marc-med-tracker/blob/main/CONTRIBUTING.md)

---

**⚠️ Medical Disclaimer**: This integration is for tracking purposes only. Always consult healthcare professionals regarding your medications.
