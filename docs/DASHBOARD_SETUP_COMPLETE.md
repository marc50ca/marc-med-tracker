# Complete Dashboard Setup Guide

This guide walks you through setting up a beautiful medication dashboard step-by-step.

## Overview

You'll create a dashboard that shows:
- ✅ Daily dose tracker (red/green buttons)
- 💊 All 9 medications with stock levels
- ⚠️ Smart alerts for low stock
- 📅 Upcoming refill schedule
- 👨‍⚕️ Medications grouped by doctor

## Prerequisites

- Marc Med Tracker integration installed via HACS
- Configuration added to `configuration.yaml`
- Home Assistant restarted

## Step 1: Verify Installation (2 minutes)

### Check Your Sensors Exist

1. Go to **Developer Tools** → **States**
2. Search for: `marc_med_`
3. You should see **9 medication sensors** and **5 daily tracking buttons**:

**Medication Sensors:**
- `sensor.marc_med_jardiance`
- `sensor.marc_med_metformin`
- `sensor.marc_med_pantoloc`
- `sensor.marc_med_rosuvastatin`
- `sensor.marc_med_candesartan`
- `sensor.marc_med_bisoprolol`
- `sensor.marc_med_spironolactone`
- `sensor.marc_med_edoxaban`
- `sensor.marc_med_zenhale_inhaler`

**Daily Dose Trackers:**
- `binary_sensor.marc_med_morning`
- `binary_sensor.marc_med_lunch`
- `binary_sensor.marc_med_evening`
- `binary_sensor.marc_med_morning_puffer`
- `binary_sensor.marc_med_evening_puffer`

✅ **All there?** Great! Continue to Step 2.  
❌ **Missing some?** Check your configuration.yaml and restart HA.

## Step 2: Create Dashboard (5 minutes)

### Method A: Add as New View (Recommended)

1. Go to your main dashboard (Overview)
2. Click **⋮** (three dots) → **Edit Dashboard**
3. Click **➕ Add View** (tab at top)
4. Configure the view:
   - **Title**: `Medications`
   - **Icon**: `mdi:pill`
   - **URL**: `medications`
5. Click **Save**
6. Click into the new **Medications** tab
7. Continue to Step 3

### Method B: Create Standalone Dashboard

1. Go to **Settings** → **Dashboards**
2. Click **➕ Add Dashboard**
3. Choose **New dashboard**
4. Name: `Medication Tracker`
5. Icon: `mdi:pill`
6. Click **Create**
7. Open the new dashboard
8. Continue to Step 3

## Step 3: Add Dashboard Cards (10 minutes)

Now you'll add cards one by one. For each card below:
1. Click **➕ Add Card** (or pencil icon if in edit mode)
2. Scroll to bottom and click **Manual**
3. Copy/paste the YAML
4. Click **Save**

### Card 1: Welcome Header

```yaml
type: markdown
content: |
  # 💊 Medication Management
  ### {{ now().strftime('%A, %B %d, %Y') }}
  
  Track your medications and never miss a dose
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 20px;
    }
```

**What it shows:** Beautiful header with current date

---

### Card 2: Today's Medication Schedule

```yaml
type: entities
title: "📅 Today's Schedule"
state_color: true
show_header_toggle: false
entities:
  - entity: binary_sensor.marc_med_morning
    name: "☀️ Morning Pills"
    secondary_info: last-changed
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_morning_puffer
    name: "💨 Morning Puffer (Zenhale)"
    secondary_info: last-changed
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_lunch
    name: "🌞 Lunch Pills"
    secondary_info: last-changed
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening
    name: "🌙 Evening Pills"
    secondary_info: last-changed
    tap_action:
      action: toggle
  - entity: binary_sensor.marc_med_evening_puffer
    name: "💨 Evening Puffer (Zenhale)"
    secondary_info: last-changed
    tap_action:
      action: toggle
```

**What it shows:** Red/green buttons for each dose time. Tap to mark as taken!

**Tips:**
- Red = Not taken yet
- Green = Taken today
- Auto-resets at midnight
- Shows when last marked

---

### Card 3: Daily Progress

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
    <h3 style="margin: 10px 0;">{{ taken }} of 5 doses taken today</h3>
    {% if percent == 100 %}
    <p style="margin: 15px 0; font-size: 28px;">🎉 Perfect adherence!</p>
    {% elif percent >= 60 %}
    <p style="margin: 15px 0; font-size: 24px;">👍 Keep going!</p>
    {% elif percent > 0 %}
    <p style="margin: 15px 0; font-size: 24px;">⏰ {{ 5 - taken }} more to go</p>
    {% else %}
    <p style="margin: 15px 0; font-size: 24px;">💊 Ready to start</p>
    {% endif %}
  </div>
