#!/usr/bin/env python3
"""Validate manifest.json file."""

import json
import sys
from pathlib import Path


def validate_manifest():
    """Validate the manifest.json file."""
    manifest_path = Path("marc_med_tracker/manifest.json")
    
    if not manifest_path.exists():
        print(f"❌ Error: {manifest_path} not found")
        return False
    
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in manifest.json: {e}")
        return False
    
    # Required fields
    required_fields = [
        "domain",
        "name",
        "version",
        "documentation",
        "requirements",
        "dependencies",
        "codeowners",
    ]
    
    missing_fields = [field for field in required_fields if field not in manifest]
    if missing_fields:
        print(f"❌ Error: Missing required fields: {', '.join(missing_fields)}")
        return False
    
    # Validate domain
    if manifest["domain"] != "marc_med_tracker":
        print(f"❌ Error: Domain must be 'marc_med_tracker', got '{manifest['domain']}'")
        return False
    
    # Validate version format
    version = manifest["version"]
    try:
        parts = version.split(".")
        if len(parts) != 3:
            raise ValueError("Version must have 3 parts")
        for part in parts:
            int(part)
    except (ValueError, AttributeError) as e:
        print(f"❌ Error: Invalid version format '{version}': {e}")
        return False
    
    # Validate Home Assistant requirement
    if "homeassistant" in manifest:
        ha_version = manifest["homeassistant"]
        print(f"✓ Home Assistant requirement: {ha_version}")
    
    print("✅ manifest.json is valid")
    print(f"   Domain: {manifest['domain']}")
    print(f"   Name: {manifest['name']}")
    print(f"   Version: {manifest['version']}")
    
    return True


if __name__ == "__main__":
    sys.exit(0 if validate_manifest() else 1)
