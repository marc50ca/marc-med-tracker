# Quick Start: Daily Dose Tracking Buttons

## What You Get

After installing this integration, you'll have 5 visual buttons that track your daily medications:

| Button | Entity | Color When Not Taken | Color When Taken |
|--------|--------|---------------------|------------------|
| ☀️ Morning Pills | `binary_sensor.marc_med_morning` | 🔴 RED | 🟢 GREEN |
| 💨 Morning Puffer | `binary_sensor.marc_med_morning_puffer` | 🔴 RED | 🟢 GREEN |
| 🌞 Lunch Pills | `binary_sensor.marc_med_lunch` | 🔴 RED | 🟢 GREEN |
| 🌙 Evening Pills | `binary_sensor.marc_med_evening` | 🔴 RED | 🟢 GREEN |
| 💨 Evening Puffer | `binary_sensor.marc_med_evening_puffer` | 🔴 RED | 🟢 GREEN |

**All buttons automatically reset to RED at midnight!**

## 3-Minute Setup

### Step 1: Add to Dashboard

Go to your Home Assistant dashboard and add a new card:

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

### Step 2: Tap to Track

- **RED button** = Not taken yet
- **Tap button** = Marks as taken (turns GREEN)
- **Tap again** = Unmarks if you made a mistake

### Step 3: Add Reminders (Optional)

Add this automation to get reminded if you haven't taken your morning meds by 8 AM:

```yaml
automation:
  - alias: "Morning Medication Reminder"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.marc_med_morning
        state: "off"
    action:
      - service: notify.mobile_app_your_phone
        data:
          title: "☀️ Morning Medications"
          message: "Time to take your morning pills and puffer!"
```

## That's It!

You now have a simple red/green button system to track your daily medications.

## Want More?

### Progress Tracker

Add a card showing your daily progress:

```yaml
type: markdown
content: |
  {% set taken = [
    states('binary_sensor.marc_med_morning'),
    states('binary_sensor.marc_med_morning_puffer'),
    states('binary_sensor.marc_med_lunch'),
    states('binary_sensor.marc_med_evening'),
    states('binary_sensor.marc_med_evening_puffer')
  ] | select('eq', 'on') | list | count %}
  
  ## Today: {{ taken }}/5 Complete
  
  {% if taken == 5 %}🎉 All done!
  {% elif taken == 0 %}⏰ Don't forget your meds
  {% else %}📋 {{ 5 - taken }} remaining
  {% endif %}
```

### Quick Glance

Prefer a horizontal layout? Use this:

```yaml
type: glance
title: Daily Doses
columns: 5
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
  - entity: binary_sensor.marc_med_morning_puffer
  - entity: binary_sensor.marc_med_lunch
  - entity: binary_sensor.marc_med_evening
  - entity: binary_sensor.marc_med_evening_puffer
```

### Weekly History

Track your adherence over time:

```yaml
type: history-graph
title: 7-Day History
hours_to_show: 168
entities:
  - binary_sensor.marc_med_morning
  - binary_sensor.marc_med_lunch
  - binary_sensor.marc_med_evening
  - binary_sensor.marc_med_morning_puffer
  - binary_sensor.marc_med_evening_puffer
```

## Common Questions

**Q: What if I take my meds at different times?**
A: Just tap the button whenever you take them. It tracks that you took them, not when.

**Q: Can I mark them from my phone?**
A: Yes! The buttons work in the Home Assistant mobile app too.

**Q: What if I forget to tap the button?**
A: You can tap it later in the day. Or set up automations that remind you.

**Q: Do I need the custom button-card?**
A: No! The built-in entity cards work great with state_color enabled.

**Q: Can I change the colors?**
A: Yes! Install the included `marc_med_tracker_theme.yaml` for optimized red/green colors.

**Q: Can I add more buttons?**
A: The integration comes with these 5 buttons. To add more, you'd need to modify the `binary_sensor.py` file.

## Need Help?

- Check `DOSE_TRACKING_GUIDE.md` for detailed documentation
- See `automations_dose_tracking.yaml` for automation examples
- Review `dashboard_simple.yaml` for more dashboard ideas
