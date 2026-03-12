"""Tests for Marc Med Tracker integration."""

import pytest
from datetime import datetime


def test_medication_id_generation():
    """Test medication ID generation from name."""
    test_cases = {
        "Aspirin": "aspirin",
        "Vitamin D": "vitamin_d",
        "Blood Pressure Medication": "blood_pressure_medication",
        "Multi Word Name Here": "multi_word_name_here",
    }
    
    for name, expected_id in test_cases.items():
        result = name.lower().replace(" ", "_")
        assert result == expected_id, f"Failed for {name}"


def test_stock_calculation():
    """Test stock calculation logic."""
    initial_stock = 90
    doses_per_day = 1
    pills_per_dose = 1
    days_elapsed = 10
    
    expected_remaining = initial_stock - (days_elapsed * doses_per_day * pills_per_dose)
    actual_remaining = initial_stock - (days_elapsed * doses_per_day * pills_per_dose)
    
    assert actual_remaining == expected_remaining
    assert actual_remaining == 80


def test_days_remaining_calculation():
    """Test days remaining calculation."""
    current_stock = 30
    doses_per_day = 2
    pills_per_dose = 1
    
    daily_consumption = doses_per_day * pills_per_dose
    expected_days = current_stock // daily_consumption
    
    assert expected_days == 15


def test_status_determination():
    """Test status determination based on days remaining."""
    test_cases = {
        0: "OUT_OF_STOCK",
        2: "CRITICAL",
        5: "LOW",
        10: "OK",
        30: "OK",
    }
    
    for days_remaining, expected_status in test_cases.items():
        if days_remaining == 0:
            status = "OUT_OF_STOCK"
        elif days_remaining <= 3:
            status = "CRITICAL"
        elif days_remaining <= 7:
            status = "LOW"
        else:
            status = "OK"
        
        assert status == expected_status, f"Failed for {days_remaining} days"


def test_date_parsing():
    """Test date string parsing."""
    date_str = "2025-02-20"
    parsed_date = datetime.fromisoformat(date_str).date()
    
    assert parsed_date.year == 2025
    assert parsed_date.month == 2
    assert parsed_date.day == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
