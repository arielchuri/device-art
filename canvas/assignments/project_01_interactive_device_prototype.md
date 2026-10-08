---
title: "Project 1: Interactive Device Prototype (Cardboard & Breadboard)"
module: "Week 08"
points_possible: 100
due_at: "2026-10-14 19:00"
submission_types: ["online_upload", "online_url"]
allowed_extensions: ["pdf", "zip", "mp4", "py", "mov"]
published: false
---

# Project 1: Interactive Device Prototype (Cardboard & Breadboard)

- **Due Date**: Wednesday, October 14, 2026 at 7:00 PM (Week 08)
- **Points**: 100 Points
- **Submission Type**: Online File Upload (Code, Photos, Video Demonstration) or URL (GitHub/Documentation link)

---

## Project Overview

In this project, you will bridge physical user experience (form, ergonomics, tactile affordances) and embedded electronic behavior. You will conceptualize an interactive device of your own design and build two parallel prototypes that mirror each other:

1. **The Paper & Cardboard Prototype**: A physical mock-up constructed from a small cardboard box. This prototype defines the form factor, tactile controls, labeling, ergonomics, and physical affordances. It communicates to a human user how the device is held, approached, and operated.
2. **The Functional Breadboard Prototype**: The matching electronic circuit wired on your solderless breadboard, controlled by the Raspberry Pi Pico running CircuitPython. This prototype executes the working logic, sensing user inputs, processing state changes, and driving output feedback.

You decide what the device is, what problem or absurd ritual it addresses, and how it behaves. The output indicator (LEDs or optional speaker) must make it clear that the device is running, in what state it currently resides, and how it responds to the user.

---

## Component Constraints

### Required Hardware
Your breadboard circuit and cardboard prototype must incorporate the following core elements:

- **1x Pushbutton**: Digital input (momentary switch wired with pull-down or internal pull-up resistor) for triggering actions, toggling states, or momentary engagement.
- **1x Potentiometer**: Analog input (ADC) for continuous rotary control (e.g., threshold tuning, speed adjustment, intensity setting).
- **1x Digital Indicator LED**: Visual digital output showing power, operational readiness, or boolean state (with appropriate current-limiting resistor, 220 Ohm to 330 Ohm).
- **1x PWM LED**: Visual variable output using Pulse Width Modulation to express continuous state changes, pulsing rhythms, or responsive brightness curves.
- **1x Raspberry Pi Pico**: Running CircuitPython to govern logic and input/output communication.
- **1x Solderless Breadboard & Jumper Wires**: For clean, testable circuit wiring.

### Optional & Extensible Components
You may optionally incorporate additional components if your interaction concept calls for them:

- **Light Sensor (Photocell / LDR)**: Analog input (ADC via voltage divider) to make the device responsive to ambient environmental light or shadow gestures.
- **Piezo Speaker / Buzzer**: Auditory output (PWM tone generation) for audible state chimes, alarms, or sonic feedback.
- **Other Unspecified Components**: Tilt switches, additional LEDs, mechanical linkages, slide switches, or capacitive touch surfaces.

---

## Prototype Requirements

### 1. The Paper & Cardboard Box Prototype (Form & UX)
- Construct your enclosure using a small, sturdy cardboard box (e.g., small mailing box, tea box, soap box, or card box).
- Layout your interface deliberately: consider how hands grip the object, which fingers reach the button, and where indicator lights are visible.
- Cut and mount paper/cardboard representations of every control:
  - Mark or install the button location.
  - Mark or install the rotary knob/potentiometer.
  - Indicate LED apertures or light pipes.
  - If using sensors or speakers, create grills, bezels, or sightlines for them.
- Include clear, intentional typographic labeling and visual graphics directly on the cardboard (hand-drawn, stenciled, or printed paper glued to the surface).

### 2. The Breadboard Prototype (Electronics & Logic)
- Wire the corresponding physical circuit on your breadboard cleanly.
- Keep wire routing low to the board using appropriate jumper lengths.
- Write modular, well-commented CircuitPython code (`code.py`):
  - Configure pins cleanly with descriptive variable names.
  - Implement a defined state machine or interaction logic.
  - Map analog input values (potentiometer readings) to meaningful output behaviors (such as PWM duty cycle or timing parameters).
  - Use non-blocking timing with `time.monotonic()` where multiple behaviors occur concurrently (avoid blocking `time.sleep()` for primary loops).
  - Provide continuous visual (or audio) confirmation that the device is running.

