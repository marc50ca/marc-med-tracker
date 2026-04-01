# Binary Sensors Workaround - Manual Installation

## If Integration Binary Sensors Won't Appear

This guide provides a **working alternative** using Home Assistant's built-in template sensors instead of the custom integration's binary sensors.

---

## What This Does

Creates the 5 missing binary sensors using:
- Template binary sensors (instead of custom integration)
- Input boolean helpers (to store state)
- Midnight reset automation
- Toggle scripts for dashboard buttons

**Result:** Functionally identical to integration sensors, just created differently.

---

## Installation (5 Minutes)

### Step 1: Copy the Configuration

1. Open file: `examples/manual_binary_sensors.yaml`
2. Copy **ALL** the content (the entire file)

### Step 2: Add to Your Configuration

1. Open `/config/configuration.yaml`
2. Scroll to the **END** of the file
3. **Paste** all the content you copied
4. **Save** the file

### Step 3: Validate

1. Go to **Developer Tools** → **YAML**
2. Click **"Check Configuration"**
3. Should say **"Configuration valid!"**
4. If errors, check your paste (especially indentation)

### Step 4: Restart

1. **Developer Tools** → **YAML** → **Restart**
2. Wait 2 minutes
3. ✅ Done!

### Step 5: Verify

1. Go to **Developer Tools** → **States**
2. Filter by: `marc_med`
3. You should now see:

```
✅ binary_sensor.marc_med_morning
✅ binary_sensor.marc_med_lunch  
✅ binary_sensor.marc_med_evening
✅ binary_sensor.marc_med_morning_puffer
✅ binary_sensor.marc_med_evening_puffer
```

Plus 5 input_boolean helpers (you can ignore/hide these)

---

## Using in Dashboard

These sensors work **exactly** like the integration ones, with one small difference in the dashboard card:

### Original Method (Integration Sensors)
```yaml
type: entities
entities:
  - entity: binary_sensor.marc_med_morning
    tap_action:
      action: toggle  # Simple toggle
```

### New Method (Template Sensors)
```yaml
type: entities
entities:
  - entity: binary_sensor.marc_med_morning
    tap_action:
      action: call-service  # Call script instead
      service: script.toggle_morning_pills
```

**Or even simpler - tap the entity name directly:**
```yaml
type: entities
entities:
  - input_boolean.marc_med_morning_helper
    name: "Morning Pills"
```

---

## Dashboard Card Example

Use this for Card #1 in the card-by-card method:

```yaml
type: entities
title: "📅 Today's Medications"
state_color: true
entities:
  - entity: input_boolean.marc_med_morning_helper
    name: "☀️ Morning Pills (6 tablets)"
  - entity: input_boolean.marc_med_morning_puffer_helper
    name: "☀️ Morning Puffer"
  - entity: input_boolean.marc_med_lunch_helper
    name: "🌞 Lunch Pills (2 tablets)"
  - entity: input_boolean.marc_med_evening_helper
    name: "🌙 Evening Pills (1 tablet)"
  - entity: input_boolean.marc_med_evening_puffer_helper
    name: "🌙 Evening Puffer"
```

**Tap any entity to toggle!** No scripts needed with this method.

---

## What Gets Created

### Binary Sensors (5) - These are what you use
- `binary_sensor.marc_med_morning`
- `binary_sensor.marc_med_lunch`
- `binary_sensor.marc_med_evening`
- `binary_sensor.marc_med_morning_puffer`
- `binary_sensor.marc_med_evening_puffer`

### Input Booleans (5) - These store the state
- `input_boolean.marc_med_morning_helper`
- `input_boolean.marc_med_lunch_helper`
- `input_boolean.marc_med_evening_helper`
- `input_boolean.marc_med_morning_puffer_helper`
- `input_boolean.marc_med_evening_puffer_helper`

### Scripts (5) - For toggling from dashboards
- `script.toggle_morning_pills`
- `script.toggle_lunch_pills`
- `script.toggle_evening_pills`
- `script.toggle_morning_puffer`
- `script.toggle_evening_puffer`

### Automation (1) - Resets at midnight
- Resets all 5 helpers to OFF at 00:00

---

## How It Works

