#!/usr/bin/env python3
"""
Full Canvas LMS Sync Script for Device Art (Fall 2026)
Pushes files, pages, assignments, discussions, syllabus, and modules in UNPUBLISHED (draft) state.
"""

import os
import sys
import re
import json
import mimetypes
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
CANVAS_DIR = BASE_DIR / "canvas"
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

# --- File Upload via Canvas 3-Step Flow ---

def upload_file_to_canvas(local_path: Path, target_folder="course_files"):
    if not local_path.exists() or local_path.is_dir():
        return None
    
    filename = local_path.name
    file_size = local_path.stat().st_size
    mime_type, _ = mimetypes.guess_type(str(local_path))
    if not mime_type:
        mime_type = "application/octet-stream"

    # Step 1: Tell Canvas we want to upload a file
    step1_payload = {
        "name": filename,
        "size": file_size,
        "content_type": mime_type,
        "parent_folder_path": target_folder,
        "on_duplicate": "overwrite"
    }
    step1_res = api_request("POST", "files", step1_payload)
    if not step1_res or "upload_url" not in step1_res:
        print(f"  Failed Step 1 upload initiation for {filename}")
        return None

    upload_url = step1_res["upload_url"]
    upload_params = step1_res.get("upload_params", {})

    # Step 2: Multipart POST to upload_url
    boundary = "----CanvasSyncBoundary7MA4YWxkTrZu0gW"
    body_bytes = bytearray()

    for k, v in upload_params.items():
        body_bytes.extend(f"--{boundary}\r\n".encode("utf-8"))
        body_bytes.extend(f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode("utf-8"))
        body_bytes.extend(f"{v}\r\n".encode("utf-8"))

    body_bytes.extend(f"--{boundary}\r\n".encode("utf-8"))
    body_bytes.extend(f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode("utf-8"))
    body_bytes.extend(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
    with open(local_path, "rb") as f:
        body_bytes.extend(f.read())
    body_bytes.extend(f"\r\n--{boundary}--\r\n".encode("utf-8"))

    req = urllib.request.Request(
        upload_url,
        data=body_bytes,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "DeviceArt-CanvasSync/1.0"
        },
        method="POST"
    )

    try:
        # Step 3: Handle redirection if any
        class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
            def http_error_302(self, req, fp, code, msg, headers):
                infourl = urllib.response.addinfourl(fp, headers, req.get_full_url())
                infourl.status = code
                infourl.code = code
                return infourl
            http_error_301 = http_error_303 = http_error_307 = http_error_302

        opener = urllib.request.build_opener(NoRedirectHandler)
        with opener.open(req, timeout=60) as resp:
            if resp.code in (301, 302, 303, 307):
                loc = resp.headers.get("Location")
                if loc:
                    final_req = urllib.request.Request(loc, headers=HEADERS, method="GET")
                    with urllib.request.urlopen(final_req, timeout=30) as final_resp:
                        file_obj = json.loads(final_resp.read().decode("utf-8"))
                        print(f"  Uploaded '{filename}' (ID: {file_obj.get('id')})")
                        return file_obj
            else:
                resp_data = resp.read().decode("utf-8")
                file_obj = json.loads(resp_data) if resp_data else {}
                print(f"  Uploaded '{filename}' (ID: {file_obj.get('id')})")
                return file_obj
    except Exception as e:
        print(f"  Upload error for {filename}: {e}")
        return None

_FILES_CACHE = None

def get_canvas_files_map():
    global _FILES_CACHE
    if _FILES_CACHE is None:
        files = api_request("GET", "files?per_page=100") or []
        _FILES_CACHE = {f["display_name"]: f["id"] for f in files if "display_name" in f}
    return _FILES_CACHE

def resolve_asset_links(text):
    img_map = get_canvas_files_map()
    def img_sub(match):
        alt = match.group(1)
        path = match.group(2)
        filename = path.split("/")[-1].split("?")[0]
        if filename in img_map:
            file_id = img_map[filename]
            return f"![{alt}](/courses/{COURSE_ID}/files/{file_id}/preview)"
        return match.group(0)
    
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", img_sub, text)

    def link_sub(match):
        label = match.group(1)
        path = match.group(2)
        filename = path.split("/")[-1].split("?")[0]
        if filename in img_map:
            file_id = img_map[filename]
            return f"[{label}](/courses/{COURSE_ID}/files/{file_id}/download)"
        return match.group(0)

    # Convert relative file downloads (.pdf, .zip, .mpy, .py)
    text = re.sub(r"\[(.*?)\]\(((?:(?!\/courses\/|http).)*?\.(?:pdf|zip|mpy|py))\)", link_sub, text)
    return text

