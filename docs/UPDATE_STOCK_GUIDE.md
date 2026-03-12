# Updating Pills on Hand - Stock Management Guide

## Overview

The `update_stock` service allows you to manually set the exact number of pills you currently have on hand. This is useful when:
- You need to correct the inventory after doing a physical count
- Pills were dropped, lost, or spoiled
- The automatic calculation is off
- You're adding a medication mid-supply
- You transferred pills between bottles

## Using the Service

### Method 1: Developer Tools

1. Go to **Developer Tools** → **Services**
2. Select service: `marc_med_tracker.update_stock`
3. Fill in the service data:
   ```yaml
   medication_id: aspirin
   pills: 45
   ```
4. Click **Call Service**

### Method 2: Script

Create a reusable script in your `scripts.yaml`:

```yaml
update_pill_count:
  alias: Update Pill Count
  icon: mdi:counter
  fields:
    medication:
      description: Medication ID
      example: aspirin
    count:
      description: Actual pill count
      example: 45
  sequence:
    - service: marc_med_tracker.update_stock
      data:
        medication_id: "{{ medication }}"
        pills: "{{ count }}"
    - service: notify.mobile_app
      data:
        title: "Inventory Updated"
        message: "{{ medication | replace('_', ' ') | title }} count set to {{ count }} pills"
```

### Method 3: Dashboard Button

Add a button to your dashboard:

```yaml
type: button
name: Update Aspirin Count
icon: mdi:counter
tap_action:
  action: call-service
  service: marc_med_tracker.update_stock
  service_data:
    medication_id: aspirin
    pills: 45
```

### Method 4: Input Number Helper

For a more interactive approach:

```yaml
# configuration.yaml
input_number:
  aspirin_manual_count:
    name: Aspirin Count
    min: 0
    max: 200
    step: 1
    mode: box
    icon: mdi:pill

# automations.yaml
automation:
  - alias: Update Aspirin Stock from Input
    trigger:
      - platform: state
        entity_id: input_number.aspirin_manual_count
    condition:
      - condition: template
        value_template: "{{ trigger.to_state.state != 'unknown' }}"
    action:
      - service: marc_med_tracker.update_stock
        data:
          medication_id: aspirin
          pills: "{{ states('input_number.aspirin_manual_count') | int }}"
```

Then add to dashboard:

```yaml
type: entities
title: Manual Stock Update
entities:
  - entity: input_number.aspirin_manual_count
  - entity: sensor.marc_med_aspirin
    name: Current System Count
```

## Use Cases

### 1. Physical Inventory Count

When you physically count your pills:

```yaml
service: marc_med_tracker.update_stock
data:
  medication_id: aspirin
  pills: 47  # What you actually counted
```

### 2. Pills Dropped or Lost

If you dropped pills:

```yaml
service: marc_med_tracker.update_stock
data:
  medication_id: vitamin_d
  pills: "{{ states('sensor.marc_med_vitamin_d') | int - 5 }}"  # Lost 5 pills
```

Or use a script:

```yaml
script:
  report_pills_dropped:
    alias: Report Dropped Pills
    fields:
      medication:
        description: Medication ID
        example: aspirin
      amount_dropped:
        description: Number of pills dropped
        example: 3
    sequence:
      - service: marc_med_tracker.update_stock
        data:
          medication_id: "{{ medication }}"
          pills: "{{ states('sensor.marc_med_' + medication) | int - amount_dropped }}"
      - service: notify.mobile_app
        data:
          title: "Pills Dropped"
          message: "{{ amount_dropped }} {{ medication }} pills removed from inventory"
```

### 3. Correcting Calculation Errors

If the automatic calculation is wrong:

```yaml
# First check current count
# Developer Tools → States → sensor.marc_med_aspirin
# Shows: 35 pills

# But you counted: 40 pills

service: marc_med_tracker.update_stock
data:
  medication_id: aspirin
  pills: 40
```

### 4. Adding Medication Mid-Supply

Starting to track a medication you're already taking:

```yaml
# Count your current pills
service: marc_med_tracker.update_stock
data:
  medication_id: new_medication
  pills: 52  # Whatever you counted
```

### 5. Combining Bottles

If you combined pills from multiple bottles:

```yaml
service: marc_med_tracker.update_stock
data:
  medication_id: aspirin
  pills: 85  # Total from all bottles combined
```

## Event Tracking

The service fires an event when stock is updated:

```yaml
# Track all stock changes
automation:
  - alias: Log Stock Changes
    trigger:
      - platform: event
        event_type: marc_med_tracker_stock_updated
    action:
      - service: logbook.log
        data:
          name: Inventory Adjusted
          message: >
            {{ trigger.event.data.medication_name }}: 
            {{ trigger.event.data.old_stock }} → {{ trigger.event.data.new_stock }} pills
            ({{ 'Added' if trigger.event.data.difference > 0 else 'Removed' }} 
            {{ trigger.event.data.difference | abs }} pills)
```

