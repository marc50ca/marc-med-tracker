# Beautiful Dashboard Setup Guide

## Overview

The Marc Med Tracker integration includes two beautiful, modern dashboards to display all your medication information in an attractive, easy-to-use interface.

## Dashboard Options

### 1. **dashboard_beautiful.yaml** (With Custom Cards)
**Features:**
- Stunning gradient buttons for daily tracking
- Mushroom cards for medication inventory
- Interactive button cards with state-based colors
- Professional modern design

**Requirements:**
- `card-mod` (for styling)
- `mushroom` cards (for inventory)
- `button-card` (for dose tracking)

### 2. **dashboard_beautiful_simple.yaml** (No Custom Cards) ⭐ **Recommended**
**Features:**
- All the same functionality
- Beautiful styling with gradients
- Uses only built-in Home Assistant cards
- No custom card installation needed

**Requirements:**
- Home Assistant 2024.1+
- `card-mod` for enhanced styling (optional but recommended)

## Quick Start (5 minutes)

### Step 1: Install Card-Mod (Optional but Recommended)

Card-mod enables the beautiful styling. Install via HACS:

1. Open HACS → Frontend
2. Search for "card-mod"
3. Click Install
4. Restart Home Assistant

### Step 2: Apply the Theme

1. Copy `marc_med_tracker_theme.yaml` to `/config/themes/`
2. Add to `configuration.yaml`:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Restart Home Assistant
4. Go to Profile → Themes → Select "Marc Med Tracker"

### Step 3: Add the Dashboard

**Method A: Create New View**
1. Go to your dashboard
2. Click ⋮ (three dots) → Edit Dashboard
3. Click "+ Add View" tab at top
4. Configure:
   - **Title**: Medication Dashboard
   - **Icon**: mdi:medical-bag
   - **URL**: medication-hub
5. Click into the new view
6. Click ⋮ → Raw Configuration Editor
7. Copy entire contents from `dashboard_beautiful_simple.yaml`
8. Paste and save

**Method B: Create Standalone Dashboard**
1. Go to Settings → Dashboards
2. Click "+ Add Dashboard"
3. Choose "Start with empty dashboard"
4. Name it "Medication Dashboard"
5. Click the new dashboard
6. Click ⋮ → Raw Configuration Editor
7. Paste the YAML content
8. Save

## Features Explained

### Header Section
- Shows current date and time
- Beautiful gradient background
- Welcome message

### Today's Schedule
- **Morning & Daytime section**: Morning pills, morning puffer, lunch pills
- **Evening section**: Evening pills, evening puffer
- **State colors**: Red (not taken) → Green (taken)
- **Progress indicator**: Shows % complete with encouraging messages

### Medication Inventory
- **Quick overview**: Glance card showing all medications
- **Detailed cards**: Individual cards for each medication
  - Pills remaining
  - Days left
  - Status indicator
  - Refills available
  - Prescribing doctor
  - Last refilled date
- **Color-coded backgrounds**: Different gradient for each medication

### Active Alerts
- **Dynamic alert system**: Only shows when action needed
- **Color-coded severity**:
  - 🔴 Red: OUT_OF_STOCK (immediate action)
  - 🟠 Orange: CRITICAL (≤3 days)
  - 🟡 Yellow: LOW (≤7 days)
  - 🟣 Purple: NO_REFILLS_LEFT
  - ✅ Green: All OK
- **Actionable information**: What to do and who to contact

### Refill Schedule
- **Next 30 days**: Upcoming refills
- **Color-coded urgency**:
  - Yellow background: ≤7 days
  - Blue background: 8-14 days
  - Green background: 15-30 days
- **Complete information**: Date, day of week, pills left, refills, doctor

### Prescribing Physicians
- **Grouped by doctor**: All medications per physician
- **Status at a glance**: Color-coded pill counts
- **Complete details**: Days remaining, status, refills

### 7-Day Adherence Chart
- **Visual history**: See patterns over the week
- **All doses tracked**: Morning, lunch, evening, puffers
- **Identify gaps**: Spot missed doses easily

### Quick Actions
- **Gradient buttons**: Beautiful, large, easy to tap
- **One-tap marking**: Check off doses instantly
- **Navigate**: Quick access to history

