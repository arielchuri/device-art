# Hands-On Lab: Breadboard Electricity, Multimeters & Circuit Puzzles

**Course:** Device Art (Fall 2026)  
**Lab Name:** Lab 01 — Electricity Fundamentals: Miro to Breadboard  
**Equipment Needed:**  
- Raspberry Pi Pico (for 3.3V Power & GND) or 3.3V DC Power Supply  
- 830 Tie-Point Solderless Breadboard  
- Digital Multimeter (with test leads)  
- Red 5mm LED  
- Resistors: 220Ω (Red-Red-Brown), 1kΩ (Brown-Black-Red), 10kΩ (Brown-Black-Orange)  
- 10kΩ Rotary Potentiometer  
- Light Dependent Resistor (LDR / Photocell)  
- 4-Pin Tactile Pushbutton  
- Jumper Wires  

---

## 🎯 Lab Overview & Dual-Platform Workflow

In this lab, you will explore the core pillars of physical computing: **Voltage ($V$)**, **Current ($I$)**, and **Resistance ($R$)**.

For every circuit stage, you will follow a **4-Step Workflow**:
1. **🎨 Step A: Build in Miro**  
   Drag-and-drop the 1:1 breadboard-scaled hardware vectors from the **Miro Device Canvas** (`package_components/`) to map your connections before plugging any physical wires.
2. **🔌 Step B: Build on Breadboard**  
   Assemble the physical circuit on your solderless breadboard.
3. **📏 Step C: Multimeter Measurement**  
   Measure voltage drop, resistance, or current using your digital multimeter.
4. **🧩 Step D: Solve the Circuit Puzzle**  
   Answer the conceptual inquiry question or troubleshooting puzzle.

---

## 🛠️ Multimeter Quick-Reference Cheat Sheet

| Measurement Mode | Meter Dial Setting | Probe Connection | Measurement Method |
| :--- | :--- | :--- | :--- |
| **DC Voltage ($V$)** | `V=` or `20V DC` | Red to Positive Point, Black to Ground | **In Parallel** (Across component while circuit is ON) |
| **Resistance ($\Omega$)** | `200\Omega`, `2k\Omega`, `20k\Omega` | Red and Black probes to component leads | **DISCONNECT POWER FIRST!** (Measure component isolated) |
| **DC Current ($mA$)** | `mA` or `200mA DC` | Red in `mA` jack, Black in `COM` | **In Series** (Break the circuit loop and place meter in line) |

> [!CAUTION]
> **NEVER** measure resistance while power is connected!  
> **NEVER** place multimeter probes directly across power (`3V3` to `GND`) in `mA` Current Mode—this creates a dead short and will blow your meter's internal fuse!

---

## 🔬 Lab Stage 1: The Basic LED Loop & Polarity

### Objectives:
- Power a Red 5mm LED safely using a 220Ω current-limiting resistor.
- Observe diode polarity (Anode vs. Cathode).

```text
[ 3.3V Power ] ---> [ 220Ω Resistor ] ---> [ LED (Anode +) -> (Cathode -) ] ---> [ GND ]
```

### 1.1 Step-by-Step Build
1. **Miro Canvas**: Drag `solderless_breadboard.svg` onto your Miro board. Place `resistor_topdown_scaled.svg` (220Ω) spanning **Row 5 to Row 9**. Place `led_topdown_scaled.svg` with its **Anode (+)** on **Row 9** and **Cathode (-)** on **Row 10**. Connect a Red wire from `3V3` to Row 5, and a Black wire from `GND` to Row 10.
2. **Physical Breadboard**: Replicate the exact layout on your physical breadboard. Connect Pico `3V3` (Pin 36) to Row 5, and `GND` (Pin 38) to Row 10.

### 1.2 Multimeter Measurements
Turn on power (plug in Pico USB) and measure:
- **Voltage across 220Ω Resistor ($V_R$)**: ________ Volts
- **Voltage across Red LED ($V_{\text{LED}}$)**: ________ Volts
- **Total Supply Voltage ($V_{\text{total}} = V_R + V_{\text{LED}}$)**: ________ Volts

