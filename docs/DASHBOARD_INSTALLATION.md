# Dashboard Installation Guide - Step by Step

## Version 2.1.0

This guide walks you through installing the complete Medication & Health dashboard with NO ERRORS.

---

## Prerequisites

✅ Marc Med Tracker integration installed  
✅ Configuration added to `configuration.yaml`  
✅ Home Assistant restarted  
✅ Entities verified in Developer Tools → States

---

## Part 1: Install the Main Dashboard (10 minutes)

### Step 1: Open Your Dashboard

1. Go to your **main Home Assistant dashboard** (usually "Overview")

### Step 2: Enter Edit Mode

1. Click the **⋮** (three dots) in the **top right corner**
2. Click **"Edit Dashboard"**

### Step 3: Create New View

1. At the **very top** of the screen, you'll see tabs (Overview, Map, etc.)
2. Click the **➕ Add View** tab (far right)
3. A dialog will appear

### Step 4: Configure the New View

Fill in these fields:

- **Title**: `Medication & Health`
- **Icon**: Click icon selector → search for `pill` → select `mdi:pill`
- **Path**: `medication-health-hub`
- **Theme**: Leave as default
- **Type**: Leave as default

Click **"Save"**

### Step 5: Click Into Your New Tab

1. You should now see a new tab called "Medication & Health"
2. **Click on this tab** to open it
3. It will be empty - that's correct!

### Step 6: Open Raw Configuration Editor

1. While in the **Medication & Health** tab, click **⋮** (three dots)
2. Click **"Raw configuration editor"**
3. A code editor will appear

### Step 7: DELETE EVERYTHING ⚠️ IMPORTANT

The editor will show something like this:
```yaml
title: Medication & Health
path: medication-health-hub
icon: mdi:pill
cards: []
```

**SELECT ALL OF THIS TEXT AND DELETE IT**

The editor should now be **completely empty** - blank white space.

### Step 8: Copy the Dashboard Code

1. Open the file: `examples/complete_dashboard.yaml`
2. Select **ALL** the text (Ctrl+A or Cmd+A)
3. Copy it (Ctrl+C or Cmd+C)

**Note:** This file is over 600 lines - make sure you get ALL of it!

### Step 9: Paste into the Editor

1. Click in the **empty** Raw Configuration Editor
2. Paste (Ctrl+V or Cmd+V)
3. The first line should be: `title: 💊 Medication & Health Dashboard`
4. Scroll down - you should see LOTS of cards and sections

### Step 10: Save

1. Click **"Save"** in the top right
2. Click **"Done"** to exit edit mode

### Step 11: Verify It Worked

You should now see your dashboard with sections:
- 📅 Today's Medication Schedule
- 🩸 Blood Sugar Tracking
- ❤️ Cardio-Vascular Metrics
- 😴 Sleep Metrics
- 🏃 Activity Metrics
- 📦 Medication Inventory

**✅ Dashboard installed!**

---

## Part 2: Add Shortcut Button to Main Dashboard (2 minutes)

This creates a big purple button on your Overview page that opens your new dashboard.

### Step 1: Go to Overview

1. Click on the **"Overview"** tab (your main dashboard)

### Step 2: Enter Edit Mode

1. Click **⋮** → **"Edit Dashboard"**

### Step 3: Add Card

1. Click **"➕ Add Card"** (bottom right)
2. Scroll to the bottom
3. Click **"Manual"**

### Step 4: Paste Button Code

1. Open file: `examples/shortcut_button.yaml`
2. Copy **ALL** the code
3. Paste into the card editor
4. Click **"Save"**

### Step 5: Position the Button

1. While still in edit mode, **drag** the card to where you want it
   - Top of page = easy access
   - With other navigation cards = organized
2. Click **"Done"** when finished

### Step 6: Test the Button

1. Click the purple **💊 Medications & Health** button
2. It should navigate to your Medication & Health dashboard

**✅ Shortcut button installed!**

---

## Common Errors & Fixes

### Error: "Expected an array value, but received: undefined"

**Cause:** You didn't delete the existing YAML before pasting.

**Fix:**
1. Go to the Medication & Health tab
2. Click ⋮ → Raw configuration editor
3. **DELETE EVERYTHING** (should be blank)
4. Then paste the dashboard code
5. Save

### Error: "Entity not available" or sensors show "Unknown"

**For Medication Sensors:**

**Cause:** Integration not installed or configuration not added.

**Fix:**
1. Check `configuration.yaml` has the medications
2. Restart Home Assistant
3. Check Developer Tools → States for `sensor.marc_med_`

**For Health Sensors:**

**Cause:** Health sensors not set up yet.

**Fix:**
- These are optional - dashboard will work without them
- Set up Apple Health integration for iPhone sensors
- Or comment out sections you don't have sensors for

### Error: Shortcut button doesn't navigate

**Cause:** Wrong path in button.

**Fix:**
Check the button code has:
```yaml
navigation_path: /lovelace/medication-health-hub
```

If your dashboard path is different, change `medication-health-hub` to match.

### Error: Button has no styling (plain white)

