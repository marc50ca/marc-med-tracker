# Troubleshooting: Missing Binary Sensors

## Problem

You're missing these sensors:
- `binary_sensor.marc_med_morning`
- `binary_sensor.marc_med_lunch`
- `binary_sensor.marc_med_evening`
- `binary_sensor.marc_med_morning_puffer`
- `binary_sensor.marc_med_evening_puffer`

---

## Solution Steps

### Step 1: Verify Integration is Installed

1. Go to **Settings** → **Devices & Services**
2. Look for **"Marc Med Tracker"** in the list
3. If NOT there:
   - Integration not installed via HACS
   - Go back to installation steps
   - Install via HACS first

### Step 2: Verify Configuration is Added

1. Check your `/config/configuration.yaml` file
2. Look for this section:

```yaml
marc_med_tracker:
  medications:
    - name: "Metformin"
      prescribing_doctor: "NP T. Wakefield"
      # ... rest of config
```

3. If NOT there:
   - Copy from `examples/configuration.yaml.example`
   - Paste into your configuration.yaml
   - Save the file

### Step 3: Restart Home Assistant (REQUIRED!)

**This is the most common cause of missing sensors!**

1. Go to **Settings** → **System** → **Restart**
2. Click **"Restart Home Assistant"**
3. Wait for restart to complete (1-2 minutes)
4. **IMPORTANT:** A reload is NOT enough - you must RESTART

### Step 4: Check if Sensors Appeared

1. Go to **Developer Tools** → **States**
2. Filter by: `marc_med`
3. You should see **13 entities**:

**Medication Sensors (8):**
- `sensor.marc_med_metformin`
- `sensor.marc_med_jardiance`
- `sensor.marc_med_candesartan`
- `sensor.marc_med_rosuvastatin`
- `sensor.marc_med_pantoprazole`
- `sensor.marc_med_bisoprolol`
- `sensor.marc_med_spironolactone`
- `sensor.marc_med_zenhale_inhaler`

**Binary Sensors (5):**
- `binary_sensor.marc_med_morning`
- `binary_sensor.marc_med_lunch`
- `binary_sensor.marc_med_evening`
- `binary_sensor.marc_med_morning_puffer`
- `binary_sensor.marc_med_evening_puffer`

✅ If you see all 13 - you're done!

---

## Still Missing?

### Check the Logs

1. Go to **Settings** → **System** → **Logs**
2. Search for: `marc_med_tracker`
3. Look for errors

**Common errors:**

#### Error: "Invalid config for marc_med_tracker"

**Cause:** YAML syntax error in configuration.yaml

**Fix:**
1. Check your configuration.yaml for syntax errors
2. Make sure indentation is correct (use spaces, not tabs)
3. Verify all required fields are present
4. Copy again from example file

#### Error: "Platform binary_sensor not found"

**Cause:** Integration files missing

**Fix:**
1. Reinstall via HACS
2. Make sure all files downloaded
3. Check `/config/custom_components/marc_med_tracker/` exists
4. Should contain: `__init__.py`, `sensor.py`, `binary_sensor.py`, `manifest.json`

#### Error: "Could not load binary_sensor platform"

**Cause:** Python error in binary_sensor.py

**Fix:**
1. Reinstall integration
2. Make sure you have latest version (v2.1.1)
3. Check Home Assistant version (need 2024.1.0+)

---

## Manual Verification

### Check Integration Files

1. Go to `/config/custom_components/marc_med_tracker/`
2. You should see these files:
   - `__init__.py`
   - `sensor.py`
   - `binary_sensor.py`
   - `manifest.json`
   - `services.yaml`

3. If any are missing:
   - Reinstall via HACS
   - Or manually upload missing files

### Check File Permissions

SSH into Home Assistant and run:
```bash
ls -la /config/custom_components/marc_med_tracker/
```

All files should be readable (not showing permission errors).

---

## Quick Checklist

- [ ] Integration installed via HACS
- [ ] Configuration added to configuration.yaml
- [ ] YAML syntax is correct (no tabs, proper indentation)
- [ ] Home Assistant **restarted** (not just reloaded)
- [ ] Waited 2 minutes after restart
- [ ] Checked Developer Tools → States
- [ ] Checked Settings → System → Logs for errors

---

## Configuration Template

If you're not sure your configuration is correct, use this template:

```yaml
marc_med_tracker:
  medications:
    # Morning medications
    - name: "Metformin"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "500mg"
      doses_per_day: 2
      pills_per_dose: 2
      initial_stock: 360
      notes: "2 tablets twice daily"
    
    - name: "Jardiance"
      prescribing_doctor: "NP T. Wakefield"
      refills_left: 3
      last_refilled: "2026-03-25"
      strength: "40mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
      notes: "1 tablet evening"
    
    # Add remaining medications...
```

**Key points:**
- Use **spaces** for indentation (2 or 4 spaces)
- **Never use tabs**
- Dates in format: `"YYYY-MM-DD"`
- Numbers without quotes: `3` not `"3"`
- Text with quotes: `"NP T. Wakefield"`

---

## After Binary Sensors Appear

Once you see the binary sensors:

1. **Test them:**
   - Click on `binary_sensor.marc_med_morning`
   - Should show `off` (red) by default
   - Click **Toggle** - should turn `on` (green)
   - Check again at midnight - should auto-reset to `off`

2. **Use in dashboard:**
   - Follow `docs/DASHBOARD_SIMPLE_INSTALL.md`
   - Add Card 1 (Today's Medications)
   - Buttons should appear and be clickable

3. **Set up automations:**
   - Follow `docs/NOTIFICATION_SETUP.md`
   - Add iPhone notifications
   - Test reminders

---

## Common Mistakes

### Mistake 1: Only Reloading YAML

❌ **Wrong:**
- Developer Tools → YAML → Reload All
- This does NOT load new integrations!

✅ **Correct:**
- Settings → System → Restart
- Full restart required for new integrations

### Mistake 2: Configuration in Wrong File

❌ **Wrong:**
- Adding to automations.yaml
- Adding to separate file without including it

✅ **Correct:**
- Add to `/config/configuration.yaml`
- Or add to a file that's included in configuration.yaml

### Mistake 3: Installing Integration After Config

❌ **Wrong Order:**
1. Add configuration
2. Install via HACS
3. Restart

✅ **Correct Order:**
1. Install via HACS
2. Restart
3. Add configuration
4. Restart again

---

## Getting Help

**If sensors still don't appear:**

1. Copy your configuration.yaml (medication section)
2. Copy the error from logs
3. Check Home Assistant version
4. Note which sensors ARE appearing (if any)

**Check these:**
- Is the integration in Settings → Devices & Services?
- Are the medication sensors (sensor.marc_med_*) working?
- What does the log say about binary_sensor platform?

---

## Expected Behavior

**After proper setup:**

✅ 8 medication sensors appear immediately  
✅ 5 binary sensors appear immediately  
✅ All sensors show in Developer Tools → States  
✅ Binary sensors start as `off` (red)  
✅ Clicking toggles them to `on` (green)  
✅ Auto-reset to `off` at midnight  
✅ Services available in Developer Tools → Services  

---

**Bottom line:** If binary sensors are missing, 99% of the time it's because Home Assistant wasn't fully restarted after adding the configuration. Do a full restart and wait 2 minutes!
