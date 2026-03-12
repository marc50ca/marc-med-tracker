"""
Marc Med Tracker Binary Sensor Platform

Creates binary sensors for tracking daily doses - shows red when not taken, green when taken.
Automatically resets at midnight.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "marc_med_tracker"

# Dose times configuration
DOSE_TIMES = {
    "morning": {"name": "Morning Pills", "icon": "mdi:weather-sunset-up", "time": "08:00"},
    "lunch": {"name": "Lunch Pills", "icon": "mdi:weather-sunny", "time": "12:00"},
    "evening": {"name": "Evening Pills", "icon": "mdi:weather-sunset-down", "time": "20:00"},
    "morning_puffer": {"name": "Morning Puffer", "icon": "mdi:spray", "time": "08:00"},
    "evening_puffer": {"name": "Evening Puffer", "icon": "mdi:spray", "time": "20:00"},
}


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the medication tracker binary sensors."""
    sensors = []
    
    for dose_id, dose_info in DOSE_TIMES.items():
        sensors.append(MedicationDoseTracker(hass, dose_id, dose_info))
    
    async_add_entities(sensors, True)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up medication tracker binary sensors from config entry."""
    sensors = []
    
    for dose_id, dose_info in DOSE_TIMES.items():
        sensors.append(MedicationDoseTracker(hass, dose_id, dose_info))
    
    async_add_entities(sensors, True)


class MedicationDoseTracker(BinarySensorEntity):
    """Representation of a daily dose tracker that resets at midnight."""
    
    _attr_has_entity_name = False
    
    def __init__(self, hass: HomeAssistant, dose_id: str, dose_info: dict[str, str]) -> None:
        """Initialize the binary sensor."""
        self.hass = hass
        self._dose_id = dose_id
        self._dose_info = dose_info
        self._attr_name = f"Marc Med {dose_info['name']}"
        self._attr_unique_id = f"{DOMAIN}_dose_{dose_id}"
        self._state = False
        self._last_taken = None
        
        # Load state from storage if available
        if DOMAIN in hass.data and "dose_tracking" in hass.data[DOMAIN]:
            stored_data = hass.data[DOMAIN]["dose_tracking"].get(dose_id, {})
            last_taken_str = stored_data.get("last_taken")
            
            if last_taken_str:
                last_taken = datetime.fromisoformat(last_taken_str)
                # Only restore state if it was taken today
                if last_taken.date() == datetime.now().date():
                    self._state = True
                    self._last_taken = last_taken
    
    @property
    def is_on(self) -> bool:
        """Return true if the dose has been taken today."""
        # Check if we need to reset (new day)
        if self._last_taken and self._last_taken.date() < datetime.now().date():
            self._state = False
            self._last_taken = None
        return self._state
    
    @property
    def icon(self) -> str:
        """Return the icon - changes based on state."""
        if self.is_on:
            return f"{self._dose_info['icon']}-check"
        return self._dose_info['icon']
    
    @property
    def device_class(self) -> str | None:
        """Return the device class."""
        return None
    
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        attrs = {
            "dose_type": self._dose_id,
            "dose_name": self._dose_info['name'],
            "scheduled_time": self._dose_info['time'],
            "taken_today": self.is_on,
            "last_taken": self._last_taken.isoformat() if self._last_taken else None,
        }
        
        if self._last_taken:
            attrs["taken_at"] = self._last_taken.strftime("%I:%M %p")
            attrs["minutes_ago"] = int((datetime.now() - self._last_taken).total_seconds() / 60)
        
        return attrs
    
    async def async_turn_on(self, **kwargs) -> None:
        """Mark the dose as taken."""
        self._state = True
        self._last_taken = datetime.now()
        
        # Save to storage
        if DOMAIN not in self.hass.data:
            self.hass.data[DOMAIN] = {}
        if "dose_tracking" not in self.hass.data[DOMAIN]:
            self.hass.data[DOMAIN]["dose_tracking"] = {}
        
        self.hass.data[DOMAIN]["dose_tracking"][self._dose_id] = {
            "last_taken": self._last_taken.isoformat(),
            "state": True
        }
        
        # Save to persistent storage
        if "store" in self.hass.data[DOMAIN]:
            await self.hass.data[DOMAIN]["store"].async_save(self.hass.data[DOMAIN])
        
        self.async_write_ha_state()
        
        # Fire event for automations
        self.hass.bus.async_fire(
            f"{DOMAIN}_dose_checked",
            {"dose_id": self._dose_id, "dose_name": self._dose_info['name']}
        )
        
        _LOGGER.info(f"Marked {self._dose_info['name']} as taken")
    
    async def async_turn_off(self, **kwargs) -> None:
        """Mark the dose as not taken (for corrections)."""
        self._state = False
        self._last_taken = None
        
        # Update storage
        if DOMAIN in self.hass.data and "dose_tracking" in self.hass.data[DOMAIN]:
            self.hass.data[DOMAIN]["dose_tracking"][self._dose_id] = {
                "last_taken": None,
                "state": False
            }
            
            if "store" in self.hass.data[DOMAIN]:
                await self.hass.data[DOMAIN]["store"].async_save(self.hass.data[DOMAIN])
        
        self.async_write_ha_state()
        _LOGGER.info(f"Unmarked {self._dose_info['name']}")
    
    async def async_update(self) -> None:
        """Update the sensor state."""
        # Check if we need to reset for a new day
        if self._last_taken and self._last_taken.date() < datetime.now().date():
            self._state = False
            self._last_taken = None
            self.async_write_ha_state()
