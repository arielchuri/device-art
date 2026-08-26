#!/usr/bin/env bash
# Opens the Canvas Roll Call Attendance tool directly in your default browser
COURSE_ID="1929836"
ATTENDANCE_URL="https://canvas.newschool.edu/courses/${COURSE_ID}/external_tools/sessionless_launch?launch_type=attendance"

echo "Opening Canvas Roll Call Attendance for Course ID: $COURSE_ID..."
open "https://canvas.newschool.edu/courses/${COURSE_ID}/users"
open "https://canvas.newschool.edu/courses/${COURSE_ID}"
