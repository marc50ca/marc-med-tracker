# Notification Quick Reference Card

## 📱 Your Medication Reminders

**Device:** Marc's iPhone 14  
**Service:** `notify.mobile_app_marcs_iphone_14`

---

## ⏰ Daily Reminder Schedule

| Time | What | Details |
|------|------|---------|
| **9:30 AM** | 💊 Morning Pills | 6 tablets |
| **9:30 AM** | 💨 Morning Puffer | Zenhale 1-2 puffs |
| **2:30 PM** | 💊 Lunch Pills | 2 Metformin tablets |
| **7:30 PM** | 💊 Evening Pill | 1 Jardiance tablet |
| **7:30 PM** | 💨 Evening Puffer | Zenhale 1-2 puffs |
| **10:00 PM** | 📊 Daily Summary | Adherence report |

---

## 🔔 Alert Levels

### 🟢 Normal (Respects Do Not Disturb)
- Low stock warnings (≤7 days)
- Weekly check-ins
- Daily summaries
- Perfect day celebrations

### 🔴 Critical (Bypasses Do Not Disturb)
- Critical stock (≤3 days)
- Out of stock alerts
- Can override silent mode
- Louder volume

---

## 📲 Actionable Notifications

When you receive a medication reminder:

### Option 1: Mark as Taken ✅
- Tap **"Mark as Taken"**
- Automatically updates dashboard
- Turns button green
- Sends confirmation

### Option 2: Snooze ⏰
- Tap **"Snooze 15 min"**
- Reminder goes away
- Returns in 15 minutes
- Only if still not taken

### Option 3: Dismiss
- Swipe away notification
- Mark manually in dashboard later

---

## 🚨 Stock Alert Timeline

### Week Before (7 days)
🟡 **Low Stock Alert**
- Yellow status on dashboard
- Normal notification
- "Request refill soon"

### 3 Days Before
🟠 **Critical Alert**
- Orange status on dashboard
- **Critical notification**
- "Request refill NOW"
- Bypasses Do Not Disturb

### Day Of (0 pills)
🔴 **Out of Stock**
- Red status on dashboard
- **3 urgent alerts** (1 min apart)
- Maximum volume
- "Contact doctor IMMEDIATELY"

---

## 📅 Weekly Check-In

**Every Sunday at 6:00 PM**
- Review upcoming refills
- Check dashboard status
- Plan for the week

---

## 🎉 Perfect Day Celebration

**Triggers when:**
- All 5 dose times completed
- Morning pills ✅
- Morning puffer ✅
- Lunch pills ✅
- Evening pill ✅
- Evening puffer ✅

**You get:** Congratulations message! 🎊

---

## 🔧 Quick Fixes

### Not Getting Notifications?

**Check iPhone:**
1. Settings → Home Assistant
2. Notifications → ON
3. Sounds → ON
4. Critical Alerts → ON

**Check Home Assistant:**
1. Settings → Devices → Mobile App
2. Find "marcs_iphone_14"
3. Test notification:
   ```
   Developer Tools → Services
   notify.mobile_app_marcs_iphone_14
   ```

### Wrong Time Zone?

1. Settings → System → General
2. Check time zone setting
3. Should match your location

### Buttons Not Working?

Make sure all 18 automations are enabled:
- 5 Reminders
- 3 Snooze handlers
- 5 Action handlers
- 3 Stock alerts
- 1 Daily summary
- 1 Celebration
- 1 Weekly check

---

## 📝 Customization

### Change Reminder Times

Edit in `/config/automations.yaml`:

```yaml
trigger:
  - platform: time
    at: "09:30:00"  # Morning
    # at: "14:30:00"  # Lunch (2:30 PM)
    # at: "19:30:00"  # Evening (7:30 PM)
```

### Change Messages

```yaml
action:
  - service: notify.mobile_app_marcs_iphone_14
    data:
      title: "Your Title Here"
      message: "Your message here"
```

### Change Sound

```yaml
data:
  push:
    sound:
      name: default  # or: alarm, update
      volume: 0.8    # 0.0 to 1.0
      critical: 1    # 1 = bypass DND
```

---

## 💡 Pro Tips

1. **Use Action Buttons**  
   Faster than opening dashboard - just tap "Mark as Taken"

2. **Check Daily Summary**  
   Review at 10 PM to see what you missed

3. **Enable Critical Alerts**  
   Never miss important stock warnings

4. **Snooze Strategically**  
   If you're about to eat, snooze until after meal

5. **Perfect Week Goal**  
   Try to get celebration message every day!

---

## 📞 Emergency Contacts

**NP T. Wakefield** (5 medications)
- Metformin, Jardiance, Candesartan, Rosuvastatin, Pantoprazole

**Dr. K. Ducet** (3 medications)
- Bisoprolol, Spironolactone, Zenhale

---

**Print this card and keep it handy!** 📱💊