**Cause:** card-mod not installed.

**Fix:**
- Install card-mod via HACS (optional)
- Or use this simpler button code:

```yaml
type: button
name: 💊 Medications & Health
icon: mdi:pill
tap_action:
  action: navigate
  navigation_path: /lovelace/medication-health-hub
```

---

## Customizing Your Dashboard

### Change the Tab Icon

1. Edit Dashboard → Click the tab
2. Click ⋮ → Edit view
3. Click the icon → search for a different one
4. Save

### Reorder Sections

1. Edit Dashboard
2. Drag cards up/down to reorder
3. Done when satisfied

### Remove Sections You Don't Need

**Example: Remove Blood Sugar section if you don't track it**

1. Edit Dashboard → Raw configuration editor
2. Find the section (search for `## 🩸 Blood Sugar`)
3. Delete from that line until the next `##` section header
4. Save

### Change Button Color

In the shortcut button, change:
```yaml
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Try these:
- Green: `#56ab2f 0%, #a8e063 100%`
- Blue: `#4A90E2 0%, #357ABD 100%`
- Red: `#FF6B6B 0%, #C44569 100%`

---

## Testing Each Section

### Medications
- [ ] Tap morning button → turns green
- [ ] Progress shows percentage
- [ ] Inventory shows pill counts

### Blood Sugar
- [ ] Current reading shows (if sensor exists)
- [ ] Graph displays history
- [ ] Stats card shows test count

### Cardio-Vascular
- [ ] Gauges show BP and heart rate
- [ ] Graphs show 7-day trends
- [ ] O2 saturation displays

### Sleep
- [ ] Sleep hours show from last night
- [ ] Graph shows weekly pattern

### Activity
- [ ] Steps show today's count
- [ ] Graphs show trends
- [ ] All metrics display

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Dashboard blank | Check you copied ALL 600+ lines |
| "Array" error | DELETE everything first, then paste |
| Sensors unavailable | Set up health sensors or remove those sections |
| Button doesn't work | Check navigation_path matches your view path |
| No styling on button | Install card-mod or use simple button code |

---

## File Locations

- **Dashboard code**: `examples/complete_dashboard.yaml`
- **Shortcut button**: `examples/shortcut_button.yaml`
- **Configuration**: `examples/configuration.yaml.example`
- **Automations**: `examples/automations_with_notifications.yaml`

---

## Dashboard Structure

```
💊 Medication & Health Dashboard
│
├── 📅 Today's Medication Schedule (3 cards)
├── 📊 Daily Progress (1 card)
├── 🩸 Blood Sugar (3 cards)
│   ├── Current reading
│   ├── 7-day graph
│   └── Stats with A1C calculator
├── ❤️ Cardio-Vascular (5 cards)
│   ├── BP gauges
│   ├── Heart rate gauges
│   ├── Details
│   └── 7-day graphs
├── 😴 Sleep (3 cards)
│   ├── Duration cards
│   ├── Details
│   └── 7-day graph
├── 🏃 Activity (5 cards)
│   ├── Steps/distance cards
│   ├── Exercise cards
│   ├── Details
│   └── 7-day graphs
└── 📦 Medication Inventory (3 cards)
    ├── NP T. Wakefield meds
    ├── Dr. K. Ducet meds
    └── Active alerts
```

**Total: 29 cards across 6 major sections**

---

## Video Tutorial Steps

If you prefer visual instructions:

1. **Dashboard** tab
2. **⋮** → **Edit Dashboard**
3. **➕ Add View**
4. Fill in: Title, Icon, Path
5. **Save**
6. **Click new tab**
7. **⋮** → **Raw configuration editor**
8. **DELETE EVERYTHING**
9. **Paste dashboard code**
10. **Save** → **Done**

For shortcut button:
1. **Overview** tab
2. **Edit Dashboard**
3. **➕ Add Card** → **Manual**
4. **Paste button code**
5. **Save** → **Done**

---

## Success Checklist

- [ ] Dashboard view created
- [ ] Dashboard code pasted (600+ lines)
- [ ] No YAML errors
- [ ] All sections visible
- [ ] Shortcut button on Overview
- [ ] Button navigates to dashboard
- [ ] Medication sensors working
- [ ] Health sensors configured (optional)

---

## Need Help?

**Dashboard not showing:**
- Make sure you clicked into the new tab
- Check you're in Raw Configuration Editor
- Verify you deleted old YAML first

**Still having issues:**
- See `docs/TROUBLESHOOTING.md`
- Check YAML syntax at yamllint.com
- Verify file was fully copied

---

## Version Information

- **Dashboard Version**: 2.1.0
- **Integration Version**: 2.1.0
- **Last Updated**: March 2026
- **Compatible with**: Home Assistant 2024.1+

---

**Your medication and health dashboard is ready!** 💊📊❤️

**Next Steps:**
1. ✅ Dashboard installed
2. 📱 Set up notifications (see `docs/NOTIFICATION_SETUP.md`)
3. 🎨 Customize colors and layout (optional)
4. 📊 Add more health sensors (optional)
