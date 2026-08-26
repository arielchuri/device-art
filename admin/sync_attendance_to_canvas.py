#!/usr/bin/env python3
"""
Sync local attendance marks from attendance_ledger.md to Canvas Roll Call / Gradebook.
"""
import os, sys, re, urllib.request, json
from pathlib import Path

DIR = Path(__file__).resolve().parent
ENV_PATH = DIR.parents[2] / ".env"

token = None
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("CANVAS_API_TOKEN="):
            token = line.split("=", 1)[1].strip().strip('"').strip("'")

if not token:
    print("Error: CANVAS_API_TOKEN not found in .env")
    sys.exit(1)

course_id = "1929836"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

ledger_file = DIR / "attendance" / "attendance_ledger.md"
if not ledger_file.exists():
    print(f"Error: {ledger_file} not found.")
    sys.exit(1)

print(f"Attendance ledger found: {ledger_file.name}")
print(f"Target Canvas Course ID: {course_id}")
print("Ready to synchronize attendance marks to Canvas gradebook.")
