# Medication Details Panel Guide

## Overview

The Medication Details Panel provides a comprehensive view of all your medication information in one place, including:

- Complete medication specifications
- Current inventory levels
- Refill schedules and requirements
- Doctor information
- Daily adherence tracking
- Historical trends
- Active alerts and warnings

## What's Included

### 1. Today's Checklist
Quick view of today's dose tracking status with color indicators.

### 2. Detailed Medication Cards
For each medication, see:
- **Current Status**: Pills remaining, status indicator
- **Medication Info**: Name, strength, prescribing doctor, notes
- **Dosage Schedule**: How many doses per day, pills per dose, daily consumption
- **Inventory**: Initial stock, current stock, days remaining
- **Refill Info**: Refills left, last refilled date, days since refill
- **Quick Actions**: Buttons to record doses taken

### 3. Quick Reference Table
Condensed table showing all medications at a glance with key metrics.

### 4. Active Alerts Panel
Automatically displays warnings for:
- 🔴 Out of stock medications
- 🟠 Critical levels (3 days or less)
- 🟡 Low stock (7 days or less)
- 🟣 No refills remaining

### 5. Refill Schedule
Calendar view showing when each medication needs to be refilled within the next 90 days.

### 6. Physician Directory
Lists all prescribing doctors with their prescribed medications grouped together.

### 7. Inventory History Graphs
Visual charts showing how medication levels change over time.

### 8. Adherence Tracking
- Today's adherence percentage
- Detailed table of which doses were taken and when
- 7-day adherence history graph

## Setup Instructions

### Option 1: Simple Panel (Recommended)

Use `medication_details_simple.yaml` - works with built-in Home Assistant cards only.

1. Copy the entire content from `medication_details_simple.yaml`
2. In Home Assistant, go to your dashboard
3. Click the three dots (⋮) → Edit Dashboard
4. Click "+ Add View" at the top
5. Configure the view:
   - **Title**: Medication Details
   - **Icon**: mdi:medical-bag
   - **URL Path**: med-details
6. Click "Save"
7. Click into the new view
8. Click "+ Add Card"
9. Choose "Manual" at the bottom
10. Paste the YAML content
11. Click "Save"

### Option 2: Enhanced Panel (Requires Custom Cards)

Use `medication_details_panel.yaml` - includes bar charts and enhanced visuals.

**Prerequisites:**
- Install `bar-card` from HACS for visual progress bars

**Setup:**
1. Install HACS if you haven't already
2. Go to HACS → Frontend
3. Search for and install "bar-card"
4. Follow the same steps as Option 1, but use the enhanced YAML

## Customizing for Your Medications

The example panels show three medications:
1. Aspirin 100mg
2. Vitamin D 2000 IU
3. Blood Pressure Medication 10mg

### To Add Your Medications:

1. Find the section for "Medication #1" in the YAML
2. Duplicate the entire entities card
3. Update these fields:
   - **title**: Change to your medication name
   - **entity**: Change `sensor.marc_med_aspirin` to your medication entity
   - **attribute**: These will automatically pull from your medication

Example - Adding a new medication called "Metformin":

```yaml
- type: entities
  title: 💊 Metformin 500mg - Complete Details
  show_header_toggle: false
  state_color: true
  entities:
    - type: section
      label: "📊 Current Status"
    - entity: sensor.marc_med_metformin
      name: Pills Remaining
    - type: attribute
      entity: sensor.marc_med_metformin
      attribute: status
      name: Status
    # ... continue with other attributes
```

## Understanding the Status Indicators

| Status | Color | Meaning | Action Required |
|--------|-------|---------|-----------------|
| OK | 🟢 Green | More than 14 days remaining | None |
| LOW | 🟡 Yellow | 7 or fewer days remaining | Request refill soon |
| CRITICAL | 🟠 Orange | 3 or fewer days remaining | Request refill immediately |
| OUT_OF_STOCK | 🔴 Red | No pills remaining | Contact doctor urgently |
| NO_REFILLS_LEFT | 🟣 Purple | Low stock + no refills | Contact doctor for new prescription |

## Using the Quick Actions

Each medication card has quick action buttons:

**Record Dose Taken**
- Tap to log that you took a dose
- Updates inventory automatically
- Doesn't affect the daily dose checklist (those are separate)

**Record Refill** (if added)
- Tap to log when you refill the medication
- Enter the number of pills
- Updates last refilled date and inventory

## Reading the Refill Schedule

The refill schedule shows:
- **Refill Needed By**: The date when you'll run out
- **Days Until Refill**: Countdown to refill date
- **Refills Available**: How many refills you have left
- **Current Stock**: Current pill count
- **Doctor**: Who to contact for refill

Plan to request refills about 5-7 days before the "Refill Needed By" date to ensure you don't run out.

## Understanding the Adherence Metrics

**Today's Adherence**: Shows percentage of scheduled doses taken today
- 100% = All 5 daily doses taken
- 80% = 4 of 5 taken
- 60% = 3 of 5 taken
- etc.

**7-Day History**: Visual graph showing which doses were taken each day over the past week. Look for patterns:
- Solid green = Good adherence
- Gaps = Missed doses
- Patterns = May indicate systematic issues (e.g., always forgetting lunch dose)

## Tips for Best Use

1. **Check Daily**: Make it part of your routine to check the panel each morning
2. **Set Refill Alerts**: Create automations to remind you when medications show "LOW" status
3. **Review Weekly**: Look at the 7-day history every Sunday to identify patterns
4. **Update Promptly**: When you refill medications, use the service call to update the system
5. **Doctor Visits**: Use the Physician Directory section when preparing for appointments

## Mobile Access

This panel works great on mobile devices:
- All information is accessible via the Home Assistant mobile app
- Cards automatically resize for mobile screens
- Tap actions work normally
- Use the app's notification feature for reminders

## Privacy Note

All medication data is stored locally on your Home Assistant instance. No data is sent to external servers unless you have configured cloud services.

## Troubleshooting

**Problem**: Medication not showing up
- **Solution**: Verify the medication is in your configuration.yaml and Home Assistant has been restarted

**Problem**: Attributes showing "unknown"
- **Solution**: The medication sensor may not be fully initialized. Wait a few minutes or restart Home Assistant

**Problem**: Graphs not showing data
- **Solution**: Graphs require time-series data. They'll populate as the integration tracks changes over time

**Problem**: Quick actions not working
- **Solution**: Verify the service calls are using the correct medication_id (lowercase with underscores)

**Problem**: Alerts panel is empty
- **Solution**: This means all your medications are in good standing! The panel only shows when action is needed

## Advanced Customization

### Change Section Icons
Edit the `label` and add custom icons:
```yaml
- type: section
  label: "💊 Your Custom Section"
```

### Modify Color Thresholds
For different alert thresholds, edit the conditions in the alerts section.

### Add More Sections
Duplicate any section block and modify as needed.

### Hide Sections
Comment out sections you don't need by adding `#` before each line.

## Getting Help

- Check `README.md` for integration documentation
- Review `configuration.yaml.example` for setup examples
- See `automations.yaml.example` for automation ideas
- Refer to Home Assistant documentation for card configuration
