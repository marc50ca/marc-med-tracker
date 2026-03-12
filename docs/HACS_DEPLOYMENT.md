# HACS Deployment Guide

## For Users: Installing via HACS

### Prerequisites
- Home Assistant installed
- HACS installed ([Get HACS](https://hacs.xyz/))

### Installation Steps

1. **Open HACS**
   - Go to HACS in your Home Assistant sidebar

2. **Add Custom Repository** (if not in default)
   - Click on Integrations
   - Click the ⋮ (three dots) menu
   - Select "Custom repositories"
   - Enter repository URL: `https://github.com/yourusername/marc-med-tracker`
   - Category: Integration
   - Click Add

3. **Install Integration**
   - Search for "Marc Med Tracker"
   - Click on it
   - Click "Download"
   - Select latest version
   - Click "Download"

4. **Configure**
   - Add to `configuration.yaml`:
   ```yaml
   marc_med_tracker:
     medications:
       - name: "Aspirin"
         prescribing_doctor: "Dr. Smith"
         refills_left: 3
         last_refilled: "2025-02-20"
         strength: "100mg"
         doses_per_day: 1
         pills_per_dose: 1
         initial_stock: 90
   ```

5. **Restart Home Assistant**
   - Settings → System → Restart

6. **Verify Installation**
   - Developer Tools → States
   - Search for: `marc_med_`
   - Should see sensors and binary sensors

### Updates

HACS will notify you when updates are available:
1. Go to HACS → Integrations
2. Find "Marc Med Tracker"
3. Click "Update" when available
4. Restart Home Assistant

---

## For Developers: Preparing for HACS

### Repository Requirements

✅ **Required Files** (All Present)
- `hacs.json` - HACS configuration
- `info.md` - HACS info page
- `README.md` - Main documentation
- `LICENSE` - MIT License
- Custom component in `marc_med_tracker/`
- `manifest.json` with proper version

✅ **File Structure** (Correct for HACS)
```
marc-med-tracker/             # Repository root
├── __init__.py               # Integration code (in root!)
├── sensor.py
├── binary_sensor.py
├── manifest.json
├── services.yaml
├── hacs.json                 # HACS config
├── info.md                   # HACS info page
├── README.md                 # Documentation
├── LICENSE                   # MIT License
├── docs/                     # Documentation folder
├── examples/                 # Example configs
└── .github/workflows/        # CI/CD workflows
```

**Important**: HACS requires `content_in_root: true` with integration files at repository root.
Users install it, and HACS automatically places files in `/config/custom_components/marc_med_tracker/`

### Submitting to HACS Default

1. **Prepare Repository**
   - Ensure all files are present
   - Version in `manifest.json` matches git tag
   - README is comprehensive
   - Examples are included

2. **Create Release**
   ```bash
   git tag v2.0.0
   git push origin v2.0.0
   ```

3. **Submit to HACS**
   - Go to https://github.com/hacs/default
   - Fork the repository
   - Add your repo to `integration` file:
   ```
   yourusername/marc-med-tracker
   ```
   - Create Pull Request
   - Wait for review

4. **HACS Review Process**
   - HACS team reviews repository
   - Ensures requirements are met
   - May request changes
   - Once approved, appears in HACS default

### Validation Checklist

Before submitting to HACS, verify:

- [ ] Repository is public
- [ ] `hacs.json` is valid
- [ ] `info.md` exists and is formatted
- [ ] `manifest.json` has correct version
- [ ] Integration domain matches folder name
- [ ] README has installation instructions
- [ ] LICENSE file exists (MIT)
- [ ] Repository has releases with tags
- [ ] Examples folder exists
- [ ] No hardcoded paths or secrets
- [ ] Code follows Home Assistant standards

### Testing Locally

Test HACS compatibility:

```bash
# 1. Validate hacs.json
python -m json.tool hacs.json

# 2. Check manifest
python scripts/validate_manifest.py

# 3. Validate structure
ls -la marc_med_tracker/

# 4. Test installation
# Add as custom repository in HACS
# Install and verify
```

### HACS Configuration Explained

**hacs.json**:
```json
{
  "name": "Marc Med Tracker",           // Display name in HACS
  "content_in_root": false,             // Integration is in subfolder
  "render_readme": true,                // Show README in HACS
  "domains": ["marc_med_tracker"],      // Integration domain
  "country": ["US", "CA", "GB", ...],   // Supported countries
  "homeassistant": "2024.1.0",          // Minimum HA version
  "iot_class": "calculated",            // Device classification
  "zip_release": true,                  // Use release assets
  "filename": "marc-med-tracker.zip"    // Release asset name
}
```

### Release Asset Creation

GitHub Actions automatically creates releases:

```yaml
# .github/workflows/release.yml
on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Create Release
        # Creates marc-med-tracker.zip
```

Manual release:
```bash
# Create release archive
make release

# Upload to GitHub release
# Attach marc-med-tracker.zip to release
```

### Version Management

1. **Update Version**
   - Edit `marc_med_tracker/manifest.json`
   - Update `version` field
   - Update `CHANGELOG.md`

2. **Create Tag**
   ```bash
   git add marc_med_tracker/manifest.json CHANGELOG.md
   git commit -m "Bump version to 2.0.1"
   git tag v2.0.1
   git push origin main --tags
   ```

3. **GitHub Actions**
   - Automatically creates release
   - Builds and attaches zip file
   - HACS detects new version

### Troubleshooting HACS Issues

**"Repository structure not compliant"**
- Ensure `marc_med_tracker/` folder exists
- Check `manifest.json` is present
- Verify `hacs.json` is valid JSON

**"Version mismatch"**
- Version in `manifest.json` must match git tag
- Remove 'v' prefix in manifest: `2.0.0` not `v2.0.0`

**"Integration not loading"**
- Check `manifest.json` domain matches folder name
- Verify all required files are present
- Check logs for errors

**"Updates not showing"**
- Ensure new tag is created
- Wait a few minutes for HACS to detect
- Try clearing HACS cache

### Best Practices

1. **Semantic Versioning**
   - MAJOR.MINOR.PATCH (2.0.0)
   - Breaking changes: Increment MAJOR
   - New features: Increment MINOR
   - Bug fixes: Increment PATCH

2. **Release Notes**
   - Update CHANGELOG.md for every release
   - List all changes clearly
   - Include upgrade instructions if needed

3. **Testing**
   - Test installation via HACS before submitting
   - Verify on fresh Home Assistant install
   - Test updates from previous versions

4. **Documentation**
   - Keep README updated
   - Include screenshots
   - Provide troubleshooting section
   - Link to detailed docs

### HACS Categories

This integration qualifies for:
- ✅ **Integration** - Custom component for HA
- ❌ Plugin - Not a Lovelace plugin
- ❌ Theme - Separate theme file included but not primary
- ❌ Python Script - Not a Python script

### Resources

- [HACS Documentation](https://hacs.xyz/docs/)
- [HACS Integration Requirements](https://hacs.xyz/docs/publish/integration)
- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [HACS Default Repository](https://github.com/hacs/default)

---

## Quick Reference

### User Installation
```
HACS → Integrations → + → Search "Marc Med Tracker" → Download
```

### Developer Release
```bash
# 1. Update version in manifest.json
# 2. Update CHANGELOG.md
# 3. Commit and tag
git commit -m "Release v2.0.1"
git tag v2.0.1
git push origin main --tags
# 4. GitHub Actions creates release
```

### File Locations
- Integration: `marc_med_tracker/`
- HACS Config: `hacs.json`
- HACS Info: `info.md`
- Main Docs: `README.md`
- Examples: `examples/`

---

**Status**: ✅ Ready for HACS deployment
