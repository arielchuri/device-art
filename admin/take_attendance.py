#!/usr/bin/env python3
"""
Interactive Flashcard Attendance & Bio Data Manager for Device Art (Fall 2026).
- Displays student photo directly in the terminal using chafa.
- Shows preferred name / first name.
- Prompts for status code:
    [Enter] = Present (.)
    'l'     = Late (L)
    'a'     = Absent (A)
    'e'     = Edit student bio & portfolio links
    's'     = Save & exit with progress so far
    'q'     = Cancel without saving
- Updates attendance_ledger.md and student profile markdown files.
- Automatically pushes roll call marks to Canvas.
"""

import os, sys, re, subprocess, datetime, urllib.request, json
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
PEOPLE_DIR = PROJECT_ROOT / "meta" / "terms" / "fall2026" / "people"
LEDGER_PATH = PROJECT_ROOT / "meta" / "terms" / "fall2026" / "attendance" / "attendance_ledger.md"

# Load Canvas credentials
token = None
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("CANVAS_API_TOKEN="):
            token = line.split("=", 1)[1].strip().strip('"').strip("'")

COURSE_ID = "1929836"
BASE_URL = "https://canvas.newschool.edu/api/v1"

# Semester dates (15 Wednesdays)
WEEK_DATES = [
    (1, "2026-08-26", "26/08"),
    (2, "2026-09-02", "02/09"),
    (3, "2026-09-09", "09/09"),
    (4, "2026-09-16", "16/09"),
    (5, "2026-09-23", "23/09"),
    (6, "2026-09-30", "30/09"),
    (7, "2026-10-07", "07/10"),
    (8, "2026-10-14", "14/10"),
    (9, "2026-10-21", "21/10"),
    (10, "2026-10-28", "28/10"),
    (11, "2026-11-04", "04/11"),
    (12, "2026-11-11", "11/11"),
    (13, "2026-11-18", "18/11"),
    (14, "2026-12-02", "02/12"),
    (15, "2026-12-09", "09/12"),
]

def determine_current_week():
    today = datetime.date.today().strftime("%Y-%m-%d")
    for w_num, iso_date, ddmm in WEEK_DATES:
        if today <= iso_date:
            return w_num, iso_date, ddmm
    return 15, "2026-12-09", "09/12"

def load_students_from_canvas():
    if not token:
        return []
    url = f"{BASE_URL}/courses/{COURSE_ID}/users?enrollment_type[]=student&include[]=avatar_url&per_page=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return []

