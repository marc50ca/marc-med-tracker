# Daily Dose Tracking with Red/Green Buttons

## Overview

The Marc Med Tracker now includes visual daily dose tracking buttons that:
- Start RED each day (not taken)
- Turn GREEN when you tap them (taken)
- Automatically reset to RED at midnight
- Track when each dose was taken

## Available Dose Trackers

1. **Morning Pills** (`binary_sensor.marc_med_morning`)
2. **Lunch Pills** (`binary_sensor.marc_med_lunch`)
3. **Evening Pills** (`binary_sensor.marc_med_evening`)
4. **Morning Puffer** (`binary_sensor.marc_med_morning_puffer`)
5. **Evening Puffer** (`binary_sensor.marc_med_evening_puffer`)

## How to Use

### Method 1: Dashboard Buttons (Recommended)

Add this to your Lovelace dashboard:

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

**Simply tap any button to mark it as taken!**

### Method 2: Service Calls

Use the service in automations or scripts:

```yaml
service: marc_med_tracker.check_off_dose
data:
  dose_id: morning  # or: lunch, evening, morning_puffer, evening_puffer
```

### Method 3: Custom Button Card (Optional)

For extra visual appeal, install the `button-card` from HACS and use:

```yaml
type: custom:button-card
entity: binary_sensor.marc_med_morning
name: Morning Pills
tap_action:
  action: call-service
  service: marc_med_tracker.check_off_dose
  service_data:
    dose_id: morning
state:
  - value: 'on'
    styles:
      card:
        - background-color: '#4CAF50'
        - color: white
  - value: 'off'
    styles:
      card:
        - background-color: '#f44336'
        - color: white
```

## Visual Appearance

**When Not Taken (Red):**
- Button shows as red/off state
- Icon appears in red (if using custom theme)
- Status: OFF

**When Taken (Green):**
- Button shows as green/on state
- Icon appears in green
- Status: ON
- Shows time taken (e.g., "8:30 AM")

## Automatic Reset

All buttons automatically reset to RED (not taken) at midnight. No manual intervention needed!

## Integration with Reminders

Set up reminders that only trigger if dose not taken:

```yaml
automation:
  - alias: "Morning Med Reminder"
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
          title: "Morning Medications"
          message: "Don't forget your morning pills!"
```

## Check from Notification

Create notifications with action buttons:

```yaml
action:
  - service: notify.mobile_app
    data:
      title: "Morning Medications"
      message: "Time for your morning meds"
      data:
        actions:
          - action: "MARK_MORNING"
            title: "Mark as Taken"
```

Then handle the action:

```yaml
automation:
  - alias: "Handle Notification Action"
    trigger:
      - platform: event
        event_type: mobile_app_notification_action
        event_data:
          action: "MARK_MORNING"
    action:
      - service: marc_med_tracker.check_off_dose
        data:
          dose_id: morning
```

## Tracking Compliance

Create a sensor to track daily compliance:

```yaml
template:
  - sensor:
      - name: "Daily Medication Compliance"
        state: >
          {% set taken = [
            states('binary_sensor.marc_med_morning'),
            states('binary_sensor.marc_med_morning_puffer'),
            states('binary_sensor.marc_med_lunch'),
            states('binary_sensor.marc_med_evening'),
            states('binary_sensor.marc_med_evening_puffer')
          ] | select('eq', 'on') | list | count %}
          {{ (taken / 5 * 100) | round(0) }}
        unit_of_measurement: "%"
```

## Weekly History

View your adherence over time:

```yaml
type: history-graph
title: Weekly Medication Adherence
hours_to_show: 168
entities:
  - entity: binary_sensor.marc_med_morning
  - entity: binary_sensor.marc_med_lunch
  - entity: binary_sensor.marc_med_evening
  - entity: binary_sensor.marc_med_morning_puffer
  - entity: binary_sensor.marc_med_evening_puffer
```

## Customizing Colors

To get the best red/green appearance, install the included theme:

1. Copy `marc_med_tracker_theme.yaml` to `/config/themes/`
2. Add to `configuration.yaml`:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Select the "Marc Med Tracker" theme in your profile

## Tips

1. **Hold to Undo**: Set up hold actions to uncheck if you tap by mistake
2. **Batch Check**: Create scripts to check multiple doses at once
3. **Voice Control**: Integrate with voice assistants to check off doses hands-free
4. **Notification Sounds**: Customize notification sounds for different times of day
5. **Family Sharing**: Create separate users/dashboards for different family members

## Troubleshooting

**Buttons not changing color:**
- Enable `state_color: true` in your entity card
- Install and activate the medication tracker theme
- Check that the entity is actually toggling (check Developer Tools → States)

**Not resetting at midnight:**
- Verify Home Assistant is running at midnight
- Check the automation logs for the reset automation
- Manually test: `service: marc_med_tracker.uncheck_dose`

**Entity not found:**
- Verify the integration loaded correctly
- Check for errors in Settings → System → Logs
- Restart Home Assistant after installation
