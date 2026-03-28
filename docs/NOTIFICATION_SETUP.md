# iPhone Notification Setup Guide

## Overview

Get medication reminders sent to **Marc's iPhone 14** at specific times:
- ⏰ **9:30 AM** - Morning medications
- ⏰ **2:30 PM** - Lunch medications  
- ⏰ **7:30 PM** - Evening medications

Plus alerts for low stock, out of stock, and daily summaries.

---

## Prerequisites

✅ **Home Assistant Mobile App installed** on iPhone 14  
✅ **Marc Med Tracker integration** installed and configured  
✅ **Push notifications enabled** in iPhone settings

---

## Step 1: Verify Mobile App (2 minutes)

### Check Device Name

1. Go to **Settings** → **Devices & Services** → **Mobile App**
2. Find your iPhone entry
3. Verify the device name is: `marcs_iphone_14`

**If different:**
- Note the actual device name (e.g., `mobile_app_marcs_iphone`)
- You'll need to replace `mobile_app_marcs_iphone_14` in the automations

**To find the exact name:**
1. **Developer Tools** → **Services**
2. Type: `notify.`
3. Look for `notify.mobile_app_marcs_iphone_14` (or similar)
4. That's your notification service name

---

## Step 2: Add Automations (5 minutes)

### Method A: Copy All Automations

1. Open `/config/automations.yaml`
2. Open file: `examples/automations_with_notifications.yaml`
3. **Copy ALL contents** from the example file
4. **Paste at the end** of your automations.yaml
5. Save the file
6. Go to **Settings** → **Automations & Scenes**
7. Click **⋮** (three dots) → **Reload Automations**

**✅ You should see 18 new automations added:**
- 5 Medication reminders (morning, lunch, evening, puffers)
- 3 Snooze handlers
- 5 Action button handlers
- 3 Low stock alerts
- 1 Daily summary
- 1 Perfect day celebration
- 1 Weekly check

### Method B: Add via UI (Manual)

If you prefer adding through the UI, I'll show you one example:

1. **Settings** → **Automations & Scenes** → **Create Automation**
2. Click **Skip** (we'll do it manually)
3. Click **⋮** → **Edit in YAML**
4. Paste this:

```yaml
alias: "Medication Reminder - Morning Pills 9:30 AM"
description: "Remind to take morning medications at 9:30 AM"
trigger:
  - platform: time
    at: "09:30:00"
condition:
  - condition: state
    entity_id: binary_sensor.marc_med_morning
    state: "off"
action:
  - service: notify.mobile_app_marcs_iphone_14
    data:
      title: "💊 Morning Medications"
      message: "Time to take your 6 morning pills!"
      data:
        push:
          sound:
            name: default
            critical: 1
            volume: 0.8
        actions:
          - action: "MARK_MORNING_TAKEN"
            title: "Mark as Taken"
          - action: "SNOOZE_MORNING"
            title: "Snooze 15 min"
```

5. Click **Save**
6. Repeat for other automations

---

## Step 3: Test Notifications (2 minutes)

### Test One Automation

1. **Developer Tools** → **Services**
2. Service: `notify.mobile_app_marcs_iphone_14`
3. YAML:
```yaml
title: "Test Notification"
message: "This is a test from Home Assistant"
```
4. Click **Call Service**

**Expected:** You should receive a notification on your iPhone 14

**If no notification:**
- Check iPhone notification settings
- Verify Home Assistant app has notifications enabled
- Check the device name is correct

---

## Notification Schedule

### Daily Reminders

**9:30 AM - Morning**
- 💊 Morning Pills (6 tablets)
- 💨 Morning Puffer (Zenhale)
- Only sends if NOT marked as taken
- Actionable buttons: "Mark as Taken" or "Snooze 15 min"

**2:30 PM - Lunch**
- 💊 Lunch Pills (2 Metformin tablets)
- Only sends if NOT marked as taken
- Actionable buttons: "Mark as Taken" or "Snooze 15 min"

**7:30 PM - Evening**
- 💊 Evening Pill (1 Jardiance)
- 💨 Evening Puffer (Zenhale)
- Only sends if NOT marked as taken
- Actionable buttons: "Mark as Taken" or "Snooze 15 min"

**10:00 PM - Daily Summary**
- Shows which doses were taken/missed today
- Sent every night

### Stock Alerts

**🟡 Low Stock (≤7 days)**
- Notification when medication reaches 7 days
- Shows days remaining
- Shows which prescriber to contact
- Normal priority

**🟠 Critical Stock (≤3 days)**
- Notification when medication reaches 3 days
- **Critical alert** (bypasses Do Not Disturb)
- Louder sound
- Shows prescriber contact info
- Urgent priority

**🔴 Out of Stock**
- **Critical alert** when medication runs out
- Bypasses Do Not Disturb
- Maximum volume
- Sends 3 repeat alerts (1 minute apart)
- **Immediate action required**

### Weekly Check

**Sunday 6:00 PM**
- Reminder to check dashboard
- Review upcoming refills
- Plan for the week ahead

### Celebration 🎉

**Perfect Adherence**
- Triggers when ALL 5 doses marked for the day
- Congratulatory message
- Motivational feedback

---

## Using Actionable Notifications

### When You Get a Reminder

**Option 1: Mark as Taken**
1. Notification appears
2. Tap **"Mark as Taken"**
3. Automatically marks dose in dashboard (green ✅)
4. Confirmation notification received

**Option 2: Snooze**
1. Notification appears
2. Tap **"Snooze 15 min"**
3. Notification goes away
4. Comes back in 15 minutes (if still not taken)

**Option 3: Ignore**
1. Swipe away notification
2. You can mark manually in dashboard later

---

## Customizing Notification Times

To change reminder times:

1. Open `/config/automations.yaml`
2. Find the automation (e.g., "Morning Pills 9:30 AM")
3. Change the time:
```yaml
trigger:
  - platform: time
    at: "09:30:00"  # Change to "10:00:00" for 10 AM
```
4. Save file
5. Reload automations

**Time Format:** 24-hour format (HH:MM:SS)
- 9:30 AM = `"09:30:00"`
- 2:30 PM = `"14:30:00"`
- 7:30 PM = `"19:30:00"`

---

## Customizing Notification Messages

To change what the notification says:

```yaml
action:
  - service: notify.mobile_app_marcs_iphone_14
    data:
      title: "Your Custom Title"
      message: "Your custom message here"
```

---

## Troubleshooting

### Notifications Not Received

**Check Device Name:**
```
Developer Tools → Services → notify.mobile_app_
```
Should show your iPhone. If name is different, update automations.

**Check iPhone Settings:**
1. iPhone Settings → Home Assistant
2. Notifications → Enabled
3. Allow Notifications → ON
4. Sounds → ON
5. Badges → ON

**Check Do Not Disturb:**
- Critical alerts bypass DND
- Normal alerts (Low Stock) respect DND
- Check if DND is active

### Automations Not Triggering

**Check Time:**
- Automations use 24-hour format
- Verify times are correct
- Check Home Assistant timezone (Settings → System → General)

**Check Conditions:**
- Automation only runs if dose is NOT taken
- If already marked green, won't send notification
- Test by unmarking dose first

**Reload Automations:**
- Settings → Automations & Scenes
- Click ⋮ → Reload Automations

### Action Buttons Not Working

**Check Event Names:**
- Action names must match exactly
- Case sensitive: `MARK_MORNING_TAKEN` not `mark_morning_taken`

**Check Handler Automations:**
- Each action button needs a handler automation
- All 5 handlers should be present

**Test in Developer Tools:**
```yaml
service: marc_med_tracker.check_off_dose
data:
  dose_id: "morning"
```

### Critical Alerts Not Bypassing DND

**iPhone Settings:**
1. Settings → Home Assistant → Notifications
2. **Critical Alerts** → ON
3. This allows urgent medication alerts through DND

---

## Notification Sound Options

### Available Sounds

```yaml
data:
  push:
    sound:
      name: default      # Default sound
      # name: update     # Update sound  
      # name: alarm      # Alarm sound
      critical: 1        # Bypass DND (0 = respect DND)
      volume: 0.8        # 0.0 to 1.0
```

### Testing Different Sounds

```yaml
service: notify.mobile_app_marcs_iphone_14
data:
  title: "Sound Test"
  message: "Testing notification sound"
  data:
    push:
      sound:
        name: alarm
        volume: 1.0
```

---

## Advanced Features

### Location-Based Reminders

Only send reminder if at home:

```yaml
condition:
  - condition: state
    entity_id: binary_sensor.marc_med_morning
    state: "off"
  - condition: zone
    entity_id: device_tracker.marcs_iphone_14
    zone: zone.home
```

### Retry Failed Doses

Send second reminder 30 min later:

```yaml
- alias: "Medication Reminder - Morning Second Attempt"
  trigger:
    - platform: time
      at: "10:00:00"  # 30 min after first reminder
  condition:
    - condition: state
      entity_id: binary_sensor.marc_med_morning
      state: "off"
  action:
    - service: notify.mobile_app_marcs_iphone_14
      data:
        title: "💊 Medication Reminder"
        message: "Second reminder: Please take morning pills"
```

---

## Summary

✅ **18 automations** added  
✅ **3 reminder times:** 9:30 AM, 2:30 PM, 7:30 PM  
✅ **Actionable buttons** to mark doses from notification  
✅ **15-minute snooze** option  
✅ **Stock alerts** (Low, Critical, Out of Stock)  
✅ **Daily summary** at bedtime  
✅ **Weekly check-in** on Sundays  
✅ **Perfect day celebration** 🎉

**You'll never miss a medication again!** 💊✨

---

## Quick Reference

| Time | Notification | What It's For |
|------|--------------|---------------|
| 9:30 AM | Morning Pills + Puffer | 6 tablets + Zenhale |
| 2:30 PM | Lunch Pills | 2 Metformin tablets |
| 7:30 PM | Evening Pills + Puffer | 1 Jardiance + Zenhale |
| 10:00 PM | Daily Summary | Adherence report |
| As Needed | Low Stock | ≤7 days remaining |
| As Needed | Critical Stock | ≤3 days remaining |
| As Needed | Out of Stock | 0 pills/puffs left |
| Sunday 6:00 PM | Weekly Check | Review refills |

**Device:** Marc's iPhone 14  
**Service:** `notify.mobile_app_marcs_iphone_14`
