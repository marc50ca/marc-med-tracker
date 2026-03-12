# Quick Installation Guide

## Prerequisites

Before installing, ensure you have:
- **Home Assistant 2024.1.0 or later** (check Settings → System → About)
- **Python 3.11 or later** (bundled with modern HA)
- Access to your Home Assistant configuration files

⚠️ **Version Check**: If you're running Home Assistant 2023.x or earlier, please upgrade before installing.

## Installation Steps

1. **Copy the integration to Home Assistant:**
   ```
   Copy the entire `marc_med_tracker` folder to:
   /config/custom_components/marc_med_tracker/
   ```

2. **Restart Home Assistant:**
   - Go to Settings → System → Restart
   - Or restart via command line/SSH

3. **Add configuration:**
   - Open your `configuration.yaml` file
   - Add the medication tracker configuration (see `configuration.yaml.example`)
   - Adjust the medication details to match your actual medications

4. **Restart again:**
   - After adding configuration, restart Home Assistant one more time

5. **Verify installation:**
   - Go to Developer Tools → States
   - Search for entities starting with `sensor.marc_med_`
   - You should see one sensor for each medication

## File Structure

After installation, your file structure should look like:

```
config/
├── configuration.yaml (with your medication tracker config)
└── custom_components/
    └── marc_med_tracker/
        ├── __init__.py
        ├── sensor.py
        ├── manifest.json
        └── services.yaml
```

## Quick Start Configuration

Minimal example to add to `configuration.yaml`:

```yaml
marc_med_tracker:
  medications:
    - name: "My Medication"
      prescribing_doctor: "Dr. Name"
      refills_left: 3
      last_refilled: "2026-02-16"  # Today's date
      strength: "100mg"
      doses_per_day: 1
      pills_per_dose: 1
      initial_stock: 90
```

## Testing Services

After installation, test the services in Developer Tools → Services:

### Test taking a dose:
```yaml
service: marc_med_tracker.take_dose
data:
  medication_id: "my_medication"
  doses: 1
```

### Test recording a refill:
```yaml
service: marc_med_tracker.refill
data:
  medication_id: "my_medication"
  pills: 90
```

## Troubleshooting

### "Integration not found"
- Verify the `marc_med_tracker` folder is in `custom_components`
- Restart Home Assistant
- Check logs: Settings → System → Logs

### "Invalid config"
- Verify YAML syntax (use a YAML validator)
- Check date format is YYYY-MM-DD
- Ensure all required fields are present

### Sensors not updating
- Check Developer Tools → States for the entity
- Verify the medication_id matches (lowercase, underscores)
- Look for errors in the logs

## Next Steps

1. **Add automations** - Use examples from `automations.yaml.example`
2. **Create dashboard** - Use examples from `lovelace.yaml.example`
3. **Set up notifications** - Configure mobile app notifications
4. **Test the workflow** - Take a dose, check the count updates

## Support

For issues or questions:
- Check the README.md for detailed documentation
- Review example files for usage patterns
- Check Home Assistant logs for errors