```

**What it shows:** Big percentage showing daily completion with encouraging messages

---

### Card 4: Diabetes Medications

```yaml
type: entities
title: "💉 Diabetes Management"
state_color: true
show_header_toggle: false
entities:
  - entity: sensor.marc_med_jardiance
    name: "Jardiance 10mg"
    secondary_info: last-changed
  - type: attribute
    entity: sensor.marc_med_jardiance
    attribute: days_remaining
    name: "Days Remaining"
    suffix: " days"
  - type: attribute
    entity: sensor.marc_med_jardiance
    attribute: refills_left
    name: "Refills Left"
  - type: divider
  - entity: sensor.marc_med_metformin
    name: "Metformin 500mg"
    secondary_info: last-changed
  - type: attribute
    entity: sensor.marc_med_metformin
    attribute: days_remaining
    name: "Days Remaining"
    suffix: " days"
  - type: attribute
    entity: sensor.marc_med_metformin
    attribute: refills_left
    name: "Refills Left"
```

**What it shows:** Your diabetes medications with stock details

---

### Card 5: Heart & Blood Pressure

```yaml
type: entities
title: "❤️ Heart & Blood Pressure"
state_color: true
show_header_toggle: false
entities:
  - entity: sensor.marc_med_candesartan
    name: "Candesartan 16mg"
  - type: attribute
    entity: sensor.marc_med_candesartan
    attribute: days_remaining
    suffix: " days"
  - type: divider
  - entity: sensor.marc_med_bisoprolol
    name: "Bisoprolol 5mg"
  - type: attribute
    entity: sensor.marc_med_bisoprolol
    attribute: days_remaining
    suffix: " days"
  - type: divider
  - entity: sensor.marc_med_spironolactone
    name: "Spironolactone 25mg"
  - type: attribute
    entity: sensor.marc_med_spironolactone
    attribute: days_remaining
    suffix: " days"
  - type: divider
  - entity: sensor.marc_med_edoxaban
    name: "Edoxaban 60mg (Blood Thinner)"
    secondary_info: last-changed
  - type: attribute
    entity: sensor.marc_med_edoxaban
    attribute: days_remaining
    suffix: " days"
  - type: attribute
    entity: sensor.marc_med_edoxaban
    attribute: status
    name: "Status"
```

**What it shows:** All cardiovascular medications grouped together

**Note:** Edoxaban is highlighted as critical - don't miss doses!

---

### Card 6: Other Medications

```yaml
type: entities
title: "💊 Other Medications"
state_color: true
show_header_toggle: false
entities:
  - entity: sensor.marc_med_pantoloc
    name: "Pantoloc 40mg"
  - type: attribute
    entity: sensor.marc_med_pantoloc
    attribute: days_remaining
    suffix: " days"
  - type: divider
  - entity: sensor.marc_med_rosuvastatin
    name: "Rosuvastatin 20mg"
  - type: attribute
    entity: sensor.marc_med_rosuvastatin
    attribute: days_remaining
    suffix: " days"
  - type: divider
  - entity: sensor.marc_med_zenhale_inhaler
    name: "Zenhale Inhaler 100/6"
  - type: attribute
    entity: sensor.marc_med_zenhale_inhaler
    attribute: days_remaining
    suffix: " days"
  - type: attribute
    entity: sensor.marc_med_zenhale_inhaler
    attribute: notes
    name: "Instructions"