### 🧩 Puzzle 1: The Reversed Diode Mystery
1. Unplug power. Flip the LED upside down so the **Cathode (-)** is on Row 9 and **Anode (+)** is on Row 10.
2. Re-apply power. Does the LED light up?  
   **Answer:** [ ] Yes  [ ] No
3. Measure the voltage across the flipped LED ($V_{\text{flipped}}$): ________ Volts.
4. **Question:** Why does a diode block current when reversed, and where did all the supply voltage go?  
   *Write your explanation in 1–2 sentences:*  
   ___________________________________________________________________________

---

## 🔬 Lab Stage 2: Resistance & Brightness (Ohm's Law in Action)

### Objectives:
- Test how changing resistance controls current flow ($I = \frac{V}{R}$).
- Calculate expected current using Ohm's Law and verify with your multimeter.

### 2.1 The Resistor Swap Test
Keep the LED circuit from Stage 1. You will test 3 different resistor values in series with the Red LED:

| Resistor Value | Color Bands | LED Brightness (Dim / Medium / Bright) | Measured Resistor Drop ($V_R$) | Calculated Current ($I = \frac{V_R}{R}$) | Measured Current ($mA$ in Series) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **220 Ω** | Red-Red-Brown-Gold | | _______ V | _______ mA | _______ mA |
| **1 kΩ (1,000 Ω)** | Brown-Black-Red-Gold | | _______ V | _______ mA | _______ mA |
| **10 kΩ (10,000 Ω)** | Brown-Black-Orange-Gold | | _______ V | _______ mA | _______ mA |

### 🧩 Puzzle 2: The Resistor Detective
Imagine you are building an artwork where an LED must stay dimly lit for 1 year on a small battery.
1. Which resistor value (220Ω, 1kΩ, or 10kΩ) draws the least amount of current from the battery?  
   **Answer:** ____________________
2. If an LED requires a forward voltage of $2.0\text{V}$ and you want exactly $10\text{mA}$ ($0.010\text{A}$) of current from a $3.3\text{V}$ power source, calculate the ideal resistor value using Ohm's Law ($R = \frac{V_{\text{supply}} - V_{\text{LED}}}{I}$):  
   $$R = \frac{3.3\text{V} - 2.0\text{V}}{0.010\text{A}} = \text{\_\_\_\_\_\_\_\_ }\Omega$$

---

## 🔬 Lab Stage 3: The Variable Dimmer (Potentiometer)

### Objectives:
- Wire a 10kΩ Rotary Potentiometer as a variable voltage divider.
- Understand wiper output voltage ($V_{\text{out}}$).

```text
[ 3.3V ] ---> Pin 1 (Potentiometer)
              Pin 2 (Wiper Output) ---> [ 220Ω Resistor ] ---> [ LED (+) -> (-) ] ---> [ GND ]
[ GND ]  ---> Pin 3 (Potentiometer)
```

### 3.1 Step-by-Step Build
1. **Miro Canvas**: Place `potentiometer_topdown_scaled.svg` on your Miro breadboard (Pins on Rows 15, 16, 17). Connect `3V3` to Row 15, Wiper Pin (Row 16) to 220Ω Resistor, and `GND` to Row 17.
2. **Physical Breadboard**: Build the physical circuit.
3. Turn the potentiometer dial all the way **counter-clockwise (0%)**, to the **middle (50%)**, and all the way **clockwise (100%)**.

### 3.2 Measurements
Connect DC Voltage probe to Wiper Pin (Row 16) and Black probe to GND:
- **Wiper Voltage at 0% Knob Turn:** ________ Volts (LED status: ________)
- **Wiper Voltage at 50% Knob Turn:** ________ Volts (LED status: ________)
- **Wiper Voltage at 100% Knob Turn:** ________ Volts (LED status: ________)

### 🧩 Puzzle 3: The Burnt Potentiometer Danger Trap
> [!WARNING]
> Look closely at the circuit diagram above. Notice that we kept a **fixed 220Ω resistor** in series between the Potentiometer Wiper and the LED.

**Question:** What would happen to the LED if you removed the 220Ω fixed resistor and turned the potentiometer knob all the way to 0Ω resistance?  
*Explain why a potentiometer alone cannot safely limit LED current at the end of its dial:*  
___________________________________________________________________________

---

