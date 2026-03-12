# Marc Med Tracker v2.0.0 - Upgrade Notes

## What Changed in Version 2.0.0

This release updates Marc Med Tracker to be fully compatible with **Home Assistant 2025.2** and future versions, while maintaining backward compatibility with your existing configuration.

## Code Modernization

### Type Hints Updated
**Before (v1.0):**
```python
from typing import Dict, Optional
def my_function(data: Dict[str, Any]) -> Optional[str]:
```

**After (v2.0):**
```python
from __future__ import annotations
def my_function(data: dict[str, Any]) -> str | None:
```

### Modern Imports
- Added `from __future__ import annotations` for better performance
- Updated to use `ConfigType` and `DiscoveryInfoType` from helpers
- Removed deprecated `dt_util` imports
- Updated to modern callback decorators

### Entity Properties
- Added `_attr_has_entity_name = False` to all entities (preserves current naming)
- Updated property type hints to use pipe notation (`str | None`)
- Modernized attribute dictionaries

### Manifest Updates
- Changed `iot_class` from `local_polling` to `calculated` (more accurate)
- Added explicit `homeassistant` minimum version requirement
- Bumped version to 2.0.0

## What You Need to Do

### If Installing Fresh
Nothing special - just install as normal. Works with HA 2024.1.0+

### If Upgrading from v1.0
**Good news**: No configuration changes needed!

1. **Your current config works as-is**
   - No changes to `configuration.yaml` required
   - Entity IDs stay the same
   - Service calls unchanged
   - All data preserved

2. **Just replace the files**
   ```bash
   # Backup (optional but recommended)
   cp -r /config/custom_components/marc_med_tracker /config/marc_med_tracker.backup
   
   # Replace with new version
   rm -rf /config/custom_components/marc_med_tracker
   unzip med-tracker.zip
   cp -r med-tracker/marc_med_tracker /config/custom_components/
   
   # Restart
   ha core restart
   ```

3. **Verify it worked**
   - Check Settings → System → Logs for errors
   - Confirm all entities still exist
   - Test a service call

## Benefits of Upgrading

### For Current HA Versions (2024.x - 2025.2)
- ✅ Eliminates deprecation warnings
- ✅ Better type checking and IDE support
- ✅ Improved code maintainability
- ✅ Future-proof for upcoming HA versions

### For Future HA Versions (2025.3+)
- ✅ Ready for any upcoming type system changes
- ✅ Follows current best practices
- ✅ Won't break when old patterns are removed

## Technical Details

### Files Changed
1. `__init__.py` - Updated imports and type hints
2. `sensor.py` - Modern typing, added entity properties
3. `binary_sensor.py` - Modern typing, added entity properties
4. `manifest.json` - Updated metadata and requirements

### Files Added
1. `COMPATIBILITY.md` - Version compatibility matrix
2. `UPGRADE_NOTES.md` - This file

### No Changes To
- Service definitions (`services.yaml`)
- Configuration schema
- Entity naming
- Data storage format
- Dashboard configurations
- Automation examples

## Compatibility

| Component | v1.0 | v2.0 |
|-----------|------|------|
| Home Assistant | 2023.1+ | 2024.1+ |
| Python | 3.10+ | 3.11+ |
| Configuration | Same | Same |
| Entity IDs | Same | Same |
| Data Format | Same | Same |

## Breaking Changes

**None!** This is a non-breaking upgrade focused on modernization.

## Rollback Instructions

If you need to go back to v1.0:

1. Restore backup:
   ```bash
   rm -rf /config/custom_components/marc_med_tracker
   cp -r /config/marc_med_tracker.backup /config/custom_components/marc_med_tracker
   ha core restart
   ```

2. Or reinstall v1.0 files from your archive

All data is preserved - storage format hasn't changed.

## Testing Recommendations

After upgrading, test:

1. **Entity states** - Verify all sensors show correct values
2. **Service calls** - Test take_dose, refill, update_doctor
3. **Daily tracking** - Toggle dose buttons
4. **Automations** - Ensure automations still trigger
5. **Dashboards** - Check all cards render properly

## Support

If you encounter issues after upgrading:

1. Check the logs: Settings → System → Logs
2. Look for entries containing "marc_med_tracker"
3. Common issues:
   - **Import errors**: Verify HA version is 2024.1+
   - **Entities missing**: Did files copy correctly?
   - **Service errors**: Restart HA again

4. If problems persist, you can safely roll back (see above)

## Questions?

- **"Do I have to upgrade?"** - No, v1.0 still works, but v2.0 is recommended
- **"Will my data be lost?"** - No, data format is unchanged
- **"Can I skip versions?"** - Yes, you can go directly from v1.0 to v2.0
- **"When should I upgrade?"** - Anytime, but especially before HA 2026+

## Summary

✅ **Safe**: Non-breaking, backward compatible  
✅ **Easy**: Drop-in replacement, no config changes  
✅ **Beneficial**: Future-proof, eliminates warnings  
✅ **Reversible**: Can roll back if needed  

**Recommendation**: Upgrade when convenient. Not urgent, but good to do.
