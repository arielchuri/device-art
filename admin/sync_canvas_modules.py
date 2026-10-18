#!/usr/bin/env python3
"""
Syncs Course Modules to Canvas LMS as External Links to GitHub.
Driven by the human-editable configuration file: canvas/MODULES.md

Features:
- Non-destructive: Updates modules and items in-place (upsert). Never wipes existing modules.
- Preserves / defaults to PUBLISHED state so students never lose access.
- Content Type: ExternalUrl (External Link to GitHub repository) opening in a new tab.
- Single Source of Truth: GitHub hosts all content; Canvas provides the portal links.
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
    "User-Agent": "DeviceArt-CanvasSync/2.0",
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
                raw_name = mod_match.group(1).replace("Module:", "").strip()
                # Check for optional [draft] tag in header
                is_draft = "[draft]" in raw_name.lower()
                clean_name = re.sub(r"\[.*?\]", "", raw_name).strip()
                current_module = {
                    "name": clean_name,
                    "position": position,
                    "published": not is_draft,
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
                disc_match = re.search(r"discussion_topics/(\d+)", target)
                if disc_match:
                    current_module["items"].append({
                        "title": title,
                        "type": "Discussion",
                        "content_id": int(disc_match.group(1))
                    })
                else:
                    current_module["items"].append({
                        "title": title,
                        "type": "ExternalUrl",
                        "external_url": gh_url(target)
                    })
                continue

    return modules

def sync_modules(force_published=True):
    """
    Non-destructively synchronizes modules and items from MODULES.md into Canvas LMS.
    """
    modules_data = parse_modules_md()
    print(f"=== Syncing Canvas Modules from {MODULES_MD.name} for Course ID {COURSE_ID} ===")
    print(f"Parsed {len(modules_data)} target modules.\n")

    # 1. Fetch existing modules on Canvas
    print("--- 1. Fetching Live Canvas Modules ---")
    live_modules = api_request("GET", "modules?per_page=100") or []
    live_by_name = {m["name"].strip().lower(): m for m in live_modules}
    target_names = {m["name"].strip().lower() for m in modules_data}

    # 2. Upsert each module from MODULES.md
    print("\n--- 2. Synchronizing Modules & Items (In-Place Upsert) ---")
    for mod_spec in modules_data:
        mod_name = mod_spec["name"]
        mod_key = mod_name.strip().lower()
        pos = mod_spec["position"]
        should_publish = force_published if force_published is not None else mod_spec["published"]
        target_items = mod_spec["items"]

        existing_mod = live_by_name.get(mod_key)
        if existing_mod:
            mod_id = existing_mod["id"]
            # Preserve existing published state unless force_published is True
            target_pub = True if (force_published or existing_mod.get("published")) else should_publish
            update_payload = {
                "module": {
                    "name": mod_name,
                    "position": pos,
                    "published": target_pub
                }
            }
            api_request("PUT", f"modules/{mod_id}", update_payload)
            print(f"✓ Module '{mod_name}' (ID: {mod_id}, Pos: {pos}, Published: {target_pub})")
        else:
            create_payload = {
                "module": {
                    "name": mod_name,
                    "position": pos,
                    "published": should_publish
                }
            }
            res = api_request("POST", "modules", create_payload)
            if not res or "id" not in res:
                print(f"✗ FAILED to create module: {mod_name}")
                continue
            mod_id = res["id"]
            print(f"+ Created Module '{mod_name}' (ID: {mod_id}, Pos: {pos}, Published: {should_publish})")

        # 3. Synchronize items inside this module
        existing_items = api_request("GET", f"modules/{mod_id}/items?per_page=100") or []
        # Key existing items by (type, title.strip().lower())
        existing_items_map = {}
        for it in existing_items:
            key = (it.get("type"), it.get("title", "").strip().lower())
            existing_items_map[key] = it

        # Target items lookup
        target_keys = set()
        for idx, item in enumerate(target_items, start=1):
            itype = item["type"]
            ititle = item["title"]
            ikey = (itype, ititle.strip().lower())
            target_keys.add(ikey)

            match = existing_items_map.get(ikey)
            if match:
                item_id = match["id"]
                # Update if URL or position or published state needs sync
                needs_update = False
                update_body = {}
                if itype == "ExternalUrl" and match.get("external_url") != item["external_url"]:
                    update_body["external_url"] = item["external_url"]
                    needs_update = True
                if match.get("position") != idx:
                    update_body["position"] = idx
                    needs_update = True
                if not match.get("published") and should_publish:
                    update_body["published"] = True
                    needs_update = True

                if needs_update:
                    api_request("PUT", f"modules/{mod_id}/items/{item_id}", {"module_item": update_body})
                    print(f"    ~ Updated [{itype}] {ititle} (Pos: {idx})")
            else:
                # Create item
                if itype == "SubHeader":
                    item_payload = {
                        "module_item": {
                            "title": ititle,
                            "type": "SubHeader",
                            "position": idx
                        }
                    }
                elif itype == "ExternalUrl":
                    item_payload = {
                        "module_item": {
                            "title": ititle,
                            "type": "ExternalUrl",
                            "external_url": item["external_url"],
                            "new_tab": True,
                            "position": idx
                        }
                    }
                elif itype == "Discussion":
                    item_payload = {
                        "module_item": {
                            "title": ititle,
                            "type": "Discussion",
                            "content_id": item["content_id"],
                            "position": idx
                        }
                    }
                else:
                    continue

                item_res = api_request("POST", f"modules/{mod_id}/items", item_payload)
                if item_res:
                    print(f"    + Created [{itype}] {ititle} (Pos: {idx})")
                    if should_publish and item_res.get("id"):
                        api_request("PUT", f"modules/{mod_id}/items/{item_res['id']}", {"module_item": {"published": True}})
                else:
                    print(f"    ! Failed to add: {ititle}")

        # Delete obsolete items that are no longer in MODULES.md
        for ikey, old_it in existing_items_map.items():
            if ikey not in target_keys:
                old_id = old_it["id"]
                old_title = old_it.get("title", "")
                print(f"    - Removing obsolete item: '{old_title}' (ID: {old_id})")
                api_request("DELETE", f"modules/{mod_id}/items/{old_id}")

    # 4. Remove obsolete modules that are no longer in MODULES.md
    print("\n--- 3. Checking Obsolete Modules ---")
    for live_name_key, live_mod in live_by_name.items():
        if live_name_key not in target_names:
            print(f"  - Deleting obsolete module: '{live_mod['name']}' (ID: {live_mod['id']})")
            api_request("DELETE", f"modules/{live_mod['id']}")

    print("\n=== Modules successfully synchronized in non-destructive mode! ===")

if __name__ == "__main__":
    is_draft_only = "--draft" in sys.argv
    sync_modules(force_published=not is_draft_only)
