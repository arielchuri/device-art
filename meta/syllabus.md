# Device Art

**Course Code**: PSAM 2230 | CRN 15895  
**Institution**: The New School | Parsons School of Design | School of Art, Media, and Technology (AMT)  
**Term**: Fall 2026 (August 26, 2026 – December 09, 2026)  
**Meeting Time**: Wednesday Evenings, 19:00 – 21:40  
**Location**: In-Person (TBD / Parsons Making Center & Computer Lab)  
**Instructor**: Ariel Churi  
**Email**: `ariel@sparklelabs.com` / `churia@newschool.edu`  
**Office Hours**: By appointment  

---

## Course Description

Device Art is a platform for students to invent new works of art that do not distinguish the object from a tool, the mechanism from the concept; through playfulness these devices are caught between definitions of art, design, and engineering. 

In this course devices are the artwork themselves; the mechanisms of the piece become part of the concept behind the work and the very essence of "making" and "play" is embedded in each of the pieces. Device Art can break the mold of art commercialization, propelled by the new forms of manufacturing and the ease of prototyping as production tools become more accessible. These artworks are easily replicable and can become commercialized, and even display features of playful utility for everyday life. 

Students will learn new methods for prototyping by combining new digital fabrication techniques as well as commonly used fabrication processes including repurposing readymades. They will explore their own artistic concepts and develop a deeper understanding of how their ideas can be reproduced. Device Art will challenge students to rethink their ideas of what art can become, and where the threshold lies between playfulness, utility, and conceptual inquiry. 

They will develop basic electronics and physical computing skills, such as microcontroller programming and circuitry design. They will engage in fabrication experiments to rethink and envision new devices that can facilitate invention from an artistic perspective, gaining new skills in device design, computing media, and device fabrication. They will use physical computing methods to expand on the field of open source hardware, learn interaction design methods and rapid prototyping tools for 3D printing. This course will provide a platform to enhance the design process of material experimentation and propel functional and accessible models of device art.

- **Prerequisites / Open To**: All university undergraduate degree students. Some seats reserved for BFA Design & Technology majors.

---

## Course Learning Outcomes (CLOs)

Upon successful completion of this course, students will be able to:

1. **Formulate Critical, Playful & Adversarial Device Concepts**: Situate physical computing artifacts within the intertwined traditions of *Device Art / Chindōgu* (whimsical absurdism) and *Disobedient Objects / Design Activism* (political resistance, anti-surveillance, counter-narratives), creating objects that interrogate power, labor, and cultural norms rather than merely serving commercial utility.
2. **Engineer Safe, Functional Embedded Electronic Systems**: Design, wire, test, and debug mixed-signal electronic circuits on breadboards and soldered proto-boards using digital multimeters, understanding fundamental principles of voltage, current, resistance, power regulation, and signal integrity.
3. **Program Responsive Microcontroller Behaviors**: Write modular, non-blocking code (CircuitPython / Python) to interface microcontrollers (Raspberry Pi Pico) with diverse sensor inputs (capacitive touch, photocells, ultrasonic rangefinders) and actuator outputs (OLED screens, addressable RGB LEDs, audio buzzers, servos) using finite state machine architectures.
4. **Execute Iterative Physical Enclosures & Mechanisms**: Translate initial conceptual sketches through iterative physical prototyping—progressing from rapid structural cardboard models to digital fabrication (laser cutting, 3D printing, casting/molding)—to produce durable, finished standalone device enclosures.
5. **Synthesize Technical & Visual Portfolio Documentation**: Produce professional portfolio-quality documentation, including wiring schematics, mechanical drawings, user-interaction flowcharts, and video demonstrations conveying the device's operational behavior and political/conceptual premise.

---

## Required Materials & Hardware Kit

Students are required to have a physical computing prototyping kit for benchwork in every class. 

- **Instructor-Provided Kit Bundle ($44.50)**: Pre-assembled wholesale kit available directly from the instructor (payable via Venmo, Zelle, PayPal, or cash).
- **Kit Contents**:
  - Raspberry Pi Pico (with pre-soldered headers)
  - Micro-USB cable & USB-A to USB-C adapter
  - Solderless breadboard & jumper wire bundle
  - Digital Multimeter (multitester)
  - SSD1306 OLED Display (128x64 I2C)
  - 2x NeoPixel RGB LEDs
  - 2x Capacitive Touch Sensor modules
  - Ultrasonic Rangefinder (HC-SR04)
  - DS3231 Real-Time Clock module
  - Light-Dependent Resistor (LDR / photocell)
  - 10k Potentiometer, Pushbutton switches, 8-ohm speaker
  - Assorted Resistors (100–220Ω, 1kΩ, 1MΩ)
