#!/usr/bin/env python3
"""
Canvas LMS Sync Utility for Device Art
Converts local markdown files (syllabus, modules, assignments, announcements)
and synchronizes with Canvas via the Canvas REST API.

Environment variables required:
  CANVAS_API_TOKEN: API token generated from Canvas Settings
  CANVAS_BASE_URL: e.g. "https://canvas.newschool.edu"
  CANVAS_COURSE_ID: Numeric course ID in Canvas URL (e.g. 1234567)
"""

import os
import sys
import glob
import re
import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def check_env():
    token = os.environ.get("CANVAS_API_TOKEN")
    base_url = os.environ.get("CANVAS_BASE_URL", "https://canvas.newschool.edu")
    course_id = os.environ.get("CANVAS_COURSE_ID")
    return token, base_url, course_id

def parse_frontmatter(content):
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].strip()
            for line in fm_text.strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    frontmatter[key.strip()] = val.strip().strip('"').strip("'")
    return frontmatter, body

def main():
    token, base_url, course_id = check_env()
    if not token or not course_id:
        print("Missing CANVAS_API_TOKEN or CANVAS_COURSE_ID environment variables.")
        print("Usage: CANVAS_API_TOKEN='...' CANVAS_COURSE_ID='...' python3 admin/canvas_sync.py [plan|upload|download]")
        sys.exit(0)
    
    action = sys.argv[1] if len(sys.argv) > 1 else "plan"
    print(f"Canvas Sync running in '{action}' mode for Course ID: {course_id} at {base_url}")

if __name__ == "__main__":
    main()
