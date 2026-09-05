# Device Art Session Note — Hardware Kit, Roster & Miro Canvas Updates

**Date**: September 2, 2026  
**Course**: Device Art (Course ID: `1929836`)  
**Instructor**: Ariel Churi  

---

## 1. Hardware Kit & Financial Updates
- **Materials Zelle Email**: Updated to `money@sparklelabs.com` across all local markdown files and live Canvas assignment `15087096` (`assignment_01_hardware_kit_readiness.md`).

---

## 2. Student Roster & Dossiers (Fall 2026)
- **Active Enrolled Roster**: **14 Active Students**.
  - Dossiers updated in `Life/projects/work/device-art/meta/terms/fall2026/people/*.md`.
  - Portraits extracted & added for all students (including PDF & Google Doc submissions).
- **Dropped Students**: 6 dropped students moved to `Life/projects/work/device-art/meta/terms/fall2026/people/dropped/`.
- **Student SVG Cards Folder (`svg_cards/`)**: Cleaned up to contain **EXACTLY 14 student cards**:
  - Location: `Life/projects/work/device-art/meta/terms/fall2026/people/svg_cards/`
  - Relocated non-student cards: `instructor_card.svg` and `all_students_roster_grid.svg` placed in `people/`.

---

## 3. Solderless Breadboard & Row Line Numbers
- **Row Numbers (1 to 63)**: Added left-aligned row numbers along the vertical channel in `Andale Mono` monospace typography (`#888888`, 8px).
- **Row Pitch Calibration**: Exactly calibrated at **18.593 px per row/hole (0.1" pitch)** across `solderless_breadboard.svg` and `construction-doc_breadboard.svg`.

---

## 4. Miro Device Canvas Architecture Reorganization
Reorganized `Life/projects/work/device-art/meta/pedagogy_and_notes/miro_device_canvas/` into 3 clean top-level directories:

```text
Life/projects/work/device-art/meta/pedagogy_and_notes/miro_device_canvas/
├── package_components/         # 1:1 Breadboard-scaled physical hardware SVGs
│   ├── breadboards/            # Solderless breadboard vector models
│   ├── inputs_controls/        # Resistors (top/side), pots (top/side), buttons (top/side), LDR
│   ├── microcontrollers/       # Raspberry Pi Pico (top-down DIP-40), RTC DS3231
│   ├── outputs_displays/       # LEDs (top/side), OLED SSD1306, Piezo Speaker
│   └── sensors_environment/    # Ultrasonic HC-SR04, Capacitive Touch TTP223
├── modular_cards/              # 200x200 Miro schematic cards (categories 01 to 08 + ports)
└── showcases/                  # Grid overview reference sheets
```

*Note: Cleaned up all legacy unorganized staging folders (`svg_components_staging*`).*

---

## 5. Live Code Teaching & Real-Time Student Visibility
Created a dedicated live teaching guide and automated dashboard:
- **Guide Location**: `Life/projects/work/device-art/meta/pedagogy_and_notes/live_code_teaching_guide.md`
- **Live Code Monitor Script**: `Life/projects/work/device-art/admin/live_code_monitor.py`
  - Launches a 14-student live code wall displaying student avatars, online status, and CircuitPython `code.py` scripts side-by-side for studio projector display.
- **Teaching Workflows**:
  1. **VS Code Live Share**: Best for live lectures, demonstrations, and paired debugging.
  2. **Live Code Wall**: Best for studio workshops and side-by-side code visibility.
  3. **Shared Scratchpad**: Best for 5-minute micro-challenges.
