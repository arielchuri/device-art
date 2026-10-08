#!/usr/bin/env python3
"""
Publishes the Microcontroller Intro Module, Pages, and Assignment to Canvas LMS.
"""

import json
import urllib.request
import urllib.parse
import re
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
    token = env.get("CANVAS_API_TOKEN")
    base_url = env.get("CANVAS_BASE_URL", "https://canvas.newschool.edu")
    course_id = env.get("CANVAS_COURSE_ID", "1929836")
    return token, base_url, course_id

TOKEN, BASE_URL, COURSE_ID = load_env()
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def api_request(method, endpoint, data=None):
    url = f"{BASE_URL}/api/v1/courses/{COURSE_ID}/{endpoint}"
    req_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=req_data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"[API ERROR {e.code}] {method} {url}: {err_body}")
        return None

_CANVAS_FILES_MAP = None

def get_canvas_files_map():
    global _CANVAS_FILES_MAP
    if _CANVAS_FILES_MAP is None:
        files = api_request("GET", "files?per_page=100") or []
        _CANVAS_FILES_MAP = {f['display_name']: f['id'] for f in files}
    return _CANVAS_FILES_MAP

def resolve_image_links(text):
    img_map = get_canvas_files_map()
    def sub_func(match):
        alt = match.group(1)
        path = match.group(2)
        filename = path.split("/")[-1]
        if filename in img_map:
            file_id = img_map[filename]
            return f"![{alt}](/courses/{COURSE_ID}/files/{file_id}/preview)"
        return match.group(0)
    return re.sub(r"!\[(.*?)\]\((.*?)\)", sub_func, text)

def md_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    text = resolve_image_links(text)
    html = markdown.markdown(text, extensions=['fenced_code', 'tables', 'nl2br'])
    return html

def push_page(title, md_path):
    html_body = md_to_html(md_path)
    url_slug = urllib.parse.quote(title.lower().replace(" ", "-").replace(":", "").replace("(", "").replace(")", "").replace("&", "and"))
    payload = {
        "wiki_page": {
            "title": title,
            "body": html_body,
            "published": True
        }
    }
    # Try updating first, or create
    res = api_request("PUT", f"pages/{url_slug}", payload)
    if not res:
        res = api_request("POST", "pages", payload)
    print(f"Page '{title}' synced. URL slug: {res.get('url') if res else 'ERROR'}")
    return res

def push_assignment(title, md_path, points=100):
    html_body = md_to_html(md_path)
    # Check if assignment already exists
    existing = api_request("GET", "assignments?per_page=100") or []
    match = next((a for a in existing if a['name'].strip().lower() == title.strip().lower()), None)
    payload = {
        "assignment": {
            "name": title,
            "description": html_body,
            "points_possible": points,
            "published": True,
            "submission_types": ["online_url", "online_upload"]
        }
    }
    if match:
        res = api_request("PUT", f"assignments/{match['id']}", payload)
        print(f"Assignment '{title}' updated (ID: {match['id']})")
    else:
        res = api_request("POST", "assignments", payload)
        print(f"Assignment '{title}' created (ID: {res.get('id') if res else 'ERROR'})")
    return res

def sync_module():
    module_name = "Microcontroller Intro: Raspberry Pi Pico & CircuitPython"
    
    # 1. Sync Pages
    page_lecture = push_page(
        "Lecture: Code Meets Electricity",
        CANVAS_DIR / "pages" / "lecture_code_meets_electricity.md"
    )
    page_intro = push_page(
        "Microcontroller Intro: Raspberry Pi Pico & CircuitPython",
        CANVAS_DIR / "pages" / "pico_microcontroller_intro.md"
    )
    page_vscode = push_page(
        "VS Code & CircuitPython Setup Guide",
        CANVAS_DIR / "pages" / "vscode_circuitpython_setup.md"
    )
    page_cheatsheet = push_page(
        "Raspberry Pi Pico & CircuitPython Cheat Sheet",
        CANVAS_DIR / "files" / "cheatsheets" / "pico_circuitpython_cheatsheet.md"
    )
    page_sim = push_page(
        "Python LED Blink Simulation",
        CANVAS_DIR / "pages" / "python_led_blink_simulation.md"
    )
    page_resources = push_page(
        "Course Resources & Technical References",
        CANVAS_DIR / "pages" / "course_resources.md"
    )
    
    # 2. Sync Assignments
    assignment_obj = push_assignment(
        "Assignment: My First Object (Pico Breadboarding & Multitasking)",
        CANVAS_DIR / "assignments" / "my_first_object" / "my_first_object.md",
        points=100
    )
    
    # 3. Create / Fetch Module
    modules = api_request("GET", "modules?per_page=50") or []
    mod = next((m for m in modules if m['name'].strip().lower() == module_name.strip().lower()), None)
    
    if not mod:
        mod = api_request("POST", "modules", {"module": {"name": module_name, "position": 2}})
        print(f"Created module '{module_name}' (ID: {mod.get('id')})")
    else:
        print(f"Found existing module '{module_name}' (ID: {mod['id']})")
    
    module_id = mod['id']
    
    # Publish Module
    api_request("PUT", f"modules/{module_id}", {"module": {"published": True}})
    
    # 4. Populate Items
    existing_items = api_request("GET", f"modules/{module_id}/items?per_page=50") or []
    existing_titles = {it['title'] for it in existing_items}
    
    items_to_add = [
        {"title": "Lecture Notes & Guides", "type": "SubHeader"},
        {"title": "Lecture: Code Meets Electricity", "type": "Page", "page_url": page_lecture.get('url') if page_lecture else "lecture-code-meets-electricity"},
        {"title": "Microcontroller Intro: Raspberry Pi Pico & CircuitPython", "type": "Page", "page_url": page_intro.get('url') if page_intro else "microcontroller-intro-raspberry-pi-pico-and-circuitpython"},
        {"title": "VS Code & CircuitPython Setup Guide", "type": "Page", "page_url": page_vscode.get('url') if page_vscode else "vs-code-and-circuitpython-setup-guide"},
        {"title": "Raspberry Pi Pico & CircuitPython Cheat Sheet", "type": "Page", "page_url": page_cheatsheet.get('url') if page_cheatsheet else "raspberry-pi-pico-and-circuitpython-cheat-sheet"},
        {"title": "Python LED Blink Simulation", "type": "Page", "page_url": page_sim.get('url') if page_sim else "python-led-blink-simulation"},
        {"title": "Course Resources & Technical References", "type": "Page", "page_url": page_resources.get('url') if page_resources else "course-resources-and-technical-references"},
        {"title": "Studio Lab & Assignments", "type": "SubHeader"},
        {"title": "Assignment: My First Object (Pico Breadboarding & Multitasking)", "type": "Assignment", "content_id": assignment_obj.get('id') if assignment_obj else None}
    ]
    
    for item in items_to_add:
        if item["title"] in existing_titles:
            print(f"Item '{item['title']}' already exists in module.")
            continue
        
        payload = {"module_item": item}
        res = api_request("POST", f"modules/{module_id}/items", payload)
        if res:
            print(f"Added item to module: '{item['title']}' (ID: {res.get('id')})")
        else:
            print(f"Failed to add item: '{item['title']}'")
            
    print(f"\nModule '{module_name}' successfully built and published on Canvas!")

if __name__ == "__main__":
    sync_module()
