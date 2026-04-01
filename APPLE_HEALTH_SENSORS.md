# Apple Health Sensor Mapping Reference

## Sensor Replacements

### Blood Glucose
- ~~sensor.blood_glucose_marc~~ → `hae.marchealthsync_blood_glucose`

### Cardio-Vascular (10 sensors - alphabetically sorted)
- ~~sensor.blood_pressure_diastolic_marc~~ → `hae.marchealthsync_blood_pressure_diastolic`
- ~~sensor.blood_pressure_systolic_marc~~ → `hae.marchealthsync_blood_pressure_systolic`
- ~~sensor.oxygen_saturation_marc~~ → `hae.marchealthsync_blood_oxygen_saturation`
- NEW: `hae.marchealthsync_cardio_recovery`
- ~~sensor.heart_rate_marc~~ → `hae.marchealthsync_heart_rate_avg`
- NEW: `hae.marchealthsync_heart_rate_max`
- NEW: `hae.marchealthsync_heart_rate_min`
- NEW: `hae.marchealthsync_heart_rate_variability`
- NEW: `hae.marchealthsync_respiratory_rate`
- ~~sensor.resting_heart_rate_marc~~ → `hae.marchealthsync_resting_heart_rate`

### Sleep (8 sensors - alphabetically sorted)
- NEW: `hae.marchealthsync_apple_sleeping_wrist_temperature`
- ~~sensor.flights_climbed_marc~~ → `hae.marchealthsync_flights_climbed`
- ~~sensor.sleep_awake_hours_marc~~ → `hae.marchealthsync_sleep_analysis_awake`
- ~~sensor.sleep_core_hours_marc~~ → `hae.marchealthsync_sleep_analysis_core`
- ~~sensor.sleep_deep_hours_marc~~ → `hae.marchealthsync_sleep_analysis_deep`
- ~~sensor.sleep_duration_marc~~ → `hae.marchealthsync_sleep_analysis_inbed`
- NEW: `hae.marchealthsync_sleep_analysis_rem`
- NEW: `hae.marchealthsync_sleep_analysis_sleep`

### Weight (3 sensors - NEW SECTION - alphabetically sorted)
- ~~sensor.body_mass_marc~~ → `hae.marchealthsync_body_mass_index`
- NEW: `hae.marchealthsync_lean_body_mass`
- NEW: `hae.marchealthsync_weight_body_mass`

### Activity (13 sensors - alphabetically sorted)
- NEW: `hae.marchealthsync_active_energy`
- ~~sensor.exercise_time_marc~~ → `hae.marchealthsync_apple_exercise_time`
- NEW: `hae.marchealthsync_apple_stand_hour`
- ~~sensor.stand_time_marc~~ → `hae.marchealthsync_apple_stand_time`
- NEW: `hae.marchealthsync_environment_audio_exposure`
- `hae.marchealthsync_flights_climbed` (also in Sleep section)
- NEW: `hae.marchealthsync_headphone_audio_exposure`
- NEW: `hae.marchealthsync_stair_speed_down`
- NEW: `hae.marchealthsync_stair_speed_up`
- ~~sensor.steps_marc~~ → `hae.marchealthsync_step_count`
- NEW: `hae.marchealthsync_time_in_daylight`
- ~~sensor.distance_marc~~ → `hae.marchealthsync_walking_running_distance`
- ~~sensor.walking_speed_marc~~ → `hae.marchealthsync_walking_speed`

## Summary

**Total Apple Health Sensors:** 35

**By Category:**
- Blood Glucose: 1 sensor
- Cardio-Vascular: 10 sensors
- Sleep: 8 sensors
- Weight: 3 sensors (NEW section)
- Activity: 13 sensors

**Duplicates Removed:**
- `flights_climbed` appears in both Sleep and Activity (kept in both for context)

**All sensors alphabetically sorted within each section**

## Dashboard Cards

**Total Cards:** 17

1. Medication Schedule
2. Daily Progress
3. Blood Glucose
4. Blood Glucose Graph
5. Cardio-Vascular Metrics
6. Blood Pressure Graph
7. Heart Rate Graph
8. Sleep Metrics
9. Sleep Graph
10. Weight Metrics
11. Weight Graph
12. Activity Metrics
13. Activity Graph - Steps & Distance
14. Activity Graph - Exercise
15. NP T. Wakefield Medications
16. Dr. K. Ducet Medications
17. Dr. K. Safka Medications

## Installation

**File:** `examples/dashboard_cards_apple_health.yaml`

**Method:** Card-by-card installation
1. Open your Overview dashboard
2. Click Edit
3. Add Card → Manual
4. Copy/paste Card 1
5. Save
6. Repeat for Cards 2-17

**See:** `docs/DASHBOARD_SIMPLE_INSTALL.md` for detailed instructions