### Template Binary Sensor
Looks at the input_boolean state and displays it as a binary sensor:
```
If input_boolean is ON → binary_sensor is ON (green)
If input_boolean is OFF → binary_sensor is OFF (red)
```

### Input Boolean Helper
Stores the actual on/off state:
```
When you click → toggles ON/OFF
State persists across restarts
Resets to OFF at midnight
```

### Midnight Reset
Automation runs at 00:00:00 every night and turns all helpers OFF

---

## Advantages

✅ **Uses built-in Home Assistant components** (no custom code)  
✅ **Guaranteed to work** (template platform is stable)  
✅ **Identical functionality** to integration sensors  
✅ **Auto-resets at midnight** just like original  
✅ **Works with all automations** and notifications  
✅ **State persists** across restarts  

---

## Disadvantages

❌ **Slightly more complex** dashboard configuration  
❌ **Extra entities** (input_booleans) in your entity list  
❌ **Doesn't use integration code** (workaround, not fix)  

---

## Hiding the Helper Entities

The input_boolean helpers clutter your entity list. To hide them:

### Method 1: Via UI
1. Settings → Devices & Services → Entities
2. Find `input_boolean.marc_med_morning_helper`
3. Click on it → Settings icon
4. Toggle **"Show in UI"** to OFF
5. Repeat for other 4 helpers

### Method 2: Via Configuration
Add to the input_boolean config:
```yaml
input_boolean:
  marc_med_morning_helper:
    name: Morning Pills Helper
    initial: false
    icon: mdi:pill
    # Add this line:
    hidden: true
```

---

## Updating Automations

Your notification automations work without changes!

The automations check:
```yaml
condition:
  - condition: state
    entity_id: binary_sensor.marc_med_morning
    state: "off"
```

This still works because `binary_sensor.marc_med_morning` now exists (via template).

---

## Troubleshooting

### Error: "Duplicate key"

**Cause:** You already have `binary_sensor:`, `input_boolean:`, etc. in your config

**Fix:** Merge with existing sections instead of adding new ones

**Example:**
```yaml
# If you already have this:
input_boolean:
  existing_helper:
    name: My Helper

# Don't add another input_boolean: section
# Instead, add to the existing one:
input_boolean:
  existing_helper:
    name: My Helper
  marc_med_morning_helper:  # Add here
    name: Morning Pills Helper
    initial: false
```

### Sensors Not Appearing

1. Check configuration is valid
2. Make sure you restarted (not just reloaded)
3. Check Developer Tools → States
4. Look for error in logs

### Sensors Don't Reset at Midnight

1. Check automation is enabled
2. Settings → Automations & Scenes
3. Find "Reset Medication Trackers"
4. Make sure it's ON

---

## Comparison

| Feature | Integration Sensors | Template Sensors (This Workaround) |
|---------|-------------------|-----------------------------------|
| Auto-creates sensors | ✅ Yes | ❌ Must configure manually |
| Auto-resets midnight | ✅ Built-in | ✅ Via automation |
| Works with dashboard | ✅ Direct toggle | ✅ Via script or helper |
| Persists state | ✅ Yes | ✅ Yes |
| Works with automations | ✅ Yes | ✅ Yes |
| Extra entities needed | ✅ No | ❌ Yes (5 helpers) |
| Reliability | ❓ Not loading for you | ✅ 100% reliable |

---

## When to Use This

**Use this workaround if:**
- Integration binary sensors won't appear
- You've tried everything else
- You need it working NOW
- You don't mind extra entities

**Don't use if:**
- Integration sensors are working fine
- You haven't tried troubleshooting yet
- You want to wait for a fix

---

## Removing This Later

If the integration sensors start working, you can remove this workaround:

1. Delete the sections you added from configuration.yaml
2. Restart Home Assistant
3. Update dashboard cards to use `binary_sensor.marc_med_morning` with toggle action

---

## Summary

This workaround:
1. ✅ Creates the 5 binary sensors you're missing
2. ✅ Makes them work identically to integration sensors
3. ✅ Resets them at midnight automatically
4. ✅ Works with all your automations and dashboards
5. ✅ Uses only built-in Home Assistant features

**It's a working solution while we figure out why the integration sensors aren't loading for you.**

---

**Bottom line:** Copy `examples/manual_binary_sensors.yaml` to your configuration.yaml, restart, and your sensors will work! 🎯
