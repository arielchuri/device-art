# Device Art — Internal Repository Index (Non-Student Facing)

> **Assistant Maintenance Instruction**:  
> Keep this file updated whenever new internal notes, scripts, dossiers, or pedagogical reference files are created, renamed, or restructured in `meta/` or `admin/`.

This index catalogs backstage instructor notes, planning documents, student dossiers, reference readings, and administrative tools that are **not student-facing**.

---

## 1. Core Instructor Manuals & Governance

- [meta/INSTRUCTOR_MANUAL.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/INSTRUCTOR_MANUAL.md) — Weekly teaching rhythm, 1-click SpeedGrader rubric protocol, and file privacy guidelines.
- [meta/weekly-tasks.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/weekly-tasks.md) — Comprehensive weekly instructor checklist (pre-class, in-class, and post-class routines).
- [AGENTS.md](file:///Users/arielchuri/Life/projects/work/device-art/AGENTS.md) — Master repository specification, AI assistant boundaries, Canvas API endpoints, and Miro visual rules.
- [CLAUDE.md](file:///Users/arielchuri/Life/projects/work/device-art/CLAUDE.md) — Assistant boundaries, pedagogy rules, and strict no-emoji policy.
- [meta/syllabus.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/syllabus.md) — Working source copy of the official course syllabus and university policies.
- [meta/HUMANS.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/HUMANS.md) — Instructor credentials, contacts, and institutional affiliations.
- [meta/operational_semester_roadmap.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/operational_semester_roadmap.md) — Master week-by-week timeline and milestone tracker.

---

## 2. Term Operations (Fall 2026)

### Attendance & Rosters
- [meta/terms/fall2026/attendance/attendance_ledger.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/terms/fall2026/attendance/attendance_ledger.md) — Live attendance tracking ledger by date and student.
- [meta/terms/fall2026/people/](file:///Users/arielchuri/Life/projects/work/device-art/meta/terms/fall2026/people/) — Individual student dossiers, biographies, interests, and portrait photos.
- [meta/terms/fall2026/people/dropped/](file:///Users/arielchuri/Life/projects/work/device-art/meta/terms/fall2026/people/dropped/) — Archived dossiers of withdrawn students.
- [meta/terms/fall2026/people/svg_cards/](file:///Users/arielchuri/Life/projects/work/device-art/meta/terms/fall2026/people/svg_cards/) — Generated 200x200 Miro student cards and roster grid.
- [meta/terms/fall2026/live_code_wall.html](file:///Users/arielchuri/Life/projects/work/device-art/meta/terms/fall2026/live_code_wall.html) — Local dashboard for live student code monitoring during class.

---

## 3. Administrative Scripts (`admin/`)

- [admin/take_attendance.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/take_attendance.py) — Interactive CLI roll call with ASCII portraits.
- [admin/sync_attendance_to_canvas.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/sync_attendance_to_canvas.py) — Syncs local attendance ledger marks to Canvas gradebook.
- [admin/canvas_sync.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/canvas_sync.py) — Canvas REST API synchronizer for assignments, pages, and rubrics.
- [admin/generate_student_cards.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/generate_student_cards.py) — Generates 200x200 Miro SVG cards from student dossiers.
- [admin/live_code_monitor.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/live_code_monitor.py) — Real-time in-class code monitoring daemon.
- [admin/send_canvas_announcement.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/send_canvas_announcement.py) — CLI utility to broadcast announcements to Canvas.
- [admin/send_canvas_messages.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/send_canvas_messages.py) — Direct messaging to students via Canvas Conversations API.
- [admin/send_personalized_messages.py](file:///Users/arielchuri/Life/projects/work/device-art/admin/send_personalized_messages.py) — Personalized batch messages (e.g. kit payment reminders).
- [admin/open_attendance.sh](file:///Users/arielchuri/Life/projects/work/device-art/admin/open_attendance.sh) — Quick-launcher for Canvas Roll Call tool in browser.

---

## 4. Pedagogy, Lesson Plans & Studio Notes

### Lesson Plans & Studio Prototypes
- [meta/pedagogy_and_notes/first_class_lesson_plan.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/first_class_lesson_plan.md) — Step-by-step agenda for Day 1.
- [meta/pedagogy_and_notes/first_class_demo_and_hook.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/first_class_demo_and_hook.md) — Opening interactive hook and demo breakdown.
- [meta/pedagogy_and_notes/nano_terminal_live_demo.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/nano_terminal_live_demo.md) — Terminal and text-editor live coding script.
- [meta/pedagogy_and_notes/assignment-ideas.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/assignment-ideas.md) — Raw brainstorming pool for potential course assignments.

### Lecture Drafts & Discussion Guides
- [meta/pedagogy_and_notes/lectures/electricity-fundamentals.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/electricity-fundamentals.md) — Deep-dive lecture notes on circuit physics.
- [meta/pedagogy_and_notes/lectures/code-meets-electricity.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/code-meets-electricity.md) — Microcontroller I/O bridge concepts.
- [meta/pedagogy_and_notes/lectures/coding-fundamentals.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/coding-fundamentals.md) — Computational thinking lecture notes.
- [meta/pedagogy_and_notes/lectures/cardboard-engineering.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/cardboard-engineering.md) — Rapid mechanical prototyping guide.
- [meta/pedagogy_and_notes/lectures/product-photography.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/product-photography.md) — Staging and lighting guide for physical devices.
- [meta/pedagogy_and_notes/lectures/user-persona.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/user-persona.md) — Interaction design and audience frameworks.
- [meta/pedagogy_and_notes/lectures/utopia-dystopia.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/lectures/utopia-dystopia.md) — Critical design and speculative device discourse.

### Programming Intro Reference Code
- [meta/pedagogy_and_notes/programming_intro/](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/programming_intro/) — Standalone Python demo scripts (`stringAndInteger.py`, `comparison.py`, `calculator1.py`, etc.).

### Hardware Parts & Circuit Docs
- [meta/pedagogy_and_notes/parts/parts.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/parts/parts.md) — Master technical documentation for kit components.
- [meta/pedagogy_and_notes/parts/audio.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/parts/audio.md) — Piezo and PWM sound synthesis guide.
- [meta/pedagogy_and_notes/parts/piano.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/parts/piano.md) — Capacitive touch musical keyboard reference.

---

## 5. Miro Device Canvas Vector Assets

- [meta/pedagogy_and_notes/miro_device_canvas/package_components/](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/miro_device_canvas/package_components/) — 1:1 breadboard-scaled SVG hardware vector library (Pico, breadboards, ICs, sensors, switches).
- [meta/pedagogy_and_notes/miro_device_canvas/modular_cards/](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/miro_device_canvas/modular_cards/) — 200x200 schematic concept cards.
- [meta/pedagogy_and_notes/miro_device_canvas/showcases/](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/miro_device_canvas/showcases/) — Overview vector showcase grids for Miro export.

---

## 6. Critical Theory, Artist Dossiers & Source Readings

### Artist Reference Dossiers
- [meta/pedagogy_and_notes/artist-references/maywa-denki_device-art.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/maywa-denki_device-art.md) — Nonsense machines and commercial device art.
- [meta/pedagogy_and_notes/artist-references/kenji-kawakami_chindogu.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/kenji-kawakami_chindogu.md) — The 10 tenets of Chindōgu.
- [meta/pedagogy_and_notes/artist-references/dunne-and-raby_critical-design.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/dunne-and-raby_critical-design.md) — Speculative and critical design frameworks.
- [meta/pedagogy_and_notes/artist-references/va-museum_disobedient-objects.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/va-museum_disobedient-objects.md) — Social protest and subverted everyday objects.
- [meta/pedagogy_and_notes/artist-references/natalie-jeremijenko_experimental-design.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/natalie-jeremijenko_experimental-design.md) — Tangible environmental inquiry devices.
- [meta/pedagogy_and_notes/artist-references/kelly-heaton_electronic-animism.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/kelly-heaton_electronic-animism.md) — Analog circuit behaviors and animism.
- [meta/pedagogy_and_notes/artist-references/steve-mann_wearable-computing.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/steve-mann_wearable-computing.md) — Sousveillance and wearable systems.
- [meta/pedagogy_and_notes/artist-references/survival-research-labs_industrial-performance.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/survival-research-labs_industrial-performance.md) — Kinetic machine performance and risk.
- [meta/pedagogy_and_notes/artist-references/toshio-iwai_interactive-media.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/toshio-iwai_interactive-media.md) — Audiovisual interfaces and tangible music.
- [meta/pedagogy_and_notes/artist-references/bernie-lubell_mechanical-analog.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/pedagogy_and_notes/artist-references/bernie-lubell_mechanical-analog.md) — Wood, acoustic, and low-tech interactive installations.

### Curated Readings Pool
- [meta/readings_source_pool/INDEX.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/readings_source_pool/INDEX.md) — Master bibliography of foundational PDFs categorized across:
  - **Theory & Art**: Kusahara (*Device Art*), Huizinga (*Homo Ludens*), Dunne & Raby (*Speculative Everything*), V&A (*Disobedient Objects*).
  - **Electronics**: Mims (*Getting Started in Electronics*), Platt (*Make: Electronics*), Scherz & Monk (*Practical Electronics*).
  - **Prototyping**: Kuniavsky (*Smart Things*), Houde & Hill (*What Do Prototypes Prototype?*).

---

## 7. Historical Course Archives & Reference Syllabi

- [meta/old_courses/Device_Art_Fa20/](file:///Users/arielchuri/Life/projects/work/device-art/meta/old_courses/Device_Art_Fa20/) — Device Art Fall 2020 Canvas modules, assignments, and syllabus archive.
- [meta/old_courses/Emergent_Objects_Sp25/](file:///Users/arielchuri/Life/projects/work/device-art/meta/old_courses/Emergent_Objects_Sp25/) — Emergent Objects Spring 2025 Canvas archive.
- [meta/old_courses/Emergent_Objects_Sp26/](file:///Users/arielchuri/Life/projects/work/device-art/meta/old_courses/Emergent_Objects_Sp26/) — Emergent Objects Spring 2026 Canvas archive.
- [meta/old_courses/Core_Lab_Objects_Fa15/](file:///Users/arielchuri/Life/projects/work/device-art/meta/old_courses/Core_Lab_Objects_Fa15/) — Core Lab Objects Fall 2015 archive.
- [meta/reference_syllabi/web_syllabi_and_links.md](file:///Users/arielchuri/Life/projects/work/device-art/meta/reference_syllabi/web_syllabi_and_links.md) — Links and notes from external peer courses at NYU ITP, MIT Media Lab, and CMU.
