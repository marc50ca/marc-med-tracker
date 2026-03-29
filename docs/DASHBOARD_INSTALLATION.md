# Complete Dashboard Installation Guide

## Fix for "Expected an array value" Error

The error happens when you paste the dashboard YAML in the wrong place. Follow these exact steps:

---

## Method 1: Add as Dashboard View (RECOMMENDED)

This adds the dashboard as a new tab in your existing dashboard.

### Step-by-Step Instructions:

1. **Go to your main dashboard** (Overview)

2. **Enter Edit Mode**
   - Click **⋮** (three dots in top right)
   - Click **Edit Dashboard**

3. **Add New View**
   - Click **➕ Add View** (tab at the very top)
   
4. **Configure the View**
   - **Title**: `Medication & Health`
   - **Icon**: `mdi:pill`
   - **URL**: `medication-health-hub`
   - **Theme**: Leave as default
   - Click **Save**

5. **Click into the NEW tab** you just created

6. **Open Raw Configuration Editor**
   - Click **⋮** (three dots) in the view
   - Click **Raw Configuration Editor**

7. **IMPORTANT: Delete EVERYTHING in the editor**
   - You should see something like:
   ```yaml
   title: Medication & Health
   path: medication-health-hub
   icon: mdi:pill
   cards: []
   ```
   - **DELETE ALL OF IT**

8. **Copy the Complete Dashboard**
   - Open file: `examples/complete_dashboard.yaml`
   - Copy **EVERYTHING** from the file (all 600+ lines)

9. **Paste into the Empty Editor**
   - The editor should now be completely empty
   - Paste all the content you copied
   - The first line should be: `title: 💊 Medication & Health Dashboard`

10. **Save**
    - Click **Save** in top right
    - Exit edit mode

**Done!** Your dashboard should now load with all sections.

---

## Method 2: Standalone Dashboard

If you want a completely separate dashboard:

### Step-by-Step Instructions:

1. **Go to Settings** → **Dashboards**

2. **Add New Dashboard**
   - Click **➕ Add Dashboard**
   - Choose **New dashboard**
   - **Name**: `Medication & Health Tracker`
   - **Icon**: `mdi:pill`
   - **Show in sidebar**: ON
   - Click **Create**

3. **Open the New Dashboard**
   - It should appear in your sidebar
   - Click on it

4. **Open Raw Configuration**
   - Click **⋮** (three dots)
   - Click **Edit Dashboard**
   - Click **⋮** again
   - Click **Raw Configuration Editor**

5. **Replace All Content**
   - **DELETE EVERYTHING** in the editor
   - Copy ALL content from `examples/complete_dashboard.yaml`
   - Paste into the empty editor
   - Click **Save**

**Done!**

---

## What You'll See

### Section 1: Medication Tracking
✅ Today's schedule (morning, lunch, evening)
✅ Daily progress percentage
✅ Medication inventory by prescriber

### Section 2: Blood Sugar 🩸
✅ Current glucose reading
✅ Graph of glucose history (7 days)
✅ **Statistics card showing:**
- Total tests count (since April 30)
- Average glucose level
- **Estimated A1C** (when you have 21+ readings)
  - Formula: (Average + 2.9) / 1.59

### Section 3: Cardio-Vascular ❤️
✅ Blood Pressure gauges (Systolic & Diastolic)
✅ Heart Rate & O2 Saturation gauges
✅ Resting Heart Rate
✅ 7-day history graphs for:
- Blood pressure trends
- Heart rate trends

### Section 4: Sleep 😴
✅ Sleep duration, core, and deep sleep
✅ Awake hours tracking
✅ Flights climbed
✅ 7-day sleep quality graph

### Section 5: Activity 🏃
✅ Steps, distance, active calories
✅ Exercise time, stand time
✅ Walking speed, body mass
✅ 7-day activity graphs
✅ 7-day exercise metrics graphs

---

## Troubleshooting

### Error: "Expected an array value"

**Cause**: You pasted the dashboard in the wrong location.

**Fix**: You need to paste in **Raw Configuration Editor**, NOT in the regular view editor.

**Steps:**
1. Make sure you're in **Raw Configuration Editor** (shows YAML code)
2. **DELETE EVERYTHING** first
3. Then paste the dashboard YAML
4. Save

### Error: "Entity not found" or sensors show "unavailable"

**Cause**: Health sensors not configured in Home Assistant.

**Health Sensors Required:**
- `sensor.blood_glucose_marc`
- `sensor.blood_pressure_systolic_marc`
- `sensor.blood_pressure_diastolic_marc`
- `sensor.heart_rate_marc`
- `sensor.resting_heart_rate_marc`
- `sensor.oxygen_saturation_marc`
- `sensor.sleep_duration_marc`
- `sensor.sleep_core_hours_marc`
- `sensor.sleep_deep_hours_marc`
- `sensor.sleep_awake_hours_marc`
- `sensor.flights_climbed_marc`
- `sensor.steps_marc`
- `sensor.distance_marc`
- `sensor.active_calories_marc`
- `sensor.exercise_time_marc`
- `sensor.stand_time_marc`
- `sensor.walking_speed_marc`
- `sensor.body_mass_marc`

