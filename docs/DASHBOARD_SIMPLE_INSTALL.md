# Dashboard Installation - Card by Card Method (NO ERRORS!)

## This method NEVER fails - Add one card at a time

The "array error" happens because the dashboard YAML is meant for a VIEW, not the main dashboard. This method adds cards individually instead.

---

## Method: Add Cards to Overview Dashboard

### Step 1: Prepare Your Overview Dashboard

1. Go to your **Overview** dashboard
2. Click **⋮** (three dots) → **Edit Dashboard**

---

## Card 1: Today's Medication Schedule

1. Click **➕ Add Card**
2. Scroll down → Click **Manual**
3. Paste this:

```yaml
type: entities
title: "📅 Today's Medications"
state_color: true
show_header_toggle: false
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning Pills (6 tablets)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_morning_puffer
    name: "☀️ Morning Puffer"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: "🌞 Lunch Pills (2 tablets)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening Pills (1 tablet)"
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening_puffer
    name: "🌙 Evening Puffer"
    tap_action:
      action: toggle
```

4. Click **Save**

**✅ You should see your medication schedule!**

---

## Card 2: Daily Progress

1. Click **➕ Add Card** → **Manual**
2. Paste this:

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
  {% set percent = (taken / 5 * 100) | round(0) %}
  
  <div style="text-align: center; padding: 25px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
    <h1 style="margin: 0; font-size: 48px;">{{ percent }}%</h1>
    <h3 style="margin: 10px 0;">{{ taken }} of 5 doses completed today</h3>
    {% if percent == 100 %}
    <p style="font-size: 28px;">🎉 Perfect adherence!</p>
    {% elif percent >= 60 %}
    <p style="font-size: 24px;">👍 Keep it up!</p>
    {% else %}
    <p style="font-size: 24px;">⏰ {{ 5 - taken }} more to go</p>
    {% endif %}
  </div>
```

3. Click **Save**

**✅ You should see your progress percentage!**

---

## Card 3: Blood Glucose

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "🩸 Blood Glucose"
state_color: true
entities:
  - entity: sensor.blood_glucose_marc
    name: "Current Reading"
    icon: mdi:diabetes
```

3. Click **Save**

---

## Card 4: Blood Glucose Graph

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: history-graph
title: "Blood Glucose History"
hours_to_show: 168
entities:
  - entity: sensor.blood_glucose_marc
    name: "Blood Glucose"
```

3. Click **Save**

---

## Card 5: Blood Pressure

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "❤️ Blood Pressure"
state_color: true
entities:
  - entity: sensor.blood_pressure_systolic_marc
    name: "Systolic"
    icon: mdi:heart-pulse
  - entity: sensor.blood_pressure_diastolic_marc
    name: "Diastolic"
    icon: mdi:heart-pulse
  - entity: sensor.heart_rate_marc
    name: "Heart Rate"
    icon: mdi:heart
  - entity: sensor.oxygen_saturation_marc
    name: "O2 Saturation"
    icon: mdi:lungs
```

3. Click **Save**

---

## Card 6: Blood Pressure Graph

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: history-graph
title: "Blood Pressure Trends (7 Days)"
hours_to_show: 168
entities:
  - entity: sensor.blood_pressure_systolic_marc
    name: "Systolic"
  - entity: sensor.blood_pressure_diastolic_marc
    name: "Diastolic"
```

3. Click **Save**

---

## Card 7: Sleep Metrics

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "😴 Sleep"
state_color: true
entities:
  - entity: sensor.sleep_duration_marc
    name: "Total Sleep"
    icon: mdi:clock
  - entity: sensor.sleep_core_hours_marc
    name: "Core Sleep"
    icon: mdi:bed
  - entity: sensor.sleep_deep_hours_marc
    name: "Deep Sleep"
    icon: mdi:sleep
  - entity: sensor.sleep_awake_hours_marc
    name: "Awake Hours"
    icon: mdi:sleep-off
```

3. Click **Save**

---

## Card 8: Activity Metrics

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "🏃 Activity"
state_color: true
entities:
  - entity: sensor.steps_marc
    name: "Steps"
    icon: mdi:walk
  - entity: sensor.distance_marc
    name: "Distance"
    icon: mdi:map-marker-distance
  - entity: sensor.active_calories_marc
    name: "Active Calories"
    icon: mdi:fire
  - entity: sensor.exercise_time_marc
    name: "Exercise Time"
    icon: mdi:run