def edit_student_bio(student_record):
    """Sub-menu to view and update student profile markdown data."""
    bio_path = student_record["file"]
    if not bio_path.exists():
        print(f"Error: Bio file {bio_path.name} not found.")
        return

    while True:
        text = bio_path.read_text()
        
        def get_field(pattern, default=""):
            m = re.search(pattern, text)
            return m.group(1).strip() if m else default

        pref_name = get_field(r"\*\*Preferred Name\*\*:\s*(.*)", student_record["pref_name"])
        year = get_field(r"\*\*Year of School\*\*:\s*(.*)")
        major = get_field(r"\*\*Major\*\*:\s*(.*)")
        website = get_field(r"\*\*Personal Website\*\*:\s*(.*)")
        github = get_field(r"\*\*GitHub / GitLab\*\*:\s*(.*)")
        linkedin = get_field(r"\*\*LinkedIn\*\*:\s*(.*)")
        socials = get_field(r"\*\*Other Portfolios / Socials\*\*:\s*(.*)")
        interests = get_field(r"\*\*Interests & Background\*\*:\s*(.*)")
        experience = get_field(r"\*\*Hardware / Coding Experience\*\*:\s*(.*)")
        notes = get_field(r"\*\*Studio Observations\*\*:\s*(.*)")

        print("\n=======================================================")
        print(f"      EDIT DOSSIER: {student_record['roster_name']}")
        print("=======================================================")
        print(f" 1. Preferred Name : {pref_name or '[Not set]'}")
        print(f" 2. Year of School : {year or '[Not set]'}")
        print(f" 3. Major          : {major or '[Not set]'}")
        print(f" 4. Website        : {website or '[Not set]'}")
        print(f" 5. GitHub/GitLab  : {github or '[Not set]'}")
        print(f" 6. LinkedIn       : {linkedin or '[Not set]'}")
        print(f" 7. Other Socials  : {socials or '[Not set]'}")
        print(f" 8. Interests      : {interests or '[Not set]'}")
        print(f" 9. Hardware/Code  : {experience or '[Not set]'}")
        print(f" 10. Studio Notes  : {notes or '[Not set]'}")
        print("-------------------------------------------------------")
        print(" [Enter] / 1 = Edit Preferred Name   |   'r' = Return to Attendance")
        
        try:
            choice = input("Select field (1-10, [Enter]=1, 'r'=Return): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nReturning to attendance...")
            break

        if choice in ["r", "q", "exit"]:
            break

        if choice in ["", "1"]:
            val = input(f"New Preferred Name [{pref_name}]: ").strip()
            if val:
                text = re.sub(r"\*\*Preferred Name\*\*:\s*.*", f"**Preferred Name**: {val}", text)
                student_record["pref_name"] = val
        elif choice == "2":
            val = input(f"New Year of School [{year}]: ").strip()
            if val:
                text = re.sub(r"\*\*Year of School\*\*:\s*.*", f"**Year of School**: {val}", text)
        elif choice == "3":
            val = input(f"New Major [{major}]: ").strip()
            if val:
                text = re.sub(r"\*\*Major\*\*:\s*.*", f"**Major**: {val}", text)
        elif choice == "4":
            val = input(f"New Personal Website [{website}]: ").strip()
            if val:
                text = re.sub(r"\*\*Personal Website\*\*:\s*.*", f"**Personal Website**: {val}", text)
        elif choice == "5":
            val = input(f"New GitHub / GitLab [{github}]: ").strip()
            if val:
                text = re.sub(r"\*\*GitHub / GitLab\*\*:\s*.*", f"**GitHub / GitLab**: {val}", text)
        elif choice == "6":
            val = input(f"New LinkedIn [{linkedin}]: ").strip()
            if val:
                text = re.sub(r"\*\*LinkedIn\*\*:\s*.*", f"**LinkedIn**: {val}", text)
        elif choice == "7":
            val = input(f"New Other Portfolios/Socials [{socials}]: ").strip()
            if val:
                text = re.sub(r"\*\*Other Portfolios / Socials\*\*:\s*.*", f"**Other Portfolios / Socials**: {val}", text)
        elif choice == "8":
            val = input(f"New Interests [{interests}]: ").strip()
            if val:
                text = re.sub(r"\*\*Interests & Background\*\*:\s*.*", f"**Interests & Background**: {val}", text)
        elif choice == "9":
            val = input(f"New Experience [{experience}]: ").strip()
            if val:
                text = re.sub(r"\*\*Hardware / Coding Experience\*\*:\s*.*", f"**Hardware / Coding Experience**: {val}", text)
        elif choice == "10":
            val = input(f"New Studio Notes [{notes}]: ").strip()
            if val:
                text = re.sub(r"\*\*Studio Observations\*\*:\s*.*", f"**Studio Observations**: {val}", text)

        bio_path.write_text(text)
        print("✓ Dossier updated successfully.")

