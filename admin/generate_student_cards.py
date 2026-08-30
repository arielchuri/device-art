#!/usr/bin/env python3
"""
Generate Miro/Figma compatible student SVG cards matching the user's edited style:
- 200x200 square dimensions with sharp 90-degree corners (no rx)
- Outer border: 2px solid stroke in student's theme color (x=1, y=1, w=198, h=198)
- Bottom color bar: filled rect (x=1, y=172, w=198, h=27) in student's theme color
- Large circular avatar: radius=49.4 centered at (100, 82) with 2px theme color stroke
- Monospace typography (Andale Mono)
- Top-left category: "STUDENT" at (4.7, 12.3)
- Top-right term: "FA26" at (194.7, 12.3)
- Main name at y=154
- Subheadline (preferred name if present) at y=166 (or inside banner if needed)
"""

import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PEOPLE_DIR = BASE_DIR / 'meta' / 'terms' / 'fall2026' / 'people'
OUTPUT_DIR = PEOPLE_DIR / 'svg_cards'
OUTPUT_DIR.mkdir(exist_ok=True)

# 14 distinct bright yet toned-down / sophisticated colors
PALETTE = [
    {'name': 'Terracotta Red', 'bar': '#D95C4A', 'bg_tint': '#FDF2F0'},
    {'name': 'Warm Marigold',  'bar': '#D98E28', 'bg_tint': '#FEF9F0'},
    {'name': 'Sage Emerald',   'bar': '#369666', 'bg_tint': '#F0F9F4'},
    {'name': 'Periwinkle',     'bar': '#635CE0', 'bg_tint': '#F3F2FC'},
    {'name': 'Ocean Cobalt',   'bar': '#2F7EB8', 'bg_tint': '#F0F7FC'},
    {'name': 'Rust Tangerine', 'bar': '#D6622E', 'bg_tint': '#FDF3EE'},
    {'name': 'Mint Teal',      'bar': '#289C91', 'bg_tint': '#EFF9F8'},
    {'name': 'Mulberry Berry', 'bar': '#B83E6A', 'bg_tint': '#FDF0F5'},
    {'name': 'Mustard Ochre',  'bar': '#BC901C', 'bg_tint': '#FDF9EE'},
    {'name': 'Slate Indigo',   'bar': '#4E57B8', 'bg_tint': '#F2F3FC'},
    {'name': 'Dusty Rose',     'bar': '#C45474', 'bg_tint': '#FCF1F4'},
    {'name': 'Olive Green',    'bar': '#5C963E', 'bg_tint': '#F3F9EE'},
    {'name': 'Sky Azure',      'bar': '#348BCC', 'bg_tint': '#F1F7FD'},
    {'name': 'Amethyst Purple','bar': '#8B48A8', 'bg_tint': '#F7F1FB'}
]

students = []
for f in sorted(PEOPLE_DIR.glob('*.md')):
    if f.name == 'TEMPLATE_student.md':
        continue
    lines = f.read_text().splitlines()
    data = {'slug': f.stem}
    for l in lines:
        if ':' in l and l.startswith('- **'):
            k, v = l.split(':', 1)
            k = k.replace('- **', '').replace('**', '').strip()
            data[k] = v.strip().replace('`', '')
    photo_file = PEOPLE_DIR / f'{f.stem}.jpg'
    data['has_photo'] = photo_file.exists()
    data['photo_path'] = photo_file if photo_file.exists() else None
    students.append(data)