- **Independent Sourcing**: Complete vendor links (Adafruit / Amazon) are available on Canvas for students who choose to source components independently.

---

## Grading Breakdown & Evaluation

| Component | Weight | Description |
| :--- | :---: | :--- |
| **Weekly Lab Exercises & Journals** | 20% | In-class circuit labs, code exercises, reading reflections, and process logs. |
| **Project 1: The "Unuseless" Apparatus (Chindōgu)** | 20% | A functional physical device solving an everyday problem through absurd engineering. |
| **Project 2: The Adversarial / Disobedient Object** | 20% | A physical artifact that resists compliance, exposes dark patterns, or jams surveillance. |
| **Final Capstone: Standalone Device Exhibition** | 30% | Fully fabricated, self-contained interactive device with complete portfolio documentation. |
| **Class Participation, Attendance & Critiques** | 10% | Active engagement in discussions, peer reviews, and studio workbench troubleshooting. |
| **Total** | **100%** | |

### Evaluation Criteria (Canvas 1-Click Rubrics)
All major assignments are evaluated using standardized rubrics in Canvas:
- **Conceptual Depth & Critical Inquiry (30%)**: Rigor of research, thematic clarity, and cultural/artistic provocation.
- **Technical Execution & Circuitry/Code (40%)**: Circuit stability, code architecture, sensor reliability, and electrical safety.
- **Physical Craft & Enclosure (20%)**: Structural integrity, material choice, finish quality, and mechanical durability.
- **Process Documentation (10%)**: Wiring schematics, mechanical drawings, process photos, and clear demonstration video.

---

## Course Schedule & Assignments

### Phase 1: Foundations, Electronics & Chindōgu (Weeks 01–05)

#### Week 01 (Aug 26): The Premise of Device Art & The Art of the Unuseless
- **In-Class**: Course introduction, passing around physical working artifacts (Buddha Box, optical shutters), live 5-minute Pico CircuitPython demo, hardware kit distribution.
- **Readings**:
  - Machiko Kusahara, *Device Art: A New Form of Media Art from a Japanese Perspective* (2006)
  - Kenji Kawakami, *The 10 Tenets of Chindōgu*
- **Assignment 01 (Due Week 02)**: **Hardware Audit & Initial Idea Board** (10 pts)
  - Verify your hardware kit, set up Mu Editor / VS Code with CircuitPython on your computer, and post 3 concept sketches of everyday frictions to the Canvas discussion board.

#### Week 02 (Sep 02): Electricity Fundamentals & Structural Cardboard Engineering
- **In-Class**: Voltage, current, resistance, Ohm's law heuristics, multimeter diagnostics (continuity, resistance, voltage testing). Cardboard cutting techniques, folded chassis, internal mounting tabs.
- **Readings**: Charles Platt, *Make: Electronics* (Experiments 1–4); Forrest Mims, *Getting Started in Electronics*.
- **Assignment 02 (Due Week 03)**: **Cardboard Chassis & Analog Circuit** (100 pts)
  - Fabricate a structural cardboard enclosure housing a basic LED/switch circuit with proper strain relief and battery access.

#### Week 03 (Sep 09): Microcontrollers, CircuitPython & Digital I/O
- **In-Class**: Raspberry Pi Pico pinout, writing non-blocking CircuitPython event loops, digital input (pushbuttons, debouncing) and digital output (LEDs, buzzers).
- **Readings**: Tom Igoe & Dan O'Sullivan, *Physical Computing* (Chapters 1–3).
- **Assignment 03 (Due Week 04)**: **Microcontroller State Trigger** (100 pts)
  - Program the Pico to monitor a physical switch and execute a multi-stage light/sound pattern.

#### Week 04 (Sep 16): Sensors & Dynamic Feedback (OLED & NeoPixels)
- **In-Class**: Analog-to-digital conversion (ADC), photocells, capacitive touch pads, ultrasonic distance sensing, I2C bus wiring for SSD1306 OLED displays.
- **Readings**: Johan Huizinga, *Homo Ludens: A Study of the Play-Element in Culture*; Kelli Anderson, *Curious Things for Curious People*.
- **Assignment 04 (Due Week 05)**: **Project 1 Submission — The "Unuseless" Apparatus** (100 pts)
  - Deliver a working physical Chindōgu device combining sensor input, microcontroller logic, and custom cardboard/physical housing.

#### Week 05 (Sep 23): Project 1 Critiques & Transition to Subversion
- **In-Class**: Full class physical demonstration and critique of Project 1. Deconstructing commercial consumer gadgets vs. tactical media.

---

### Phase 2: Resistance, Finite State Machines & Mechanisms (Weeks 06–10)

