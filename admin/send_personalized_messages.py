#!/usr/bin/env python3
"""
Send personalized 1-on-1 Canvas Inbox messages to each enrolled student using their Preferred Name.
- Automatically fetches live Canvas enrollment.
- Substitutes {preferred_name} or {first_name} in the message body/subject.
- Sends 1-on-1 private messages (group_conversation=False).
"""

import sys, urllib.request, json, re
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

# Preferred name mapping exceptions
PREFERRED_NAMES = {
    "hyungrok son": "Roy",
    "pinkgua mao": "Pink",
    "maren mchugh": "Maren",
    "isabella pan": "Isabella"
}

def get_live_students():
    url = f"{BASE_URL}/courses/{COURSE_ID}/users?enrollment_type[]=student&per_page=100"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print("Error fetching enrolled students:", e)
        return []

def send_personalized(subject_template, body_template):
    students = get_live_students()
    if not students:
        print("No enrolled students found on Canvas.")
        return

    print(f"Preparing personalized messages for {len(students)} enrolled students...\n")

    for s in students:
        full_name = s.get("name", "")
        uid = str(s.get("id"))
        
        # Determine preferred name
        pref = PREFERRED_NAMES.get(full_name.lower())
        if not pref:
            pref = s.get("short_name", full_name).split()[0]

        subj = subject_template.replace("{name}", pref).replace("{preferred_name}", pref)
        body = body_template.replace("{name}", pref).replace("{preferred_name}", pref)

        url = f"{BASE_URL}/conversations"
        payload = {
            "recipients": [uid],
            "subject": subj,
            "body": body,
            "group_conversation": False,
            "context_code": f"course_{COURSE_ID}"
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")

        try:
            with urllib.request.urlopen(req) as resp:
                print(f"✓ Sent to {full_name} (Preferred: {pref}) [ID: {uid}]")
        except Exception as e:
            print(f"Error sending to {full_name}:", e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_personalized_messages.py '<Subject>' '<Body with {name}>'")
        print("Example: python3 send_personalized_messages.py 'Hi {name}' 'Hi {name}, checking in regarding...'")
        sys.exit(1)
        
    send_personalized(sys.argv[1], sys.argv[2])