```

**What it shows:** Digestive, cholesterol, and respiratory medications

---

### Card 7: Active Alerts

```yaml
type: markdown
title: "⚠️ Medication Alerts"
content: |
  {% set ns = namespace(has_alerts=false) %}
  
  {% for entity in [
    'sensor.marc_med_jardiance',
    'sensor.marc_med_metformin',
    'sensor.marc_med_pantoloc',
    'sensor.marc_med_rosuvastatin',
    'sensor.marc_med_candesartan',
    'sensor.marc_med_bisoprolol',
    'sensor.marc_med_spironolactone',
    'sensor.marc_med_edoxaban',
    'sensor.marc_med_zenhale_inhaler'
  ] %}
    {% set status = state_attr(entity, 'status') %}
    {% set days = state_attr(entity, 'days_remaining') | int %}
    {% set name = state_attr(entity, 'medication_name') %}
    {% set doctor = state_attr(entity, 'prescribing_doctor') %}
    
    {% if status in ['CRITICAL', 'LOW', 'OUT_OF_STOCK'] %}
      {% set ns.has_alerts = true %}
      
      {% if status == 'OUT_OF_STOCK' %}
  <div style="padding: 15px; margin: 10px 0; background: #ffebee; border-left: 5px solid #f44336; border-radius: 8px;">
    <h3 style="color: #c62828; margin: 0 0 5px 0;">🔴 {{ name }} - OUT OF STOCK</h3>
    <p style="margin: 5px 0;"><strong>URGENT:</strong> Contact {{ doctor }} immediately!</p>
  </div>
      {% elif status == 'CRITICAL' %}
  <div style="padding: 15px; margin: 10px 0; background: #fff3e0; border-left: 5px solid #ff9800; border-radius: 8px;">
    <h3 style="color: #e65100; margin: 0 0 5px 0;">🟠 {{ name }} - CRITICAL</h3>
    <p style="margin: 5px 0;">Only {{ days }} days remaining ({{ states(entity) }} pills)</p>
    <p style="margin: 5px 0;"><strong>Action:</strong> Request refill NOW</p>
  </div>
      {% elif status == 'LOW' %}
  <div style="padding: 15px; margin: 10px 0; background: #fff9c4; border-left: 5px solid #fbc02d; border-radius: 8px;">
    <h3 style="color: #f57f17; margin: 0 0 5px 0;">🟡 {{ name }} - Running Low</h3>
    <p style="margin: 5px 0;">{{ days }} days remaining ({{ states(entity) }} pills)</p>
    <p style="margin: 5px 0;"><strong>Action:</strong> Schedule refill soon</p>
  </div>
      {% endif %}
    {% endif %}
  {% endfor %}
  
  {% if not ns.has_alerts %}
  <div style="padding: 20px; text-align: center; background: #e8f5e9; border-left: 5px solid #4caf50; border-radius: 8px;">
    <h3 style="color: #2e7d32; margin: 0;">✅ All Medications in Good Standing</h3>
    <p style="margin: 10px 0; color: #1b5e20;">No immediate action required</p>
  </div>
  {% endif %}
```

**What it shows:**
- Real-time alerts when medications are running low
- Color-coded by urgency (red/orange/yellow)
- Action recommendations
- Green "all clear" when everything is fine

---

### Card 8: Refill Schedule

```yaml
type: markdown
title: "📅 Upcoming Refills (Next 30 Days)"
content: |
  {% for entity in [
    'sensor.marc_med_jardiance',
    'sensor.marc_med_metformin',
    'sensor.marc_med_pantoloc',
    'sensor.marc_med_rosuvastatin',
    'sensor.marc_med_candesartan',
    'sensor.marc_med_bisoprolol',
    'sensor.marc_med_spironolactone',
    'sensor.marc_med_edoxaban',
    'sensor.marc_med_zenhale_inhaler'
  ] %}
  {% set days = state_attr(entity, 'days_remaining') | int %}
  {% if days > 0 and days <= 30 %}
  {% set refill_date = (now().timestamp() + (days * 86400)) | timestamp_custom('%B %d, %Y') %}
  {% set dow = (now().timestamp() + (days * 86400)) | timestamp_custom('%A') %}
  {% set name = state_attr(entity, 'medication_name') %}
  {% set doctor = state_attr(entity, 'prescribing_doctor') %}
  {% set refills = state_attr(entity, 'refills_left') %}
  
  <div style="padding: 15px; margin: 10px 0; {% if days <= 7 %}background: #fff3cd;{% elif days <= 14 %}background: #d1ecf1;{% else %}background: #d4edda;{% endif %} border-left: 5px solid {% if days <= 7 %}#ffc107;{% elif days <= 14 %}#17a2b8;{% else %}#28a745;{% endif %} border-radius: 10px;">
    <h3 style="margin: 0 0 10px 0;">{{ name }}</h3>
    <table style="width: 100%;">
      <tr><td><strong>📅 Refill Date:</strong></td><td>{{ dow }}, {{ refill_date }}</td></tr>
      <tr><td><strong>⏰ Days Until:</strong></td><td>{{ days }} days</td></tr>
      <tr><td><strong>💊 Pills Left:</strong></td><td>{{ states(entity) }} pills</td></tr>
      <tr><td><strong>🔄 Refills:</strong></td><td>{{ refills }} available</td></tr>
      <tr><td><strong>👨‍⚕️ Doctor:</strong></td><td>{{ doctor }}</td></tr>
    </table>
  </div>
  {% endif %}
  {% endfor %}
