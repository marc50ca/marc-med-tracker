# Troubleshooting Guide - Marc Med Tracker

## Common Installation Issues

### Error: 'NoneType' object has no attribute 'domain'

**Full Error:**
```
Error during setup of component marc_med_tracker: 'NoneType' object has no attribute 'domain'
```

**Cause:** This error occurred in earlier versions when the integration tried to set up platforms before YAML configuration was loaded.

**Solution:** Update to version 2.0.0 or later, which fixes this issue.

---

### Error: 'HomeAssistant' object has no attribute 'helpers'

**Full Error:**
```
Error during setup of component marc_med_tracker: 'HomeAssistant' object has no attribute 'helpers'
```

**Cause:** Platform discovery was being called incorrectly in an intermediate version.

**Solution:** Update to the latest version 2.0.0 which properly imports and uses the discovery helper.

**If still seeing this error:**
1. Make sure you have the latest `__init__.py` file
2. Check that `from homeassistant.helpers.discovery import async_load_platform` is in the imports
3. Delete the integration folder completely and reinstall from the latest zip
4. Restart Home Assistant

**If still seeing this error:**
1. Make sure you're using the latest version (check `manifest.json` - should be 2.0.0)
2. Delete the integration folder completely and reinstall
3. Restart Home Assistant twice (first restart loads config, second loads platforms)

---

### Integration Not Found

**Symptom:** Home Assistant doesn't recognize the integration

**Solutions:**
1. **Check installation path:**
   ```
   /config/custom_components/marc_med_tracker/
   ```
   NOT: `/config/custom_components/marc-med-tracker/` (no hyphens!)

2. **Verify file structure:**
   ```
   custom_components/
   └── marc_med_tracker/
       ├── __init__.py
       ├── sensor.py
       ├── binary_sensor.py
       ├── manifest.json
       └── services.yaml
   ```

3. **Check file permissions:**
   ```bash
   chmod -R 755 /config/custom_components/marc_med_tracker/
   ```

4. **Restart Home Assistant:**
   - Settings → System → Restart
   - Or: `ha core restart`

---

### Invalid Configuration

**Symptom:** "Invalid config for [marc_med_tracker]"

**Solutions:**

1. **Check YAML syntax:**
   ```yaml
   marc_med_tracker:  # Must use underscore, not hyphen
     medications:
       - name: "Aspirin"
         prescribing_doctor: "Dr. Smith"
         refills_left: 3
         last_refilled: "2026-02-20"  # Must be YYYY-MM-DD format
         strength: "100mg"
         doses_per_day: 1
         pills_per_dose: 1
         initial_stock: 90
   ```

2. **Common mistakes:**
   - Using `marc-med-tracker:` instead of `marc_med_tracker:`
   - Missing quotes around strings
   - Wrong date format (must be YYYY-MM-DD)
   - Missing required fields
   - Indentation errors (use 2 spaces, not tabs)

3. **Validate YAML:**
   - Use https://www.yamllint.com/
   - Or Developer Tools → YAML Configuration Check

---

### Entities Not Appearing

**Symptom:** No sensors or binary sensors created

**Solutions:**

1. **Check if integration loaded:**
   - Settings → System → Logs
   - Look for "marc_med_tracker" entries

2. **Verify medications in config:**
   - Open `configuration.yaml`
   - Ensure medications are listed under `marc_med_tracker:`

3. **Check entity registry:**
   - Developer Tools → States
   - Search for: `marc_med_`
   - Should see: `sensor.marc_med_aspirin`, etc.

4. **Force reload:**
   ```bash
   # Delete and recreate
   rm -rf /config/custom_components/marc_med_tracker
   # Reinstall files
   # Restart HA
   ```

---

### Services Not Found

**Symptom:** Service calls fail with "Service not found"

**Solutions:**

1. **Check service registration:**
   - Developer Tools → Services
   - Search for: `marc_med_tracker`
   - Should see 6 services

2. **Verify integration loaded:**
   - Settings → Integrations
   - If not shown, check logs for errors

3. **Correct service names:**
   ```yaml
   # Correct:
   service: marc_med_tracker.take_dose
   
   # Wrong:
   service: marc-med-tracker.take_dose  # No hyphens!
   service: med_tracker.take_dose       # Old name
   ```

---

### Binary Sensors Not Toggling

**Symptom:** Daily dose buttons don't turn green when clicked

**Solutions:**

1. **Check entity ID in automation:**
   ```yaml
   # Correct:
   entity_id: binary_sensor.marc_med_morning
   
   # Wrong:
   entity_id: binary_sensor.med_morning  # Old name
   ```

2. **Use correct service:**
   ```yaml
   service: marc_med_tracker.check_off_dose
   data:
     dose_id: morning
   ```

