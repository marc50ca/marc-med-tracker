"""
Marc Med Tracker Integration for Home Assistant

This integration tracks medications including refills, dosage, and inventory.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.storage import Store
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "marc_med_tracker"
PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]

STORAGE_VERSION = 1
STORAGE_KEY = f"{DOMAIN}.medications"

# Configuration schema
MEDICATION_SCHEMA = vol.Schema({
    vol.Required("name"): cv.string,
    vol.Required("prescribing_doctor"): cv.string,
    vol.Required("refills_left"): cv.positive_int,
    vol.Required("last_refilled"): cv.date,
    vol.Required("strength"): cv.string,
    vol.Required("doses_per_day"): cv.positive_int,
    vol.Required("pills_per_dose"): cv.positive_int,
    vol.Required("initial_stock"): cv.positive_int,
    vol.Optional("notes"): cv.string,
})

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema({
            vol.Required("medications"): vol.All(cv.ensure_list, [MEDICATION_SCHEMA])
        })
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Medication Tracker component."""
    hass.data[DOMAIN] = {}
    
    if DOMAIN not in config:
        return True
    
    # Initialize storage
    store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
    stored_data = await store.async_load()
    
    if stored_data is None:
        stored_data = {"medications": {}, "dose_tracking": {}}
    
    hass.data[DOMAIN]["store"] = store
    hass.data[DOMAIN]["medications"] = stored_data.get("medications", {})
    hass.data[DOMAIN]["dose_tracking"] = stored_data.get("dose_tracking", {})
    
    # Load medications from configuration
    for med_config in config[DOMAIN]["medications"]:
        med_id = med_config["name"].lower().replace(" ", "_")
        
        # Calculate current stock
        last_refilled = med_config["last_refilled"]
        if isinstance(last_refilled, str):
            last_refilled = datetime.fromisoformat(last_refilled).date()
        
        days_since_refill = (datetime.now().date() - last_refilled).days
        pills_consumed = days_since_refill * med_config["doses_per_day"] * med_config["pills_per_dose"]
        current_stock = max(0, med_config["initial_stock"] - pills_consumed)
        
        hass.data[DOMAIN]["medications"][med_id] = {
            **med_config,
            "id": med_id,
            "last_refilled": last_refilled.isoformat(),
            "current_stock": current_stock,
        }
    
    await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
    
    # Register services
    async def handle_take_dose(call: ServiceCall) -> None:
        """Handle taking a dose of medication."""
        med_id = call.data.get("medication_id")
        doses = call.data.get("doses", 1)
        
        if med_id not in hass.data[DOMAIN]["medications"]:
            _LOGGER.error(f"Medication {med_id} not found")
            return
        
        medication = hass.data[DOMAIN]["medications"][med_id]
        pills_taken = doses * medication["pills_per_dose"]
        medication["current_stock"] = max(0, medication["current_stock"] - pills_taken)
        
        await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
        hass.bus.async_fire(f"{DOMAIN}_dose_taken", {"medication_id": med_id, "doses": doses})
        _LOGGER.info(f"Recorded {doses} dose(s) of {medication['name']}")
    
    async def handle_refill(call: ServiceCall) -> None:
        """Handle refilling a medication."""
        med_id = call.data.get("medication_id")
        pills = call.data.get("pills")
        
        if med_id not in hass.data[DOMAIN]["medications"]:
            _LOGGER.error(f"Medication {med_id} not found")
            return
        
        medication = hass.data[DOMAIN]["medications"][med_id]
        medication["current_stock"] += pills
        medication["last_refilled"] = datetime.now().date().isoformat()
        medication["refills_left"] = max(0, medication["refills_left"] - 1)
        
        await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
        hass.bus.async_fire(f"{DOMAIN}_refilled", {"medication_id": med_id, "pills": pills})
        _LOGGER.info(f"Refilled {medication['name']} with {pills} pills")
    
    async def handle_update_refills(call: ServiceCall) -> None:
        """Update the number of refills left."""
        med_id = call.data.get("medication_id")
        refills = call.data.get("refills")
        
        if med_id not in hass.data[DOMAIN]["medications"]:
            _LOGGER.error(f"Medication {med_id} not found")
            return
        
        medication = hass.data[DOMAIN]["medications"][med_id]
        medication["refills_left"] = refills
        
        await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
        _LOGGER.info(f"Updated refills for {medication['name']} to {refills}")
    
    async def handle_check_off_dose(call: ServiceCall) -> None:
        """Check off a daily dose (turn on the input_boolean helper)."""
        dose_id = call.data.get("dose_id")
        entity_id = f"input_boolean.marc_med_{dose_id}_helper"

        if hass.states.get(entity_id) is None:
            _LOGGER.error(f"Dose helper {entity_id} not found")
            return

        await hass.services.async_call(
            "input_boolean",
            "turn_on",
            {"entity_id": entity_id},
            blocking=True,
        )
        _LOGGER.info(f"Checked off dose: {dose_id}")

    async def handle_uncheck_dose(call: ServiceCall) -> None:
        """Uncheck a daily dose (turn off the input_boolean helper)."""
        dose_id = call.data.get("dose_id")
        entity_id = f"input_boolean.marc_med_{dose_id}_helper"

        if hass.states.get(entity_id) is None:
            _LOGGER.error(f"Dose helper {entity_id} not found")
            return

        await hass.services.async_call(
            "input_boolean",
            "turn_off",
            {"entity_id": entity_id},
            blocking=True,
        )
        _LOGGER.info(f"Unchecked dose: {dose_id}")
    
    async def handle_update_doctor(call: ServiceCall) -> None:
        """Update the prescribing doctor for a medication."""
        med_id = call.data.get("medication_id")
        doctor_name = call.data.get("doctor_name")
        
        if med_id not in hass.data[DOMAIN]["medications"]:
            _LOGGER.error(f"Medication {med_id} not found")
            return
        
        medication = hass.data[DOMAIN]["medications"][med_id]
        old_doctor = medication.get("prescribing_doctor", "Unknown")
        medication["prescribing_doctor"] = doctor_name
        
        await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
        hass.bus.async_fire(
            f"{DOMAIN}_doctor_updated",
            {
                "medication_id": med_id,
                "medication_name": medication["name"],
                "old_doctor": old_doctor,
                "new_doctor": doctor_name
            }
        )
        _LOGGER.info(f"Updated doctor for {medication['name']} from {old_doctor} to {doctor_name}")
    
    async def handle_update_stock(call: ServiceCall) -> None:
        """Update the current stock (pills on hand) for a medication."""
        med_id = call.data.get("medication_id")
        new_stock = call.data.get("pills")
        
        if med_id not in hass.data[DOMAIN]["medications"]:
            _LOGGER.error(f"Medication {med_id} not found")
            return
        
        medication = hass.data[DOMAIN]["medications"][med_id]
        old_stock = medication.get("current_stock", 0)
        medication["current_stock"] = new_stock
        
        await store.async_save({
        "medications": hass.data[DOMAIN]["medications"],
        "dose_tracking": hass.data[DOMAIN]["dose_tracking"],
    })
        hass.bus.async_fire(
            f"{DOMAIN}_stock_updated",
            {
                "medication_id": med_id,
                "medication_name": medication["name"],
                "old_stock": old_stock,
                "new_stock": new_stock,
                "difference": new_stock - old_stock
            }
        )
        _LOGGER.info(f"Updated stock for {medication['name']} from {old_stock} to {new_stock} pills")
    
    hass.services.async_register(DOMAIN, "take_dose", handle_take_dose)
    hass.services.async_register(DOMAIN, "refill", handle_refill)
    hass.services.async_register(DOMAIN, "update_refills", handle_update_refills)
    hass.services.async_register(DOMAIN, "check_off_dose", handle_check_off_dose)
    hass.services.async_register(DOMAIN, "uncheck_dose", handle_uncheck_dose)
    hass.services.async_register(DOMAIN, "update_doctor", handle_update_doctor)
    hass.services.async_register(DOMAIN, "update_stock", handle_update_stock)
    
    # Load platforms using discovery for YAML config
    hass.async_create_task(
        async_load_platform(hass, "sensor", DOMAIN, {}, config)
    )
    hass.async_create_task(
        async_load_platform(hass, "binary_sensor", DOMAIN, {}, config)
    )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