def md_to_html(md_path: Path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    text = resolve_asset_links(text)
    return markdown.markdown(text, extensions=['fenced_code', 'tables', 'nl2br'])

def push_page(title: str, md_path: Path, published=False):
    html_body = md_to_html(md_path)
    url_slug = urllib.parse.quote(title.lower().replace(" ", "-").replace(":", "").replace("(", "").replace(")", "").replace("&", "and").replace("/", "-"))
    payload = {
        "wiki_page": {
            "title": title,
            "body": html_body,
            "published": published
        }
    }
    res = api_request("PUT", f"pages/{url_slug}", payload)
    if not res:
        res = api_request("POST", "pages", payload)
    slug = res.get("url") if res else "ERROR"
    print(f"  Page '{title}' -> url: {slug} (published={published})")
    return res

def push_assignment(title: str, md_path: Path, points=100, published=False):
    html_body = md_to_html(md_path)
    existing = api_request("GET", "assignments?per_page=100") or []
    match = next((a for a in existing if a.get('name', '').strip().lower() == title.strip().lower()), None)
    payload = {
        "assignment": {
            "name": title,
            "description": html_body,
            "points_possible": points,
            "published": published,
            "submission_types": ["online_url", "online_upload"]
        }
    }
    if match:
        res = api_request("PUT", f"assignments/{match['id']}", payload)
        print(f"  Assignment '{title}' updated (ID: {match['id']}, published={published})")
    else:
        res = api_request("POST", "assignments", payload)
        print(f"  Assignment '{title}' created (ID: {res.get('id') if res else 'ERROR'}, published={published})")
    return res

def push_discussion(title: str, md_path: Path, published=False):
    html_body = md_to_html(md_path)
    existing = api_request("GET", "discussion_topics?per_page=100") or []
    match = next((d for d in existing if d.get('title', '').strip().lower() == title.strip().lower()), None)
    payload = {
        "title": title,
        "message": html_body,
        "published": published
    }
    if match:
        res = api_request("PUT", f"discussion_topics/{match['id']}", payload)
        print(f"  Discussion '{title}' updated (ID: {match['id']}, published={published})")
    else:
        res = api_request("POST", "discussion_topics", payload)
        print(f"  Discussion '{title}' created (ID: {res.get('id') if res else 'ERROR'}, published={published})")
    return res

def push_syllabus(md_path: Path):
    html_body = md_to_html(md_path)
    payload = {
        "course": {
            "syllabus_body": html_body
        }
    }
    res = api_request("PUT", "", payload)
    print(f"  Course Syllabus updated in Canvas settings.")
    return res

def sync_all(published=False):
    print(f"=== Starting Canvas Full Sync for Course ID {COURSE_ID} (Published={published}) ===\n")

    # 1. Upload All Files & Media Assets
    print("--- 1. Syncing Files & Assets ---")
    files_to_upload = list(CANVAS_DIR.rglob("*"))
    for fpath in files_to_upload:
        if fpath.is_file() and not fpath.name.startswith(".") and fpath.suffix.lower() in [
            ".png", ".jpg", ".jpeg", ".svg", ".pdf", ".zip", ".py", ".mpy", ".mp4", ".odg"
        ]:
            # Calculate folder relative to canvas/
            rel = fpath.parent.relative_to(CANVAS_DIR)
            folder_path = f"course_files/{rel}" if str(rel) != "." else "course_files"
            upload_file_to_canvas(fpath, target_folder=folder_path)

    # Refresh files map
    global _FILES_CACHE
    _FILES_CACHE = None
    get_canvas_files_map()

    # 2. Sync Syllabus
    print("\n--- 2. Syncing Syllabus ---")
    syllabus_md = CANVAS_DIR / "syllabus" / "syllabus_fall2026.md"
    if syllabus_md.exists():
        push_syllabus(syllabus_md)

    # 3. Sync Discussions
    print("\n--- 3. Syncing Discussions ---")
    disc_file = CANVAS_DIR / "discussions" / "discussion_01_introductions_and_objects.md"
    if disc_file.exists():
        push_discussion("Discussion 01: Introductions & Objects", disc_file, published=published)

    # 4. Sync Wiki Pages
    print("\n--- 4. Syncing Pages ---")
    pages_map = {
        "Electricity Intro": CANVAS_DIR / "pages" / "electricity_intro.md",
        "Lab 01: Breadboard Electricity Puzzles": CANVAS_DIR / "pages" / "lab-01-breadboard-electricity-puzzles.md",
        "Lecture: Code Meets Electricity": CANVAS_DIR / "pages" / "lecture_code_meets_electricity.md",
        "Breadboard & Electricity Exercises": CANVAS_DIR / "pages" / "breadboard_and_electricity_exercises.md",
        "Multimeter Beginner Guide": CANVAS_DIR / "pages" / "multimeter-beginner-guide.md",
        "VS Code & CircuitPython Setup Guide": CANVAS_DIR / "pages" / "vscode_circuitpython_setup.md",
        "Course Resources & Technical References": CANVAS_DIR / "pages" / "course_resources.md",
        "Python LED Blink Simulation": CANVAS_DIR / "pages" / "python_led_blink_simulation.md",
        "Microcontroller Intro: Raspberry Pi Pico & CircuitPython": CANVAS_DIR / "pages" / "pico_microcontroller_intro.md",
        "Course Materials List": CANVAS_DIR / "files" / "materials_list.md",
        "Raspberry Pi Pico & CircuitPython Cheat Sheet": CANVAS_DIR / "files" / "cheatsheets" / "pico_circuitpython_cheatsheet.md",
        "Git and GitHub Cheat Sheet": CANVAS_DIR / "files" / "cheatsheets" / "git_and_github_cheatsheet.md",
        "Terminal Cheat Sheet": CANVAS_DIR / "files" / "cheatsheets" / "terminal_cheatsheet.md",
        "Python Cheat Sheet": CANVAS_DIR / "files" / "cheatsheets" / "python_cheatsheet.md",
        "Blender Cheat Sheet": CANVAS_DIR / "files" / "cheatsheets" / "blender_cheatsheet.md",
        "Parts & Hardware Reference": CANVAS_DIR / "files" / "parts" / "parts.md",
        "Capacitive Touch Sensor": CANVAS_DIR / "files" / "parts" / "captouch_sensor" / "captouch_sensor.md",
        "Display SSD1306 OLED": CANVAS_DIR / "files" / "parts" / "display" / "display.md",
        "Neopixel WS2812B": CANVAS_DIR / "files" / "parts" / "neopixel" / "neopixel.md",
        "Real Time Clock DS3231": CANVAS_DIR / "files" / "parts" / "realTimeClock" / "realTimeClock_ds3231.md",
        "Ultrasonic Distance Sensor HC-SR04": CANVAS_DIR / "files" / "parts" / "ultrasonic_sensor" / "ultrasonic_sensor.md",
        "Audio and Speaker": CANVAS_DIR / "files" / "parts" / "audio.md",
        "Piano Synthesizer": CANVAS_DIR / "files" / "parts" / "piano.md",
        "RGB LED": CANVAS_DIR / "files" / "parts" / "RGB_LED" / "rgb_led.md",
        "Digital In/Out Code Guide": CANVAS_DIR / "files" / "raspberryPiPico" / "02_digital_inout" / "digital_inout.md",
        "Microcontroller Programming Quiz Guide": CANVAS_DIR / "files" / "raspberryPiPico" / "micro_programming_quiz.md"
    }

    synced_pages = {}
    for title, path in pages_map.items():
        if path.exists():
            res = push_page(title, path, published=published)
            synced_pages[title] = res

    # 5. Sync Assignments
    print("\n--- 5. Syncing Assignments ---")
    assignments_map = {
        "Assignment 01: Hardware Kit Readiness": (CANVAS_DIR / "assignments" / "assignment_01_hardware_kit_readiness.md", 100),
        "Assignment 02: Python Interactive Script (Age Validator)": (CANVAS_DIR / "assignments" / "assignment_02_python_age_validator.md", 100),
        "Assignment 03: GitHub Account & Desktop Setup": (CANVAS_DIR / "assignments" / "assignment_03_github_account_and_desktop.md", 100),
        "Assignment 04: Blender Device Modeling": (CANVAS_DIR / "assignments" / "assignment_04_blender_device_modeling.md", 100),
        "Assignment: My First Object (Pico Breadboarding & Multitasking)": (CANVAS_DIR / "assignments" / "my_first_object" / "my_first_object.md", 100),
        "Assignment: Moodlight Device": (CANVAS_DIR / "assignments" / "moodlight" / "moodlight.md", 100),
        "Hardware / Software Challenge": (CANVAS_DIR / "assignments" / "hardware-software-challenge" / "hardware-software.md", 100),
        "In-Class Exercise: Speculative Device Miro Mapping": (CANVAS_DIR / "assignments" / "in_class_exercise_speculative_device_miro.md", 50),
        "Project 01: Interactive Device Prototype": (CANVAS_DIR / "assignments" / "project_01_interactive_device_prototype.md", 100),
        "Reading: Week 02 Electricity Fundamentals": (CANVAS_DIR / "assignments" / "reading_week02_electricity_fundamentals.md", 20),
        "Quiz: Electricity Fundamentals & Circuits": (CANVAS_DIR / "assignments" / "quiz_electricity_and_circuits.md", 50),
    }

    synced_assignments = {}
    for title, (path, pts) in assignments_map.items():
        if path.exists():
            res = push_assignment(title, path, points=pts, published=published)
            synced_assignments[title] = res

    # 6. Sync Modules (Weeks 01-15)
    print("\n--- 6. Syncing Modules ---")
    existing_modules = api_request("GET", "modules?per_page=50") or []
    modules_lookup = {m.get("name", "").strip().lower(): m for m in existing_modules}

    weeks = [
        ("Week 01: Course Overview & Device Art Introduction", CANVAS_DIR / "modules" / "week-01" / "overview.md", 1),
        ("Week 02: Electricity & Electronics Fundamentals", CANVAS_DIR / "modules" / "week-02" / "overview.md", 2),
        ("Week 03: Microcontrollers & CircuitPython", CANVAS_DIR / "modules" / "week-03" / "overview.md", 3),
        ("Week 04: Sensors, Displays & Analog Inputs", CANVAS_DIR / "modules" / "week-04" / "overview.md", 4),
        ("Week 05: Prototyping & Multitasking Architecture", CANVAS_DIR / "modules" / "week-05" / "overview.md", 5),
        ("Week 06: Actuators, Motors & Physical Output", CANVAS_DIR / "modules" / "week-06" / "overview.md", 6),
        ("Week 07: Midterm Device Critiques", CANVAS_DIR / "modules" / "week-07" / "overview.md", 7),
        ("Week 08: Serial Communication & Device Networks", CANVAS_DIR / "modules" / "week-08" / "overview.md", 8),
        ("Week 09: Enclosures & Physical Fabrication", CANVAS_DIR / "modules" / "week-09" / "overview.md", 9),
        ("Week 10: Interaction Design & User Affordances", CANVAS_DIR / "modules" / "week-10" / "overview.md", 10),
        ("Week 11: Final Project Concept & Architecture", CANVAS_DIR / "modules" / "week-11" / "overview.md", 11),
        ("Week 12: Final Project Fabrication & Bench Testing", CANVAS_DIR / "modules" / "week-12" / "overview.md", 12),
        ("Week 13: Final Project Debugging & Iteration", CANVAS_DIR / "modules" / "week-13" / "overview.md", 13),
        ("Week 14: Final Rehearsals & Documentation", CANVAS_DIR / "modules" / "week-14" / "overview.md", 14),
        ("Week 15: Final Showcase & Device Art Exhibition", CANVAS_DIR / "modules" / "week-15" / "overview.md", 15),
    ]

    for mod_name, overview_path, pos in weeks:
        # 1. Sync overview page
        page_title = f"{mod_name} - Overview"
        overview_page = None
        if overview_path.exists():
            overview_page = push_page(page_title, overview_path, published=published)

        # 2. Create or update module
        mod_key = mod_name.strip().lower()
        mod_obj = modules_lookup.get(mod_key)
        if not mod_obj:
            mod_payload = {"module": {"name": mod_name, "position": pos, "published": published}}
            mod_obj = api_request("POST", "modules", mod_payload)
            print(f"  Created Module '{mod_name}' (ID: {mod_obj.get('id') if mod_obj else 'ERR'}, published={published})")
        else:
            api_request("PUT", f"modules/{mod_obj['id']}", {"module": {"published": published, "position": pos}})
            print(f"  Updated Module '{mod_name}' (ID: {mod_obj['id']}, published={published})")

        if mod_obj and "id" in mod_obj:
            mod_id = mod_obj["id"]
            if overview_page and "url" in overview_page:
                # Add overview page to module if not already present
                items = api_request("GET", f"modules/{mod_id}/items?per_page=50") or []
                item_titles = {it.get("title") for it in items}
                if page_title not in item_titles:
                    item_payload = {
                        "module_item": {
                            "title": page_title,
                            "type": "Page",
                            "page_url": overview_page["url"]
                        }
                    }
                    api_request("POST", f"modules/{mod_id}/items", item_payload)

    print("\n=== All items successfully synchronized to Canvas in UNPUBLISHED state! ===")

if __name__ == "__main__":
    sync_all(published=False)
