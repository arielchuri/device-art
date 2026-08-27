# Device Art — Instructor Field Manual & Workflow Guide

Welcome to the central operational manual for managing **Device Art (Fall 2026)**. This guide outlines how to organize course materials, use local folders, grade on Canvas with 1-click rubrics, and maintain student privacy.

---

## 1. Directory Usage: Where Everything Goes

| Folder | What Goes Here | Student Privacy & Git Status |
| :--- | :--- | :--- |
| **`canvas/syllabus/`** | Official course syllabus (`syllabus_fall2026.md`) | Public (Syncs to Canvas) |
| **`canvas/modules/`** | Weekly overviews, agenda notes, and reading pages (`week-01` to `15`) | Public (Syncs to Canvas) |
| **`canvas/assignments/`** | Assignment briefs, project guidelines, and rubric point tables | Public (Syncs to Canvas) |
| **`canvas/announcements/`** | Announcements to post to Canvas | Public (Syncs to Canvas) |
| **`canvas/grades/`** | **Local gradebooks, attendance exports, and student spreadsheets** | **100% PRIVATE (Blocked by `.gitignore`)** |
| **`meta/`** | Your research PDFs, other teachers' syllabi, brainstorming, and private notes | Private Backstage |

---

## 2. Using Built-In Canvas Rubrics (Fast, 1-Click Grading)

Canvas allows rubrics to be attached directly to assignments for fast, objective grading in **SpeedGrader**.

### How We Build & Use Rubrics:
1. **Define the Rubric Locally**: Every assignment file in `canvas/assignments/` has a standard 3-to-4 criteria table:
   ```markdown
   | Criteria | Description | Points |
   | :--- | :--- | :---: |
   | Concept & Critical Inquiry | Depth of idea, research, and cultural relevance | 30 |
   | Technical Execution | Working circuit, code logic, and wiring neatness | 40 |
   | Craft & Enclosure | Durability, finish, and material integration | 20 |
   | Documentation & Process | Clean photos, schematic, and reflection text | 10 |
   | **Total** | | **100** |
   ```
2. **Push to Canvas**: The sync script creates the assignment and attaches the rubric in Canvas.
3. **1-Click Grading in SpeedGrader**:
   * Open Canvas SpeedGrader on your laptop or iPad.
   * Click **View Rubric**.
   * Click the point score for each criterion—Canvas automatically tallies the final grade, updates the gradebook, and gives students transparent feedback instantly.

---

## 3. Weekly Executive Rhythm (Pacing Protocol)

1. **Wednesday Evening (In-Class Attendance)**:
   * Open Canvas Roll Call on phone/laptop via [`admin/open_attendance.sh`](../admin/open_attendance.sh) or direct URL `https://canvas.newschool.edu/courses/1929836/external_tools/18235`.
   * Click **Mark All Present** $\to$ toggle any absent students to Red (takes 15 seconds).
2. **Thursday Morning (30-Minute SpeedGrader Siphon & Ledger Check)**:
   * Open SpeedGrader in Canvas with your 1-click Rubrics attached.
   * Grade all weekly submissions in one sitting before 24 hours pass.
   * Verify attendance ledger in `meta/terms/fall2026/attendance/attendance_ledger.md`.
3. **Monday (Content Lock & Prep)**:
   * Review upcoming week's module in `canvas/modules/week-XX/overview.md`.
   * Confirm required parts/materials or PDF readings are linked.
4. **Tuesday (Sync & Broadcast)**:
   * Run sync script to publish the module $\to$ Send Canvas weekly announcement.
