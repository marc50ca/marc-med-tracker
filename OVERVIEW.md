# Marc Med Tracker Integration - Complete Overview

## What This Integration Provides

This is a comprehensive Home Assistant custom integration for complete medication management. It tracks everything from daily dose compliance to long-term inventory management.

## Three Main Features

### 1. 📅 Daily Dose Tracking (Red/Green Buttons)
**What it does:**
- Provides 5 visual buttons that track if you've taken your medications today
- Buttons start RED (not taken) and turn GREEN when you tap them
- Automatically resets to RED at midnight
- Tracks exact time each dose was taken

**What you can track:**
- Morning Pills
- Lunch Pills
- Evening Pills
- Morning Puffer
- Evening Puffer

**Benefits:**
- Simple one-tap interface
- Visual confirmation you took your meds
- Weekly adherence history
- Prevents double-dosing

### 2. 📦 Medication Inventory Management
**What it does:**
- Tracks how many pills you have remaining
- Automatically calculates based on your dosage schedule
- Monitors refills available
- Alerts when running low

**What you can track:**
- Current pill count
- Days of medication remaining
- Number of refills left
- Last refill date
- Status (OK, LOW, CRITICAL, OUT_OF_STOCK)

**Benefits:**
- Never run out of medication
- Plan refills in advance
- Track multiple medications
- Know exactly when to call your doctor

### 3. 💊 Detailed Medication Information Panel
**What it does:**
- Shows all medication details in one organized view
- Displays active alerts and warnings
- Projects refill schedules
- Groups medications by doctor

**What you can see:**
- Complete medication specifications
- Prescribing doctor information
- Dosage schedules
- Refill requirements
- Historical trends
- Adherence statistics

**Benefits:**
- All info in one place
- Professional medical record view
- Easy to share with healthcare providers
- Historical tracking for patterns

## File Structure

```
marc_med_tracker_integration/
├── marc_med_tracker/          # Core integration files
│   ├── __init__.py             # Main integration logic
│   ├── sensor.py               # Inventory tracking sensors
│   ├── binary_sensor.py        # Daily dose tracking buttons
│   ├── services.yaml           # Available services
│   └── manifest.json           # Integration manifest
│
├── README.md                    # Main documentation
├── INSTALL.md                   # Quick installation guide
│
├── configuration.yaml.example  # Example configuration
│
├── Dashboard Files:
├── dashboard_simple.yaml        # Daily tracker (built-in cards)
├── dashboard_with_buttons.yaml  # Daily tracker (custom cards)
├── medication_details_simple.yaml    # Details panel (built-in)
├── medication_details_panel.yaml     # Details panel (custom)
├── complete_dashboard.yaml      # All views combined
│
├── Automation Files:
├── automations.yaml.example     # General automations
├── automations_dose_tracking.yaml    # Dose tracking automations
│
├── Theme:
├── marc_med_tracker_theme.yaml     # Red/green color theme
│
└── Guides:
    ├── QUICK_START_BUTTONS.md   # 3-minute button setup
    ├── DOSE_TRACKING_GUIDE.md   # Complete dose tracking docs
    └── DETAILS_PANEL_GUIDE.md   # Details panel documentation
```

## What You Get Out of the Box

### Sensors Created

**Inventory Sensors** (one per medication):
- `sensor.marc_med_aspirin`
- `sensor.marc_med_vitamin_d`
- `sensor.marc_med_blood_pressure_medication`
- (One for each medication in your config)

**Daily Dose Buttons** (5 total):
- `binary_sensor.marc_med_morning`
- `binary_sensor.marc_med_lunch`
- `binary_sensor.marc_med_evening`
- `binary_sensor.marc_med_morning_puffer`
- `binary_sensor.marc_med_evening_puffer`

### Services Available

1. **marc_med_tracker.take_dose** - Record taking medication
2. **marc_med_tracker.refill** - Record a refill
3. **marc_med_tracker.update_refills** - Update refill count
4. **marc_med_tracker.check_off_dose** - Check off daily dose
5. **marc_med_tracker.uncheck_dose** - Uncheck daily dose
6. **marc_med_tracker.update_doctor** - Update prescribing doctor name
7. **marc_med_tracker.update_stock** - Manually set pills on hand

### Automation Examples

15+ ready-to-use automations including:
- Daily reminders
- Low stock alerts
- Critical warnings
- Refill reminders
- Notification actions
- Weekly summaries
- Compliance tracking