---

## Step-by-Step Milestones

### Week 1 (Milestone Check-in): Concept, Layout & Circuit Bench Test
- Define your device concept and write down its interaction loop: What is the object? Who operates it? What does each input do, and what does the output communicate?
- Wire the button, potentiometer, and both LEDs on the breadboard. Verify in the serial REPL that inputs read reliably and outputs illuminate as expected.
- Sketch the faceplate and control layout onto your cardboard box.

### Week 2 (Final Assembly & Documentation): Fabrication & Integration
- Finish the cardboard box enclosure, including cutouts, labels, and physical controls.
- Refine the CircuitPython firmware to implement complete interaction states and feedback responses.
- Test both prototypes side by side to ensure the breadboard's electrical behavior directly matches the affordances presented on the cardboard model.
- Record your demonstration video and capture documentation photos.

---

## Submission Deliverables

Upload the following materials to Canvas before the deadline:

1. **CircuitPython Code (`code.py`)**:
   - The complete, working script running on your Pico. Must include comments explaining pin assignments, state variables, and input-to-output mapping logic.
2. **Cardboard Prototype Photographs**:
   - At least 2 clear, well-lit photos showing:
     - Isometric/front view showing overall form and control placements.
     - Detail view of labels, cutouts, and tactile interfaces.
3. **Breadboard Circuit Photograph**:
   - 1 clear top-down photo of your wired breadboard showing component placement and organized jumper wire layout.
4. **Demonstration Video (30 to 90 seconds)**:
   - A short, clear video showing the interaction in action. Demonstrate:
     - The physical cardboard prototype and its intended interaction ritual.
     - The working breadboard circuit responding to button presses, potentiometer adjustments, and status LED/PWM output changes.
   - You may demonstrate them side-by-side on your desk.
5. **Interaction Summary (1 to 2 paragraphs)**:
   - Name and purpose of the device.
   - Explanation of the mapping: what does the button do, what does the potentiometer modulate, and what do the indicator LED and PWM LED communicate?

---

## Evaluation Rubric

| Criteria | Exceptional (Full Marks) | Proficient | Developing | Unsatisfactory | Points |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Cardboard Prototype & UX Design** | Enclosure is thoughtfully crafted with precise cutouts, clear labeling, intentional ergonomics, and strong tactile affordances that communicate how the device is operated. | Enclosure is complete with controls placed and labeled; minor rough edges in craft or ergonomics. | Basic box with minimal labeling or loose controls; interaction affordances are ambiguous. | Incomplete, missing box prototype, or controls are unlabeled and non-functional in concept. | 30 |
| **Circuit Construction & Wiring** | Clean, stable breadboard circuit with correct resistor values (220-330 Ohm for LEDs), proper analog wiring, secure jumpers, and reliable electrical connections. | Circuit works reliably; wiring is slightly crowded or disorganized, but all required components are operational. | Intermittent electrical connections, missing pull-down/pull-up, or incorrect component wiring requiring manual intervention. | Circuit does not function, missing required components, or short circuits present. | 30 |
| **CircuitPython Firmware & Logic** | Well-structured, readable code with descriptive variable names, non-blocking timing, clear input-to-output mapping, and active device state indication. | Code functions correctly; mappings work as described; minor reliance on blocking `time.sleep` or sparse comments. | Code executes partially; input responses are erratic or poorly mapped; limited commenting. | Code fails to execute or syntax errors prevent microcontroller operation. | 25 |
| **Documentation & Video Demonstration** | Video clearly demonstrates both cardboard affordances and breadboard responsiveness; well-lit photos; concise, articulate interaction summary. | Video and photos present and demonstrate working device; minor gaps in description or video framing. | Video is unclear, blurry, or missing demonstration of either the box or breadboard prototype. | Missing video, missing photos, or deliverables omitted. | 15 |
| **Total** | | | | | **100** |
