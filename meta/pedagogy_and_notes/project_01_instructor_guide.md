# Project 1: Instructor Pedagogy & Facilitation Guide

**Course**: Device Art (PSAM 2230 | CRN 15895)  
**Instructor**: Ariel Churi  
**Milestone Window**: 2-Week Development Cycle (Launched Sep 30, Due Oct 14 at 19:00)  
**Deliverable Document (Student-Facing)**: [canvas/assignments/project_01_interactive_device_prototype.md](file:///Users/arielchuri/Life/projects/school/device-art/canvas/assignments/project_01_interactive_device_prototype.md)

---

## 1. Pedagogical Intent & Learning Objectives

Project 1 is the foundational inflection point of the course where students transition from discrete technical labs to integrated device thinking. 

### Core Conceptual Objective: Bridging UX Form and Electrical Logic
Novice physical computing students often treat hardware as an afterthought—building a breadboard mess and then attempting to cram it into an ill-fitting enclosure. 

This project intentionally decouples and parallels the design process:
1. **The Cardboard Paper Prototype**: Forces immediate confrontation with physical ergonomics, finger reach, label legibility, orientation, and interaction ritual without getting bogged down by electrical failures.
2. **The Breadboard Circuit**: Enforces rigor in electrical schematics, component ratings, and clean CircuitPython firmware architecture.
3. **The Mirroring**: The physical affordances designed into the cardboard box must correspond 1:1 with the logical states executed on the breadboard.

---

## 2. Hardware Constraints & Bill of Materials

### Required Baseline (Every Student)
- 1x Raspberry Pi Pico (pre-flashed with CircuitPython 8.x or 9.x)
- 1x Solderless Breadboard (830 or 400 tie-points)
- 1x Tactile Pushbutton (momentary)
- 1x 10k Ohm Rotary Potentiometer (breadboard-friendly terminal pitch)
- 1x Standard 5mm LED (digital indicator) + 1x 220 Ohm to 330 Ohm resistor
- 1x Standard 5mm LED (PWM output) + 1x 220 Ohm to 330 Ohm resistor
- Assorted jumper wires (male-to-male)
- 1x Small sturdy cardboard box (tea box, soap box, shipping carton, or craft cardstock)

### Optional Extensions (Permitted & Encouraged)
- **Photocell / LDR (Cadmium Sulfide cell)**: Paired with a 10k Ohm pull-down resistor in a voltage divider circuit into an ADC pin.
- **Piezo Buzzer / Speaker**: Wired to a PWM pin for audible frequency synthesis (`pwmio.PWMOut` with variable frequency).
- **Other Components**: Tilt sensors, slider pots, mechanical linkages, paper cut spring-loaded actuators.

---

## 3. Two-Week Studio Timeline & Milestone Plan

### Week 1 (Day 1 – Launch & Circuit Bench Testing)
- **Introduce Brief**: Review the prompt, emphasize that students define the identity and ritual of the device.
- **Studio Lab (Hands-on)**:
  - Bench-test the baseline circuit: Button to GP13, Potentiometer to GP26 (ADC0), Digital LED to GP14, PWM LED to GP15.
  - Review non-blocking loops with `time.monotonic()` vs blocking `time.sleep()`.
  - Pass around sample cardboard boxes and demonstrate rapid cardstock scoring, cutting, and typographic labeling.
- **Exit Ticket / Check-in**:
  - Each student demonstrates:
    1. A working REPL reading the potentiometer from 0 to 65535.
    2. A rough box mockup with penciled control locations.

### Week 2 (Day 2 – Final Assembly, Lab Support & Critique)
- **First 45 Minutes**: Desk check-ins for code bugs, jittery ADC values, and cardboard finishing.
- **Middle 60 Minutes**: Desk-side peer testing and exhibition:
  - Students place their cardboard box prototype alongside their working breadboard.
  - Peers physically hold and operate the cardboard prototype while watching the breadboard respond in real time.
- **Final 30 Minutes**: Video documentation and Canvas submission wrap-up.

---

## 4. Technical Pitfalls & Rapid In-Class Troubleshooting

### Common Student Mistakes

1. **ADC Wired to 5V (VBUS)**:
   - *Risk*: The Raspberry Pi Pico's RP2040 ADC inputs (GP26, GP27, GP28) have a maximum absolute rating of 3.3V. Connecting the outer leg of a potentiometer to VBUS (5V USB rail) will damage the ADC pin.
   - *Fix*: Verify that the potentiometer high-side is connected strictly to **Pin 36 (3V3 OUT)**.

2. **Floating Button Inputs**:
   - *Symptoms*: LED flickers randomly or button triggers when hands hover near the board.
   - *Fix*: In CircuitPython, ensure internal pull-up/down is explicitly declared:
     ```python
     button = digitalio.DigitalInOut(board.GP13)
     button.direction = digitalio.Direction.INPUT
     button.pull = digitalio.Pull.DOWN # or Pull.UP if switching to ground
     ```

3. **Missing Current-Limiting Resistors on LEDs**:
   - *Symptoms*: Dimmed Pico, board resets, or burnt-out LED.
   - *Fix*: Every discrete LED must have a 220 Ohm to 330 Ohm resistor in series on either the anode or cathode.

4. **Potentiometer ADC Jitter**:
   - *Symptoms*: PWM LED flickers when knob is held stationary.
   - *Fix*: ADC noise is normal on breadboards. Teach students simple integer division or threshold dampening:
     ```python
     # Downsample 16-bit reading to smooth jitter
     smoothed_val = (pot.value // 256) * 256
     ```

5. **Blocking `time.sleep()` Traps**:
   - *Symptoms*: Pressing the button does nothing unless held down for several seconds.
   - *Cause*: A long `time.sleep(1.0)` pauses execution, blinding the Pico to momentary input events.
   - *Fix*: Direct students to the `time.monotonic()` non-blocking pattern established in earlier labs.

---

## 5. Scaffolding Prompts for Stuck Students

If a student struggles with "What should my device be?", prompt them with these conceptual anchors:

- **Kenji Kawakami's Chindōgu Philosophy**: "Solve a very specific everyday minor inconvenience in a manner that creates new absurdities." (e.g., a device that forces you to turn a knob 100 times before unlocking a button).
- **Ritual & Behavior Regulation**: A personal device for setting an anxiety threshold or pacing breathing using a pulsing PWM light.
- **Speculative Diagnostic Tools**: An apparatus that measures an invisible metric (ambient room awkwardness, conversation fatigue, sunshine deficiency).
- **Physical Game or Micro-Challenge**: A reaction timer where the user must dial a knob to match a brightness target before hitting the button.

---

## 6. SpeedGrader Grading Guide (100 Points Total)

Use the Canvas SpeedGrader rubric with the following grading standards:

### 1. Cardboard Prototype & UX Design (30 Points)
- **27–30 pts**: Intentional craftsmanship. Box is cleanly cut, controls are seated securely, labeling is legible, and ergonomic affordances clearly explain how a human interacts with it.
- **21–26 pts**: Complete box with all controls represented. Cutouts might be slightly rough or labeling handwritten without hierarchy, but usability is clear.
- **15–20 pts**: Bare cardboard box with holes poked through; missing labels or confusing layout.
- **0–14 pts**: Incomplete or missing cardboard prototype.

### 2. Circuit Construction & Wiring (30 Points)
- **27–30 pts**: Exemplary breadboard layout. Jumper wires trimmed or flat, resistors correctly placed, no exposed uninsulated leads shorting, reliable electrical contacts.
- **21–26 pts**: Fully functional circuit with standard jumper nest. All required inputs and outputs respond reliably.
- **15–20 pts**: Intermittent wiring connections, missing pull-down resistors, or incorrect component wiring.
- **0–14 pts**: Circuit non-functional or missing required components.

### 3. CircuitPython Firmware & Logic (25 Points)
- **23–25 pts**: Clean, organized code. Clear variable names, sensible pin mappings, non-blocking timing, and thoughtful input-to-output behavioral logic.
- **18–22 pts**: Working code that achieves the interaction, but relies partly on blocking sleeps or lacks explanatory comments.
- **12–17 pts**: Code executes with bugs, input lag, or unstable state handling.
- **0–11 pts**: Syntax errors, unsubmitted code, or code from another assignment.

### 4. Documentation & Demonstration (15 Points)
- **14–15 pts**: Concise video (under 90 sec) showcasing both prototypes in operation. Clear photos and thoughtful interaction summary paragraph.
- **11–13 pts**: Complete submission; video or photos slightly out of focus or missing one detail.
- **7–10 pts**: Missing video or photos; inadequate explanation of the device.
- **0–6 pts**: Incomplete submission.
