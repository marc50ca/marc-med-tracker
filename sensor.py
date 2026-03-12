"""
Marc Med Tracker Sensor Platform

Creates sensors for each medication showing current stock and status.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "marc_med_tracker"


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the medication tracker sensors."""
    medications = hass.data[DOMAIN]["medications"]
    
    sensors = []
    for med_id, medication in medications.items():
        sensors.append(MedicationSensor(hass, med_id, medication))
    
    async_add_entities(sensors, True)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up medication tracker sensors from config entry."""
    medications = hass.data[DOMAIN]["medications"]
    
    sensors = []
    for med_id, medication in medications.items():
        sensors.append(MedicationSensor(hass, med_id, medication))
    
    async_add_entities(sensors, True)


class MedicationSensor(SensorEntity):
    """Representation of a Medication Sensor."""
    
    _attr_has_entity_name = False
    
    def __init__(self, hass: HomeAssistant, med_id: str, medication: dict[str, Any]) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self._med_id = med_id
        self._medication = medication
        self._attr_name = f"Marc Med {medication['name']}"
        self._attr_unique_id = f"{DOMAIN}_{med_id}"
        self._state = None
        self._update_state()
    
    @property
    def native_value(self) -> int:
        """Return the state of the sensor."""
        return self._medication.get("current_stock", 0)
    
    @property
    def native_unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "pills"
    
    @property
    def icon(self) -> str:
        """Return the icon to use in the frontend."""
        current_stock = self._medication.get("current_stock", 0)
        days_remaining = self._calculate_days_remaining()
        
        if current_stock == 0:
            return "mdi:pill-off"
        elif days_remaining <= 7:
            return "mdi:pill-alert"
        else:
            return "mdi:pill"
    
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        days_remaining = self._calculate_days_remaining()
        last_refilled = self._medication.get("last_refilled")
        
        if isinstance(last_refilled, str):
            last_refilled_date = datetime.fromisoformat(last_refilled).date()
        else:
            last_refilled_date = last_refilled
        
        days_since_refill = (datetime.now().date() - last_refilled_date).days
        
        return {
            "medication_name": self._medication.get("name"),
            "prescribing_doctor": self._medication.get("prescribing_doctor"),
            "strength": self._medication.get("strength"),
            "refills_left": self._medication.get("refills_left"),
            "last_refilled": last_refilled,
            "days_since_refill": days_since_refill,
            "doses_per_day": self._medication.get("doses_per_day"),
            "pills_per_dose": self._medication.get("pills_per_dose"),
            "initial_stock": self._medication.get("initial_stock"),
            "current_stock": self._medication.get("current_stock"),
            "days_remaining": days_remaining,
            "status": self._get_status(),
            "daily_consumption": self._medication.get("doses_per_day") * self._medication.get("pills_per_dose"),
            "needs_refill": days_remaining <= 7,
            "out_of_stock": self._medication.get("current_stock", 0) == 0,
            "notes": self._medication.get("notes", ""),
        }
    
    def _calculate_days_remaining(self) -> int:
        """Calculate days of medication remaining."""
        current_stock = self._medication.get("current_stock", 0)
        doses_per_day = self._medication.get("doses_per_day", 1)
        pills_per_dose = self._medication.get("pills_per_dose", 1)
        
        daily_consumption = doses_per_day * pills_per_dose
        
        if daily_consumption == 0:
            return 999
        
        return current_stock // daily_consumption
    
    def _get_status(self) -> str:
        """Get the current status of the medication."""
        current_stock = self._medication.get("current_stock", 0)
        days_remaining = self._calculate_days_remaining()
        refills_left = self._medication.get("refills_left", 0)
        
        if current_stock == 0:
            return "OUT_OF_STOCK"
        elif days_remaining <= 3:
            return "CRITICAL"
        elif days_remaining <= 7:
            return "LOW"
        elif days_remaining <= 14 and refills_left == 0:
            return "NO_REFILLS_LEFT"
        else:
            return "OK"
    
    def _update_state(self) -> None:
        """Update the internal state."""
        self._medication = self.hass.data[DOMAIN]["medications"][self._med_id]
    
    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        self._update_state()