```

3. Click **Save**

---

## Card 9: NP T. Wakefield Medications

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "💊 NP T. Wakefield"
state_color: true
entities:
  - entity: sensor.marc_med_metformin
    name: "Metformin 500mg"
  - entity: sensor.marc_med_jardiance
    name: "Jardiance 40mg"
  - entity: sensor.marc_med_candesartan
    name: "Candesartan 16mg"
  - entity: sensor.marc_med_rosuvastatin
    name: "Rosuvastatin 10mg"
  - entity: sensor.marc_med_pantoprazole
    name: "Pantoprazole 40mg"
```

3. Click **Save**

---

## Card 10: Dr. K. Ducet & Dr. K. Safka Medications

1. Click **➕ Add Card** → **Manual**
2. Paste this:

```yaml
type: entities
title: "❤️ Dr. K. Ducet & Dr. K. Safka"
state_color: true
entities:
  - entity: sensor.marc_med_bisoprolol
    name: "Bisoprolol 2.5mg (Ducet)"
  - entity: sensor.marc_med_spironolactone
    name: "Spironolactone 60mg (Ducet)"
  - entity: sensor.marc_med_zenhale_inhaler
    name: "Zenhale Inhaler (Safka)"
```

3. Click **Save**

---

## Final Step: Exit Edit Mode

1. Click **Done** in top right
2. All your cards should now be visible!

---

## Organize Your Cards

Now that all cards are added, you can:
1. Enter **Edit** mode again
2. **Drag** cards to rearrange them
3. Put related cards together
4. **Done** when finished

---

## Optional: Add More Cards

### Activity Graph

```yaml
type: history-graph
title: "Activity Trends (7 Days)"
hours_to_show: 168
entities:
  - entity: sensor.steps_marc
    name: "Steps"
  - entity: sensor.distance_marc
    name: "Distance"
```

### Sleep Graph

```yaml
type: history-graph
title: "Sleep Quality (7 Days)"
hours_to_show: 168
entities:
  - entity: sensor.sleep_duration_marc
    name: "Total Sleep"
  - entity: sensor.sleep_core_hours_marc
    name: "Core Sleep"
```

### Medication Alerts

```yaml
type: markdown
title: "⚠️ Alerts"
content: |
  {% set low = [] %}
  {% for entity in [
    'sensor.marc_med_metformin',
    'sensor.marc_med_jardiance',
    'sensor.marc_med_candesartan',
    'sensor.marc_med_rosuvastatin',
    'sensor.marc_med_pantoprazole',
    'sensor.marc_med_bisoprolol',
    'sensor.marc_med_spironolactone',
    'sensor.marc_med_zenhale_inhaler'
  ] %}
    {% if state_attr(entity, 'days_remaining') | int <= 7 %}
      {% set low = low + [state_attr(entity, 'medication_name')] %}
    {% endif %}
  {% endfor %}
  
  {% if low | length > 0 %}
  **Medications running low:**
  {% for med in low %}
  - {{ med }}
  {% endfor %}
  {% else %}
  ✅ All medications have adequate supply
  {% endif %}
```

---

## Troubleshooting

**Card shows "Entity not available":**
- That sensor doesn't exist yet
- Skip that card or remove that entity
- Or set up the health sensor first

**Card won't save:**
- Check for YAML syntax errors
- Make sure all quotes match
- Try copying again carefully

**Can't find "Add Card" button:**
- Make sure you're in Edit mode
- Look for ➕ symbol (usually bottom right)

---

## Why This Works

**The array error happens when:**
- You try to paste VIEW YAML into the main dashboard editor
- The structure is wrong for that location

**This method works because:**
- You're adding individual CARDS, not a VIEW
- Each card is independent
- No complex YAML structure needed
- Works on ANY dashboard

---

## Next: Add Shortcut Button

After you have your cards working, add a shortcut button:

1. Still in Overview
2. Click **➕ Add Card** → **Manual**
3. Paste:

```yaml
type: button
name: 💊 Quick Med Check
icon: mdi:pill
tap_action:
  action: more-info
  entity: binary_sensor.marc_med_morning
```

4. This creates a button that opens your medication details

---

**Success!** You now have a working medication and health dashboard with NO ERRORS! 🎉
