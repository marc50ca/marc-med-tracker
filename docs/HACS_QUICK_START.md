# HACS Quick Start Guide

## Installing Marc Med Tracker via HACS

### Step 1: Install via HACS (2 minutes)

1. **Open HACS**
   - In Home Assistant, click on "HACS" in the sidebar

2. **Find Integration**
   - Click "Integrations"
   - Click "+ Explore & Download Repositories"
   - Search for "Marc Med Tracker"

3. **Download**
   - Click on "Marc Med Tracker"
   - Click "Download"
   - Click "Download" again to confirm
   - Wait for download to complete

### Step 2: Configure (3 minutes)

1. **Edit configuration.yaml**
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

2. **Restart Home Assistant**
   - Settings → System → Restart
   - Wait for restart to complete

3. **Verify Installation**
   - Developer Tools → States
   - Search for: `marc_med_`
   - You should see:
     - `sensor.marc_med_aspirin`
     - `binary_sensor.marc_med_morning`
     - And 4 more binary sensors

### Step 3: Add Dashboard (2 minutes)

1. **Go to a Dashboard**
2. **Edit Dashboard** (three dots menu)
3. **Add Card** → **Manual**
4. **Copy/Paste** this YAML:

```yaml
type: entities
title: "Today's Medications"
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
  - entity: sensor.marc_med_aspirin
    name: "💊 Aspirin Stock"
```

5. **Save**

### Step 4: Start Tracking! 🎉

**Mark doses as taken:**
- Tap the red buttons
- They turn green! ✅
- Auto-reset at midnight

**Check inventory:**
- See pills remaining
- Days until refill
- Status: OK, LOW, CRITICAL

## What's Next?

### Use Beautiful Dashboards

1. **Find examples** in HACS:
   - HACS → Integrations → Marc Med Tracker
   - Click "Information"
   - Scroll to "Examples"

2. **Copy a dashboard:**
   - `dashboard_beautiful_simple.yaml` - Recommended
   - Beautiful, modern, no custom cards needed

3. **Apply the theme** (optional):
   - Copy `marc_med_tracker_theme.yaml` to `/config/themes/`
   - Add to configuration.yaml:
     ```yaml
     frontend:
       themes: !include_dir_merge_named themes
     ```
   - Restart HA
   - Select theme in Profile

### Add More Medications

In `configuration.yaml`:

```yaml
marc_med_tracker:
  medications:
    - name: "Aspirin"
      # ... existing config
    
    - name: "Vitamin D"  # Add another!
      prescribing_doctor: "Dr. Johnson"
      refills_left: 5
      last_refilled: "2025-02-15"
      strength: "2000 IU"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 100
```

Restart Home Assistant after each change.

### Set Up Automations

Create reminders:

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
      - service: notify.mobile_app
        data:
          message: "Time to take your morning medications!"
```

## Updating via HACS

HACS will notify you when updates are available:

1. **Notification** appears in HACS
2. **Click** on Marc Med Tracker
3. **Click "Update"**
4. **Restart** Home Assistant
5. **Done!** All your data is preserved

## Troubleshooting

### Integration Not Loading

1. **Check logs:**
   - Settings → System → Logs
   - Filter: `marc_med_tracker`

2. **Verify files:**
   - HACS → Integrations → Marc Med Tracker → "…" menu → Reinstall

3. **Restart twice:**
   - Sometimes needs two restarts after installation

### Entities Not Appearing

1. **Check configuration:**
   - Ensure `marc_med_tracker:` is in configuration.yaml
   - Check YAML syntax (no tabs, proper indentation)

2. **Validate config:**
   - Developer Tools → YAML → Check Configuration

3. **View entities:**
   - Developer Tools → States
   - Search: `marc_med_`

### HACS Not Finding Integration

**If in HACS Default:**
- Update HACS
- Clear HACS cache
- Restart Home Assistant

**If custom repository:**
1. HACS → Integrations → ⋮ → Custom repositories
2. Add: `https://github.com/yourusername/marc-med-tracker`
3. Category: Integration
4. Click Add

## Getting Help

1. **Documentation**: Check the full docs in GitHub
2. **Examples**: Browse the examples folder
3. **Troubleshooting Guide**: See TROUBLESHOOTING.md
4. **Issues**: Report bugs on GitHub

## Quick Command Reference

```bash
# Check if integration loaded
ha core logs | grep marc_med_tracker

# List all entities
ha states | grep marc_med_

# Restart Home Assistant  
ha core restart
```

## Key Features Summary

✅ **7 Services** for complete control
✅ **Daily tracking** with red/green buttons
✅ **Automatic inventory** calculation
✅ **Smart alerts** for low stock
✅ **Refill reminders** based on schedule
✅ **Beautiful dashboards** included
✅ **Complete automation** support

---

**Installation Time**: ~7 minutes total
**Difficulty**: Easy
**Requirements**: HACS + Home Assistant 2024.1+

🎉 **You're all set! Happy tracking!**
