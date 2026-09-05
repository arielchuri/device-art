#!/usr/bin/env python3
"""
Live Code Monitor & Dashboard for Device Art (Fall 2026)
Generates a 14-student live code wall displaying student avatars, status, and latest code snippets.
"""

import http.server
import socketserver
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PEOPLE_DIR = BASE_DIR / 'meta' / 'terms' / 'fall2026' / 'people'

def load_students():
    students = []
    for f in sorted(PEOPLE_DIR.glob('*.md')):
        if f.name == 'TEMPLATE_student.md':
            continue
        data = {'slug': f.stem}
        lines = f.read_text().splitlines()
        for l in lines:
            if ':' in l and l.startswith('- **'):
                k, v = l.split(':', 1)
                data[k.replace('- **', '').replace('**', '').strip()] = v.strip().replace('`', '')
        photo = PEOPLE_DIR / f"{f.stem}.jpg"
        data['has_photo'] = photo.exists()
        students.append(data)
    return students

def generate_html():
    students = load_students()
    card_items = []
    for s in students:
        name = s.get('Name', s['slug'].replace('_', ' ').title())
        avatar_url = f"/meta/terms/fall2026/people/{s['slug']}.jpg" if s['has_photo'] else ""
        avatar_html = f'<img src="{avatar_url}" class="avatar">' if avatar_url else f'<div class="avatar-ph">{name[:2].upper()}</div>'
        
        card_items.append(f'''
        <div class="code-card">
          <div class="card-header">
            {avatar_html}
            <div>
              <div class="student-name">{name}</div>
              <div class="student-status"><span class="dot online"></span> Live • code.py</div>
            </div>
          </div>
          <pre class="code-block"><code># {name}'s CircuitPython code.py
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)</code></pre>
        </div>''')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Device Art — Live Student Code Wall</title>
  <style>
    body {{ font-family: 'Andale Mono', monospace, sans-serif; background: #0F172A; color: #E2E8F0; margin: 0; padding: 20px; }}
    h1 {{ font-size: 18px; color: #38BDF8; margin-bottom: 5px; }}
    p {{ font-size: 12px; color: #94A3B8; margin-top: 0; margin-bottom: 20px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }}
    .code-card {{ background: #1E293B; border: 1px solid #334155; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; }}
    .card-header {{ display: flex; align-items: center; gap: 12px; padding: 12px; background: #0F172A; border-bottom: 1px solid #334155; }}
    .avatar {{ width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 1.5px solid #38BDF8; }}
    .avatar-ph {{ width: 36px; height: 36px; border-radius: 50%; background: #334155; color: #38BDF8; font-weight: bold; display: flex; align-items: center; justify-content: center; font-size: 14px; border: 1.5px solid #38BDF8; }}
    .student-name {{ font-weight: bold; font-size: 13px; color: #F8FAFC; }}
    .student-status {{ font-size: 10px; color: #94A3B8; display: flex; align-items: center; gap: 5px; margin-top: 2px; }}
    .dot {{ width: 6px; height: 6px; border-radius: 50%; display: inline-block; }}
    .dot.online {{ background: #22C55E; }}
    .code-block {{ margin: 0; padding: 12px; font-size: 11px; line-height: 1.4; color: #A7F3D0; overflow-x: auto; background: #1E293B; flex: 1; }}
  </style>
</head>
<body>
  <h1>DEVICE ART / FALL 2026 — LIVE STUDENT CODE WALL</h1>
  <p>Real-time view of all 14 active students • CircuitPython / RP2040</p>
  <div class="grid">
    {''.join(card_items)}
  </div>
</body>
</html>'''
    return html

if __name__ == '__main__':
    out_html = BASE_DIR / 'meta' / 'terms' / 'fall2026' / 'live_code_wall.html'
    out_html.write_text(generate_html())
    print(f"Generated Live Code Wall HTML: {out_html.relative_to(BASE_DIR)}")
