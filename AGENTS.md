# AGENTS.md — Device Art Repository Guide & Agent Vocabulary

## 1. Project Overview & Institutional Context

- **Course**: Device Art (Course ID: `1929836`)
- **Institution**: The New School / Parsons School of Design (Fall 2026)
- **Instructor**: Ariel Churi (`ariel@sparklelabs.com` / `churia@newschool.edu`)
- **Payment / Materials Email**: `money@sparklelabs.com` (Zelle / PayPal)

---

## 2. Strict AI Assistant Boundaries (Instructor-Led Pedagogy)

1. **No Synthetic IP / Artistic Concepts**:
   - The instructor designs, writes, and directs all pedagogy and artistic direction.
   - The AI must **never** invent synthetic creative projects, fictional devices, or course philosophies.
   - When illustrating technical possibilities, refer only to established historic artworks (e.g., Maywa Denki, Natalie Jeremijenko, Kenji Kawakami, Bill Vorn) or describe capabilities in abstract engineering terms.
2. **Relegated AI Responsibilities**:
   - **Housekeeping**: Formatting tables, organizing assets, linting, mirroring files.
   - **Management**: Structuring announcements, sorting rosters, updating attendance ledgers.
   - **Calculations**: Grade conversions, attendance percentage tallies, schedule date alignment.
   - **Canvas Sync**: Updating assignments, rubrics, pages, and discussions via Canvas LMS API.
3. **Explicit Permissions**:
   - Do **NOT** publish to Canvas or modify existing curriculum files without explicit user instruction.

---

## 3. Core Domain Vocabulary & Glossary

### Physical Computing & Electronics
- **Raspberry Pi Pico (RP2040)**: Dual-core ARM Cortex-M0+ microcontroller development board in a 40-pin DIP package (0.6" pin row span, 0.1" / 2.54mm pitch). Operates at 3.3V logic.
- **Solderless Breadboard**: 830 tie-point prototyping platform. Consists of:
  - Two 5-hole terminal strip columns per row (numbered **Row 1 to Row 63**), separated by a central IC trough.
  - Dual positive (`+` red) and negative (`-` blue) power distribution rails on both outer edges.
  - Standard vertical pitch: ~18.593 px in SVG canvas coordinate space.
- **CircuitPython / MicroPython**: Python runtime used on the Pico for interactive hardware programming and REPL prototyping.
- **I2C (Inter-Integrated Circuit)**: 2-wire serial protocol (SDA data, SCL clock) used for displays (SSD1306) and real-time clocks (DS3231).
- **SPI (Serial Peripheral Interface)**: Synchronous serial communication (SCK, TX/MOSI, RX/MISO, CS).
- **PWM (Pulse Width Modulation)**: Technique for simulating analog output (controlling LED brightness, audio tone synthesis, servo angles).
- **ADC (Analog-to-Digital Converter)**: Pins GP26 (ADC0), GP27 (ADC1), GP28 (ADC2) for reading continuous voltages from sensors (potentiometer, light sensor).

### Device Art & Critical Interaction Theory
- **Device Art**: An art movement and design philosophy where the physical mechanism, tangible interface, and technical enclosure *are* the artwork itself, challenging passive consumer technology.
- **Chindōgu**: The Japanese art of "un-useless" inventions pioneered by Kenji Kawakami—objects that solve a specific problem but introduce new absurdities.
- **Disobedient Objects**: Everyday or modified objects adapted for political protest and social resistance, subverting conventional user experiences.
- **Maywa Denki**: Art unit known for "Nonsense Machines" and electromechanical musical toys (e.g., Otamatone, Bitman).

---

## 4. Miro Device Canvas Visual Design System

The SVG component library under `meta/pedagogy_and_notes/miro_device_canvas/` provides a standardized visual language for diagrams, state machines, and hardware mapping in Miro and Figma:

- **Dimensions**:
  - Modular cards: `200x200` viewBox with sharp corners or subtle outer borders.
  - Breadboard: `429.59 x 1220.14` viewBox with numbered rows (1 to 63).
  - Scaled Hardware Components (e.g., `pico_breadboard_scaled.svg` / `raspberry_pi_pico_topdown.svg`): Exactly calibrated to match the breadboard row pitch (~18.593 px).
- **Typography**:
  - Font Family: `'Andale Mono', monospace` across all labels, pin numbers, and code blocks.
- **Color Coding & Patterns**:
  - Signal / GPIO: `#2F7EB8` (Cobalt Blue)
  - Power / VBUS / 3V3 / VSYS: `#D40000` (Red)
  - Ground (GND): `#000000` (Solid Black)
  - Chips / ICs: 45-degree monochrome diagonal hatching (`url(#hatch)`).
  - Sub-labels / Notes: `#888888` / `#777777`.

---

## 5. Repository Structure & Source-of-Truth Layout

```text
device-art/
├── AGENTS.md                               # Guide and vocabulary specification
├── CLAUDE.md                               # AI boundaries and instructor pedagogy rules
├── canvas/                                 # Canvas LMS mirror (Source-of-Truth)
│   ├── assignments/                        # Assignment markdown files with rubric tables
│   ├── files/                              # Course materials and media assets
│   ├── pages/                              # Canvas wiki pages (materials list, cheat sheets)
│   └── syllabus/                           # Course syllabus
├── meta/
│   ├── terms/fall2026/
│   │   ├── people/                         # Active student dossiers (*.md) and portraits (*.jpg)
│   │   │   ├── dropped/                    # Archived dossiers of dropped students
│   │   │   └── svg_cards/                  # 200x200 Miro student cards & combined grid
│   │   └── attendance/                     # attendance_ledger.md (roll call tracking)
│   └── pedagogy_and_notes/
│       └── miro_device_canvas/             # Miro SVG visual library
│           ├── package_components/         # 1:1 Breadboard-scaled hardware (Pico, ICs, LEDs, pots)
│           │   ├── breadboards/            # Breadboard vector models
│           │   ├── inputs_controls/        # Resistors, pots, switches, LDR
│           │   ├── microcontrollers/       # Raspberry Pi Pico, RTC DS3231
│           │   ├── outputs_displays/       # LEDs, OLED SSD1306, Speaker
│           │   └── sensors_environment/    # Ultrasonic HC-SR04, Touch TTP223
│           ├── modular_cards/              # 200x200 Miro schematic concept cards (01 to 08 + ports)
│           └── showcases/                  # Grid overview reference sheets
└── admin/
    ├── canvas_sync.py                      # Canvas LMS REST API synchronization script
    ├── generate_student_cards.py           # Miro student SVG card generator
    └── take_attendance.py                  # Interactive CLI roll-call with terminal avatars
```

---

## 6. Canvas API Synchronization Protocol

- **Course ID**: `1929836` (The New School)
- **Authentication**: `CANVAS_API_TOKEN` loaded from `.env` or system environment.
- **Endpoints**:
  - `GET /api/v1/courses/1929836/assignments`
  - `PUT /api/v1/courses/1929836/assignments/:id`
  - `GET /api/v1/courses/1929836/discussion_topics`
  - `GET /api/v1/courses/1929836/pages`
  - `GET /api/v1/courses/1929836/users?enrollment_type[]=student`


---

## 7. File Path Formatting Rule

- **Paths inside `Life` directory**: Always write paths starting from `Life/` (e.g., `Life/projects/work/device-art/...`).
- **Paths outside `Life` directory**: Use `~` prefix (e.g., `~/.env`, `~/.gemini/...`).