### Dashboard Options

5 complete dashboard configurations:
1. Simple daily tracker
2. Enhanced daily tracker with custom cards
3. Simple details panel
4. Enhanced details panel
5. Complete multi-view dashboard

## Setup Time

- **Basic Setup**: 5 minutes
  - Copy files, edit configuration, restart
  
- **With Daily Tracker**: 10 minutes
  - Basic setup + add dashboard card
  
- **With Details Panel**: 15 minutes
  - Basic setup + daily tracker + details view
  
- **Full Featured**: 30 minutes
  - Everything + automations + custom theme

## Requirements

### Minimum Requirements
- Home Assistant (any recent version)
- Basic YAML editing skills
- No custom cards needed for basic functionality

### Optional Enhancements
- **HACS** - For custom cards (button-card, bar-card)
- **Mobile App** - For notification actions
- **Custom Theme** - For optimal red/green colors

## Use Cases

### Individual Use
- Track your personal medications
- Never miss a dose
- Manage refills proactively
- Keep medical records organized

### Family Use
- Create separate dashboards per family member
- Track children's medications
- Coordinate medication schedules
- Share status with caregivers

### Healthcare Professional
- Demonstrate medication tracking
- Monitor patient compliance
- Provide structured tracking system
- Generate adherence reports

## Quick Start Paths

### Path 1: Just Daily Tracking
**Time**: 10 minutes
**Files needed**:
1. Copy `marc_med_tracker/` folder
2. Use `dashboard_simple.yaml`
3. No configuration.yaml changes needed for tracking only

### Path 2: Inventory Management Only
**Time**: 10 minutes
**Files needed**:
1. Copy `marc_med_tracker/` folder
2. Edit `configuration.yaml` with your medications
3. Use the inventory sensors

### Path 3: Complete System
**Time**: 30 minutes
**Files needed**:
1. All integration files
2. Configuration for your medications
3. Dashboard of your choice
4. Automations (optional)
5. Custom theme (optional)

## Common Questions

**Q: Do I need to track inventory to use the daily buttons?**
A: No! The daily dose buttons work independently. You can use just the buttons without any medication configuration.

**Q: Can I customize which buttons show up?**
A: Yes, edit `binary_sensor.py` to add/remove/rename the dose trackers.

**Q: Does this work offline?**
A: Yes! Everything runs locally on your Home Assistant instance.

**Q: Can I track more than 3 medications?**
A: Absolutely! Just add more medication entries in your configuration.yaml.

**Q: Do the buttons require custom cards?**
A: No! They work great with built-in Home Assistant cards. Custom cards just make them look fancier.

**Q: How accurate is the inventory tracking?**
A: Very accurate if you record doses/refills. It calculates based on your dosage schedule.

**Q: Can I export my medication data?**
A: Yes! Use Home Assistant's history and database features to export data.

**Q: Does this integrate with pharmacy systems?**
A: No, it's a manual tracking system. You input your medications and manage them yourself.

## What Makes This Different

Compared to other medication trackers:

✅ **Fully Local** - No cloud services, complete privacy
✅ **Home Assistant Native** - Deep integration with automations
✅ **Visual Tracking** - Red/green buttons for instant feedback
✅ **Automatic Calculations** - Smart inventory management
✅ **Professional Grade** - Detailed information panels
✅ **Highly Customizable** - Modify to your exact needs
✅ **No Monthly Fees** - Free and open source
✅ **Works Offline** - No internet required
✅ **Automation Ready** - Integrates with notifications, voice assistants, etc.

## Getting Started

1. **Read INSTALL.md** - Quick installation guide
2. **Edit configuration.yaml.example** - Add your medications
3. **Choose a dashboard** - Pick from 5 options
4. **Optional: Add automations** - Set up reminders
5. **Optional: Install theme** - Enhanced colors

## Support Files

- **README.md** - Complete documentation
- **INSTALL.md** - Installation steps
- **QUICK_START_BUTTONS.md** - 3-minute button setup
- **DOSE_TRACKING_GUIDE.md** - Detailed button documentation
- **DETAILS_PANEL_GUIDE.md** - Panel setup and customization

## Next Steps

After installation:
1. Test the basic functionality
2. Add automations for reminders
3. Customize the dashboards
4. Set up mobile notifications
5. Share with family members if needed

Enjoy never missing a dose again! 💊
