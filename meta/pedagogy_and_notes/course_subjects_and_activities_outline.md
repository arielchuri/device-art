# Comprehensive Course Outline: Subject Areas & Associated Activities

> **Primary Use**: A thematic reference mapping all 6 core subject domains (electronics, microcontrollers, sensing/actuation, enclosure craft, critical theory, major projects) to their specific hands-on labs and studio deliverables.

Synthesized across **Device Art**, **Emergent Objects**, and **School Memory Notes**, the curriculum breaks down into **6 core subject areas**. Each area pairs theoretical conceptual lenses with hands-on technical labs, studio exercises, and project deliverables.

---

## 1. Physical Computing & Electronics Fundamentals

### Core Concepts & Theory
- **Electrical Substrate**: Voltage ($V$), Current ($I$), Resistance ($R$), Ohm's Law ($V = I \times R$), and power regulation.
- **Circuit Topology**: Series vs. parallel circuits, common ground, pull-up/pull-down resistors, signal integrity, and logic levels (3.3V vs 5V).
- **Measurement & Diagnostics**: Reading schematics, using multimeters to test continuity, voltage drops, and current draw.

### Associated Activities & Labs
* **Lab 01: Breadboard Electricity Puzzles**: Hands-on breadboard wiring challenges routing power through switches, LEDs, and potentiometers.
* **Multimeter Workshop**: Measuring unknown resistor color codes, diagnosing short circuits, and probing live breadboard rails.
* **Circuit Plan Diagramming**: Translating physical breadboards into standardized schematic notation.

---

## 2. Embedded Software & Microcontroller Programming (Pico & CircuitPython)

### Core Concepts & Theory
- **Microcontroller Architecture**: Dual-core RP2040, GPIO pinout mapping, ADC (analog inputs), PWM (pulse-width modulation), and hardware serial protocols (I2C, SPI).
- **Interactive Scripting**: CircuitPython runtime execution loop (`while True`), non-blocking delays using timestamps, and state tracking.
- **Finite State Machine (FSM) Logic**: Designing state transition tables for complex device behaviors (e.g. `IDLE` $\to$ `TRIGGERED` $\to$ `COOLDOWN`).

### Associated Activities & Labs
* **Dev Environment Setup**: Installing CircuitPython on Raspberry Pi Pico, configuring Mu Editor / VS Code, and interacting via REPL.
* **Python Age Validator / Logic Challenge**: Writing interactive Python logic handling conditional branching and string inputs.
* **Digital I/O & PWM Labs**: Blinking LEDs, synthesizing variable brightness curves, and driving piezo speakers/buzzer tones.
* **State Machine Coding Assignment**: Building an explicit FSM script controlling multi-stage device behaviors based on button holds or sensor thresholds.

---

## 3. Sensing, Display & Actuation (Inputs & Outputs)

### Core Concepts & Theory
- **Analog Sensing**: Reading continuous physical signals via ADC (photocells/LDRs, potentiometers, analog distance sensors).
- **Capacitive Touch & Digital Sensors**: Human-interface touch sensing (TTP223 / built-in capacitive touch), ultrasonic pulse timing (HC-SR04), and ambient environmental sensing.
- **Visual & Acoustic Output**: I2C OLED display driving (SSD1306, rendering text/graphics), addressable RGB LED pixels (NeoPixels/WS2812B), and electromechanical movement (servos, solenoids, DC motors).

### Associated Activities & Labs
* **Analog-In & Sensor Calibration Lab**: Mapping raw 16-bit ADC values (`0–65535`) to normalized output ranges (e.g. LED brightness or servo angles).
* **Capacitive Touch Experimentation**: Building custom copper-tape touch pads and conductive object interfaces.
* **OLED & Graphical Interface Lab**: Writing custom display code to render real-time sensor graphs, state icons, and diagnostic menus.
* **Moodlight / Acoustic Actuation Lab**: Wiring and programming an interactive light or sound device responding to physical environmental triggers.

---

## 4. Physical Enclosure Craft, Digital Fabrication & Hardware Prototyping

### Core Concepts & Theory
- **Rapid Low-Fidelity Prototyping**: Structural cardboard engineering, paper prototyping, living hinges, and spatial layout planning for electronics.
- **Digital Fabrication & 3D CAD**: Constructive Solid Geometry (CSG) modeling using primitives and Boolean operations (Blender / Fusion 360) for 3D printing (`.stl`/`.3mf`), and 2D vector layout for laser cutting.
- **Enclosure Assembly & Solder Craft**: Transitioning from temporary breadboards to permanent perfboards/custom PCBs, strain relief, battery power integration, and casting/molding techniques.

### Associated Activities & Labs
* **Cardboard Engineering Workshop**: Rapidly building scale physical enclosures out of chipboard, foamcore, and structural card stock to house breadboards and switches.
* **Blender 3D Device Modeling Assignment**: Designing a 3D printable device housing utilizing only primitives and Boolean difference cuts for screens, buttons, and ports (utilizing [remotelab.newschool.edu](https://remotelab.newschool.edu) for rendering).
* **Enclosure Build Lab**: Drilling, soldering, heat-shrinking wires, and mounting components into final physical chassis.

---

## 5. Critical Interaction Theory, Chindōgu & Subversive Design

### Core Concepts & Theory
- **Device Art Movement**: Challenging passive commercial tech by embedding the concept, physical mechanism, and tangible interface directly into the artwork itself (Kusahara, Maywa Denki, Toshio Iwai).
- **Chindōgu ("Unuseless" Inventions)**: Kenji Kawakami’s 10 tenets of Chindōgu—creating physical objects that solve specific everyday problems but introduce new absurdities or social dilemmas.
- **Disobedient Objects & Adversarial Design**: Tactical media, design activism, anti-surveillance artifacts, and subverting corporate "dark patterns" through physical resistance.

### Associated Activities & Labs
* **Speculative Device Miro Vignette Exercise**: Generating 3-layer prompt narratives (*The World, The Human Tension, The Object Ritual*) and mapping device state flows in Miro.
* **Chindōgu Concept Sketches**: Drafting mechanical drawings of absurd, playful, or "unuseless" physical mechanisms.
* **Utopia / Dystopia & Persona Mapping**: Writing cultural probe scenarios, user journeys, and speculative product sell-sheets for subversive devices.

---

## 6. Major Milestone Projects & Studio Deliverables

| Milestone | Project Title | Core Focus & Integrated Subjects | Key Deliverable |
| :--- | :--- | :--- | :--- |
| **Project 1** | **The "Unuseless" Interactive Device** *(Chindōgu)* | Physical computing basics, Pico/CircuitPython, sensors, cardboard chassis, and playful absurdist theory. | Functional prototype + 2D/3D physical housing + code repository. |
| **Project 2** | **The Disobedient / Adversarial Object** | Advanced FSM logic, analog sensors, I2C OLED/actuators, digital fabrication (3D/laser), and critical design. | Working mechatronic device exposing or resisting automated/surveillance systems. |
| **Final Capstone**| **Standalone Device Art Capstone Exhibit** | Complete synthesis of mechatronics, permanent soldering, custom finished enclosure, exploded-view diagrams, and studio video docs. | Portfolio-grade physical artwork + short product video + technical documentation. |
