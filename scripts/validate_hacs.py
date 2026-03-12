#!/usr/bin/env python3
"""Validate HACS compatibility."""

import json
import sys
from pathlib import Path


def validate_hacs():
    """Validate HACS configuration and structure."""
    errors = []
    warnings = []
    
    # Check hacs.json exists
    hacs_json = Path("hacs.json")
    if not hacs_json.exists():
        errors.append("❌ hacs.json not found")
        return False
    
    # Validate hacs.json content
    try:
        with open(hacs_json) as f:
            hacs_config = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"❌ Invalid JSON in hacs.json: {e}")
        return False
    
    # Check required fields
    required_fields = ["name", "domains"]
    for field in required_fields:
        if field not in hacs_config:
            errors.append(f"❌ Missing required field in hacs.json: {field}")
    
    # Check optional but recommended fields
    recommended_fields = ["homeassistant", "render_readme"]
    for field in recommended_fields:
        if field not in hacs_config:
            warnings.append(f"⚠️  Recommended field missing in hacs.json: {field}")
    
    # Validate domains match integration folder
    if "domains" in hacs_config:
        domain = hacs_config["domains"][0] if hacs_config["domains"] else None
        
        # For content_in_root: true, check files are in root
        if hacs_config.get("content_in_root", False):
            if not Path("__init__.py").exists():
                errors.append("❌ __init__.py not found in root (content_in_root: true)")
            if not Path("manifest.json").exists():
                errors.append("❌ manifest.json not found in root (content_in_root: true)")
        else:
            # For content_in_root: false, check domain folder
            for domain in hacs_config["domains"]:
                domain_folder = Path(domain)
                if not domain_folder.exists():
                    errors.append(f"❌ Domain folder not found: {domain}")
                else:
                    if not (domain_folder / "__init__.py").exists():
                        errors.append(f"❌ {domain}/__init__.py not found")
                    if not (domain_folder / "manifest.json").exists():
                        errors.append(f"❌ {domain}/manifest.json not found")
    
    # Check info.md exists
    if not Path("info.md").exists():
        errors.append("❌ info.md not found (required for HACS)")
    
    # Check README exists
    if not Path("README.md").exists():
        errors.append("❌ README.md not found")
    
    # Check LICENSE exists
    if not Path("LICENSE").exists():
        errors.append("❌ LICENSE not found")
    
    # Validate manifest.json version
    manifest_path = Path("manifest.json")
    if manifest_path.exists():
        try:
            with open(manifest_path) as f:
                manifest = json.load(f)
            
            # Check version format
            version = manifest.get("version")
            if version:
                parts = version.split(".")
                if len(parts) != 3:
                    errors.append(f"❌ Invalid version format in manifest.json: {version}")
                
                # Validate domain matches
                manifest_domain = manifest.get("domain")
                domain = hacs_config.get("domains", [None])[0]
                if manifest_domain != domain:
                    errors.append(f"❌ Domain mismatch: manifest={manifest_domain}, hacs.json={domain}")
            else:
                errors.append("❌ No version in manifest.json")
        except json.JSONDecodeError as e:
            errors.append(f"❌ Invalid JSON in manifest.json: {e}")
    else:
        errors.append("❌ manifest.json not found")
    
    # Print results
    print("=" * 60)
    print("HACS VALIDATION REPORT")
    print("=" * 60)
    
    if not errors and not warnings:
        print("\n✅ ALL CHECKS PASSED")
        print("\n📦 HACS Configuration:")
        print(f"   Name: {hacs_config.get('name')}")
        print(f"   Domains: {', '.join(hacs_config.get('domains', []))}")
        print(f"   Min HA Version: {hacs_config.get('homeassistant', 'Not specified')}")
        print("\n✨ Ready for HACS deployment!")
        return True
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   {warning}")
    
    if errors:
        print("\n❌ ERRORS:")
        for error in errors:
            print(f"   {error}")
        print("\n🔧 Please fix the errors above before deploying to HACS")
        return False
    
    return True


if __name__ == "__main__":
    success = validate_hacs()
    sys.exit(0 if success else 1)
