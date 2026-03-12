# Marc Med Tracker - Repository Structure

## HACS-Compliant Layout

This repository follows HACS integration standards with `content_in_root: true`.

```
marc-med-tracker/                          # Repository root
│
├── 📦 Integration Files (Root Level - HACS requirement)
│   ├── __init__.py                       # Main integration setup, service handlers
│   ├── sensor.py                         # Medication inventory sensors
│   ├── binary_sensor.py                  # Daily dose tracking (red/green buttons)
│   ├── manifest.json                     # Integration metadata (domain, version)
│   └── services.yaml                     # 7 service definitions
│
├── 🎯 HACS Configuration
│   ├── hacs.json                         # HACS metadata (content_in_root: true)
│   └── info.md                           # HACS store info page
│
├── 📚 Documentation (docs/)
│   ├── HACS_QUICK_START.md               # 7-minute HACS installation
│   ├── HACS_DEPLOYMENT.md                # For developers
│   ├── DASHBOARD_SETUP.md                # Beautiful dashboard guide
│   └── ... (13 total documentation files)
│
├── 📋 Examples (examples/)
│   ├── dashboard_beautiful_simple.yaml   # Recommended dashboard
│   ├── configuration.yaml.example        # Config template
│   └── ... (12 example files)
│
└── 🛠️ Development Files
    ├── .github/workflows/                # CI/CD automation
    ├── scripts/                          # Validation scripts
    ├── tests/                            # Unit tests
    ├── Makefile                          # Dev commands
    └── README.md                         # Main docs
```

## Installation Paths

### HACS Installation (Automatic)
HACS automatically places files in:
```
/config/custom_components/marc_med_tracker/
├── __init__.py
├── sensor.py
├── binary_sensor.py
├── manifest.json
└── services.yaml
```

### Manual Installation
Copy root-level Python files to the above path.

## Key Structure Notes

**Why `content_in_root: true`?**
- HACS requirement for integrations
- Integration files (*.py, manifest.json) must be in repository root
- HACS handles copying to correct custom_components path

**User Installation:**
1. HACS downloads from GitHub
2. Finds files in root (content_in_root: true)
3. Installs to /config/custom_components/marc_med_tracker/
4. User restarts HA
5. Ready to use!

---

**HACS Compliant:** ✅ Validated  
**Structure Type:** `content_in_root: true`  
**Total Files:** 60+  
**Package Size:** ~107KB
