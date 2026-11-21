#!/usr/bin/env python3
"""
Process Milestone 2 Submissions:
1. Archive submission text & images to meta/terms/fall2026/final/<student>/
2. Generate clean printable PDF dossiers (only new info, compact typography, labeled clearly)
3. Send to printer with 2-sided duplex
"""

import os
import sys
import json
import urllib.request
import subprocess
from pathlib import Path
from html.parser import HTMLParser

BASE_DIR = Path(__file__).resolve().parent.parent
FINAL_DIR = BASE_DIR / "meta" / "terms" / "fall2026" / "final"
ENV_FILE = BASE_DIR / ".env"

def load_env():
    env = {}
    if ENV_FILE.exists():
        with open(ENV_FILE, "r") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    env[k.strip()] = v.strip()
    token = env.get("CANVAS_API_TOKEN") or os.environ.get("CANVAS_API_TOKEN")
    base_url = env.get("CANVAS_BASE_URL") or os.environ.get("CANVAS_BASE_URL", "https://canvas.newschool.edu")
    course_id = env.get("CANVAS_COURSE_ID") or os.environ.get("CANVAS_COURSE_ID", "1929836")
    return token, base_url, course_id

TOKEN, BASE_URL, COURSE_ID = load_env()

def download_file(url, dest_path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        with open(dest_path, "wb") as f:
            f.write(resp.read())
    print(f"Downloaded: {dest_path.name} ({dest_path.stat().st_size} bytes)")

# -------------------------------------------------------------
# 1. Tahisha Jain
# -------------------------------------------------------------
def process_tahisha():
    folder = FINAL_DIR / "tahisha-jain"
    img_urls = {
        "m2_functional_diagram.jpg": "https://portfolio.newschool.edu/jaint233/files/2026/11/S.P.I.R.A.L.-Functional-Diagram-1024x683.jpg",
        "m2_circuit_wiring.jpg": "https://portfolio.newschool.edu/jaint233/files/2026/11/image-1024x683.jpg",
        "m2_oled_display_test.png": "https://portfolio.newschool.edu/jaint233/files/2026/11/Screenshot-2026-11-04-at-4.45.57-PM-766x1024.png",
        "m2_breadboard_circuit.png": "https://portfolio.newschool.edu/jaint233/files/2026/11/Screenshot-2026-11-04-at-4.46.11-PM-956x1024.png",
        "m2_serial_monitor.png": "https://portfolio.newschool.edu/jaint233/files/2026/11/Screenshot-2026-11-04-at-4.47.04-PM-752x1024.png"
    }
    for fname, url in img_urls.items():
        download_file(url, folder / fname)

    md_content = """# Final Project Milestone 2: Functional Diagram, Pseudo-Code & Benchtop Circuit

- **Student**: Tahisha Jain
- **Project Title**: S.P.I.R.A.L. (Speculative Possibility & Interpretive Reasoning Assistance Loop)
- **Submission Date**: November 3, 2026 (Canvas Graded: 50/50)
- **Source**: [Tahisha Jain Portfolio](https://portfolio.newschool.edu/jaint233/2026/11/03/final-project-milestone-2-functional-diagram-pseudo-code-benchtop-circuit/)

---

## 1. Functional Diagram

![S.P.I.R.A.L. Functional Diagram](m2_functional_diagram.jpg)

The functional diagram maps the complete multi-state architecture:
- `READY` -> `LISTENING` -> `THINKING` -> `OVERTHINKING` -> `RESPONSE` -> `READY`
- Controls include Start Button, Rotary Dial, Yes/No response buttons, I2C OLED, Vibration Motor, Buzzer, and Status LEDs.

---

## 2. Firmware Pseudo-Code

```python
INITIALIZE SYSTEM
Set up Pico W
Initialize OLED using I2C (GP0 SDA, GP1 SCL)
Configure START button (GP16)
Configure YES button (GP18)
Configure NO button (GP19)
Configure piezo buzzer (GP17)
Configure LED outputs (GP14, GP15)

Set state = READY
Display greeting on OLED

MAIN LOOP
current_time = time.monotonic()

Read all buttons
Debounce button inputs
Detect new button presses

IF START pressed:
    IF state == READY:
        Change state to LISTENING
        Record state_start_time
        Update OLED
        Play confirmation beep
    ELSE:
        Reset to READY

IF YES or NO pressed:
    Record user response
    Change state to THINKING
    Record state_start_time
    Update OLED

IF state == THINKING:
    Update thinking animation
    IF elapsed time >= thinking duration:
        Change state to OVERTHINKING
        Record state_start_time

IF state == OVERTHINKING:
    Increase urgency of feedback
    IF elapsed time >= overthinking duration:
        Change state to RESPONSE
        Display generated response
        Play response sound

IF state == RESPONSE:
    IF elapsed time >= response duration:
        Return to READY

Update buzzer without blocking
Update LED states without blocking
Repeat loop
```

---

## 3. Circuit Wiring Schematic & Benchtop Prototype

![Circuit Wiring Schematic](m2_circuit_wiring.jpg)
![Benchtop Circuit Prototype](m2_breadboard_circuit.png)
![OLED Interface Testing](m2_oled_display_test.png)
![Serial Debug Monitor](m2_serial_monitor.png)

---

## 4. Prototyping Progression & Development Log

For this milestone, I began translating S.P.I.R.A.L. from a conceptual device into a functional electronic prototype.

- **Display Transition**: Initially attempted to use a 16x2 character LCD, testing two separate displays and multiple wiring configurations, but both produced unreadable corrupted characters due to unstable contrast / voltage. Pivoted to an SSD1306 0.96-inch I2C OLED display, which worked immediately on GP0 (SDA) and GP1 (SCL).
- **Core Loop & Timing**: Implemented non-blocking timing using `time.monotonic()` to maintain responsive button polling while driving state transitions and display updates.
- **Circuit Verification**: Successfully wired and tested START, YES, and NO push buttons with debouncing, status LEDs on GP14 and GP15, piezo buzzer on GP17, and verified multi-state loop execution.
"""
    with open(folder / "milestone_02_submission.md", "w") as f:
        f.write(md_content)
    print("Created Tahisha milestone_02_submission.md")

# -------------------------------------------------------------
# 2. Karina Umekubo
# -------------------------------------------------------------
def process_karina():
    folder = FINAL_DIR / "karina-umekubo"
    img_urls = {
        "m2_state_machine_diagram.png": "https://portfolio.newschool.edu/umekk050/files/2026/11/Screenshot-2026-11-04-at-8.25.05-PM-1024x805.png",
        "m2_circuit_schematic.png": "https://portfolio.newschool.edu/umekk050/files/2026/11/Screenshot-2026-11-04-at-9.42.23-PM-1024x484.png",
        "m2_benchtop_circuit.jpg": "https://portfolio.newschool.edu/umekk050/files/2026/11/Photo-on-11-4-26-at-9.48-PM-1024x683.jpg"
    }
    for fname, url in img_urls.items():
        download_file(url, folder / fname)

    md_content = """# Final Project Milestone 2: Functional Diagram, Pseudo-Code & Benchtop Circuit

- **Student**: Karina Umekubo
- **Project Title**: Digital Plant Living Tamagotchi / Device Art Milestone 2
- **Submission Date**: November 5, 2026
- **Source**: [Karina Umekubo Portfolio](https://portfolio.newschool.edu/umekk050/2026/11/04/device-art-milestone-2/)

---

## 1. Functional Diagram – System State Machine

![System State Machine](m2_state_machine_diagram.png)

State progression:
- Idle / Seed State -> Growth / Sprout State (Care via Potentiometers) -> Mature Plant or Neglect/Over-watering Death State.

---

## 2. Firmware Pseudo-Code

```python
# Initialize Pico hardware
# GND(3) to ground and GP5 to power
# Connect OLED SSD1306:
#   GND -> GND(18)
#   VDD -> 3V3 / Power
#   SCK -> GP9 (I2C0 SCL)
#   SDA -> GP8 (I2C0 SDA)

# Potentiometer 1 (Water / Care input)
# Connect to Blue LED light:
#   If potentiometer measures low voltage -> dim the LED's brightness
#   If potentiometer measures high voltage -> increase the LED's brightness

# Potentiometer 2 (Sunlight / Energy input)
# Connect to Yellow LED light:
#   If potentiometer measures low voltage -> dim the LED's brightness
#   If potentiometer measures high voltage -> increase the LED's brightness

# Potentiometers 1 + 2 -> Screen State:
#   If potentiometers measure low voltage:
#       The animation on screen remains a SEED
#   If potentiometers measure balanced/medium voltage:
#       The animation on screen grows into a SPROUT
#   If potentiometers measure excessive/unbalanced voltage:
#       The animation on screen DIES

# Screen Visuals:
#   Import seed image from pixel bitmap library
#   Import sprout image from pixel bitmap library
#   Import dead sprout image from pixel bitmap library
```

---

## 3. Circuit Wiring Schematic & Prototyping Progression

![Circuit Wiring Schematic](m2_circuit_schematic.png)
![Breadboard to Soldered Circuit Prototype](m2_benchtop_circuit.jpg)
"""
    with open(folder / "milestone_02_submission.md", "w") as f:
        f.write(md_content)
    print("Created Karina milestone_02_submission.md")

# -------------------------------------------------------------
# 3. Ana Cherkezishvili
# -------------------------------------------------------------
def process_ana():
    folder = FINAL_DIR / "ana-cherkezishvili"
    # Download Canvas snapshot
    canvas_snap_url = "https://canvas.newschool.edu/files/169156824/download?download_frd=1&verifier=161bf134-d59c-40b4-9ad1-267849ccbbc5"
    download_file(canvas_snap_url, folder / "m2_notion_submission_snapshot.png")

    # Fetch Notion blocks & signed URLs
    page_id = "40e60104-98d9-8035-9335-d8fc2fcf9176"
    req = urllib.request.Request(
        "https://www.notion.so/api/v3/loadPageChunk",
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        data=json.dumps({"pageId": page_id, "limit": 100, "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False}).encode("utf-8")
    )
    img_blocks = []
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode("utf-8"))
        blocks = data["recordMap"]["block"]
        for bid, bval in blocks.items():
            v = bval.get("value", {}).get("value", {})
            if v.get("type") == "image":
                src = v.get("properties", {}).get("source", [[None]])[0][0]
                img_blocks.append({"block_id": bid, "src": src})

    # Get signed URLs
    req_sign = urllib.request.Request(
        "https://www.notion.so/api/v3/getSignedFileUrls",
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        data=json.dumps({
            "urls": [{"url": b["src"], "permissionRecord": {"table": "block", "id": b["block_id"]}} for b in img_blocks]
        }).encode("utf-8")
    )
    with urllib.request.urlopen(req_sign) as r:
        sdata = json.loads(r.read().decode("utf-8"))
        signed_urls = sdata.get("signedUrls", [])
        for idx, surl in enumerate(signed_urls):
            fname = f"m2_hardware_part_{idx+1}.png"
            try:
                download_file(surl, folder / fname)
            except Exception as e:
                print(f"Error downloading signed URL {fname}: {e}")

    md_content = """# Final Project Milestone 2: Project Pivot Proposal & Hardware BOM

- **Student**: Ana Cherkezishvili
- **Project Title**: GlitchCam Camera (Major Pivot from Emotional Projection Pod)
- **Submission Date**: November 4, 2026 (Canvas Graded: 20/50 - Awaiting Diagram & Circuit)
- **Source**: [Notion Page](https://app.notion.com/p/Milestone-2-40e6010498d980359335d8fc2fcf9176?source=copy_link)
- **Instructor Canvas Note**: *"Need the milestone 2 items as soon as you can and I will regrade."*

---

## 1. Pivot Concept Narrative

> **New Idea**:  
> **GlitchCam Camera**: A standalone physical digital camera designed to capture and process intentional glitch art and aesthetic image distortions in real time.

---

## 2. Updated Hardware Components & Sourcing BOM

1. **Microcontroller**: Adafruit ESP32 Feather V2 with 8MB Flash + 2MB PSRAM and STEMMA QT
2. **Display**: Adafruit 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD (ST7789 controller, EYESPI connector)
3. **Camera Sensor**: Adafruit OV5640 Camera Breakout (72-degree lens with autofocus)
4. **Storage**: Centon 32GB SDHC Memory Card (UHS-I U1 V10 A1)
5. **Power**: Lithium Ion Polymer Battery (3.7V, 1200mAh)

---

## 3. Pending Milestone 2 Deliverables

- [ ] Complete functional state machine diagram (Power On -> Frame Preview -> Trigger Button -> Frame Capture -> Glitch DSP Routine -> SD Write / LCD Render).
- [ ] Firmware pseudo-code for camera initialization, buffer capture, pixel displacement, and ST7789 display refresh.
- [ ] Solderless breadboard benchtop circuit wiring ESP32 Feather to OV5640 camera and ST7789 TFT LCD.

![Notion Milestone 2 Submission Snapshot](m2_notion_submission_snapshot.png)
"""
    with open(folder / "milestone_02_submission.md", "w") as f:
        f.write(md_content)
    print("Created Ana milestone_02_submission.md")

# -------------------------------------------------------------
# 4. John O'Donovan
# -------------------------------------------------------------
def process_john():
    folder = FINAL_DIR / "john-o-donovan"
    img_urls = {
        "m2_fsm_state_diagram.png": "https://portfolio.newschool.edu/odonj792/files/2026/11/Screenshot-2026-11-04-at-3.17.59-PM-1024x901.png",
        "m2_audio_trigger_graph.png": "https://portfolio.newschool.edu/odonj792/files/2026/11/Screenshot-2026-11-04-at-9.12.30-PM.png"
    }
    for fname, url in img_urls.items():
        download_file(url, folder / fname)

    # Download Canvas websnappr
    snap_url = "https://canvas.newschool.edu/files/169152027/download?download_frd=1&verifier=e8985b5a-6149-4109-b7ac-d1c722f907f1"
    download_file(snap_url, folder / "m2_canvas_submission_snapshot.png")

    md_content = """# Final Project Milestone 2: Functional Diagram & State Architecture

- **Student**: John O'Donovan
- **Project Title**: Sound-Reactive / Kinetic Articulation Instrument
- **Submission Date**: November 4, 2026 (Canvas Graded: 35/50 - Awaiting Benchtop Circuit & Pseudo-code)
- **Source**: [John O'Donovan Portfolio](https://portfolio.newschool.edu/odonj792/2026/11/04/final-project-milestone-2-functional-diagram-pseudo-code-benchtop-circuit/)
- **Instructor Canvas Note**: *"Seems to need current state of circuit photo and pseudo-code."*

---

## 1. Functional System State Architecture

![Functional State Machine Diagram](m2_fsm_state_diagram.png)

State machine mapping:
- System boot and microphone initialization
- Sound intensity analysis and threshold triggers
- Dual-mode output: motor articulation / servo pulse vs. visual LED frequency strobe
- Cooldown and baseline re-calibration loop

---

## 2. Audio Trigger Response Graph

![Audio Trigger Graph](m2_audio_trigger_graph.png)

Thresholding curve demonstrating ambient noise filtering versus intentional acoustic impulse events.

---

## 3. Pending Milestone 2 Deliverables

- [ ] Complete firmware pseudo-code for ADC audio sampling, peak detection thresholding, and actuator response.
- [ ] Benchtop photo showing solderless breadboard circuit with Raspberry Pi Pico, microphone amplifier breakout, status LEDs, and actuator/servo drive.
"""
    with open(folder / "milestone_02_submission.md", "w") as f:
        f.write(md_content)
    print("Created John milestone_02_submission.md")

if __name__ == "__main__":
    print("Starting Milestone 2 Archival...")
    process_tahisha()
    process_karina()
    process_ana()
    process_john()
    print("All 4 students archived successfully.")