3. **Verify in Developer Tools:**
   - Developer Tools → States
   - Find: `binary_sensor.marc_med_morning`
   - Try: Developer Tools → Services → `marc_med_tracker.check_off_dose`

---

### Buttons Not Resetting at Midnight

**Symptom:** Binary sensors stay "on" the next day

**Solutions:**

1. **This is normal behavior** - they check the date when queried
   - The `is_on` property automatically checks if it's a new day
   - Just viewing the entity should trigger the check

2. **Force manual reset:**
   ```yaml
   service: marc_med_tracker.uncheck_dose
   data:
     dose_id: morning
   ```

3. **Add midnight reset automation (optional):**
   ```yaml
   automation:
     - alias: "Reset Medication Trackers"
       trigger:
         - platform: time
           at: "00:00:01"
       action:
         - service: homeassistant.reload_config_entry
           target:
             entity_id: binary_sensor.marc_med_morning
   ```

---

### Data Not Persisting

**Symptom:** Medication counts reset after restart

**Solutions:**

1. **Check storage file exists:**
   ```bash
   ls -la /config/.storage/marc_med_tracker.medications
   ```

2. **Verify write permissions:**
   ```bash
   chmod 644 /config/.storage/marc_med_tracker.medications
   ```

3. **Check for storage errors in logs:**
   - Settings → System → Logs
   - Search for "storage" or "marc_med_tracker"

---

### Dashboard Cards Not Working

**Symptom:** Dashboard shows "Entity not available"

**Solutions:**

1. **Update entity IDs in dashboard:**
   ```yaml
   # Old (wrong):
   entity: sensor.med_aspirin
   
   # New (correct):
   entity: sensor.marc_med_aspirin
   ```

2. **Check entity exists:**
   - Developer Tools → States
   - Verify the exact entity ID

3. **Reload dashboard:**
   - Three dots → Refresh

---

### Theme Not Applying

**Symptom:** Buttons don't show red/green colors

**Solutions:**

1. **Install theme:**
   ```bash
   cp marc_med_tracker_theme.yaml /config/themes/
   ```

2. **Add to configuration.yaml:**
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

3. **Select theme:**
   - Your Profile → Themes
   - Select "Marc Med Tracker"

4. **Use state_color in cards:**
   ```yaml
   type: entities
   state_color: true  # This is important!
   entities:
     - entity: binary_sensor.marc_med_morning
   ```

---

### Upgrading from Old Version

**Symptom:** Entities have old names after upgrade

**Solutions:**

1. **Entity IDs changed:**
   - Old: `sensor.med_aspirin` or `sensor.medication_aspirin`
   - New: `sensor.marc_med_aspirin`

2. **Update everywhere:**
   - Update automations
   - Update dashboard cards
   - Update scripts
   - Use find/replace in YAML files

3. **Or rename entities:**
   - Developer Tools → States
   - Click entity → Settings icon
   - Change Entity ID (requires restart)

---

## Getting Help

### Before Asking for Help

1. **Check Home Assistant version:**
   ```
   Settings → System → About
   Minimum: 2024.1.0
   ```

2. **Check logs:**
   ```
   Settings → System → Logs
   Filter: marc_med_tracker
   ```

3. **Verify installation:**
   ```bash
   ls -la /config/custom_components/marc_med_tracker/
   ```

4. **Check configuration:**
   ```bash
   cat /config/configuration.yaml | grep -A 20 marc_med_tracker
   ```

### When Reporting Issues

Include:
- Home Assistant version
- Integration version (from `manifest.json`)
- Relevant log entries
- Your configuration (remove sensitive info)
- What you were trying to do
- What actually happened

### Quick Diagnostic

Run these checks:

```yaml
# 1. Can you see the domain?
Developer Tools → Services → Search "marc_med_tracker"

# 2. Do entities exist?
Developer Tools → States → Search "marc_med"

# 3. Any errors?
Settings → System → Logs → Filter "marc_med_tracker"

# 4. Is config valid?
Developer Tools → YAML → Check Configuration
```

---

## Clean Reinstall

If all else fails:

```bash
# 1. Stop Home Assistant
ha core stop

# 2. Remove integration
rm -rf /config/custom_components/marc_med_tracker

# 3. Remove storage (optional - loses data!)
rm /config/.storage/marc_med_tracker.medications

# 4. Extract fresh copy
unzip marc-med-tracker.zip
cp -r marc-med-tracker/marc_med_tracker /config/custom_components/

# 5. Verify permissions
chmod -R 755 /config/custom_components/marc_med_tracker/

# 6. Start Home Assistant
ha core start

# 7. Check logs
ha core logs
```

---

## Still Having Issues?

1. Check [COMPATIBILITY.md](COMPATIBILITY.md) for version requirements
2. Review [INSTALL.md](INSTALL.md) for installation steps
3. Read [README.md](README.md) for configuration examples
4. Check Home Assistant Community forums
