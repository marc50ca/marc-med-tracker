# Marc Med Tracker - Version History & Compatibility

## Version 2.0.0 (Current)

### Home Assistant Compatibility
- **Minimum Version**: Home Assistant 2024.1.0
- **Tested Up To**: Home Assistant 2025.2.x
- **Recommended**: Home Assistant 2024.11.0 or later

### What's New in 2.0.0

#### Modern Home Assistant Compatibility
- ✅ Updated to use modern type hints (`dict[str, Any]` instead of `Dict[str, Any]`)
- ✅ Added `from __future__ import annotations` for better type support
- ✅ Updated imports to use `ConfigType` and `DiscoveryInfoType`
- ✅ Added `_attr_has_entity_name = False` to entities
- ✅ Updated IoT class from `local_polling` to `calculated` (more accurate)
- ✅ Added explicit Home Assistant version requirement in manifest

#### Features
- Update prescribing doctor names via service call
- Daily dose tracking with red/green buttons
- Automated inventory management
- Comprehensive medication details panel
- Multiple dashboard configurations
- Extensive automation examples

### Breaking Changes
None - fully backward compatible with configuration files

### Migration Notes
If upgrading from version 1.x:
- No configuration changes required
- All existing data will be preserved
- Service names remain the same
- Entity IDs remain unchanged

## Version 1.0.0 (Initial Release)

### Features
- Basic medication tracking
- Inventory management
- Refill tracking
- Daily dose buttons
- Details panels
- Automation support

## Compatibility Matrix

| Marc Med Tracker Version | Min HA Version | Max Tested HA Version | Notes |
|--------------------|----------------|----------------------|-------|
| 2.0.0 | 2024.1.0 | 2025.2.x | Current, recommended |
| 1.0.0 | 2023.1.0 | 2024.12.x | Legacy, deprecated |

## Python Version Support

- **Python 3.11**: ✅ Fully supported
- **Python 3.12**: ✅ Fully supported
- **Python 3.13**: ✅ Should work (not officially tested)
- **Python 3.10 or earlier**: ❌ Not supported

## Known Issues & Workarounds

### Home Assistant 2024.1.x to 2024.6.x
**Issue**: Some users may see deprecation warnings about Dict/Optional imports
**Workaround**: These are cosmetic only and don't affect functionality. Update to version 2.0.0.

### Home Assistant 2023.x
**Issue**: Version 2.0.0 may not work correctly
**Workaround**: Use version 1.0.0 or upgrade Home Assistant to 2024.1+

## Updating the Integration

### From 1.x to 2.0

1. **Backup your configuration**
   ```bash
   cp /config/configuration.yaml /config/configuration.yaml.backup
   ```

2. **Stop Home Assistant**
   ```bash
   ha core stop
   ```

3. **Replace the integration files**
   ```bash
   rm -rf /config/custom_components/marc_med_tracker
   # Extract new version
   unzip med-tracker.zip
   cp -r med-tracker/marc_med_tracker /config/custom_components/
   ```

4. **Start Home Assistant**
   ```bash
   ha core start
   ```

5. **Verify**
   - Check Settings → System → Logs for any errors
   - Verify all entities are present
   - Test a service call

### Rolling Back

If you need to revert to version 1.0:
1. Stop Home Assistant
2. Replace `/config/custom_components/marc_med_tracker` with version 1.0 files
3. Restart Home Assistant

All data is preserved during version changes.

## Future Compatibility

### Upcoming Home Assistant Changes

**2025.3+**
- Expected to continue working without changes
- Integration follows current best practices

**2026.1+ (Future)**
- May require config flow migration (we'll update before then)
- Entity naming conventions may evolve

### Deprecation Timeline

We follow Home Assistant's deprecation policy:
- Features deprecated in HA core get 6 months notice minimum
- Breaking changes announced at least 2 releases in advance
- Legacy code supported until no longer functional

## Getting Help

If you encounter compatibility issues:

1. **Check your Home Assistant version**
   ```yaml
   # Settings → System → About
   # Or in terminal:
   ha core info
   ```

2. **Check the logs**
   ```
   Settings → System → Logs
   # Look for errors containing "marc_med_tracker"
   ```

3. **Common Issues**
   - "Integration not found" → Wrong directory or HA needs restart
   - "Invalid config" → YAML syntax error in configuration.yaml
   - Import errors → Home Assistant version too old

4. **Report Issues**
   - Include your Home Assistant version
   - Include relevant log entries
   - Describe what you were trying to do

## Testing New Home Assistant Versions

If you want to test compatibility with beta/dev versions:

1. **Create a backup first**
2. **Enable debug logging**
   ```yaml
   logger:
     default: info
     logs:
       custom_components.marc_med_tracker: debug
   ```
3. **Test all features**
   - Service calls
   - Dashboard rendering
   - Automations
   - Data persistence

4. **Report findings** so we can update compatibility info

## Version Support Policy

- **Current version (2.0.x)**: Full support, active development
- **Previous version (1.0.x)**: Security fixes only, no new features
- **Older versions**: No support, upgrade recommended

## Changelog Format

We follow [Semantic Versioning](https://semver.org/):
- **Major** (2.0.0): Breaking changes, significant rewrites
- **Minor** (2.1.0): New features, backward compatible
- **Patch** (2.0.1): Bug fixes, no new features

## Development Status

- **Stability**: Production ready
- **Maintenance**: Active
- **Breaking Changes**: Only with major version bumps
- **Deprecations**: Announced at least 6 months in advance
