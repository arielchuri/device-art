# Device Art — The New School (Fall 2026)

- **Status**: active
- **Domain**: work
- **Schedule**: Wednesday evenings, 19:00 - 21:40
- **LMS**: Canvas (Course ID: `1929836`)

---

## Workspace Architecture

```
device-art/
├── CLAUDE.md              # AI boundary rules (housekeeping, pacing, calc only)
├── README.md              # Course overview and repository architecture
├── tasks.md               # Pacing checklist & grading triggers
├── .env                   # Private Canvas API credentials (gitignored)
│
├── canvas/                # DIRECT CANVAS MIRROR (The actual course)
│   ├── syllabus/          # Course syllabus & policies (syncs to Canvas Syllabus)
│   ├── modules/           # Weekly module overviews & reading pages (week-01 to 15)
│   ├── assignments/       # Assignment briefs, rubrics, and point values
│   ├── announcements/     # Drafted and published Canvas announcements
│   ├── discussions/       # Canvas discussion prompts
│   ├── files/             # Public student-facing course PDFs & diagrams
│   └── grades/            # Attendance logs, rubric score trackers
│
├── meta/                  # INSTRUCTOR BACKSTAGE (Course Creation & Research)
│   ├── old_courses/       # Backups from prior Canvas courses (Fa20, Sp25, Fa15)
│   ├── reference_syllabi/ # Syllabi from other faculty & external institutions
│   ├── readings_source_pool/ # PDF repository & potential reading material
│   ├── pedagogy_and_notes/ # Brainstorming, teaching philosophies, curriculum notes
│   └── teaching_routines/ # Pacing protocols, operational workflows & timeboxing
│
└── admin/                 # Scripts & Sync Tools
    ├── canvas_sync.py     # Two-way sync engine between canvas/ and Canvas API
    └── backups/           # Full Canvas course exports (.imscc)
```
