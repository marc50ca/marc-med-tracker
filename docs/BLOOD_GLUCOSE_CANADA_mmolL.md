# Blood Glucose Monitoring Guide - Canada (mmol/L)

## Canadian Blood Glucose Targets

### Fasting / Before Meals
- **Target Range:** 4.0 - 7.0 mmol/L
- **Good Control:** < 6.0 mmol/L
- **Acceptable:** 4.0 - 8.0 mmol/L

### 2 Hours After Meals
- **Target Range:** 5.0 - 10.0 mmol/L
- **Good Control:** 5.0 - 8.0 mmol/L
- **Acceptable:** < 10.0 mmol/L

### A1C Target
- **Target:** < 7.0%
- **Good Control:** 6.5% or lower
- **General Guideline:** 6.0 - 7.0%

### Hypoglycemia (Low Blood Sugar)
- **Low:** < 4.0 mmol/L
- **Very Low:** < 3.5 mmol/L
- **Dangerous:** < 3.0 mmol/L (treat immediately!)

### Hyperglycemia (High Blood Sugar)
- **Elevated:** > 10.0 mmol/L
- **High:** > 15.0 mmol/L
- **Very High:** > 20.0 mmol/L

---

## Dashboard Setup - mmol/L

### Input Number Helpers

Add to your `configuration.yaml`:

```yaml
input_number:
  blood_glucose_reading_1:
    name: "Blood Glucose - Morning"
    min: 0
    max: 30        # mmol/L range
    step: 0.1      # Decimal precision
    unit_of_measurement: "mmol/L"
    icon: mdi:diabetes
  
  blood_glucose_reading_2:
    name: "Blood Glucose - Afternoon"
    min: 0
    max: 30
    step: 0.1
    unit_of_measurement: "mmol/L"
    icon: mdi:diabetes
  
  blood_glucose_reading_3:
    name: "Blood Glucose - Evening"
    min: 0
    max: 30
    step: 0.1
    unit_of_measurement: "mmol/L"
    icon: mdi:diabetes
```

---

## Testing Schedule (3 Times Daily)

### Morning - Fasting (Before Breakfast)
- **Time:** Upon waking, before any food
- **Target:** 4.0 - 7.0 mmol/L
- **Purpose:** Baseline glucose level

### Afternoon - 2 Hours After Lunch
- **Time:** Exactly 2 hours after first bite
- **Target:** 5.0 - 10.0 mmol/L
- **Purpose:** Post-meal glucose response

### Evening - Before Bed
- **Time:** Before bedtime snack
- **Target:** 4.0 - 8.0 mmol/L
- **Purpose:** Overnight baseline

---

## A1C Calculation from Average

Using the simplified formula for mmol/L:

**A1C (%) = (Average mmol/L × 0.555 + 2.59)**

### Example Calculations:

| Average mmol/L | Estimated A1C |
|----------------|---------------|
| 5.0 | 5.4% (Excellent) |
| 6.0 | 5.9% (Good) |
| 7.0 | 6.5% (Target) |
| 8.0 | 7.0% (Acceptable) |
| 9.0 | 7.6% (Above target) |
| 10.0 | 8.1% (High) |

---

## Color-Coded Ranges for Dashboard

### Green (Good Control)
- **Fasting:** 4.0 - 6.0 mmol/L
- **After Meals:** 5.0 - 8.0 mmol/L

### Yellow (Acceptable)
- **Fasting:** 6.1 - 8.0 mmol/L
- **After Meals:** 8.1 - 10.0 mmol/L

### Red (Out of Range)
- **Too Low:** < 4.0 mmol/L
- **Too High:** > 10.0 mmol/L

---

## Conversion Reference

### mmol/L to mg/dL
**Multiply mmol/L by 18**

| mmol/L | mg/dL |
|--------|-------|
| 4.0 | 72 |
| 5.0 | 90 |
| 6.0 | 108 |
| 7.0 | 126 |
| 8.0 | 144 |
| 9.0 | 162 |
| 10.0 | 180 |