def get_initials(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1 and parts[0]:
        return parts[0][:2].upper()
    return 'DA'

for i, s in enumerate(students):
    color = PALETTE[i % len(PALETTE)]
    slug = s['slug']
    name = s.get('Legal / Roster Name') or s['slug'].replace('_', ' ').title()
    preferred = s.get('Preferred Name', '').strip()

    # Subheadline for preferred name
    sub_element = ''
    if preferred and preferred.lower() != name.lower():
        sub_element = f'''  <text
     x="100"
     y="166"
     font-family="'Andale Mono', monospace"
     font-size="8.5px"
     fill="#888888"
     text-anchor="middle">{preferred}</text>'''

    # Avatar (radius 49.39)
    if s['has_photo'] and s['photo_path']:
        img_bytes = s['photo_path'].read_bytes()
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        avatar_svg = f'''  <defs id="defs-{slug}">
    <clipPath id="avatar-clip-{slug}">
      <circle cx="100" cy="82" r="49.388664" />
    </clipPath>
  </defs>
  <image
     href="data:image/jpeg;base64,{img_b64}"
     x="50.611336"
     y="32.611336"
     width="98.777328"
     height="98.777328"
     clip-path="url(#avatar-clip-{slug})"
     preserveAspectRatio="xMidYMid slice" />
  <circle
     cx="100"
     cy="82"
     r="49.388664"
     fill="none"
     stroke="{color['bar']}"
     stroke-width="2"
     style="stroke:{color['bar']};stroke-width:2;stroke-dasharray:none;stroke-opacity:1" />'''
    else:
        initials = get_initials(name)
        avatar_svg = f'''  <circle
     cx="100"
     cy="82"
     r="49.388664"
     fill="{color['bg_tint']}"
     stroke="{color['bar']}"
     stroke-width="2"
     style="stroke:{color['bar']};stroke-width:2;stroke-dasharray:none;stroke-opacity:1" />
  <text
     x="100"
     y="92"
     font-family="'Andale Mono', monospace"
     font-size="28px"
     font-weight="normal"
     fill="{color['bar']}"
     text-anchor="middle">{initials}</text>'''

    # Font size for name
    font_size = 12
    if len(name) > 17:
        font_size = 10.5
    elif len(name) > 14:
        font_size = 11

    svg_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   viewBox="0 0 200 200"
   width="200"
   height="200"
   version="1.1"
   xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Slight subtle drop shadow -->
    <filter
       id="card-shadow-{slug}"
       x="0"
       y="0"
       width="1"
       height="1">
      <feDropShadow
         dx="0"
         dy="3"
         stdDeviation="4"
         flood-color="#000000"
         flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- Solid white card background with slight shadow -->
  <rect
     x="1"
     y="1"
     width="198"
     height="198"
     fill="#FFFFFF"
     filter="url(#card-shadow-{slug})" />

  <!-- Distinct bottom color bar (sharp, matching edited style) -->
  <rect
     x="1"
     y="171.95454"
     width="198"
     height="27.045454"
     fill="{color['bar']}"
     style="fill:{color['bar']};stroke-width:1" />

  <!-- Card boundary: 2px solid colored outline -->
  <rect
     x="1"
     y="1"
     width="198"
     height="198"
     fill="none"
     stroke="{color['bar']}"
     stroke-width="2"
     style="stroke-width:2;stroke-dasharray:none;fill:none;stroke:{color['bar']}" />

  <!-- Top-left category label & Top-right term tag -->
  <text
     x="4.7387695"
     y="12.319336"
     font-family="'Andale Mono', monospace"
     font-size="9px"
     fill="#888888">STUDENT</text>
  <text
     x="194.71191"
     y="12.319336"
     font-family="'Andale Mono', monospace"
     font-size="9px"
     fill="#888888"
     text-anchor="end">FA26</text>

{avatar_svg}

  <!-- Typography: Andale Mono (Main Name) -->
  <text
     x="100"
     y="154"
     font-family="'Andale Mono', monospace"
     font-size="{font_size}px"
     fill="#000000"
     text-anchor="middle">{name.upper()}</text>
{sub_element}
</svg>
'''
    out_file = OUTPUT_DIR / f'{slug}.svg'
    out_file.write_text(svg_content)
    print(f'Generated: {out_file.name} [{color["name"]}]')

# Generate combined grid (5 columns, all 15 cards)
all_cards = [{'slug': 'ariel_churi'}] + students
cols = 5
card_size = 200
gap = 20
padding = 30
rows = (len(all_cards) + cols - 1) // cols
grid_w = padding * 2 + cols * card_size + (cols - 1) * gap
grid_h = padding * 2 + rows * card_size + (rows - 1) * gap

grid_elements = []
for idx, s in enumerate(all_cards):
    slug = s['slug']
    r = idx // cols
    c = idx % cols
    x = padding + c * (card_size + gap)
    y = padding + r * (card_size + gap)
    card_svg = (OUTPUT_DIR / f"{slug}.svg").read_text()
    inner = card_svg.split("<svg", 1)[1].split(">", 1)[1].rsplit("</svg>", 1)[0]
    grid_elements.append(f'<g transform="translate({x}, {y})">\n{inner}\n</g>')

combined_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {grid_w} {grid_h}" width="{grid_w}" height="{grid_h}" fill="none">
  <!-- Board Background -->
  <rect width="{grid_w}" height="{grid_h}" fill="#F4F5F7" />
  
  <!-- Header -->
  <text x="{padding}" y="20" font-family="'Andale Mono', monospace" font-size="10" fill="#888888">DEVICE ART / FALL 2026 / ROSTER CARDS (200x200)</text>

  <!-- Cards Grid -->
  {''.join(grid_elements)}
</svg>'''

grid_file = OUTPUT_DIR / 'all_students_roster_grid.svg'
grid_file.write_text(combined_svg)
print(f'Generated combined grid: {grid_file.name} ({grid_w}x{grid_h})')
