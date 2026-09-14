---
title: "Quiz: Electricity Fundamentals, Resistors & Multimeter Calculations"
module: "Week 02"
points_possible: 10
grading_type: "pass_fail"
submission_types: ["online_quiz", "online_text_entry"]
published: false
---

# Quiz: Electricity Fundamentals, Resistors & Multimeter Calculations

- **Points:** 10 pts
- **Grading Type:** Pass / Fail (Complete / Incomplete)
- **Time Limit:** None (Self-Paced / Open Resource)
- **Reference Material:** 
  - Sparkle Labs *Discover Electronics Lesson Book* (`manual_wm_s.pdf`), especially **Pages 7–14**
  - Sparkle Labs *Multitester Basic Operations* (`multitester_basic_color.pdf`)
  - [A Designer's Friendly Guide to the Multimeter](/courses/1929836/pages/a-designers-friendly-guide-to-the-multimeter)

---

## Instructions

Answer the questions below. Each question outlines the **basic physical steps** (which meter port to use, which dial setting to choose, how to place your probes, and the mathematical formula) so you learn how to solve real benchtop problems.

Submit your answers directly via Canvas.

---

### Question 1: Solderless Breadboard Continuity Diagnostic (2.5 pts)

You just plugged a wire into row 15 on your solderless breadboard. You want to verify with your multimeter whether column 15A and column 15E are connected together beneath the plastic before applying power.

#### Step-by-Step Diagnostic Method:
1. **Probe Ports:** Leave your **Black Probe** plugged into `COM` (Center/Ground). Plug your **Red Probe** into `V Ω mA` (Right port).
2. **Meter Dial Setting:** Turn the central selector knob to **Continuity Mode** (marked with the audio/speaker wave or diode symbol: `(((🔊` or `->|-`).
3. **Probe Placement:** Touch the metallic tip of probe 1 into pinhole 15A, and the tip of probe 2 into pinhole 15E.

#### Questions to Answer:
- **1a.** What dial symbol/mode is selected to test physical continuity?
- **1b.** What audible sound will the multimeter produce if the breadboard row is properly connected?
- **1c.** Should circuit power (battery or USB) be **ON** or **OFF** when performing a continuity test?

*💡 Hint: Review Page 4 of `manual_wm_s.pdf` and `multitester_basic_color.pdf`.*

---

### Question 2: Measuring Voltage Drop & Calculating LED Resistor Sizing (2.5 pts)

You have a circuit powered by a **$V_{\text{Supply}} = 5\text{V}$** source. You want to light a **Red LED** that safely operates at a current of **$I = 0.02\text{A}$ ($20\text{mA}$)**. 

According to Page 12 of `manual_wm_s.pdf`, a standard Red LED creates a forward voltage drop ($V_{\text{LED}}$) of **$1.7\text{V}$**.

#### Step-by-Step Measurement & Calculation Method:
1. **Bench Verification:** 
   - Set the multimeter dial to **DC Volts `V=` (at the 20V range)**.
   - Power the circuit **ON**.
   - Touch probes **in parallel** across the LED (Red probe to the positive Anode lead, Black probe to the negative Cathode lead) to measure the actual voltage drop ($1.7\text{V}$).
2. **Calculate Resistor Voltage Drop:** The current-limiting resistor absorbs whatever voltage the LED does not use:
   $$V_{\text{Resistor}} = V_{\text{Supply}} - V_{\text{LED}}$$
3. **Calculate Required Resistance using Ohm's Law:**
   $$R = \frac{V_{\text{Resistor}}}{I} = \frac{V_{\text{Supply}} - V_{\text{LED}}}{I}$$

#### Questions to Answer:
- **2a.** What dial setting on your multitester is used to verify DC voltage across an active component?
- **2b.** What is the voltage drop across the resistor ($V_{\text{Resistor}} = 5\text{V} - 1.7\text{V}$)?
- **2c.** Using $R = \frac{V_{\text{Resistor}}}{0.02\text{A}}$, what is the exact resistance in Ohms ($\Omega$) needed?
- **2d.** If you have a $220\Omega$ resistor in your kit, is it safe to use here? (Yes / No)

*💡 Hint: Review Pages 11–12 of `manual_wm_s.pdf`.*

---

### Question 3: Benchtop Measurement & Calculation of Series Resistors (2.5 pts)

You place two **$220\Omega$ resistors** in **series** (daisy-chained one after another on the breadboard so current flows through both in a single path).

#### Step-by-Step Measurement & Calculation Method:
1. **Safety First:** Disconnect all power (unplug USB or turn off the battery pack). **Never measure resistance on a powered circuit.**
2. **Meter Dial Setting:** Turn the multimeter dial to the **OHMS ($\Omega$)** section (set to `2000` or `20k` scale so it can read values greater than $200\Omega$).
3. **Probe Placement:** Touch the probes across the outer free ends of the series chain.
4. **Formula for Series Resistance:**
   $$R_{\text{total}} = R_1 + R_2$$

#### Questions to Answer:
- **3a.** Why must the power supply be disconnected when measuring resistance ($\Omega$) with a multimeter?
- **3b.** Which section and range on the multimeter dial do you select to measure two $220\Omega$ resistors in series?
- **3c.** What is the total combined resistance ($R_{\text{total}}$) in Ohms ($\Omega$) of two $220\Omega$ resistors wired in series?

*💡 Hint: Review Page 14 of `manual_wm_s.pdf` and `multitester_basic_color.pdf`.*

---

### Question 4: Benchtop Measurement & Calculation of Parallel Resistors (2.5 pts)

You now wire the same two **$220\Omega$ resistors** in **parallel** (side-by-side, sharing both the entrance node and exit node).

#### Step-by-Step Measurement & Calculation Method:
1. **Safety First:** Ensure circuit power is completely **OFF**.
2. **Meter Dial Setting:** Keep the multimeter dial in the **OHMS ($\Omega$)** section (set to the `200` or `2000` scale).
3. **Probe Placement:** Place one probe on the shared input row and the other probe on the shared output row.
4. **Formula for Parallel Resistance:**
   $$\frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2}$$
   *(Shortcut for two identical resistors: $R_{\text{total}} = \frac{R}{2}$)*

#### Questions to Answer:
- **4a.** When components are in parallel, does the total resistance increase or decrease compared to a single resistor?
- **4b.** What is the total combined resistance ($R_{\text{total}}$) in Ohms ($\Omega$) of two $220\Omega$ resistors wired in parallel?

*💡 Hint: Review Page 14 of `manual_wm_s.pdf`.*

---

## Evaluation Rubric (Pass / Fail)

| Result | Criteria | Points |
| :--- | :--- | :---: |
| **Complete (Pass)** | All questions answered with correct multitester settings, physical probe techniques, and accurate calculations with units. | 10 pts |
| **Incomplete (Needs Revision)** | Incomplete steps or incorrect calculations. May be revised and resubmitted. | 0 pts |
