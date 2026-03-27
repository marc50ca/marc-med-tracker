# Quick Start Guide - 15 Minutes to Full Setup

Get your medication tracker running in 15 minutes!

## Part 1: Install (5 minutes)

### Step 1: Install via HACS

1. Open **HACS** in Home Assistant
2. Click **Integrations**
3. Click **⋮** → **Custom repositories**
4. Add: `marc50ca/marc-med-tracker`
5. Category: **Integration**
6. Click **Add**
7. Search for "Marc Med Tracker"
8. Click **Download**
9. **Restart Home Assistant**

### Step 2: Add Configuration

1. Open `/config/configuration.yaml`
2. Add this at the end:

```yaml
marc_med_tracker:
  medications:
    - name: "Jardiance"
      prescribing_doctor: "Dr. Smith"
      refills_left: 3
      last_refilled: "2025-03-01"  # ← CHANGE THIS to your actual date
      strength: "10mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Metformin"
      prescribing_doctor: "Dr. Smith"
      refills_left: 5
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "500mg"
      doses_per_day: 2
      pills_per_dose: 1
      initial_stock: 180
    
    - name: "Pantoloc"
      prescribing_doctor: "Dr. Johnson"
      refills_left: 4
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "40mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Rosuvastatin"
      prescribing_doctor: "Dr. Smith"
      refills_left: 6
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "20mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Candesartan"
      prescribing_doctor: "Dr. Wilson"
      refills_left: 5
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "16mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Bisoprolol"
      prescribing_doctor: "Dr. Wilson"
      refills_left: 4
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "5mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Spironolactone"
      prescribing_doctor: "Dr. Wilson"
      refills_left: 3
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "25mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
    
    - name: "Edoxaban"
      prescribing_doctor: "Dr. Wilson"
      refills_left: 2
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "60mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
      notes: "CRITICAL: Take at same time daily"
    
    - name: "Zenhale Inhaler"
      prescribing_doctor: "Dr. Brown"
      refills_left: 2
      last_refilled: "2025-03-01"  # ← CHANGE THIS
      strength: "100/6 mcg"
      doses_per_day: 2
      pills_per_dose: 2
      initial_stock: 120
      notes: "2 puffs twice daily - rinse mouth after"
```

3. **Update the dates!** Change `last_refilled` to when you actually got each refill
4. Update doctor names if different
5. Save file
6. **Restart Home Assistant again**

### Step 3: Verify

1. Go to **Developer Tools** → **States**
2. Search: `marc_med_`
3. Should see **14 entities total:**
   - 9 medication sensors (jardiance, metformin, etc.)
   - 5 daily dose trackers (morning, lunch, evening, puffers)

✅ All there? Continue to Part 2!

---

## Part 2: Add Dashboard (10 minutes)

### Option A: Simple Dashboard (2 minutes)

1. Go to your dashboard
2. Click **⋮** → **Edit Dashboard**
3. Click **➕ Add Card**
4. Scroll down, click **Manual**
5. Paste this:

```yaml
type: entities
title: "💊 Today's Medications"
state_color: true
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning Pills (7 pills + puffer)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: "🌞 Lunch Pills (1 pill)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening Pills (1 pill + puffer)"
    tap_action:
      action: toggle
  - type: divider
  - entity: sensor.marc_med_edoxaban
    name: "🚨 Edoxaban (Blood Thinner)"
  - entity: sensor.marc_med_jardiance
    name: "Jardiance"
  - entity: sensor.marc_med_metformin
    name: "Metformin"
  - entity: sensor.marc_med_candesartan
    name: "Candesartan"
  - entity: sensor.marc_med_bisoprolol
    name: "Bisoprolol"
```

6. Click **Save**

**Done!** You have a basic working dashboard.

### Option B: Full Dashboard (10 minutes)

For the complete beautiful dashboard with all features, see:
📖 **docs/DASHBOARD_SETUP_COMPLETE.md**

It includes:
- Welcome header
- Progress percentage
- All 9 medications
- Smart alerts
- Refill schedule
- Medications by doctor

---

## Part 3: Use It! 🎉

### Every Morning

1. Open dashboard
2. Tap ☀️ **Morning Pills** → turns green ✅
3. That's it!

### Every Lunch

1. Tap 🌞 **Lunch Pills** → turns green ✅

### Every Evening

1. Tap 🌙 **Evening Pills** → turns green ✅

### Weekly

Check which medications are running low and need refills.

---

## What Do the Colors Mean?

**Red Button** 🔴 = Not taken yet today  
**Green Button** 🟢 = Taken today  

**Sensors:**
- **Green** = More than 7 days left
- **Yellow** = 7 days or less (get refill soon)
- **Orange** = 3 days or less (get refill NOW)
- **Red** = Out of stock (call doctor!)

---

## Troubleshooting

**"Entity not available"**
- Check configuration.yaml for typos
- Restart Home Assistant
- Check Developer Tools → States for sensors

**Buttons don't toggle**
- Make sure you're in edit mode
- Try clicking directly on the entity row
- Check if binary sensors exist

**Wrong pill counts**
- Update `last_refilled` dates in configuration
- Dates should be when you actually got the refill
- Restart Home Assistant after changes

---

## Next Steps

1. ✅ Integration installed
2. ✅ Dashboard created
3. 📱 Optional: Set up notifications (see docs/automations)
4. 🎨 Optional: Install custom theme
5. 📊 Optional: Add history graphs

---

## Need Help?

- 📚 Full documentation in `docs/` folder
- 🐛 Report issues on GitHub
- 💬 Ask in Home Assistant community

**Enjoy your medication tracker!** 💊🎉
