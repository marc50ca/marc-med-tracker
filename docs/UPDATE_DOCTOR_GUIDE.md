# Updating Prescribing Doctor Information

## Overview

The Marc Med Tracker integration allows you to update the prescribing doctor for any medication. This is useful when:
- You switch to a new doctor
- A doctor changes their name
- You need to correct an entry
- Your care is transferred to a specialist

## Using the Service

### Method 1: Developer Tools

1. Go to **Developer Tools** → **Services**
2. Select service: `marc_med_tracker.update_doctor`
3. Fill in the service data:
   ```yaml
   medication_id: aspirin
   doctor_name: Dr. Jane Smith
   ```
4. Click **Call Service**

### Method 2: Script

Create a reusable script in your `scripts.yaml`:

```yaml
update_medication_doctor:
  alias: Update Medication Doctor
  icon: mdi:doctor
  fields:
    medication:
      description: Medication ID
      example: aspirin
    doctor:
      description: New doctor name
      example: Dr. Jane Smith
  sequence:
    - service: marc_med_tracker.update_doctor
      data:
        medication_id: "{{ medication }}"
        doctor_name: "{{ doctor }}"
    - service: persistent_notification.create
      data:
        title: Doctor Updated
        message: "Prescribing doctor updated to {{ doctor }}"
```

### Method 3: Dashboard Button

Add a button to your dashboard that prompts for input:

```yaml
type: button
name: Update Doctor
icon: mdi:doctor
tap_action:
  action: call-service
  service: script.update_medication_doctor
  data:
    medication: aspirin
    doctor: Dr. Jane Smith
```

### Method 4: Input Helper with Automation

For a more user-friendly approach, create input helpers:

```yaml
# configuration.yaml
input_text:
  aspirin_doctor:
    name: Aspirin Doctor
    initial: Dr. Sarah Smith
    icon: mdi:doctor

# automations.yaml
automation:
  - alias: Update Aspirin Doctor
    trigger:
      - platform: state
        entity_id: input_text.aspirin_doctor
    action:
      - service: marc_med_tracker.update_doctor
        data:
          medication_id: aspirin
          doctor_name: "{{ states('input_text.aspirin_doctor') }}"
```

Then add this to your dashboard:

```yaml
type: entities
title: Update Doctor Information
entities:
  - entity: input_text.aspirin_doctor
```

## Dashboard Card for All Medications

Create a comprehensive card to update doctors for all medications:

```yaml
type: vertical-stack
title: Prescribing Physicians
cards:
  - type: markdown
    content: |
      ## Current Prescribing Doctors
      
      {% for entity in states.sensor if 'med_' in entity.entity_id %}
      **{{ state_attr(entity.entity_id, 'medication_name') }}**: {{ state_attr(entity.entity_id, 'prescribing_doctor') }}
      {% endfor %}
  
  - type: entities
    title: Update Doctor Names
    entities:
      - type: button
        name: Update Aspirin Doctor
        icon: mdi:doctor
        tap_action:
          action: call-service
          service: marc_med_tracker.update_doctor
          service_data:
            medication_id: aspirin
            doctor_name: Dr. New Name
      
      - type: button
        name: Update Vitamin D Doctor
        icon: mdi:doctor
        tap_action:
          action: call-service
          service: marc_med_tracker.update_doctor
          service_data:
            medication_id: vitamin_d
            doctor_name: Dr. New Name
```

## Tracking Doctor Changes

The service fires an event when a doctor is updated. You can create automations to track changes:

### Log Doctor Changes

```yaml
automation:
  - alias: Log Doctor Changes
    trigger:
      - platform: event
        event_type: marc_med_tracker_doctor_updated
    action:
      - service: logbook.log
        data:
          name: Doctor Updated
          message: >
            {{ trigger.event.data.medication_name }} doctor changed 
            from {{ trigger.event.data.old_doctor }} 
            to {{ trigger.event.data.new_doctor }}
```

### Notify on Doctor Change

```yaml
automation:
  - alias: Notify Doctor Change
    trigger:
      - platform: event
        event_type: marc_med_tracker_doctor_updated
    action:
      - service: notify.mobile_app
        data:
          title: "🩺 Doctor Updated"
          message: >
            {{ trigger.event.data.medication_name }}:
            {{ trigger.event.data.old_doctor }} → {{ trigger.event.data.new_doctor }}
```

### Track All Changes in a Sensor

Create a sensor that shows the last doctor change:

```yaml
template:
  - trigger:
      - platform: event
        event_type: marc_med_tracker_doctor_updated
    sensor:
      - name: Last Doctor Change
        state: "{{ now().strftime('%Y-%m-%d %H:%M') }}"
        attributes:
          medication: "{{ trigger.event.data.medication_name }}"
          old_doctor: "{{ trigger.event.data.old_doctor }}"
          new_doctor: "{{ trigger.event.data.new_doctor }}"
```

## Use Cases

### 1. Switching Primary Care Doctor

When you change your primary care doctor who prescribes multiple medications:

```yaml
script:
  switch_to_new_primary_doctor:
    alias: Switch to New Primary Doctor
    sequence:
      - service: marc_med_tracker.update_doctor
        data:
          medication_id: aspirin
          doctor_name: Dr. New PCP
      - service: marc_med_tracker.update_doctor
        data:
          medication_id: vitamin_d
          doctor_name: Dr. New PCP
      - service: persistent_notification.create
        data:
          title: Primary Doctor Updated
          message: All medications updated to new primary care physician
```

### 2. Transferring to Specialist

When care is transferred from PCP to specialist:

```yaml
script:
  transfer_to_cardiologist:
    alias: Transfer BP Med to Cardiologist
    sequence:
      - service: marc_med_tracker.update_doctor
        data:
          medication_id: blood_pressure_medication
          doctor_name: Dr. Heart Specialist
      - service: notify.mobile_app
        data:
          title: Care Transferred
          message: Blood pressure medication now managed by cardiologist
```

### 3. Bulk Update via Loop

Update multiple medications at once:

```yaml
script:
  bulk_update_doctors:
    alias: Bulk Update All to New Doctor
    variables:
      new_doctor: Dr. Jane Smith
      medications:
        - aspirin
        - vitamin_d
        - blood_pressure_medication
    sequence:
      - repeat:
          for_each: "{{ medications }}"
          sequence:
            - service: marc_med_tracker.update_doctor
              data:
                medication_id: "{{ repeat.item }}"
                doctor_name: "{{ new_doctor }}"
```

## Notes

- The medication_id must match exactly (lowercase with underscores)
- Changes are immediately saved to persistent storage
- The sensor attributes update automatically
- An event is fired that can trigger automations
- Changes persist across Home Assistant restarts

## Medication ID Reference

Find your medication ID by:
1. Go to **Developer Tools** → **States**
2. Search for `sensor.marc_med_`
3. The entity ID after `sensor.marc_med_` is your medication_id

Examples:
- `sensor.marc_med_aspirin` → medication_id: `aspirin`
- `sensor.marc_med_vitamin_d` → medication_id: `vitamin_d`
- `sensor.marc_med_blood_pressure_medication` → medication_id: `blood_pressure_medication`

## Troubleshooting

**Service call fails:**
- Check that the medication_id is correct (lowercase, underscores)
- Verify the medication exists in your configuration
- Check logs: Settings → System → Logs

**Changes not showing:**
- Refresh your dashboard
- Check Developer Tools → States to verify the change
- Restart Home Assistant if needed

**Want to see change history:**
- Check the Logbook for doctor change events
- Use the History panel to see attribute changes over time
