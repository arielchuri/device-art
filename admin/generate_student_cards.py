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
    elif len(parts) == 1:
        return parts[0][:2].upper()
    return 'ST'

# Clean out old files in OUTPUT_DIR before generating
for old_f in OUTPUT_DIR.glob('*.svg'):
    old_f.unlink()

def render_card(s, idx, is_instructor=False):
    color = PALETTE[idx % len(PALETTE)]
    name = s.get('Name', s['slug'].replace('_', ' ').title())
    pref = s.get('Preferred Name', '')
    major = s.get('Major', '')
    year = s.get('Year', '')
    category = "INSTRUCTOR" if is_instructor else "STUDENT"

    font_size = 14
    if len(name) > 16:
        font_size = 11
    elif len(name) > 13:
        font_size = 12

    avatar_svg = ''
    if s.get('has_photo') and s.get('photo_path'):
        try:
            img_bytes = s['photo_path'].read_bytes()
            b64_img = base64.b64encode(img_bytes).decode('utf-8')
            avatar_svg = f'''  <g id="avatar_circle">
    <clipPath id="avatar_clip_{s['slug']}">
      <circle cx="100" cy="82" r="49.4" />
    </clipPath>
    <circle cx="100" cy="82" r="49.4" fill="#FFFFFF" />
    <image
       x="50.6"
       y="32.6"
       width="98.8"
       height="98.8"
       preserveAspectRatio="xMidYMid slice"
       clip-path="url(#avatar_clip_{s['slug']})"
       href="data:image/jpeg;base64,{b64_img}" />
    <circle
       cx="100"
       cy="82"
       r="49.4"
       fill="none"
       stroke="{color['bar']}"
       stroke-width="2"
       style="stroke-width:2;stroke-dasharray:none;fill:none;stroke:{color['bar']}" />
  </g>'''
        except Exception as e:
            print(f"Error embedding image for {s['slug']}: {e}")

    if not avatar_svg:
        initials = get_initials(name)
        avatar_svg = f'''  <g id="avatar_circle">
    <circle cx="100" cy="82" r="49.4" fill="{color['bg_tint']}" />
    <circle
       cx="100"
       cy="82"
       r="49.4"
       fill="none"
       stroke="{color['bar']}"
       stroke-width="2"
       style="stroke-width:2;stroke-dasharray:none;fill:none;stroke:{color['bar']}" />
    <text
       x="100"
       y="91"
       font-family="'Andale Mono', monospace"
       font-size="32px"
       font-weight="bold"
       fill="{color['bar']}"
       text-anchor="middle">{initials}</text>
  </g>'''

    sub_element = ''
    if pref and pref.lower() not in name.lower():
        sub_element = f'''  <text
     x="100"
     y="166"
     font-family="'Andale Mono', monospace"
     font-size="9px"
     fill="#666666"
     text-anchor="middle">("{pref}")</text>'''
    elif major:
        short_major = major.replace('BFA ', '').replace('Design & Technology', 'D&T')
        sub_element = f'''  <text
     x="100"
     y="166"
     font-family="'Andale Mono', monospace"
     font-size="8.5px"
     fill="#666666"
     text-anchor="middle">{short_major}</text>'''

    svg_content = f'''<svg
   xmlns="http://www.w3.org/2000/svg"
   viewBox="0 0 200 200"
   width="200"
   height="200">
  <!-- Outer Card Fill & Tint -->
  <rect x="0" y="0" width="200" height="200" fill="{color['bg_tint']}" />
  
  <!-- Bottom Color Banner -->
  <rect
     x="1"
     y="172"
     width="198"
     height="27"
     fill="{color['bar']}"
     stroke="{color['bar']}"
     stroke-width="1" />

  <!-- Outer Border -->
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
     fill="#888888">{category}</text>
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

    dest = PEOPLE_DIR / 'instructor_card.svg' if is_instructor else OUTPUT_DIR / f"{s['slug']}.svg"
    dest.write_text(svg_content)
    print(f"Generated: {dest.relative_to(BASE_DIR)} [{color['name']}]")
    return dest, svg_content

# Generate Instructor Card
ariel_data = {'slug': 'ariel_churi', 'Name': 'Ariel Churi', 'has_photo': (PEOPLE_DIR / 'ariel_churi.jpg').exists(), 'photo_path': PEOPLE_DIR / 'ariel_churi.jpg'}
inst_dest, inst_svg = render_card(ariel_data, 0, is_instructor=True)

# Generate Student Cards
student_svgs = []
for idx, s in enumerate(students):
    s_dest, s_svg = render_card(s, idx + 1, is_instructor=False)
    student_svgs.append((s, s_svg))

# Generate combined grid (5 columns, 14 student cards + instructor card)
all_cards_svgs = [('ariel_churi', inst_svg)] + [(s['slug'], svg) for s, svg in student_svgs]
cols = 5
card_size = 200
gap = 20
padding = 30
rows = (len(all_cards_svgs) + cols - 1) // cols
grid_w = padding * 2 + cols * card_size + (cols - 1) * gap
grid_h = padding * 2 + rows * card_size + (rows - 1) * gap

grid_elements = []
for idx, (slug, card_svg) in enumerate(all_cards_svgs):
    r = idx // cols
    c = idx % cols
    x = padding + c * (card_size + gap)
    y = padding + r * (card_size + gap)
    inner = card_svg.split("<svg", 1)[1].split(">", 1)[1].rsplit("</svg>", 1)[0]
    grid_elements.append(f'<g transform="translate({x}, {y})">\n{inner}\n</g>')

combined_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {grid_w} {grid_h}" width="{grid_w}" height="{grid_h}" fill="none">
  <rect width="{grid_w}" height="{grid_h}" fill="#F4F5F7" />
  <text x="{padding}" y="20" font-family="'Andale Mono', monospace" font-size="10" fill="#888888">DEVICE ART / FALL 2026 / ROSTER CARDS (200x200)</text>
  {''.join(grid_elements)}
</svg>'''

grid_file = PEOPLE_DIR / 'all_students_roster_grid.svg'
grid_file.write_text(combined_svg)
print(f'Generated combined grid: {grid_file.relative_to(BASE_DIR)} ({grid_w}x{grid_h})')
