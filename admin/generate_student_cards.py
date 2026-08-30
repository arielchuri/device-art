#!/usr/bin/env python3
"""
Generate Miro/Figma compatible student SVG cards matching the Device Art symbol language.
- White card background with subtle drop shadow
- Characteristic thick dotted card boundary (stroke-dasharray="0, 4" stroke-linecap="round")
- Andale Mono typography with category label ("STUDENT")
- Unique color bar & accent ring per student (bright yet toned down)
- Self-contained embedded Base64 photos (or monogram avatar for students without photo)
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
    preferred = s.get('Preferred Name', '')
    pronouns = s.get('Pronouns', '')
    email = s.get('Email', '')
    sis_id = s.get('N# / SIS ID', '')
    
    # Subtitle details (symbols style)
    subtitles = []
    if preferred and preferred != name:
        subtitles.append(f'goes by "{preferred}"')
    if pronouns:
        subtitles.append(pronouns.lower())
    sub_line = ' • '.join(subtitles) if subtitles else 'student'

    if s['has_photo'] and s['photo_path']:
        img_bytes = s['photo_path'].read_bytes()
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        avatar_svg = f'''  <!-- Photo circle with color accent stroke -->
  <g transform="translate(100, 85)">
    <defs>
      <clipPath id="avatar-clip-{slug}">
        <circle cx="0" cy="0" r="35" />
      </clipPath>
    </defs>
    <circle cx="0" cy="0" r="37" fill="none" stroke="{color['bar']}" stroke-width="1.5" />
    <image href="data:image/jpeg;base64,{img_b64}" x="-35" y="-35" width="70" height="70" clip-path="url(#avatar-clip-{slug})" preserveAspectRatio="xMidYMid slice" />
  </g>'''
    else:
        initials = get_initials(name)
        avatar_svg = f'''  <!-- Monogram circle with color accent stroke -->
  <g transform="translate(100, 85)">
    <circle cx="0" cy="0" r="37" fill="none" stroke="{color['bar']}" stroke-width="1.5" />
    <circle cx="0" cy="0" r="35" fill="{color['bg_tint']}" />
    <text x="0" y="8" font-family="Andale Mono, monospace" font-size="22" fill="{color['bar']}" text-anchor="middle">{initials}</text>
  </g>'''

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 230" width="200" height="230">
  <defs>
    <!-- Slight subtle drop shadow -->
    <filter id="card-shadow-{slug}" x="-10%" y="-10%" width="125%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08" />
    </filter>
    <clipPath id="card-clip-{slug}">
      <rect x="10" y="10" width="180" height="210" rx="4" />
    </clipPath>
  </defs>

  <!-- Solid white card background with slight shadow -->
  <rect x="10" y="10" width="180" height="210" rx="4" fill="#FFFFFF" filter="url(#card-shadow-{slug})" />

  <!-- Distinct top color bar -->
  <g clip-path="url(#card-clip-{slug})">
    <rect x="10" y="10" width="180" height="6" fill="{color['bar']}" />
  </g>

  <!-- Card boundary: thick dotted outline (Device Art symbol signature) -->
  <rect x="10" y="10" width="180" height="210" rx="4" fill="none" stroke="#888888" stroke-width="1" stroke-dasharray="0, 4" stroke-linecap="round"/>

  <!-- Top category label -->
  <text x="16" y="27" font-family="Andale Mono, monospace" font-size="8.5" fill="#888888">STUDENT</text>
  <text x="184" y="27" font-family="Andale Mono, monospace" font-size="8" fill="#AAAAAA" text-anchor="end">FA26</text>

{avatar_svg}

  <!-- Typography: Andale Mono in symbol hierarchy -->
  <text x="100" y="145" font-family="Andale Mono, monospace" font-size="11" fill="#000000" text-anchor="middle">{name.upper()}</text>
  <text x="100" y="160" font-family="Andale Mono, monospace" font-size="8.5" fill="#888888" text-anchor="middle">{sub_line}</text>
  <text x="100" y="174" font-family="Andale Mono, monospace" font-size="7.5" fill="#555555" text-anchor="middle">{email}</text>

  <!-- Dotted divider -->
  <line x1="25" y1="188" x2="175" y2="188" stroke="#888888" stroke-width="0.75" stroke-dasharray="0, 3" stroke-linecap="round" />

  <!-- Footer ID / Course tag -->
  <text x="100" y="204" font-family="Andale Mono, monospace" font-size="7" fill="#888888" text-anchor="middle">DEVICE ART • {sis_id if sis_id else "PARSONS DT"}</text>
</svg>
'''
    out_file = OUTPUT_DIR / f'{slug}.svg'
    out_file.write_text(svg_content)
    print(f'Generated: {out_file.name} [{color["name"]}]')

# Generate combined grid (5 columns)
cols = 5
card_w = 200
card_h = 230
gap = 20
padding = 30
rows = (len(students) + cols - 1) // cols
grid_w = padding * 2 + cols * card_w + (cols - 1) * gap
grid_h = padding * 2 + rows * card_h + (rows - 1) * gap

grid_elements = []
for idx, s in enumerate(students):
    slug = s['slug']
    r = idx // cols
    c = idx % cols
    x = padding + c * (card_w + gap)
    y = padding + r * (card_h + gap)
    card_svg = (OUTPUT_DIR / f"{slug}.svg").read_text()
    inner = card_svg.split("<svg", 1)[1].split(">", 1)[1].rsplit("</svg>", 1)[0]
    grid_elements.append(f'<g transform="translate({x}, {y})">\n{inner}\n</g>')

combined_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {grid_w} {grid_h}" width="{grid_w}" height="{grid_h}" fill="none">
  <!-- Board Background -->
  <rect width="{grid_w}" height="{grid_h}" fill="#F4F5F7" />
  
  <!-- Header -->
  <text x="{padding}" y="22" font-family="Andale Mono, monospace" font-size="12" fill="#888888">DEVICE ART / FALL 2026 / STUDENT ROSTER</text>

  <!-- Cards Grid -->
  {''.join(grid_elements)}
</svg>'''

grid_file = OUTPUT_DIR / 'all_students_roster_grid.svg'
grid_file.write_text(combined_svg)
print(f'Generated combined grid: {grid_file.name} ({grid_w}x{grid_h})')
