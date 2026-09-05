#!/usr/bin/env python3
"""
Sync local attendance marks from attendance_ledger.md directly to Canvas Roll Call / Gradebook.
"""
import os, sys, re, urllib.request, urllib.parse, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
LEDGER_PATH = BASE_DIR / "meta" / "terms" / "fall2026" / "attendance" / "attendance_ledger.md"
COURSE_ID = "1929836"
BASE_URL = "https://canvas.newschool.edu/api/v1"

# 1. Load Token
token = None
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("CANVAS_API_TOKEN="):
            token = line.split("=", 1)[1].strip().strip('"').strip("'")

if not token:
    print("Error: CANVAS_API_TOKEN not found in .env")
    sys.exit(1)

if not LEDGER_PATH.exists():
    print(f"Error: Ledger file not found at {LEDGER_PATH}")
    sys.exit(1)

# 2. Fetch Canvas Students
print(f"Connecting to Canvas Course {COURSE_ID}...")
req_users = urllib.request.Request(f"{BASE_URL}/courses/{COURSE_ID}/users?enrollment_type[]=student&per_page=100", headers={"Authorization": f"Bearer {token}"})
with urllib.request.urlopen(req_users) as resp:
    canvas_students = json.loads(resp.read().decode())

print(f"Found {len(canvas_students)} enrolled students in Canvas.")

# 3. Read Ledger
ledger_text = LEDGER_PATH.read_text()
attendance_data = {}

for line in ledger_text.splitlines():
    if line.startswith("|") and not line.startswith("| Student") and not line.startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 3:
            student_name = parts[0]
            w1_mark = parts[1] # Week 1
            w2_mark = parts[2] # Week 2
            # Latest mark
            latest_mark = w2_mark if w2_mark else w1_mark
            attendance_data[student_name] = latest_mark

# 4. Get or Create "Roll Call Attendance" Assignment on Canvas
url_assigns = f"{BASE_URL}/courses/{COURSE_ID}/assignments?per_page=100"
req_a = urllib.request.Request(url_assigns, headers={"Authorization": f"Bearer {token}"})
with urllib.request.urlopen(req_a) as resp:
    assigns = json.loads(resp.read().decode())

att_assign = next((a for a in assigns if "Attendance" in a.get("name", "")), None)
if not att_assign:
    print("Creating Roll Call Attendance assignment in Canvas Gradebook...")
    url_new = f"{BASE_URL}/courses/{COURSE_ID}/assignments"
    payload = {
        "assignment": {
            "name": "Roll Call Attendance",
            "points_possible": 100,
            "grading_type": "percent",
            "submission_types": ["none"],
            "published": True
        }
    }
    req_new = urllib.request.Request(url_new, data=json.dumps(payload).encode("utf-8"), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req_new) as resp:
        att_assign = json.loads(resp.read().decode())

assign_id = att_assign.get("id")

# 5. Post Submissions / Grade Data
grade_data = {}
for s in canvas_students:
    sname = s.get("name", "")
    sid = str(s.get("id"))
    
    # Match student mark
    mark = "P"
    for lname, lmark in attendance_data.items():
        if lname.lower() in sname.lower() or sname.lower() in lname.lower():
            mark = lmark
            break
            
    # Score calculation: Present (.) / P = 100, Late (L) = 80, Absent (A) = 0
    score = 100
    if mark.upper() == "A":
        score = 0
    elif mark.upper() == "L":
        score = 80
        
    grade_data[f"grade_data[{sid}][posted_grade]"] = str(score)

data_encoded = urllib.parse.urlencode(grade_data).encode("utf-8")
url_bulk = f"{BASE_URL}/courses/{COURSE_ID}/assignments/{assign_id}/submissions/update_grades"
req_bulk = urllib.request.Request(url_bulk, data=data_encoded, headers={"Authorization": f"Bearer {token}"}, method="POST")

with urllib.request.urlopen(req_bulk) as resp:
    print("✓ Successfully synchronized attendance scores directly to Canvas Gradebook!")