## Customization

### Change Colors

Edit the gradient colors in the YAML:

```yaml
# Current gradient (purple)
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Blue gradient
background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%);

# Green gradient
background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);

# Red gradient
background: linear-gradient(135deg, #FF6B6B 0%, #C44569 100%);
```

### Add More Medications

Find sections like this:

```yaml
- type: entities
  title: 💊 Aspirin 100mg
  entities:
    - entity: sensor.marc_med_aspirin
```

Duplicate and change:
- Title
- Entity ID
- Background color (optional)

### Hide Sections

Comment out sections you don't want:

```yaml
# - type: markdown
#   content: |
#     ## Section to hide
```

### Adjust Card Size

Change card heights:

```yaml
styles:
  card:
    - height: 120px  # Change this value
```

## Mobile Optimization

The dashboard is fully responsive:
- **Cards stack vertically** on mobile
- **Large tap targets** for easy button pressing
- **Readable text** sizes
- **Scrollable** content

### Mobile Tips:
1. Use the Home Assistant mobile app
2. Add dashboard to home screen for quick access
3. Enable notifications for medication reminders
4. Use voice commands: "Hey Google, check off morning meds"

## Troubleshooting

### Cards Not Rendering
**Issue**: Blank spaces where cards should be
**Solution**: 
1. Check entity IDs match your medications
2. Verify all sensors exist in Developer Tools → States
3. Check for YAML syntax errors

### Styling Not Working
**Issue**: Plain cards without gradients
**Solution**:
1. Install card-mod from HACS
2. Clear browser cache (Ctrl+Shift+R)
3. Check theme is selected in profile

### Custom Cards Required Error
**Issue**: "Custom element doesn't exist: custom:button-card"
**Solution**:
- Use `dashboard_beautiful_simple.yaml` instead (no custom cards needed)
- OR install required custom cards from HACS

### Progress Not Updating
**Issue**: Percentage stuck at old value
**Solution**:
1. Toggle a dose to force update
2. Refresh browser
3. Check binary sensors are working

### Alerts Not Showing
**Issue**: Empty alerts section
**Solution**:
- This is normal if all medications are OK!
- Alerts only show when action is needed
- Test by setting a medication to LOW status

## Advanced Customization

### Change Icons

Find icon definitions:

```yaml
icon: mdi:pill
```

Change to any [Material Design Icon](https://materialdesignicons.com/):
- `mdi:pill-multiple`
- `mdi:medical-bag`
- `mdi:heart-pulse`
- `mdi:bottle-tonic-plus`

### Adjust Alert Thresholds

Find the status checks:

```yaml
{% if days <= 7 %}
  # LOW status
{% elif days <= 3 %}
  # CRITICAL status
```

Change the numbers to adjust when alerts appear.

### Add Badges

Add to the top of dashboard YAML:

```yaml
badges:
  - entity: sensor.marc_med_aspirin
  - entity: sensor.marc_med_vitamin_d
  - entity: binary_sensor.marc_med_morning
```

## Screenshot Ideas

Take screenshots to share:
1. **Perfect Day**: All doses checked off (100%)
2. **Alert View**: When medications are low
3. **Refill Schedule**: The colorful upcoming refills
4. **Doctor Directory**: The physician cards

## Performance Tips

- Dashboard loads fast with built-in cards
- History graph may slow on low-end devices (reduce hours_to_show)
- Consider splitting into multiple views if you have 10+ medications

## Questions?

**"Can I use this without custom cards?"**
- Yes! Use `dashboard_beautiful_simple.yaml`

**"Do I need card-mod?"**
- No, but highly recommended for beautiful styling

**"Will this work on my phone?"**
- Yes! Fully responsive design

**"Can I edit the layout?"**
- Absolutely! The YAML is fully customizable

**"How do I add my medications?"**
- Replace entity IDs (e.g., `sensor.marc_med_aspirin`) with yours

## Next Steps

1. Install the dashboard
2. Apply the theme
3. Customize for your medications
4. Set up automations for reminders
5. Enjoy never missing a dose!

---

**Made with ❤️ for beautiful medication tracking**
