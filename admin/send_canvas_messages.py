#!/usr/bin/env python3
"""
Send individual, private Canvas Inbox messages/emails to each enrolled student.
- Filters ONLY enrolled students (excludes observers, TAs, and admins).
- Sends separate 1-on-1 messages (`group_conversation=False`) so students cannot see each other's replies or addresses.
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
BASE_URL = "https://canvas.newschool.edu/api/v1"
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def get_enrolled_students():
    url = f"{BASE_URL}/courses/{COURSE_ID}/users?enrollment_type[]=student&per_page=100"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print("Error fetching enrolled students:", e)
        return []

def send_individual_messages(subject, body):
    students = get_enrolled_students()
    if not students:
        print("No enrolled students found.")
        return

    student_ids = [str(s["id"]) for s in students if "id" in s]
    print(f"Targeting {len(student_ids)} enrolled students (strictly excluding non-students)...")

    # Canvas Conversations API endpoint
    url = f"{BASE_URL}/conversations"
    
    # group_conversation=False sends an individual message to each recipient
    payload = {
        "recipients": student_ids,
        "subject": subject,
        "body": body,
        "group_conversation": False,
        "context_code": f"course_{COURSE_ID}"
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            print(f"✓ Successfully sent {len(student_ids)} individual private messages/emails!")
            print(f"  Subject: {subject}")
            print(f"  Canvas Conversation ID: {res[0].get('id') if isinstance(res, list) and res else 'Created'}")
    except Exception as e:
        print("Error sending conversations:", e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_canvas_messages.py '<Subject>' '<Body Text>'")
        print("Example: python3 send_canvas_messages.py 'Welcome to Device Art Tonight' 'Class starts at 7:00 PM...'")
        sys.exit(1)
        
    subject = sys.argv[1]
    body = sys.argv[2]
    send_individual_messages(subject, body)
