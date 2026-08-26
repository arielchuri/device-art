# Instructor Operating System & Routine (Pacing Protocol)

This document establishes the weekly operational scaffolding to prevent drift, eliminate administrative backlogs, and protect non-teaching time.

---

## 1. The Weekly 4-Phase Loop

```
Wednesday (Class Day)  ──>  Thursday (Fast Grade)  ──>  Monday (Prep Check)  ──>  Tuesday (Final Polish)
```

### Phase A: Wednesday (Class Day Execution)
- **18:45 (T-15 min)**: Open Canvas Attendance tool on mobile/laptop.
- **19:00 - 21:40 (In-Class)**:
  - Mark attendance immediately during warm-up.
  - Keep a single plain-text buffer (`canvas/grades/in_class_notes_YYYY-MM-DD.md`) for quick critique feedback bullets.

### Phase B: Thursday Morning (The 30-Minute Grading Siphon)
- **Rule**: Never let grading roll past 24 hours. The longer an unreviewed stack sits, the higher the executive cost.
- **Workflow**:
  - Open SpeedGrader with Canvas Rubrics enabled (1-click rubric criteria selection).
  - Use brief, actionable feedback (2 positive notes, 1 technical fix).
  - Run assistant script to calculate and flag any missing submissions.

### Phase C: Monday (Content Lock)
- Review upcoming week's module in `canvas/modules/week-XX/overview.md`.
- Confirm required parts/materials or PDF readings are linked.

### Phase D: Tuesday (Canvas Push & Announcement)
- Push module from local markdown to Canvas via `admin/canvas_sync.py`.
- Post weekly Canvas announcement outlining goals and what to bring to class.

---

## 2. Preventing Course Drift

1. **The Anchor Syllabus**: Maintain a locked 15-week milestone roadmap. If a topic runs long in class, make a conscious scope adjustment in the roadmap rather than letting the schedule silently slip.
2. **Rubric-Driven Clarity**: Every assignment has a 3-criterion rubric in Canvas before students begin. Transparent rubrics cut grading time by 75% and prevent subjective grading fatigue.
