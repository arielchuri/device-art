# Device Art — Weekly Instructor Task Checklist

**Course**: PSAM 2230 | CRN 15895  
**Class Meeting**: Wednesday Evenings, 19:00 – 21:40 (7:00 PM – 9:40 PM)  
**Location**: In-Person (Parsons Making Center / Classroom TBD)  
**Instructor**: Ariel Churi (`ariel@sparklelabs.com` / `churia@newschool.edu`)  

---

## 1. Pre-Class Routine (Monday – Wednesday Afternoon)

- [ ] **Canvas Module & Content Lock (Monday)**:
  - Review upcoming week's module in `canvas/modules/week-XX/overview.md`.
  - Confirm all assignment briefs, rubric point tables, and starter code are ready.
  - Verify that required readings or external reference PDFs in `meta/readings_source_pool/` are properly linked.
- [ ] **Canvas Sync & Broadcast (Tuesday Afternoon)**:
  - Sync unpublished/draft pages or assignments to Canvas via `admin/canvas_sync.py`.
  - Send the weekly reminder announcement to students via Canvas or `admin/send_canvas_announcement.py`.
- [ ] **Hardware Kit & Lab Staging (Wednesday Morning)**:
  - Stage required physical hardware for the lab (Raspberry Pi Pico boards, breadboards, multimeters, specific sensors/actuators).
  - Verify multimeters have working 9V batteries.
  - Check incoming payments for kit bundles ($50 wholesale bundle via `money@sparklelabs.com` on Zelle / PayPal).
- [ ] **Miro Board Preparation**:
  - Duplicate or unlock the weekly Miro sandbox board template using components from `meta/pedagogy_and_notes/miro_device_canvas/`.
  - Ensure 1:1 breadboard vectors and component cards are arranged for student access.

---

## 2. In-Class Routine (Wednesday 19:00 – 21:40)

- [ ] **19:00 – 19:10 | Attendance & Roll Call**:
  - Open attendance via phone/laptop using `admin/open_attendance.sh` or the CLI tool:
    ```bash
    python3 admin/take_attendance.py
    ```
  - Mark absent/tardy students directly into the ledger (`meta/terms/fall2026/attendance/attendance_ledger.md`).
  - *Policy Check*: Habitual absences (3 weeks / 20% of class time) trigger academic alert warnings.
- [ ] **19:10 – 19:45 | Critique & Homework Pin-Up**:
  - Facilitate peer review and discussion of the previous week's assignment or project milestone.
  - Live demo student code or device prototypes.
- [ ] **19:45 – 20:30 | Miro Sandbox & Concept Introduction**:
  - Present theoretical concepts, circuit logic, and historical artist references (e.g., Maywa Denki, Kenji Kawakami, Natalie Jeremijenko).
  - Guide students through wiring and calculating circuit math inside the Miro digital sandbox first before touching physical parts.
- [ ] **20:30 – 21:30 | Hands-On Studio Lab & Bench Troubleshooting**:
  - Transition students from Miro blueprints to physical solderless breadboards, multimeters, and CircuitPython.
  - Provide 1-on-1 desk critiques and hardware debugging.
  - Monitor live coding progress if utilizing `admin/live_code_monitor.py`.
- [ ] **21:30 – 21:40 | Studio Clean-Up & Hardware Inventory**:
  - Ensure all multimeter dials are turned to **OFF** to prevent dead batteries.
  - Confirm students pack all loose ICs, jumper wires, and Pico boards back into their personal kit boxes.

---

## 3. Post-Class Routine (Thursday – Sunday)

- [ ] **Thursday Morning | 30-Minute SpeedGrader Sprint**:
  - Open Canvas SpeedGrader with attached 1-click rubrics.
  - Grade submitted assignments and weekly lab worksheets within 24 hours of class.
  - Provide concise, actionable technical and conceptual feedback.
- [ ] **Attendance & Ledger Synchronization**:
  - Sync attendance ledger marks with Canvas gradebook via `admin/sync_attendance_to_canvas.py`:
    ```bash
    python3 admin/sync_attendance_to_canvas.py
    ```
- [ ] **Repository Maintenance**:
  - Commit updated attendance ledgers, notes, or code examples to git.
  - Verify that non-student facing files or new assets are logged in `meta/INDEX.md`.
- [ ] **Student Communication & Office Hours**:
  - Answer technical inquiries on Canvas discussion boards or email.
  - Hold scheduled 1-on-1 office hours appointments.
  - Contact students who missed class or fell behind on assignments.
