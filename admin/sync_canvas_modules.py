#!/usr/bin/env python3
"""
Syncs Course Modules to Canvas LMS as External Links to GitHub.
Module Sections:
1. Code
2. Electronics
3. Microcontroller
4. Parts
5. Reading

Content Type: ExternalUrl (External Link to GitHub repository)
State: Unpublished (Draft)
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"
GITHUB_REPO_RAW = "https://github.com/arielchuri/device-art/blob/main"

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
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "User-Agent": "DeviceArt-CanvasSync/1.0",
    "Content-Type": "application/json"
}

def api_request(method, endpoint, data=None):
    if endpoint.startswith("http"):
        url = endpoint
    else:
        url = f"{BASE_URL}/api/v1/courses/{COURSE_ID}/{endpoint}"
    req_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=req_data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            return json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"  [API ERROR {e.code}] {method} {url}: {err_body}")
        return None
    except Exception as e:
        print(f"  [REQ ERROR] {method} {url}: {e}")
        return None

def gh_url(rel_path):
    quoted = urllib.parse.quote(rel_path.lstrip("/"), safe="/")
    return f"{GITHUB_REPO_RAW}/{quoted}"

MODULES_DATA = [
    {
        "name": "Code",
        "position": 1,
        "items": [
            {"title": "Cheat Sheets & Guides", "type": "SubHeader"},
            {"title": "Python Cheat Sheet", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/python_cheatsheet.md")},
            {"title": "Terminal & Shell Cheat Sheet", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/terminal_cheatsheet.md")},
            {"title": "Git & GitHub Cheat Sheet", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/git_and_github_cheatsheet.md")},
            {"title": "Blender 3D Modeling Cheat Sheet", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/blender_cheatsheet.md")},
            {"title": "Python LED Blink Simulation", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/python_led_blink_simulation.md")},
            {"title": "Digital In/Out Code Guide", "type": "ExternalUrl", "external_url": gh_url("canvas/files/raspberryPiPico/02_digital_inout/digital_inout.md")},
            {"title": "Microcontroller Programming Quiz Guide", "type": "ExternalUrl", "external_url": gh_url("canvas/files/raspberryPiPico/micro_programming_quiz.md")},
        ]
    },
    {
        "name": "Electronics",
        "position": 2,
        "items": [
            {"title": "Lessons & Lab Guides", "type": "SubHeader"},
            {"title": "Electricity Intro & Fundamentals", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/electricity_intro.md")},
            {"title": "Lab 01: Breadboard Electricity Puzzles", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/lab-01-breadboard-electricity-puzzles.md")},
            {"title": "Breadboard & Electricity Exercises", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/breadboard_and_electricity_exercises.md")},
            {"title": "Digital Multimeter Beginner Guide", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/multimeter-beginner-guide.md")},
            {"title": "Multitester Basic Color Reference (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/multitester_basic_color.pdf")},
            {"title": "Sparkle Labs Electronics Manual (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/manual_wm_s.pdf")},
        ]
    },
    {
        "name": "Microcontroller",
        "position": 3,
        "items": [
            {"title": "Pico & CircuitPython Setup", "type": "SubHeader"},
            {"title": "Lecture: Code Meets Electricity", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/lecture_code_meets_electricity.md")},
            {"title": "Microcontroller Intro: Raspberry Pi Pico & CircuitPython", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/pico_microcontroller_intro.md")},
            {"title": "VS Code & CircuitPython Setup Guide", "type": "ExternalUrl", "external_url": gh_url("canvas/pages/vscode_circuitpython_setup.md")},
            {"title": "Raspberry Pi Pico & CircuitPython Cheat Sheet", "type": "ExternalUrl", "external_url": gh_url("canvas/files/cheatsheets/pico_circuitpython_cheatsheet.md")},
            {"title": "Adafruit CircuitPython 9.x Library Bundle (ZIP)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/raspberryPiPico/adafruit-circuitpython-bundle-9.x-mpy-20250319.zip")},
            {"title": "Raspberry Pi Pico Pinout Diagram (PNG)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/raspberryPiPico/raspberry_pi_Pico-R3-Pinout-narrow.png")},
        ]
    },
    {
        "name": "Parts",
        "position": 4,
        "items": [
            {"title": "Hardware & Component Documentation", "type": "SubHeader"},
            {"title": "Course Materials & Hardware Kit List", "type": "ExternalUrl", "external_url": gh_url("canvas/files/materials_list.md")},
            {"title": "Parts & Hardware Master Reference", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/parts.md")},
            {"title": "Capacitive Touch Sensor (TTP223)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/captouch_sensor/captouch_sensor.md")},
            {"title": "Display SSD1306 OLED (I2C)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/display/display.md")},
            {"title": "Neopixel WS2812B Addressable LED", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/neopixel/neopixel.md")},
            {"title": "Real Time Clock DS3231 (I2C)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/realTimeClock/realTimeClock_ds3231.md")},
            {"title": "Ultrasonic Distance Sensor HC-SR04", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/ultrasonic_sensor/ultrasonic_sensor.md")},
            {"title": "Audio & Piezo Speaker Synthesizer", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/audio.md")},
            {"title": "Capacitive Touch Piano", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/piano.md")},
            {"title": "RGB LED Common Cathode", "type": "ExternalUrl", "external_url": gh_url("canvas/files/parts/RGB_LED/rgb_led.md")},
        ]
    },
    {
        "name": "Reading",
        "position": 5,
        "items": [
            {"title": "Electronics Readings", "type": "SubHeader"},
            {"title": "Paul Scherz: Switches & Power (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/electronics/scherz-switches.pdf")},
            {"title": "Dan O'Sullivan & Tom Igoe: Physical Computing Sensors (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/electronics/osullivan-igoe-sensors.pdf")},
            {"title": "Forrest M. Mims III: Getting Started in Electronics (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/electronics/mims-gettingstarted-basics.pdf")},
            {"title": "Massimo Banzi: Getting Started with Arduino (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/electronics/Getting_Started_with_Arduino.pdf")},
            {"title": "Charles Platt: Make: Electronics (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/electronics/make-electronics.pdf")},
            {"title": "Prototyping Readings", "type": "SubHeader"},
            {"title": "Mike Kuniavsky: Smart Things Prototyping (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/kuniavsky-smartthings-ch14.pdf")},
            {"title": "Hugh Beyer & Karen Holtzblatt: Contextual Design (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/beyer-ci.pdf")},
            {"title": "Universal Methods of Design: Simulations (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/Universal_Methods_of_Design_Expanded_and_Revised_----_(98._Simulations).pdf")},
            {"title": "Stephanie Houde & Charles Hill: What do Prototypes Prototype? (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/houde-prototypes.pdf")},
            {"title": "This is Service Design Doing: Prototyping Methods (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/TISDD_methods.pdf")},
            {"title": "Prototyping TISDD Method Ch07 (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/prototyping_tisdd_method_ch07.pdf")},
            {"title": "Sparkle Labs: Bringing Hardware to Market (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/prototyping/BRINGINGHWTOMARKET.pdf")},
            {"title": "Device Art & Critical Theory", "type": "SubHeader"},
            {"title": "Machiko Kusahara: Device Art - A New Form of Media Art (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/2006_Kusahara_Device_Art_A_New_Form.pdf")},
            {"title": "Anthony Dunne & Fiona Raby: Curious Things for Curious People (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/Curious_things_for_curious_people.pdf")},
            {"title": "Anthony Dunne & Fiona Raby: Speculative Everything (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/speculativeEverything.pdf")},
            {"title": "Alastair Fuad-Luke: Design Activism (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/designactivism-beautifulstrangenessforasustainableworld_alastairfuadluke.pdf")},
            {"title": "Harry Brignull: Dark Patterns (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/darkpatterns.pdf")},
            {"title": "Johan Huizinga: Homo Ludens (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/homoludens.pdf")},
            {"title": "CHI 2016: Destructive Games (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/2016-chi-destructive-games-paper.pdf")},
            {"title": "Hiroshi Ishii: Radical Atoms (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/radical atoms.pdf")},
            {"title": "TaskCam CHI18 (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/TaskCam CHI18 Draft.pdf")},
            {"title": "Katerina Kamprani: The Uncomfortable (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/uncomfortable.pdf")},
            {"title": "V&A Museum: Disobedient Objects (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/DisobedientObjects.pdf")},
            {"title": "John Zerzan: Running on Emptiness (PDF)", "type": "ExternalUrl", "external_url": gh_url("canvas/files/readings/theory_and_art/John_Zerzan__Running_on_Emptiness__The_Failure_of_Symbolic_Thought_a4.pdf")},
        ]
    }
]

def rebuild_modules(published=False):
    print(f"=== Rebuilding Canvas Modules for Course ID {COURSE_ID} (Published={published}) ===\n")

    # 1. Fetch and delete existing modules
    print("--- 1. Removing Old Modules ---")
    existing_modules = api_request("GET", "modules?per_page=100") or []
    for mod in existing_modules:
        mod_id = mod["id"]
        mod_name = mod.get("name", "Untitled")
        print(f"  Deleting old module: '{mod_name}' (ID: {mod_id})...")
        api_request("DELETE", f"modules/{mod_id}")

    # 2. Create the 5 new modules and add External Links
    print("\n--- 2. Creating New Section Modules with GitHub External Links ---")
    for mod_spec in MODULES_DATA:
        mod_name = mod_spec["name"]
        pos = mod_spec["position"]
        items = mod_spec["items"]

        # Create module
        mod_payload = {
            "module": {
                "name": mod_name,
                "position": pos,
                "published": published
            }
        }
        mod_res = api_request("POST", "modules", mod_payload)
        if not mod_res or "id" not in mod_res:
            print(f"  FAILED to create module: {mod_name}")
            continue

        mod_id = mod_res["id"]
        print(f"\n  Created Module: '{mod_name}' (ID: {mod_id}, Position: {pos})")

        # Add items
        for item in items:
            item_type = item["type"]
            title = item["title"]

            if item_type == "SubHeader":
                item_payload = {
                    "module_item": {
                        "title": title,
                        "type": "SubHeader"
                    }
                }
            elif item_type == "ExternalUrl":
                item_payload = {
                    "module_item": {
                        "title": title,
                        "type": "ExternalUrl",
                        "external_url": item["external_url"],
                        "new_tab": True
                    }
                }
            else:
                continue

            item_res = api_request("POST", f"modules/{mod_id}/items", item_payload)
            if item_res:
                print(f"    + [{item_type}] {title}")
            else:
                print(f"    ! Failed to add: {title}")

    print("\n=== Modules successfully rebuilt with GitHub External Links in UNPUBLISHED state! ===")

if __name__ == "__main__":
    rebuild_modules(published=False)
