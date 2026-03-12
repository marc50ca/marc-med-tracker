#!/usr/bin/env python3
"""Validate services.yaml file."""

import sys
from pathlib import Path
import yaml


def validate_services():
    """Validate the services.yaml file."""
    services_path = Path("marc_med_tracker/services.yaml")
    
    if not services_path.exists():
        print(f"❌ Error: {services_path} not found")
        return False
    
    try:
        with open(services_path) as f:
            services = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ Error: Invalid YAML in services.yaml: {e}")
        return False
    
    # Expected services
    expected_services = [
        "take_dose",
        "refill",
        "update_refills",
        "check_off_dose",
        "uncheck_dose",
        "update_doctor",
        "update_stock",
    ]
    
    if not isinstance(services, dict):
        print("❌ Error: services.yaml must be a dictionary")
        return False
    
    # Check all expected services exist
    missing_services = [s for s in expected_services if s not in services]
    if missing_services:
        print(f"❌ Error: Missing services: {', '.join(missing_services)}")
        return False
    
    # Validate each service has required fields
    for service_name, service_def in services.items():
        if "name" not in service_def:
            print(f"❌ Error: Service '{service_name}' missing 'name' field")
            return False
        
        if "description" not in service_def:
            print(f"❌ Error: Service '{service_name}' missing 'description' field")
            return False
        
        print(f"✓ Service '{service_name}' is valid")
    
    print(f"\n✅ services.yaml is valid")
    print(f"   Found {len(services)} services")
    
    return True


if __name__ == "__main__":
    sys.exit(0 if validate_services() else 1)
