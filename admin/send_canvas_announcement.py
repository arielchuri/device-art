#!/usr/bin/env python3
"""
Post an official Announcement to all students in Device Art (Fall 2026) via Canvas API.
Canvas automatically emails this announcement to all enrolled students.
"""

import sys, urllib.request, json
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
token = None
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("CANVAS_API_TOKEN="):
            token = line.split("=", 1)[1].strip().strip('"').strip("'")

if not token:
    print("Error: CANVAS_API_TOKEN not found in .env")
    sys.exit(1)

COURSE_ID = "1929836"
url = f"https://canvas.newschool.edu/api/v1/courses/{COURSE_ID}/discussion_topics"

def post_announcement(title, message_html):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "title": title,
        "message": message_html,
        "is_announcement": True,
        "published": True
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            print(f"✓ Announcement successfully posted and emailed to all students!")
            print(f"  Title: {res.get('title')}")
            print(f"  URL: {res.get('html_url')}")
    except Exception as e:
        print("Error posting announcement:", e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_canvas_announcement.py '<Title>' '<Message HTML or Text>'")
        sys.exit(1)
    post_announcement(sys.argv[1], sys.argv[2])