```

**What it shows:**
- Medications needing refills in next 30 days
- Color-coded by urgency (yellow ≤7 days, blue ≤14 days, green ≤30 days)
- Exact refill dates with day of week
- Refills remaining count

---

### Card 9: Medications by Doctor

```yaml
type: markdown
title: "👨‍⚕️ Prescribing Physicians"
content: |
  {% set doctors = {
    'Dr. Smith': ['sensor.marc_med_jardiance', 'sensor.marc_med_metformin', 'sensor.marc_med_rosuvastatin'],
    'Dr. Johnson': ['sensor.marc_med_pantoloc'],
    'Dr. Wilson': ['sensor.marc_med_candesartan', 'sensor.marc_med_bisoprolol', 'sensor.marc_med_spironolactone', 'sensor.marc_med_edoxaban'],
    'Dr. Brown': ['sensor.marc_med_zenhale_inhaler']
  } %}
  
  {% for doctor, meds in doctors.items() %}
  <div style="padding: 20px; margin: 10px 0; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border-left: 5px solid #2196F3;">
    <h2 style="margin: 0 0 15px 0; color: #1976D2;">{{ doctor }}</h2>
    
    <table style="width: 100%; border-collapse: collapse;">
    {% for entity in meds %}
      <tr style="border-bottom: 1px solid #90caf9;">
        <td style="padding: 10px 5px;">
          <strong style="color: #1565C0;">{{ state_attr(entity, 'medication_name') }}</strong>
          <span style="color: #424242;">{{ state_attr(entity, 'strength') }}</span>
        </td>
        <td style="padding: 10px 5px; text-align: right;">
          <span style="{% if state_attr(entity, 'status') == 'OK' %}color: #2e7d32;{% elif state_attr(entity, 'status') == 'LOW' %}color: #f57f17;{% else %}color: #c62828;{% endif %} font-weight: bold;">
            {{ states(entity) }} pills
          </span>
        </td>
      </tr>
      <tr>
        <td colspan="2" style="padding: 0 5px 10px 5px; font-size: 13px; color: #616161;">
          {{ state_attr(entity, 'days_remaining') }} days • 
          {{ state_attr(entity, 'status') }} • 
          {{ state_attr(entity, 'refills_left') }} refills
        </td>
      </tr>
    {% endfor %}
    </table>
  </div>
  {% endfor %}
```

**What it shows:**
- All medications grouped by prescribing doctor
- Color-coded pill counts (green=OK, yellow=LOW, red=CRITICAL)
- Days remaining and refills for each medication
- Easy to see which doctor to contact for refills

**Note:** Update doctor names to match your actual doctors

---

## Step 4: Done! 🎉

You now have a complete medication dashboard!

## Using Your Dashboard

### Daily Routine

**Morning:**
1. Open dashboard
2. Tap ☀️ Morning Pills (turns green)
3. Tap 💨 Morning Puffer
4. Check progress percentage

**Lunch:**
1. Tap 🌞 Lunch Pills

**Evening:**
1. Tap 🌙 Evening Pills
2. Tap 💨 Evening Puffer
3. Aim for 100%!

### Weekly Maintenance

- Check ⚠️ Alerts section
- Review 📅 Refill Schedule
- Request refills for anything ≤14 days

### When to Call Doctor

- 🔴 RED alert (out of stock or critical)
- 🟠 ORANGE alert (≤3 days remaining)
- When refills_left = 0 (need new prescription)

## Customization Tips

### Change Doctor Names

In Card 9, update the doctors dictionary:
```yaml
{% set doctors = {
  'Your Doctor Name': ['sensor.marc_med_jardiance', ...],
  ...
} %}
```

### Adjust Alert Thresholds

Current thresholds:
- CRITICAL: ≤3 days
- LOW: ≤7 days
- OK: >7 days

To change, edit the integration's sensor.py file.

### Add Mobile App Notifications

Create automation (next section).

## Troubleshooting

**Problem:** Cards show "Entity not available"
**Solution:** Check entity IDs in Developer Tools → States

**Problem:** Buttons don't toggle
**Solution:** Verify binary sensors exist and are not disabled

**Problem:** Alerts not showing
**Solution:** This is normal if all medications are OK (>7 days)

**Problem:** Progress percentage wrong
**Solution:** Check all 5 binary sensors are working

## Next Steps

1. ✅ Dashboard created
2. 📱 Set up mobile notifications (see automations guide)
3. 🎨 Apply custom theme (optional)
4. 📊 Add history graphs (optional)

---

**Congratulations!** You have a professional medication tracking dashboard! 🎉
