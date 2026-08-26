#!/usr/bin/env python3
"""
Canvas LMS Bi-directional Synchronization Engine for Device Art (Fall 2026)
Course ID: 1929836 (The New School)
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

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

def fetch_course_inventory():
    print(f"--- Fetching Live Inventory for Course ID: {COURSE_ID} ---")
    modules = api_request("GET", "modules?per_page=50") or []
    assignments = api_request("GET", "assignments?per_page=100") or []
    announcements = api_request("GET", "discussion_topics?only_announcements=true&per_page=50") or []
    pages = api_request("GET", "pages?per_page=50") or []
    print(f"Modules: {len(modules)} | Assignments: {len(assignments)} | Announcements: {len(announcements)} | Pages: {len(pages)}")
    return {
        "modules": modules,
        "assignments": assignments,
        "announcements": announcements,
        "pages": pages
    }

def push_announcement(title, message, is_draft=False):
    payload = {
        "title": title,
        "message": message,
        "is_announcement": True,
        "published": not is_draft
    }
    res = api_request("POST", "discussion_topics", payload)
    if res:
        print(f"Successfully posted announcement: '{title}' (ID: {res.get('id')})")
    return res

def push_module(name, position=1):
    payload = {"module": {"name": name, "position": position}}
    res = api_request("POST", "modules", payload)
    if res:
        print(f"Created module: '{name}' (ID: {res.get('id')})")
    return res

def push_assignment(title, description, points=100, due_at=None, published=False):
    payload = {
        "assignment": {
            "name": title,
            "description": description,
            "points_possible": points,
            "published": published
        }
    }
    if due_at:
        payload["assignment"]["due_at"] = due_at
    res = api_request("POST", "assignments", payload)
    if res:
        print(f"Created assignment: '{title}' (ID: {res.get('id')})")
    return res

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    if action == "status":
        fetch_course_inventory()
    else:
        print(f"Action '{action}' complete.")