**Fix Options:**

**Option 1:** Set up these sensors
- Use Home Assistant's Apple Health integration
- Or manually create sensors from your health data source

**Option 2:** Remove sections you don't have sensors for
- Comment out or delete the Blood Sugar section if you don't have that sensor
- Comment out or delete Sleep section if you don't have those sensors
- etc.

**Option 3:** Create dummy sensors (for testing)
```yaml
# Add to configuration.yaml
template:
  - sensor:
      - name: "Blood Glucose Marc"
        state: 100
        unit_of_measurement: "mg/dL"
```

### Error: "Custom element doesn't exist: custom:mini-graph-card"

**Cause**: mini-graph-card not installed.

**Fix:**
1. Install via HACS: Search "mini-graph-card"
2. Or change the card type to `history-graph` instead

**Replace this:**
```yaml
type: custom:mini-graph-card
```

**With this:**
```yaml
type: history-graph
hours_to_show: 168
```

### Blood Sugar A1C not calculating

**Requirements:**
- Must have **21 or more** blood glucose readings
- Readings must be after **April 30, 2026**
- Sensor must have history data

**Check:**
1. Go to **Developer Tools** → **States**
2. Find `sensor.blood_glucose_marc`
3. Check if it has historical data

**If not showing:**
The history tracking may need time to accumulate readings. The A1C calculation will appear automatically once you have 21+ readings.

### Gauges not showing colors

**This is normal** - gauges may take time to load initial data.

**Wait for:**
- Health data to sync
- Sensors to update
- Page to fully load

### Graphs showing "No data"

**Cause**: Sensors are new or don't have historical data yet.

**Fix**: Wait 24-48 hours for history to accumulate, or:
- Check if sensors are actually updating
- Verify sensor names are correct
- Check if recorder is enabled for these sensors

---

## Customizing the Dashboard

### Change Gauge Ranges

For blood pressure, heart rate, etc:

```yaml
- type: gauge
  entity: sensor.blood_pressure_systolic_marc
  min: 80        # Change minimum value
  max: 200       # Change maximum value
  severity:
    green: 90    # Green up to 90
    yellow: 120  # Yellow from 90-120
    red: 140     # Red above 140
```

### Change Graph Time Range

For any history graph:

```yaml
- type: history-graph
  hours_to_show: 168  # Change this (168 = 7 days)
  # 24 = 1 day
  # 72 = 3 days
  # 336 = 14 days
```

### Add More Health Metrics

Copy any section and change the entity:

```yaml
- type: sensor
  entity: sensor.YOUR_HEALTH_SENSOR_HERE
  name: Your Metric Name
  icon: mdi:icon-name
  graph: line
```

### Remove Sections You Don't Need

To remove Blood Sugar section:
1. Find the section (starts with `## 🩸 Blood Sugar Tracking`)
2. Delete from that line to the next `##` section header

To remove any section:
- Find the section header (## Section Name)
- Delete everything until the next ## header

---

## Testing the Dashboard

### Test Each Section:

1. **Medications**
   - Tap a dose button → should turn green
   - Progress should update

2. **Blood Sugar**
   - Check if current reading shows
   - Graph should show if data exists
   - A1C appears when 21+ readings

3. **Cardio-Vascular**
   - Gauges should show needle positions
   - Graphs should show historical data

4. **Sleep**
   - Numbers should show from last night
   - Graph shows weekly pattern

5. **Activity**
   - Today's stats should show
   - Graphs show daily trends

---

## Quick Reference

### Dashboard Structure

```
📱 Dashboard Title
├── 💊 Medication Schedule (3 cards)
├── 📊 Daily Progress (1 card)
├── 🩸 Blood Sugar (3 cards)
├── ❤️  Cardio-Vascular (5 cards)
├── 😴 Sleep (3 cards)
├── 🏃 Activity (5 cards)
└── 📦 Medication Inventory (3 cards)
```

### Total Cards: ~23 cards

---

## Need Help?

**Dashboard not loading at all:**
- Check for YAML syntax errors
- Make sure you're using Raw Configuration Editor
- Try Method 1 (Add as View) instead of Method 2

**Some cards work, others don't:**
- Missing sensors - see sensor list above
- Install missing custom cards
- Check entity names match exactly

**Want to simplify:**
- Remove sections you don't need
- Keep only medication tracking
- Add health sections gradually

---

**Your complete medication and health tracking dashboard is ready!** 💊📊❤️
