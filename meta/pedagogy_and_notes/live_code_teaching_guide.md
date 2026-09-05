# Live Code Teaching & Real-Time Student Visibility Guide

This guide outlines practical workflows for teaching hardware programming (CircuitPython / MicroPython on Raspberry Pi Pico) in the **Device Art** lab so that you can live-code while instantly viewing all 14 students' code in real-time.

---

## Recommended Teaching Setup Matrix

| Method | Best Used For | Setup Effort | Real-Time Visibility | Student Experience |
| :--- | :--- | :---: | :---: | :--- |
| **1. VS Code Live Share** | Live lecture demonstrations & paired debugging | Minimal (1 link) | Instant (Live Cursors) | Students watch & edit live in VS Code or Web Browser |
| **2. GitHub Classroom + Live Code Wall** | Studio lab time & multi-student progress tracking | One-time setup | On Git Commit / Push | Full version control, clean dashboard on projector |
| **3. Livecodes / Shared Scratchpad** | Quick 5-minute micro-challenges & snippet sharing | Zero (Instant) | Instant | Web scratchpad with syntax highlighting |

---

## Workflow 1: VS Code Live Share (Best for Live Demonstration & Pair Coding)

VS Code Live Share allows you to host a collaborative session where all 14 students join your workspace via a single URL.

### Features for Teaching:
- **Follow Mode**: Force all students' view to mirror your screen and cursor as you type.
- **Shared Terminal & REPL**: Share your Serial/REPL stream so students see the Pico console output live.
- **Participant Pins**: Jump directly to any student's file tab to highlight their approach on the projector.

### Setup Instructions:
1. Open VS Code in `Life/projects/work/device-art/`.
2. Click the **Live Share** button in the status bar (or run `Live Share: Start Collaboration Session`).
3. Copy the session link and paste it into Canvas announcements or class chat.
4. Set permissions to **Read-Only** during lectures, or **Read-Write** during lab workshops.

---

## Workflow 2: GitHub Classroom Live Code Wall (Best for Studio Progress)

With GitHub Classroom, each student works in their own assignment repository containing `code.py`. 

### The Live Code Wall Script (`admin/live_code_monitor.py`):
Run `python3 admin/live_code_monitor.py` locally to start a local web dashboard (`http://localhost:8000`) that displays all 14 active students' latest `code.py` side-by-side in real-time.

```bash
# Launch the live student code wall
python3 admin/live_code_monitor.py
```

### Features:
- **14-Pane Grid**: Shows every student's portrait card, current `code.py` status, last updated timestamp, and syntax-highlighted code.
- **Projector Friendly**: Display the grid on the room projector so students can look up and learn from each other's hardware control techniques.
- **Direct Link**: Click any student's pane to open their GitHub repository or Canvas submission.

---

## Workflow 3: Shared Class Scratchpad (For Quick Micro-Challenges)

For short, 5-minute exercises (e.g. *"Write a 4-line loop to pulse GP15"*):

1. Use a real-time markdown scratchpad like **HedgeDoc** or **HackMD**.
2. Pre-fill 14 headers with each student's name:
   ```markdown
   ## Akshi
   \`\`\`python
   # code here
   \`\`\`
   
   ## Ana
   \`\`\`python
   # code here
   \`\`\`
   ```
3. Project the scratchpad live so the whole class sees all 14 solutions emerging simultaneously.