### Notify on Large Changes

```yaml
automation:
  - alias: Alert on Large Stock Adjustments
    trigger:
      - platform: event
        event_type: marc_med_tracker_stock_updated
    condition:
      - condition: template
        value_template: "{{ trigger.event.data.difference | abs > 10 }}"
    action:
      - service: notify.mobile_app
        data:
          title: "⚠️ Large Inventory Adjustment"
          message: >
            {{ trigger.event.data.medication_name }}: 
            {{ trigger.event.data.difference | abs }} pill 
            {{ 'increase' if trigger.event.data.difference > 0 else 'decrease' }}
```

### Track Adjustments in Sensor

```yaml
template:
  - trigger:
      - platform: event
        event_type: marc_med_tracker_stock_updated
    sensor:
      - name: Last Stock Adjustment
        state: "{{ now().strftime('%Y-%m-%d %H:%M') }}"
        attributes:
          medication: "{{ trigger.event.data.medication_name }}"
          old_stock: "{{ trigger.event.data.old_stock }}"
          new_stock: "{{ trigger.event.data.new_stock }}"
          difference: "{{ trigger.event.data.difference }}"
          adjustment_type: "{{ 'Manual Count' }}"
```

## Dashboard Examples

### Simple Adjustment Card

```yaml
type: entities
title: Quick Stock Adjustments
entities:
  - type: button
    name: Aspirin - Set to 30
    icon: mdi:counter
    action_row:
      action: call-service
      service: marc_med_tracker.update_stock
      service_data:
        medication_id: aspirin
        pills: 30
  - type: button
    name: Aspirin - Set to 60
    icon: mdi:counter
    action_row:
      action: call-service
      service: marc_med_tracker.update_stock
      service_data:
        medication_id: aspirin
        pills: 60
  - type: button
    name: Aspirin - Set to 90
    icon: mdi:counter
    action_row:
      action: call-service
      service: marc_med_tracker.update_stock
      service_data:
        medication_id: aspirin
        pills: 90
```

### Comparison Card

```yaml
type: markdown
title: System vs Actual Count
content: |
  | Medication | System Count | Manual Entry | Match? |
  |------------|--------------|--------------|--------|
  | Aspirin | {{ states('sensor.marc_med_aspirin') }} | _[Count manually]_ | - |
  | Vitamin D | {{ states('sensor.marc_med_vitamin_d') }} | _[Count manually]_ | - |
  
  Use the input helpers below to update counts if different.
```

## Best Practices

### When to Use update_stock vs refill

**Use `update_stock` when:**
- Doing a physical inventory count
- Correcting errors
- Accounting for lost/dropped pills
- Pills expired and discarded
- Manual adjustments needed

**Use `refill` when:**
- Getting a new prescription filled
- Picking up from pharmacy
- Receiving mail order medication
- This is the proper refill workflow

### Recommended Workflow

1. **Monthly Inventory Check:**
   ```yaml
   automation:
     - alias: Monthly Pill Count Reminder
       trigger:
         - platform: time
           at: "09:00:00"
       condition:
         - condition: template
           value_template: "{{ now().day == 1 }}"
       action:
         - service: notify.mobile_app
           data:
             title: "📋 Monthly Inventory Check"
             message: "Time to count your pills and update inventory"
   ```

2. **Compare and Adjust:**
   - Look at system count: `states('sensor.marc_med_aspirin')`
   - Count physical pills
   - If different, use `update_stock`

3. **Document Why:**
   - Keep notes on large adjustments
   - Use the event tracking automations above

## Tips

- **Count carefully** - Recount if the difference is large
- **Update immediately** - Don't delay after counting
- **Check calculations** - Make sure system is tracking doses correctly
- **Use input helpers** - Easier than service calls
- **Enable logging** - Track all manual adjustments
- **Regular checks** - Monthly or quarterly inventory counts

## Troubleshooting

**Stock immediately goes back to wrong number:**
- The system recalculates based on refill date and doses
- Make sure you're not confusing `update_stock` with `refill`
- If you got a refill, use `refill` service instead

**Can't set stock to specific number:**
- Check that the medication_id is correct
- Verify pills parameter is a number
- Look for errors in logs

**Changes not saving:**
- Check storage file permissions
- Verify integration is loaded
- Restart Home Assistant if needed

## Related Services

- `take_dose` - Reduces count by one dose
- `refill` - Adds pills and updates refill date
- `update_refills` - Changes refill count only
- `update_doctor` - Changes prescribing doctor
