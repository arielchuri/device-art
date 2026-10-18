#!/usr/bin/env python3
"""
Syncs Canvas Assignments to point directly to GitHub briefs.
Ensures Canvas is only a submission portal with direct links to GitHub.
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
ASSIGNMENTS_DIR = CANVAS_DIR / "assignments"
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

def parse_frontmatter(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            for line in fm_text.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if v.startswith("[") and v.endswith("]"):
                        # simple list parser
                        items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                        meta[k] = items
                    elif v.isdigit():
                        meta[k] = int(v)
                    elif v.lower() == "true":
                        meta[k] = True
                    elif v.lower() == "false":
                        meta[k] = False
                    else:
                        meta[k] = v
    return meta

def make_github_description(title, rel_path):
    gh_link = f"{GITHUB_REPO_RAW}/{urllib.parse.quote(str(rel_path), safe='/')}"
    return f"""<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 780px;">
  <div style="background: #f6f8fa; border: 1px solid #d0d7de; border-left: 5px solid #0969da; padding: 18px; border-radius: 6px; margin-bottom: 24px;">
    <h3 style="margin-top: 0; color: #1f2328; font-size: 18px;">📋 {title}</h3>
    <p style="margin-bottom: 12px; color: #57606a; font-size: 14px;">All project specifications, deliverables checklist, hardware schematics, and evaluation rubrics are maintained on GitHub:</p>
    <p style="margin-bottom: 0;">
      👉 <a href="{gh_link}" target="_blank" rel="noopener" style="font-size: 16px; font-weight: 600; color: #0969da; text-decoration: underline;">
        <strong>View Full Assignment Brief on GitHub</strong>
      </a>
    </p>
  </div>
  <p style="font-size: 14px; color: #24292f;"><strong>Submission Instructions:</strong> Please submit your required deliverables (Learning Portfolio URL, GitHub repository link, video URL, or documentation files) using the submission box on this page.</p>
</div>"""

def sync_assignments(force_published=True):
    print(f"=== Syncing Canvas Assignments for Course ID {COURSE_ID} ===")
    
    # 1. Fetch live assignments
    live_assignments = api_request("GET", "assignments?per_page=100") or []
    live_by_title = {a["name"].strip().lower(): a for a in live_assignments}
    print(f"Found {len(live_assignments)} existing assignments on Canvas.\n")

    # 2. Find all assignment markdown files
    md_files = list(ASSIGNMENTS_DIR.glob("*.md")) + list(ASSIGNMENTS_DIR.glob("*/*.md"))
    # Filter out template
    md_files = [p for p in md_files if p.name != "assignment_template.md"]

    for md_path in sorted(md_files):
        meta = parse_frontmatter(md_path)
        title = meta.get("title")
        if not title:
            continue

        rel_path = md_path.relative_to(BASE_DIR)
        desc = make_github_description(title, rel_path)
        points = meta.get("points_possible", 100)
        due_at = meta.get("due_at")
        sub_types = meta.get("submission_types", ["online_upload", "online_url"])
        exts = meta.get("allowed_extensions", ["pdf", "zip", "mp4", "py", "mov"])
        is_published = force_published if force_published is not None else meta.get("published", True)

        assignment_payload = {
            "assignment": {
                "name": title,
                "description": desc,
                "points_possible": points,
                "submission_types": sub_types,
                "allowed_extensions": exts,
                "published": is_published
            }
        }
        if due_at:
            # Format ISO due date if present (e.g. 2026-10-28 19:00 -> 2026-10-28T19:00:00Z)
            iso_due = due_at.replace(" ", "T") + ":00Z" if len(due_at) == 16 else due_at
            assignment_payload["assignment"]["due_at"] = iso_due

        norm_title = title.strip().lower()
        existing = live_by_title.get(norm_title)

        if existing:
            aid = existing["id"]
            # update
            res = api_request("PUT", f"assignments/{aid}", assignment_payload)
            if res:
                print(f"✓ Updated Assignment '{title}' (ID: {aid}, Published: {res.get('published')})")
            else:
                print(f"✗ Failed to update '{title}' (ID: {aid})")
        else:
            # create
            res = api_request("POST", "assignments", assignment_payload)
            if res and "id" in res:
                aid = res["id"]
                print(f"+ Created Assignment '{title}' (ID: {aid}, Published: {res.get('published')})")
            else:
                print(f"✗ Failed to create assignment '{title}'")

    print("\n=== Assignments successfully synced to GitHub portal model! ===")

if __name__ == "__main__":
    sync_assignments(force_published=True)
