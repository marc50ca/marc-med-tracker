# Marc Med Tracker for Home Assistant

A comprehensive Home Assistant custom integration for tracking medications, including refills, dosage schedules, inventory management, automated alerts, **and visual daily dose tracking with red/green buttons**.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-blue.svg)](https://www.home-assistant.io/)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](CHANGELOG.md)
[![hacs](https://img.shields.io/badge/HACS-Default-orange.svg)](https://hacs.xyz)
[![GitHub Release](https://img.shields.io/github/release/yourusername/marc-med-tracker.svg)](https://github.com/yourusername/marc-med-tracker/releases)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/marc-med-tracker/graphs/commit-activity)

## Quick Links

- 📖 [Full Documentation](docs/)
- 🚀 [Quick Start](docs/QUICK_START_BUTTONS.md)
- 📦 [Installation Guide](docs/INSTALL.md)
- 🐛 [Troubleshooting](docs/TROUBLESHOOTING.md)
- 📋 [Examples](examples/)
- 🔄 [Changelog](CHANGELOG.md)
- 🤝 [Contributing](CONTRIBUTING.md)

## Project Structure

```
marc-med-tracker/
├── marc_med_tracker/         # Integration code
├── docs/                     # Documentation
├── examples/                 # Configuration examples
├── README.md                 # This file
├── OVERVIEW.md              # Feature overview
└── CHANGELOG.md             # Version history
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed layout.

## Features

- **Complete Medication Tracking**: Name, strength, prescribing doctor, refill count
- **Automated Inventory**: Tracks pills remaining based on dosage schedule
- **Smart Status Monitoring**: Visual indicators for low stock, critical levels, and out of stock
- **Refill Management**: Track refills left and when last refilled
- **Daily Dose Tracking**: Visual buttons that change from red (not taken) to green (taken)
- **Automatic Reset**: Dose trackers reset at midnight each day
- **Service Calls**: Easy integration with automations and scripts
- **Persistent Storage**: Data saved across restarts

## New: Daily Dose Tracking Buttons

The integration now includes binary sensors for tracking daily doses:
- **Morning Pills** - Red button turns green when checked off
- **Lunch Pills** - Red button turns green when checked off  
- **Evening Pills** - Red button turns green when checked off
- **Morning Puffer** - Red button turns green when checked off
- **Evening Puffer** - Red button turns green when checked off

All buttons automatically reset to red at midnight!

## New: Detailed Medication Information Panel

A comprehensive dashboard view showing:
- **Complete medication specifications** with all attributes
- **Active alerts** for medications needing attention
- **Refill schedules** with upcoming dates
- **Physician directory** grouped by prescribing doctor
- **Inventory history graphs** showing trends over time
- **Adherence tracking** with today's progress and weekly history
- **Quick reference tables** for at-a-glance information

See `medication_details_simple.yaml` for a ready-to-use panel!

## Installation

### HACS Installation (Recommended) ⭐

1. **Prerequisites**
   - [HACS](https://hacs.xyz/) installed in Home Assistant
   
2. **Add Integration**
   - Open HACS in Home Assistant
   - Go to "Integrations"
   - Click "+ Explore & Download Repositories"
   - Search for "Marc Med Tracker"
   - Click "Download"
   - Restart Home Assistant

3. **Configure**
   - Add to your `configuration.yaml` (see Configuration section below)
   - Restart Home Assistant

### Compatibility

- **Home Assistant Version**: 2024.1.0 or later
- **Python**: 3.11 or later
- **Tested**: Up to Home Assistant 2025.2.x

See [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) for detailed version information.

### Manual Installation

1. Copy the `marc_med_tracker` folder to your Home Assistant `custom_components` directory:
   ```
   /config/custom_components/marc_med_tracker/
   ```

2. Restart Home Assistant

### HACS Installation (Coming Soon)

This integration will be available through HACS in the future.

## Configuration

Add the following to your `configuration.yaml`:

```yaml
marc_med_tracker:
  medications:
    - name: "Aspirin"
      prescribing_doctor: "Dr. Smith"
      refills_left: 3
      last_refilled: "2026-01-15"
      strength: "100mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
      notes: "Take with food"
    
    - name: "Vitamin D"
      prescribing_doctor: "Dr. Johnson"
      refills_left: 5
      last_refilled: "2026-02-01"
      strength: "2000 IU"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 120
      notes: "Take in the morning"
    
    - name: "Blood Pressure Medication"
      prescribing_doctor: "Dr. Smith"
      refills_left: 2
      last_refilled: "2026-02-10"
      strength: "10mg"
      doses_per_day: 2
      pills_per_dose: 1
      initial_stock: 60
      notes: "Take morning and evening"
```

### Configuration Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Name of the medication |
| `prescribing_doctor` | string | Yes | Doctor who prescribed the medication |
| `refills_left` | integer | Yes | Number of refills remaining |
| `last_refilled` | date | Yes | Date of last refill (YYYY-MM-DD) |
| `strength` | string | Yes | Dosage strength (e.g., "100mg", "2000 IU") |
| `doses_per_day` | integer | Yes | Number of times taken per day |
| `pills_per_dose` | integer | Yes | Number of pills per dose |
| `initial_stock` | integer | Yes | Number of pills at last refill |
| `notes` | string | No | Additional notes about the medication |

## Sensors

Each medication creates a sensor with the following attributes:

### Main State
- Current number of pills remaining

### Attributes
- `medication_name`: Name of the medication
- `prescribing_doctor`: Doctor who prescribed it
- `strength`: Dosage strength
- `refills_left`: Number of refills remaining
- `last_refilled`: Date of last refill
- `days_since_refill`: Days since last refill
- `doses_per_day`: Doses per day
- `pills_per_dose`: Pills per dose
- `initial_stock`: Starting inventory
- `current_stock`: Current pills remaining
- `days_remaining`: Days of medication left
- `daily_consumption`: Pills consumed per day
- `status`: Current status (OK, LOW, CRITICAL, OUT_OF_STOCK, NO_REFILLS_LEFT)
- `needs_refill`: Boolean indicating if refill needed soon
- `out_of_stock`: Boolean indicating if out of stock
- `notes`: Any additional notes

### Status Values
- **OK**: More than 14 days remaining
- **LOW**: 7 or fewer days remaining
- **CRITICAL**: 3 or fewer days remaining
- **OUT_OF_STOCK**: No pills remaining
- **NO_REFILLS_LEFT**: Less than 14 days remaining and no refills left

## Binary Sensors (Daily Dose Trackers)

Five binary sensors for tracking daily doses that automatically reset at midnight:

### Entities
- `binary_sensor.marc_med_morning` - Morning Pills
- `binary_sensor.marc_med_lunch` - Lunch Pills
- `binary_sensor.marc_med_evening` - Evening Pills
- `binary_sensor.marc_med_morning_puffer` - Morning Puffer
- `binary_sensor.marc_med_evening_puffer` - Evening Puffer

### Binary Sensor States
- **Off** (Red): Dose not taken today
- **On** (Green): Dose taken today

### Binary Sensor Attributes
- `dose_type`: The dose identifier
- `dose_name`: Display name
- `scheduled_time`: Suggested time to take
- `taken_today`: Boolean if taken
- `last_taken`: ISO timestamp when taken
- `taken_at`: Formatted time (e.g., "08:30 AM")
- `minutes_ago`: Minutes since taken

## Services

### `marc_med_tracker.take_dose`

Record taking a dose of medication.

**Service Data:**
```yaml
service: marc_med_tracker.take_dose
data:
  medication_id: "aspirin"  # lowercase name with underscores
  doses: 1  # optional, defaults to 1
```

### `marc_med_tracker.refill`

Record a medication refill.

**Service Data:**
```yaml
service: marc_med_tracker.refill
data:
  medication_id: "aspirin"
  pills: 90
```

### `marc_med_tracker.update_refills`

Update the number of refills remaining.

**Service Data:**
```yaml
service: marc_med_tracker.update_refills
data:
  medication_id: "aspirin"
  refills: 5
```

### `marc_med_tracker.check_off_dose`

Mark a daily dose as taken (turns button from red to green).

**Service Data:**
```yaml
service: marc_med_tracker.check_off_dose
data:
  dose_id: "morning"  # Options: morning, lunch, evening, morning_puffer, evening_puffer
```

### `marc_med_tracker.uncheck_dose`

Unmark a daily dose (for corrections - turns button from green to red).

**Service Data:**
```yaml
service: marc_med_tracker.uncheck_dose
data:
  dose_id: "morning"
```

### `marc_med_tracker.update_doctor`

Update the prescribing doctor for a medication.

**Service Data:**
```yaml
service: marc_med_tracker.update_doctor
data:
  medication_id: "aspirin"
  doctor_name: "Dr. Jane Smith"
```

### `marc_med_tracker.update_stock`

Manually update the current number of pills on hand.

**Service Data:**
```yaml
service: marc_med_tracker.update_stock
data:
  medication_id: "aspirin"
  pills: 45
```

**Use Cases:**
- Correct inventory after manual count
- Adjust for pills dropped/lost
- Fix calculation errors
- Set initial count after adding medication

## Automation Examples

### Daily Dose Tracking Button

```yaml
# Simply toggle the button to mark as taken
automation:
  - alias: "Mark Morning Meds via Dashboard"
    trigger:
      - platform: state
        entity_id: binary_sensor.marc_med_morning
        to: "on"
    action:
      - service: notify.mobile_app
        data:
          message: "Morning medications marked as taken!"
```

### Check Off Dose via Automation

```yaml
automation:
  - alias: "Auto-check Morning Meds at 8 AM"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: state
        entity_id: input_boolean.auto_check_meds
        state: "on"
    action:
      - service: marc_med_tracker.check_off_dose
        data:
          dose_id: morning
```

### Daily Medication Reminder

```yaml
automation:
  - alias: "Morning Medication Reminder"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.marc_med_morning
        state: "off"  # Only remind if not taken
    action:
      - service: notify.mobile_app
        data:
          title: "Medication Reminder"
          message: "Time to take your morning medications"
          data:
            actions:
              - action: "CHECK_MORNING"
                title: "Mark as Taken"
```

### Handle Notification Action

```yaml
automation:
  - alias: "Handle Morning Meds Notification"
    trigger:
      - platform: event
        event_type: mobile_app_notification_action
        event_data:
          action: "CHECK_MORNING"
    action:
      - service: marc_med_tracker.check_off_dose
        data:
          dose_id: morning
      - service: marc_med_tracker.check_off_dose
        data:
          dose_id: morning_puffer
```

### Daily Medication Reminder

```yaml
automation:
  - alias: "Morning Medication Reminder"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.marc_med_aspirin
        above: 0
    action:
      - service: notify.mobile_app
        data:
          title: "Medication Reminder"
          message: "Time to take your morning medications"
```

### Low Stock Alert

```yaml
automation:
  - alias: "Medication Low Stock Alert"
    trigger:
      - platform: state
        entity_id: sensor.marc_med_aspirin
    condition:
      - condition: template
        value_template: "{{ state_attr('sensor.marc_med_aspirin', 'needs_refill') }}"
    action:
      - service: notify.mobile_app
        data:
          title: "Medication Alert"
          message: >
            {{ state_attr('sensor.marc_med_aspirin', 'medication_name') }} 
            is running low. Only {{ state_attr('sensor.marc_med_aspirin', 'days_remaining') }} 
            days remaining. Refills left: {{ state_attr('sensor.marc_med_aspirin', 'refills_left') }}
```

### Out of Stock Alert

```yaml
automation:
  - alias: "Medication Out of Stock"
    trigger:
      - platform: numeric_state
        entity_id: sensor.marc_med_aspirin
        below: 1
    action:
      - service: notify.mobile_app
        data:
          title: "Medication Out of Stock!"
          message: "{{ state_attr('trigger.entity_id', 'medication_name') }} is out of stock!"
          data:
            priority: high
```

### Track Dose Taking with Button

```yaml
script:
  take_morning_meds:
    alias: "Take Morning Medications"
    sequence:
      - service: marc_med_tracker.take_dose
        data:
          medication_id: "aspirin"
      - service: marc_med_tracker.take_dose
        data:
          medication_id: "vitamin_d"
      - service: notify.mobile_app
        data:
          message: "Morning medications recorded"
```

### Update Prescribing Doctor

```yaml
# Update doctor name via script
script:
  update_aspirin_doctor:
    alias: "Update Aspirin Doctor"
    sequence:
      - service: marc_med_tracker.update_doctor
        data:
          medication_id: "aspirin"
          doctor_name: "Dr. Jane Smith"
      - service: notify.mobile_app
        data:
          title: "Doctor Updated"
          message: "Aspirin prescribing doctor changed to Dr. Jane Smith"

# Or use in an automation
automation:
  - alias: "Notify on Doctor Change"
    trigger:
      - platform: event
        event_type: marc_med_tracker_doctor_updated
    action:
      - service: notify.mobile_app
        data:
          title: "Prescribing Doctor Updated"
          message: >
            {{ trigger.event.data.medication_name }} doctor changed 
            from {{ trigger.event.data.old_doctor }} 
            to {{ trigger.event.data.new_doctor }}
```

## Dashboard Card Examples

### Dashboard Files Included

The integration includes several complete dashboard configurations:

1. **dashboard_simple.yaml** - Daily dose tracker using built-in cards
2. **dashboard_with_buttons.yaml** - Enhanced tracker with custom button-card
3. **medication_details_simple.yaml** - Comprehensive details panel
4. **medication_details_panel.yaml** - Enhanced details with bar-card
5. **complete_dashboard.yaml** - All views combined in one file

Choose the one that fits your needs and copy it to your Lovelace configuration!

### Daily Dose Tracker with Buttons

```yaml
type: entities
title: Today's Medications
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning Pills"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_morning_puffer
    name: "💨 Morning Puffer"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: "🌞 Lunch Pills"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening Pills"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening_puffer
    name: "💨 Evening Puffer"
    tap_action:
      action: toggle
```

### Quick Glance View

```yaml
type: glance
title: Daily Doses
columns: 5
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
    name: Morning
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_morning_puffer
    name: Puffer
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: Lunch
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: Evening
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening_puffer
    name: Puffer
    tap_action:
      action: toggle
```

### Progress Tracker Card

```yaml
type: markdown
content: |
  {% set morning = states('binary_sensor.marc_med_morning') == 'on' %}
  {% set lunch = states('binary_sensor.marc_med_lunch') == 'on' %}
  {% set evening = states('binary_sensor.marc_med_evening') == 'on' %}
  {% set morning_puffer = states('binary_sensor.marc_med_morning_puffer') == 'on' %}
  {% set evening_puffer = states('binary_sensor.marc_med_evening_puffer') == 'on' %}
  {% set total = morning|int + lunch|int + evening|int + morning_puffer|int + evening_puffer|int %}
  
  ## Today's Progress: {{ total }}/5 Complete
  
  {{ '✅' if morning else '❌' }} Morning Pills
  {{ '✅' if morning_puffer else '❌' }} Morning Puffer
  {{ '✅' if lunch else '❌' }} Lunch Pills
  {{ '✅' if evening else '❌' }} Evening Pills
  {{ '✅' if evening_puffer else '❌' }} Evening Puffer
```

### Simple Entities Card

```yaml
type: entities
title: My Medications
entities:
  - entity: sensor.marc_med_aspirin
    secondary_info: last-changed
  - entity: sensor.marc_med_vitamin_d
    secondary_info: last-changed
  - entity: sensor.marc_med_blood_pressure_medication
    secondary_info: last-changed
```

### Detailed Card with Status

```yaml
type: custom:auto-entities
card:
  type: entities
  title: Marc Med Tracker
filter:
  include:
    - entity_id: "sensor.marc_med_*"
      options:
        type: custom:multiple-entity-row
        entity: this.entity_id
        secondary_info:
          attribute: status
        entities:
          - attribute: days_remaining
            name: Days Left
          - attribute: refills_left
            name: Refills
```

### Markdown Card with Details

```yaml
type: markdown
content: >
  ## 💊 Aspirin Status
  
  **Current Stock:** {{ states('sensor.marc_med_aspirin') }} pills
  
  **Days Remaining:** {{ state_attr('sensor.marc_med_aspirin', 'days_remaining') }} days
  
  **Refills Left:** {{ state_attr('sensor.marc_med_aspirin', 'refills_left') }}
  
  **Doctor:** {{ state_attr('sensor.marc_med_aspirin', 'prescribing_doctor') }}
  
  **Status:** {{ state_attr('sensor.marc_med_aspirin', 'status') }}
```

### Button Card for Taking Medication

```yaml
type: button
name: Take Aspirin
icon: mdi:pill
tap_action:
  action: call-service
  service: marc_med_tracker.take_dose
  service_data:
    medication_id: aspirin
```

## Medication ID Format

The medication ID is automatically generated from the medication name by:
1. Converting to lowercase
2. Replacing spaces with underscores

Examples:
- "Aspirin" → `aspirin`
- "Vitamin D" → `vitamin_d`
- "Blood Pressure Medication" → `blood_pressure_medication`

## Troubleshooting

### Sensor Not Appearing

1. Check your `configuration.yaml` for syntax errors
2. Verify the marc_med_tracker folder is in `custom_components`
3. Restart Home Assistant
4. Check the logs for errors: Settings → System → Logs

### Incorrect Stock Count

The integration calculates current stock based on:
- Initial stock at last refill
- Days since last refill
- Daily consumption (doses_per_day × pills_per_dose)

If the count is incorrect:
1. Record a refill with the correct pill count
2. Use the `marc_med_tracker.refill` service

### Dates Not Working

Ensure dates are in ISO format: `YYYY-MM-DD`
Example: `2026-02-16`

## Support

For issues, feature requests, or contributions, please visit:
[GitHub Repository](https://github.com/yourusername/marc_med_tracker)

## License

This project is licensed under the MIT License.

## Disclaimer

This integration is for informational and tracking purposes only. It should not be used as a substitute for professional medical advice. Always consult with healthcare professionals regarding your medications.
# marc-med-tracker