#### Week 06 (Sep 30): Finite State Machines & Complex Behaviors
- **In-Class**: Designing multi-state embedded behaviors (`IDLE`, `TRIGGERED`, `DEFENSIVE`, `RESET`), non-blocking timers with `time.monotonic()`.
- **Readings**: Catherine Flood & Gavin Grindon, *Disobedient Objects* (V&A); Harry Brignull, *Dark Patterns*.
- **Assignment 05 (Due Week 07)**: **State Machine Interaction Flowchart & Breadboard Lab** (100 pts)
  - Implement a 3-state interactive behavioral loop on your breadboard.

#### Week 07 (Oct 07): Mechanical Movement & Actuation (Servos & Solenoids)
- **In-Class**: Pulse-Width Modulation (PWM), standard and continuous rotation servos, mechanical linkages, cams, and lever arms.
- **Readings**: Alastair Fuad-Luke, *Design Activism: Beautiful Strangeness for a Sustainable World*.
- **Assignment 06 (Due Week 08)**: **Mechanical Linkage Prototype** (100 pts)
  - Build a motor-driven mechanism that physically moves, covers, reveals, or alters a physical interface.

#### Week 08 (Oct 14): Project 2 Midterm Critiques — The Adversarial / Disobedient Object
- **In-Class**: Midterm presentations and live demonstrations of Project 2: A device that playfully resists compliance, jams tracking, or critiques institutional surveillance.
- **Assignment 07 (Due Week 08)**: **Midterm Project 2 Documentation** (100 pts)
  - Submit working video, wiring diagram, and conceptual reflection.

#### Week 09 (Oct 21): Casting, Molding & Advanced Materiality
- **In-Class**: Silicone two-part molds, resin casting, urethane rubbers, embedding electronics directly inside cast materials.
- **Readings**: Anthony Dunne & Fiona Raby, *Speculative Everything*.
- **Assignment 08 (Due Week 10)**: **Final Project Proposal & Bill of Materials (BOM)** (10 pts)
  - Submit 2-page design brief, system block diagram, and complete parts sourcing list.

#### Week 10 (Oct 28): System Architecture & User Persona Mapping
- **In-Class**: One-on-one desk crits, mechanical tolerance verification, power budget calculations (battery vs. wall power).

---

### Phase 3: Final Fabrication, Exhibition & Documentation (Weeks 11–15)

#### Week 11 (Nov 04): Prototype 1 Bench Testing (Breadboard + Chassis)
- **In-Class**: Hands-on studio workbench testing. Bench-check of all sensors, power rails, and primary code logic.
- **Assignment 09 (Due Week 12)**: **Prototype 1 Working Video Check-In** (100 pts)

#### Week 12 (Nov 11): Prototype 2 Digital Fabrication (Soldering & Precision Enclosures)
- **In-Class**: Point-to-point soldering on proto-boards, wire harness routing, laser-cutter kerf compensation, 3D print print-in-place tolerances.
- **Assignment 10 (Due Week 13)**: **Assembled Physical Enclosure Check-In** (100 pts)

#### Week 13 (Nov 18): Mechanical Refinement & Studio Troubleshooting
- **In-Class**: Enclosure assembly, hardware deburring, surface finishing, strain relief, code optimization.
- **Readings**: Stephanie Houde & Charles Hill, *What Do Prototypes Prototype?*

*(Nov 25: Thanksgiving Eve — No Class)*

#### Week 14 (Dec 02): Final Rehearsal & Documentation Staging
- **In-Class**: Studio product photography lighting setup, shooting high-frame-rate video demos, generating exploded-view mechanical drawings and Fritzing/KiCad schematics.

#### Week 15 (Dec 09): Final Exhibition & Public Critiques
- **In-Class**: Final exhibition of fully operational Device Art capstone artifacts, peer critiques, and public showcase.
- **Assignment 11 (Due Dec 16)**: **Final Comprehensive Portfolio Documentation** (300 pts)
  - High-res product photos, exploded-view drawing, schematic diagram, 60-second video demo, and GitHub/web process archive.

---

## Course Policies & Academic Guidelines

### Attendance & Participation
Class time is dedicated studio workbench time. Attendance is recorded at the start of each session on Canvas. More than two unexcused absences will result in a reduction of the final course grade.

### Lab Safety & Tool Etiquette
Always wear eye protection when cutting, stripping wire, or soldering. Never leave soldering irons unattended. Clean your workbench and return all shop tools to their designated storage bins before leaving the studio.

### Academic Integrity
Students are encouraged to borrow, adapt, and learn from open-source hardware and software libraries (e.g. Adafruit CircuitPython libraries), provided that **all external sources, code repositories, and circuit designs are properly credited and cited in your documentation**. Presenting someone else's physical device or uncredited code as your original design is a violation of university policy.