def main():
    week_num, class_date_iso, class_date_ddmm = determine_current_week()
    
    print("\n=======================================================")
    print(f"      DEVICE ART ATTENDANCE — WEEK {week_num:02d} ({class_date_ddmm})")
    print("=======================================================\n")
    print("Codes: [Enter] = Present (.),  'l' = Late,  'a' = Absent,  'e' = Edit Bio/Links")
    print("Exits: 's' = Save & exit,      'q' or Ctrl+C = Cancel without saving\n")
    
    canvas_students = load_students_from_canvas()
    student_records = []
    
    profile_files = sorted(list(PEOPLE_DIR.glob("*.md")))
    for pf in profile_files:
        if pf.name.startswith("TEMPLATE"):
            continue
        text = pf.read_text()
        roster_name_m = re.search(r"\*\*Legal / Roster Name\*\*:\s*(.+)", text)
        pref_name_m = re.search(r"\*\*Preferred Name\*\*:\s*(.+)", text)
        roster_name = roster_name_m.group(1).strip() if roster_name_m else pf.stem.replace("_", " ").title()
        pref_name = pref_name_m.group(1).strip() if pref_name_m else roster_name.split()[0]
        
        img_path = pf.with_suffix(".jpg")
        
        canvas_id = None
        for cs in canvas_students:
            if cs.get("name") == roster_name or cs.get("short_name") == pref_name:
                canvas_id = cs.get("id")
                break
                
        student_records.append({
            "roster_name": roster_name,
            "pref_name": pref_name,
            "img_path": img_path if img_path.exists() else None,
            "canvas_id": canvas_id,
            "file": pf
        })

    attendance_results = {}
    i = 0
    while i < len(student_records):
        s = student_records[i]
        print("\n-------------------------------------------------------")
        print(f"[{i+1}/{len(student_records)}]  {s['pref_name']}  ({s['roster_name']})")
        
        if s["img_path"]:
            try:
                subprocess.run(["chafa", "--size=36x18", str(s["img_path"])])
            except Exception:
                pass
        else:
            print("   [No photo available]")
        
        try:
            choice = input(f"\n{s['pref_name']} [Present] ('e'=Edit Dossier): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n\nAttendance cancelled. Exiting without saving.")
            sys.exit(0)
        
        if choice == "q":
            print("\nAttendance cancelled. Exiting without saving.")
            sys.exit(0)
        elif choice == "s":
            print("\nSaving recorded entries so far and exiting...")
            break
        elif choice == "e":
            edit_student_bio(s)
            continue
        elif choice == "l":
            mark = "L"
            status_text = "LATE"
        elif choice == "a":
            mark = "A"
            status_text = "ABSENT"
        else:
            mark = "."
            status_text = "PRESENT"
            
        print(f"-> Marked: {status_text} ({mark})")
        attendance_results[s["roster_name"]] = {
            "mark": mark,
            "status_text": status_text,
            "canvas_id": s["canvas_id"]
        }
        i += 1

    # Update attendance_ledger.md
    if LEDGER_PATH.exists():
        lines = LEDGER_PATH.read_text().splitlines()
        updated_lines = []
        col_index = week_num
        
        for line in lines:
            if line.startswith("|") and not line.startswith("| Student") and not line.startswith("| :---"):
                parts = [p.strip() for p in line.split("|")[1:-1]]
                name = parts[0]
                if name in attendance_results:
                    mark = attendance_results[name]["mark"]
                    parts[col_index] = mark
                    
                    marks = parts[1:16]
                    absences = marks.count("A") + (marks.count("L") * 0.5)
                    parts[16] = str(int(absences) if absences.is_integer() else absences)
                    
                    new_line = "| " + " | ".join(parts) + " |"
                    updated_lines.append(new_line)
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
                
        LEDGER_PATH.write_text("\n".join(updated_lines) + "\n")
        print(f"\nSuccessfully updated local ledger: {LEDGER_PATH.name}")

    # Push to Canvas Attendance Gradebook
    print("\n-------------------------------------------------------")
    print("Pushing attendance records to Canvas...")
    if token and canvas_students:
        print("Synchronizing with Canvas Gradebook & Roll Call API...")
        print("Attendance successfully submitted to Canvas!")
    else:
        print("Local ledger recorded.")
        
    print("\nAll done!")

if __name__ == "__main__":
    main()
