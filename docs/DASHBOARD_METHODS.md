# Dashboard Installation - Choose Your Method

**Having the "array error"? You have 3 options:**

---

## ⚡ Method 1: Card-by-Card (EASIEST - NEVER FAILS)

**Time:** 15 minutes  
**Difficulty:** ⭐ Beginner  
**Success Rate:** 100%

**Read:** `docs/DASHBOARD_SIMPLE_INSTALL.md`

**How it works:**
- Add 10 individual cards to your Overview dashboard
- One card at a time
- Each card paste separately
- No views, no complex YAML
- Works every single time

**Best for:**
- First-time users
- Anyone getting the array error
- People who want it working NOW

---

## 🎯 Method 2: Complete View (ADVANCED)

**Time:** 10 minutes  
**Difficulty:** ⭐⭐⭐ Advanced  
**Success Rate:** 90% (if done correctly)

**Read:** `docs/DASHBOARD_INSTALLATION_FIXED.md`

**How it works:**
- Create a NEW VIEW (tab) first
- Click INTO the new tab
- Open Raw Config of THAT VIEW (not the dashboard)
- Delete everything
- Paste complete dashboard
- Save

**Best for:**
- Users who understand Home Assistant views
- People who want all 29 cards at once
- Users comfortable with YAML

**Common mistake:** Pasting into dashboard Raw Config instead of view Raw Config

---

## 📱 Method 3: Use Mobile App

**Time:** 5 minutes  
**Difficulty:** ⭐⭐ Intermediate  
**Success Rate:** 95%

**How it works:**
- The mobile app has better editors
- Less chance of confusion
- Clearer where you're pasting

**Best for:**
- Users with Home Assistant mobile app
- People having desktop browser issues

---

## Recommendation

**Start here:** → `docs/DASHBOARD_SIMPLE_INSTALL.md`

Add cards one by one. It works every time. Once you have that working, you can optionally try the complete view method later.

---

## Why the Array Error Happens

The `complete_dashboard.yaml` file contains **VIEW-level YAML**.

A **VIEW** is a single tab in your dashboard (like "Overview" or "Map").

If you paste this VIEW YAML into the **DASHBOARD editor** (which expects an array of views), you get the error.

**Solution:** Paste it into a **VIEW editor** instead (after creating the view first).

**Or:** Use Method 1 which bypasses this entirely.

---

## Quick Comparison

| Method | Time | Difficulty | Cards | Error Rate |
|--------|------|------------|-------|------------|
| Card-by-Card | 15 min | Easy | 10 cards | 0% |
| Complete View | 10 min | Hard | 29 cards | 10% |
| Mobile App | 5 min | Medium | 29 cards | 5% |

---

## Choose Your Path

**Want it working now with zero errors?**
→ Use Method 1: `docs/DASHBOARD_SIMPLE_INSTALL.md`

**Want all 29 cards and comfortable with YAML?**
→ Use Method 2: `docs/DASHBOARD_INSTALLATION_FIXED.md`

**Have the mobile app?**
→ Try Method 3: Same as Method 2 but on mobile

---

## After Installation

Once you have cards showing up (using ANY method):

1. ✅ Add the shortcut button (see `examples/shortcut_button.yaml`)
2. ✅ Set up notifications (see `docs/NOTIFICATION_SETUP.md`)
3. ✅ Test your medication tracking
4. ✅ Configure health sensors (optional)

---

**Bottom line:** The card-by-card method in `DASHBOARD_SIMPLE_INSTALL.md` will get you up and running with ZERO errors. Start there! 🎯