### mg/dL to mmol/L
**Divide mg/dL by 18**

---

## Template Sensors with mmol/L

### Average Sensors (Already Configured)

The statistics sensors in `blood_glucose_averages.yaml` work with mmol/L automatically - they just calculate the mean of whatever unit your sensor uses.

### A1C Calculation Sensor

Add this to `configuration.yaml` for automatic A1C calculation:

```yaml
template:
  - sensor:
      - name: "Blood Glucose A1C Estimate"
        unique_id: blood_glucose_a1c_estimate
        unit_of_measurement: "%"
        state: >
          {% set avg = states('sensor.blood_glucose_90_day_average') | float(0) %}
          {% if avg > 0 %}
            {{ ((avg * 0.555 + 2.59) | round(1)) }}
          {% else %}
            unavailable
          {% endif %}
        icon: mdi:clipboard-pulse
        attributes:
          average_glucose: "{{ states('sensor.blood_glucose_90_day_average') }} mmol/L"
          formula: "(Average × 0.555 + 2.59)"
```

This creates: `sensor.blood_glucose_a1c_estimate`

---

## Dashboard Card - A1C with mmol/L

Add this card to show A1C estimate:

```yaml
type: entities
title: "🩸 A1C Estimate"
state_color: true
entities:
  - entity: sensor.blood_glucose_a1c_estimate
    name: "Estimated A1C"
    icon: mdi:clipboard-pulse
  - entity: sensor.blood_glucose_90_day_average
    name: "90-Day Average"
    icon: mdi:calculator
  - type: custom:bar-card
    entity: sensor.blood_glucose_a1c_estimate
    min: 5
    max: 10
    target: 7
    severity:
      - color: "#4caf50"
        from: 5
        to: 6.5
      - color: "#ffc107"
        from: 6.5
        to: 7.5
      - color: "#f44336"
        from: 7.5
        to: 10
```

---

## Sample Daily Readings

### Good Control Example
- Morning (Fasting): **5.2 mmol/L** ✅
- Afternoon (2hrs after): **7.4 mmol/L** ✅
- Evening (Before bed): **6.1 mmol/L** ✅
- **Average:** 6.2 mmol/L
- **Estimated A1C:** 6.0%

### Needs Improvement Example
- Morning (Fasting): **8.1 mmol/L** ⚠️
- Afternoon (2hrs after): **12.3 mmol/L** ❌
- Evening (Before bed): **9.8 mmol/L** ⚠️
- **Average:** 10.1 mmol/L
- **Estimated A1C:** 8.2%

---

## When to Test

### Always Test When:
- ✅ Waking up (fasting)
- ✅ Before major meals
- ✅ 2 hours after meals
- ✅ Before bed
- ✅ Feeling symptoms (shaky, dizzy, tired)
- ✅ Before/after exercise
- ✅ When sick

### Minimum: 3 Times Daily
- Morning fasting
- 2 hours after lunch
- Before bed

---

## Action Steps

### If Reading is Low (< 4.0 mmol/L)
1. **15-15 Rule:** 15g fast-acting carbs
2. Wait 15 minutes
3. Re-test
4. Repeat if still low
5. Eat a snack with protein once normal

### If Reading is High (> 10.0 mmol/L)
1. Drink water
2. Check ketones (if Type 1)
3. Take correction dose if prescribed
4. Re-test in 2 hours
5. Contact doctor if consistently high

### If Very High (> 15.0 mmol/L)
1. Contact healthcare provider
2. Check for ketones
3. Follow sick day protocol
4. Monitor closely

---

## Canadian Resources

**Diabetes Canada Guidelines:**
- Website: diabetes.ca
- Target ranges updated regularly
- Provincial coverage info

**Healthcare Team:**
- Your doctor
- Diabetes educator
- Dietitian
- Pharmacist

---

**Your blood glucose is now properly configured for Canadian mmol/L readings!** 🇨🇦🩸📊
