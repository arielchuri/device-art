#!/usr/bin/env python3
"""
Generate Miro/Figma compatible student & instructor SVG cards matching Device Art symbol specifications:
- 200x200 square dimensions with sharp 90-degree corners (no rx)
- White card background with subtle drop shadow
- Characteristic thick dotted card boundary (stroke-dasharray="0, 4" stroke-linecap="round")
- Monospace typography (Andale Mono)
- Top-left category: "STUDENT" (or "INSTRUCTOR" for Ariel)
- Top-right term: "FA26"
- Color bar along top edge (bright yet toned down for students, solid black for instructor)
- Self-contained embedded Base64 photo/gif
- Headline (y=150): Full legal/roster name in uppercase
- Subheadline (y=168): Preferred name IF present and distinct from full name; otherwise left completely blank
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

    # If preferred name exists and differs from full legal name, use it; otherwise blank
    sub_element = ''
    if preferred and preferred.lower() != name.lower():
        sub_element = f'\n  <!-- Subheadline: Preferred Name -->\n  <text x="100" y="168" font-family="Andale Mono, monospace" font-size="9" fill="#888888" text-anchor="middle">{preferred}</text>'

    # Avatar element centered at (100, 82)
    if s['has_photo'] and s['photo_path']:
        img_bytes = s['photo_path'].read_bytes()
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        avatar_svg = f'''  <!-- Photo circle -->
  <defs>
    <clipPath id="avatar-clip-{slug}">
      <circle cx="100" cy="82" r="32" />
    </clipPath>
  </defs>
  <circle cx="100" cy="82" r="33" fill="none" stroke="{color['bar']}" stroke-width="1.5" />
  <image href="data:image/jpeg;base64,{img_b64}" x="68" y="50" width="64" height="64" clip-path="url(#avatar-clip-{slug})" preserveAspectRatio="xMidYMid slice" />
  <circle cx="100" cy="82" r="32" fill="none" stroke="#000000" stroke-width="0.5" />'''
    else:
        initials = get_initials(name)
        avatar_svg = f'''  <!-- Monogram circle -->
  <circle cx="100" cy="82" r="33" fill="none" stroke="{color['bar']}" stroke-width="1.5" />
  <circle cx="100" cy="82" r="32" fill="{color['bg_tint']}" stroke="#000000" stroke-width="0.5" />
  <text x="100" y="89" font-family="Andale Mono, monospace" font-size="20" fill="{color['bar']}" text-anchor="middle">{initials}</text>'''

    # Name font size adjust if long
    font_size = 12
    if len(name) > 17:
        font_size = 10.5
    elif len(name) > 14:
        font_size = 11

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <!-- Slight subtle drop shadow -->
    <filter id="card-shadow-{slug}" x="-10%" y="-10%" width="125%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- Solid white card background with slight shadow -->
  <rect x="10" y="10" width="180" height="180" fill="#FFFFFF" filter="url(#card-shadow-{slug})" />

  <!-- Distinct top color bar (sharp, no corner rounding) -->
  <rect x="10" y="10" width="180" height="5" fill="{color['bar']}" />

  <!-- Card boundary: thick dotted outline (Device Art symbol signature) -->
  <rect x="10" y="10" width="180" height="180" fill="none" stroke="#888888" stroke-width="1" stroke-dasharray="0, 4" stroke-linecap="round"/>

  <!-- Top-left category label & Top-right term tag -->
  <text x="16" y="24" font-family="Andale Mono, monospace" font-size="9" fill="#888888">STUDENT</text>
  <text x="184" y="24" font-family="Andale Mono, monospace" font-size="9" fill="#888888" text-anchor="end">FA26</text>

{avatar_svg}

  <!-- Typography: Andale Mono (Main Name) -->
  <text x="100" y="150" font-family="Andale Mono, monospace" font-size="{font_size}" fill="#000000" text-anchor="middle">{name.upper()}</text>{sub_element}
</svg>
'''
    out_file = OUTPUT_DIR / f'{slug}.svg'
    out_file.write_text(svg_content)
    pref_note = f' (Preferred: "{preferred}")' if (preferred and preferred.lower() != name.lower()) else ' (No preferred name)'
    print(f'Generated: {out_file.name} [{color["name"]}]{pref_note}')

# Generate Instructor Card for Ariel Churi using ariel_churi.gif (Color: Black)
ariel_gif = PEOPLE_DIR / 'ariel_churi.gif'
if not ariel_gif.exists():
    ariel_gif = Path('/Users/arielchuri/Downloads/ariel.gif')

ariel_avatar_svg = ''
if ariel_gif.exists():
    img_bytes = ariel_gif.read_bytes()
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    ariel_avatar_svg = f'''  <!-- GIF/Photo circle -->
  <defs>
    <clipPath id="avatar-clip-ariel_churi">
      <circle cx="100" cy="82" r="32" />
    </clipPath>
  </defs>
  <circle cx="100" cy="82" r="33" fill="none" stroke="#000000" stroke-width="1.5" />
  <image href="data:image/gif;base64,{img_b64}" x="68" y="50" width="64" height="64" clip-path="url(#avatar-clip-ariel_churi)" preserveAspectRatio="xMidYMid slice" />
  <circle cx="100" cy="82" r="32" fill="none" stroke="#000000" stroke-width="0.5" />'''
else:
    ariel_avatar_svg = f'''  <!-- Monogram circle -->
  <circle cx="100" cy="82" r="33" fill="none" stroke="#000000" stroke-width="1.5" />
  <circle cx="100" cy="82" r="32" fill="#F0F0F0" stroke="#000000" stroke-width="0.5" />
  <text x="100" y="89" font-family="Andale Mono, monospace" font-size="20" fill="#000000" text-anchor="middle">AC</text>'''

ariel_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <!-- Slight subtle drop shadow -->
    <filter id="card-shadow-ariel_churi" x="-10%" y="-10%" width="125%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- Solid white card background with slight shadow -->
  <rect x="10" y="10" width="180" height="180" fill="#FFFFFF" filter="url(#card-shadow-ariel_churi)" />

  <!-- Distinct top black color bar (sharp, no corner rounding) -->
  <rect x="10" y="10" width="180" height="5" fill="#000000" />

  <!-- Card boundary: thick dotted outline (Device Art symbol signature) -->
  <rect x="10" y="10" width="180" height="180" fill="none" stroke="#888888" stroke-width="1" stroke-dasharray="0, 4" stroke-linecap="round"/>

  <!-- Top-left category label & Top-right term tag -->
  <text x="16" y="24" font-family="Andale Mono, monospace" font-size="9" fill="#888888">INSTRUCTOR</text>
  <text x="184" y="24" font-family="Andale Mono, monospace" font-size="9" fill="#888888" text-anchor="end">FA26</text>

{ariel_avatar_svg}

  <!-- Typography: Andale Mono (Main Name) -->
  <text x="100" y="150" font-family="Andale Mono, monospace" font-size="12" fill="#000000" text-anchor="middle">ARIEL CHURI</text>
</svg>
'''
ariel_out = OUTPUT_DIR / 'ariel_churi.svg'
ariel_out.write_text(ariel_svg)
print(f'Generated: {ariel_out.name} [Black / Instructor / GIF Embedded]')

# Generate combined grid (including instructor as first card + 14 students in 5 cols)
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
  <text x="{padding}" y="20" font-family="Andale Mono, monospace" font-size="10" fill="#888888">DEVICE ART / FALL 2026 / ROSTER CARDS (200x200)</text>

  <!-- Cards Grid -->
  {''.join(grid_elements)}
</svg>'''

grid_file = OUTPUT_DIR / 'all_students_roster_grid.svg'
grid_file.write_text(combined_svg)
print(f'Generated combined grid: {grid_file.name} ({grid_w}x{grid_h})')