## 🔬 Lab Stage 4: Light-Activated Sensor (LDR Photocell)

### Objectives:
- Measure how physical ambient light changes the resistance of a Light Dependent Resistor (LDR).
- Construct a light-sensing voltage divider circuit.

### 4.1 Measuring LDR Resistance (Power OFF!)
1. Disconnect USB power. Set multimeter to Resistance Mode ($20\text{k}\Omega$).
2. Connect multimeter probes directly to the 2 leads of your LDR:
   - **Ambient Room Light Resistance ($R_{\text{room}}$):** ________ kΩ
   - **Covered with Thumb / Dark Resistance ($R_{\text{dark}}$):** ________ kΩ
   - **Phone Flashlight Shined Directly / Bright Resistance ($R_{\text{bright}}$):** ________ kΩ

### 4.2 Light Divider Circuit Build
Wire the LDR in series with a 10kΩ fixed resistor:
```text
[ 3.3V ] ---> [ LDR Photocell ] ---> ( Node A ) ---> [ 10kΩ Fixed Resistor ] ---> [ GND ]
                                          |
                                 [ Multimeter Probe V_out ]
```

1. **Miro Canvas**: Place `ldr_topdown_scaled.svg` spanning Row 22 to Row 24. Place a 10kΩ resistor spanning Row 24 to GND. Connect `3V3` to Row 22.
2. **Physical Breadboard**: Assemble on breadboard and connect multimeter DC Voltage probe to **Node A (Row 24)**.

### 4.3 Voltage Divider Measurements
- **Output Voltage under Ambient Room Light ($V_{\text{room}}$):** ________ Volts
- **Output Voltage when LDR is Covered / Dark ($V_{\text{dark}}$):** ________ Volts
- **Output Voltage under Flashlight ($V_{\text{bright}}$):** ________ Volts

### 🧩 Puzzle 4: The Nightlight Inversion Challenge
1. In your circuit above, does the voltage at Node A **increase** or **decrease** when it gets dark?  
   **Answer:** ____________________
2. How would you swap the physical positions of the LDR and the 10kΩ resistor so that Node A voltage goes **HIGH** in the dark instead of in the light?  
   *Describe the physical change needed on your breadboard:*  
   ___________________________________________________________________________

---

## 🔬 Lab Stage 5: Pushbutton Momentary Control

### Objectives:
- Master the internal pin layout of a 4-pin tactile pushbutton.
- Prevent accidental power shorts across breadboard rows.

```text
[ 3.3V ] ---> [ Pushbutton Pin A1 ]
              [ Pushbutton Pin B1 ] ---> [ 220Ω Resistor ] ---> [ LED ] ---> [ GND ]
```

### 5.1 Step-by-Step Build
1. **Miro Canvas**: Place `pushbutton_topdown_scaled.svg` straddling the **center IC trough** of the breadboard (Pins 1 & 2 on Row 30 left/right; Pins 3 & 4 on Row 32 left/right).
2. **Physical Breadboard**: Insert the pushbutton into the breadboard center trough so its pins snap across the center divider.
3. Wire `3V3` to Row 30 Left. Connect Row 30 Right to 220Ω Resistor -> LED -> GND.

### 🧩 Puzzle 5: The Diagonal Pin Trap
Tactile pushbuttons have 4 legs, but internally they are paired into 2 connected rails!

```text
  Leg 1 [--- Internally Connected ---] Leg 2
                   |  (Switch Contacts)
  Leg 3 [--- Internally Connected ---] Leg 4
```

1. If you place a pushbutton on a single side of the breadboard without straddling the center trough, why might your LED stay stuck ON continuously even when you aren't pressing the button?  
   *Explain how breadboard terminal rows connect 5 holes vertically:*  
   ___________________________________________________________________________
2. **Final Verification**: Press the button. Does the LED turn ON only while held down?  
   [ ] Verified Clean Operation!

---

## 📝 Submission Checklist & Reflection

Before leaving lab, turn in your completed worksheet or upload to Canvas:

- [ ] Miro Canvas circuit diagrams created for Stages 1 through 5.
- [ ] Multimeter voltage, current, and resistance table completed.
- [ ] All 5 Circuit Puzzles answered.
- [ ] Hardware kit components cleaned and packed safely.
