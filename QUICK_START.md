# Quick Start Guide - Your Medication Tracker

## Your Medications

You're tracking **8 medications**:

**NP T. Wakefield (Refilled March 25, 2026):**
- Metformin 500mg (2 tablets, twice daily)
- Jardiance 40mg (1 tablet, evening)
- Candesartan 16mg (1 tablet, morning)
- Rosuvastatin 10mg (1 tablet, morning)
- Pantoprazole 40mg (1 tablet, morning)

**Dr. K. Ducet (Refilled February 1, 2026):**
- Bisoprolol 2.5mg (1 tablet, morning)
- Spironolactone 60mg (0.5 tablet/HALF, morning)
- Zenhale Inhaler (1-2 puffs, twice daily)

**Daily Total:** 9 tablets + 2-4 puffs

---

## Installation (10 minutes)

### Step 1: Install via HACS

1. Open **HACS** → **Integrations**
2. Click **⋮** → **Custom repositories**
3. Repository: `marc50ca/marc-med-tracker`
4. Category: **Integration**
5. Click **Add**
6. Search "Marc Med Tracker" → **Download**
7. **Restart Home Assistant**

### Step 2: Add Configuration

1. Open `/config/configuration.yaml`
2. Copy the ENTIRE contents from `examples/configuration.yaml.example`
3. Paste at the end of your configuration.yaml
4. **Save the file**
5. **Restart Home Assistant** again

### Step 3: Verify Installation

1. Go to **Developer Tools** → **States**
2. Search for: `marc_med_`
3. You should see **13 entities**:
   - 8 medication sensors (metformin, jardiance, etc.)
   - 5 daily tracking buttons (morning, lunch, evening, puffers)

✅ All there? Continue to dashboard setup!

---

## Dashboard Setup (5 minutes)

### Option A: Copy Complete Dashboard (Recommended)

1. Go to your main dashboard
2. Click **⋮** (three dots) → **Edit Dashboard**
3. Click **➕ Add View** (new tab at top)
4. Configure:
   - **Title**: Medications
   - **Icon**: mdi:pill
   - **URL**: medications
5. Click **Save**
6. Click into the new "Medications" tab
7. Click **⋮** → **Raw Configuration Editor**
8. **Delete everything** in the editor
9. Open file: `examples/complete_dashboard.yaml`
10. **Copy ALL the contents**
11. **Paste into the editor**
12. Click **Save**

**Done!** You now have a complete medication dashboard.

### Option B: Quick Simple Card (2 minutes)

If you just want something basic right now:

1. Go to dashboard → **Edit**
2. Click **➕ Add Card**
3. Scroll down → **Manual**
4. Paste this:

```yaml
type: entities
title: "💊 Today's Medications"
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning (6 pills + puffer)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: "🌞 Lunch (2 pills - Metformin)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening (1 pill + puffer)"
    tap_action:
      action: toggle
```

5. Click **Save**

---

## Using Your Dashboard

### Every Day

**Morning:**
1. Take your 6 pills + puffer
2. Tap ☀️ **Morning** button → turns GREEN ✅

**Lunch:**
1. Take 2 Metformin tablets
2. Tap 🌞 **Lunch** button → turns GREEN ✅

**Evening:**
1. Take Jardiance + puffer
2. Tap 🌙 **Evening** button → turns GREEN ✅

### Weekly

Check the **⚠️ Medication Alerts** section:
- 🟢 Green = All good (>7 days left)
- 🟡 Yellow = Order refill soon (≤7 days)
- 🟠 Orange = Order NOW (≤3 days)
- 🔴 Red = OUT OF STOCK - call doctor!

---

## Dashboard Features

### Today's Schedule
Shows your 5 dose times with red/green buttons:
- Red = Not taken yet
- Green = Taken today
- Auto-resets at midnight

### Daily Progress
Shows % complete with motivating messages:
- 100% = "Perfect adherence!"
- 60%+ = "Keep it up!"
- <60% = Shows how many more to go

### Medication Inventory
**Two cards organized by prescriber:**

**NP T. Wakefield Card:**
- Metformin
- Jardiance
- Candesartan
- Rosuvastatin
- Pantoprazole

**Dr. K. Ducet Card:**
- Bisoprolol
- Spironolactone
- Zenhale Inhaler

Each shows:
- Pills/puffs remaining
- Days until refill needed
- Status (OK/LOW/CRITICAL)
- Refills left
- Special instructions

### Active Alerts
Only shows when action needed:
- Running low medications
- Out of stock items
- No refills left

### Refill Schedule
Color-coded cards for next 30 days:
- Yellow background = ≤7 days
- Blue background = 8-14 days
- Green background = 15-30 days

Shows:
- Exact refill date (day & date)
- Days until refill
- Current stock
- Refills available
- Which doctor to call

### Quick Summary
4 colorful boxes showing:
- Total medications (8)
- Prescribers (2)
- Pills per day (9)
- Puffs per day (4)

### Important Reminders
Highlights:
- **Spironolactone**: Take HALF tablet
- **Metformin**: 2 tablets at a time
- **Zenhale**: Rinse mouth after use

---

## Troubleshooting

**"Entity not available"**
- Check configuration.yaml - copy EXACTLY from example
- Restart Home Assistant
- Check Developer Tools → States

**Dashboard shows errors**
- Make sure you copied the ENTIRE dashboard YAML
- Check for any cut-off lines
- Try Option B (simple card) first

**Wrong pill counts**
- Dates in configuration should be March 25, 2026 (NP Wakefield)
- Or February 1, 2026 (Dr. Ducet)
- These are when you got refills, not today's date

**Buttons don't toggle**
- Make sure entities exist (check Developer Tools)
- Try tapping directly on entity name
- Refresh browser page

---

## Important Notes

### Spironolactone Reminder
- Your dose is **HALF a 60mg tablet**
- Cut the tablet in half before taking
- Take only 0.5 tablet = 30mg

### Metformin Dosing
- Take **2 tablets** each time
- Twice daily (morning AND lunch)
- Total: 4 tablets per day

### Zenhale Inhaler
- **ALWAYS rinse mouth after each use**
- This prevents thrush (oral yeast infection)
- Spit out rinse water - don't swallow

---

## What's Next?

1. ✅ Integration installed
2. ✅ Dashboard created
3. 📱 Optional: Set up phone notifications
4. 📋 Optional: Print medication schedule (docs/MEDICATION_SCHEDULE.md)
5. 📊 Optional: Add history graphs

---

## Need Help?

- 📖 **Full Documentation**: See `docs/` folder
- 📅 **Medication Schedule**: `docs/MEDICATION_SCHEDULE.md`
- 🎨 **Complete Dashboard**: `examples/complete_dashboard.yaml`
- 🐛 **Issues**: GitHub Issues page

**Enjoy tracking your medications!** 💊✨
