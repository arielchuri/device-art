#!/usr/bin/env python3
"""
Syncs Course Modules to Canvas LMS as External Links to GitHub.
Driven by the human-editable configuration file: canvas/MODULES.md

Content Type: ExternalUrl (External Link to GitHub repository)
State: Unpublished (Draft)
"""

import os
import sys
import re
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CANVAS_DIR = BASE_DIR / "canvas"
MODULES_MD = CANVAS_DIR / "MODULES.md"
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
    if rel_path.startswith("http://") or rel_path.startswith("https://"):
        return rel_path
    quoted = urllib.parse.quote(rel_path.lstrip("/"), safe="/")
    return f"{GITHUB_REPO_RAW}/{quoted}"

def parse_modules_md(md_path=MODULES_MD):
    """
    Parses canvas/MODULES.md into structured module definitions:
    ## Module Name
    ### SubHeader Title
    - [Item Title](target_file_or_url)
    """
    if not md_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {md_path}")

    modules = []
    current_module = None
    position = 1

    with open(md_path, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not line_str or line_str.startswith("<!--"):
                continue

            # Check Module header: ## Module Name
            mod_match = re.match(r"^##\s+(?!#)(.*)", line_str)
            if mod_match:
                mod_name = mod_match.group(1).replace("Module:", "").strip()
                current_module = {
                    "name": mod_name,
                    "position": position,
                    "items": []
                }
                modules.append(current_module)
                position += 1
                continue

            # Check SubHeader: ### SubHeader Title
            sub_match = re.match(r"^###\s+(?!#)(.*)", line_str)
            if sub_match and current_module:
                sub_title = sub_match.group(1).strip()
                current_module["items"].append({
                    "title": sub_title,
                    "type": "SubHeader"
                })
                continue

            # Check Item: - [Title](path)
            item_match = re.match(r"^-\s+\[(.*?)\]\((.*?)\)", line_str)
            if item_match and current_module:
                title = item_match.group(1).strip()
                target = item_match.group(2).strip()
                current_module["items"].append({
                    "title": title,
                    "type": "ExternalUrl",
                    "external_url": gh_url(target)
                })
                continue

    return modules

def rebuild_modules(published=False):
    modules_data = parse_modules_md()
    print(f"=== Rebuilding Canvas Modules from {MODULES_MD.name} for Course ID {COURSE_ID} (Published={published}) ===\n")
    print(f"Parsed {len(modules_data)} modules from {MODULES_MD.name}.")

    # 1. Fetch and delete existing modules
    print("\n--- 1. Removing Old Modules ---")
    existing_modules = api_request("GET", "modules?per_page=100") or []
    for mod in existing_modules:
        mod_id = mod["id"]
        mod_name = mod.get("name", "Untitled")
        print(f"  Deleting old module: '{mod_name}' (ID: {mod_id})...")
        api_request("DELETE", f"modules/{mod_id}")

    # 2. Create the new modules and add External Links
    print("\n--- 2. Creating New Section Modules with GitHub External Links ---")
    for mod_spec in modules_data:
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
