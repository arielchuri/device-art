#!/usr/bin/env python3
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PEOPLE_DIR = BASE_DIR / 'meta' / 'terms' / 'fall2026' / 'people'
OUTPUT_DIR = PEOPLE_DIR / 'svg_cards'
OUTPUT_DIR.mkdir(exist_ok=True)

# 14 distinct bright yet toned-down / sophisticated colors
PALETTE = [
    {'name': 'Terracotta Red', 'bar': '#D95C4A', 'bg_tint': '#FDF2F0', 'badge': '#FCE7E4'},
    {'name': 'Warm Marigold',  'bar': '#D98E28', 'bg_tint': '#FEF9F0', 'badge': '#FDF0DC'},
    {'name': 'Sage Emerald',   'bar': '#369666', 'bg_tint': '#F0F9F4', 'badge': '#DEF3E7'},
    {'name': 'Periwinkle',     'bar': '#635CE0', 'bg_tint': '#F3F2FC', 'badge': '#E6E4FA'},
    {'name': 'Ocean Cobalt',   'bar': '#2F7EB8', 'bg_tint': '#F0F7FC', 'badge': '#DDEEFA'},
    {'name': 'Rust Tangerine', 'bar': '#D6622E', 'bg_tint': '#FDF3EE', 'badge': '#FCE6DC'},
    {'name': 'Mint Teal',      'bar': '#289C91', 'bg_tint': '#EFF9F8', 'badge': '#DBF3F1'},
    {'name': 'Mulberry Berry', 'bar': '#B83E6A', 'bg_tint': '#FDF0F5', 'badge': '#FBE0EC'},
    {'name': 'Mustard Ochre',  'bar': '#BC901C', 'bg_tint': '#FDF9EE', 'badge': '#F9F1DB'},
    {'name': 'Slate Indigo',   'bar': '#4E57B8', 'bg_tint': '#F2F3FC', 'badge': '#E3E6F9'},
    {'name': 'Dusty Rose',     'bar': '#C45474', 'bg_tint': '#FCF1F4', 'badge': '#F9E2E8'},
    {'name': 'Olive Green',    'bar': '#5C963E', 'bg_tint': '#F3F9EE', 'badge': '#E4F3DA'},
    {'name': 'Sky Azure',      'bar': '#348BCC', 'bg_tint': '#F1F7FD', 'badge': '#DDEEFC'},
    {'name': 'Amethyst Purple','bar': '#8B48A8', 'bg_tint': '#F7F1FB', 'badge': '#EDE0F5'}
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
    
    # Subtitle badges
    badges = []
    if preferred and preferred != name:
        badges.append(f'Goes by "{preferred}"')
    if pronouns:
        badges.append(pronouns)
    badge_str = ' • '.join(badges)
    
    if s['has_photo'] and s['photo_path']:
        img_bytes = s['photo_path'].read_bytes()
        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        avatar_svg = f'''    <g transform="translate(140, 112)">
      <defs>
        <clipPath id="avatar-clip-{slug}">
          <circle cx="0" cy="0" r="52" />
        </clipPath>
      </defs>
      <circle cx="0" cy="0" r="55" fill="none" stroke="{color['bar']}" stroke-width="3.5" />
      <image href="data:image/jpeg;base64,{img_b64}" x="-52" y="-52" width="104" height="104" clip-path="url(#avatar-clip-{slug})" preserveAspectRatio="xMidYMid slice" />
    </g>'''
    else:
        initials = get_initials(name)
        avatar_svg = f'''    <g transform="translate(140, 112)">
      <circle cx="0" cy="0" r="55" fill="none" stroke="{color['bar']}" stroke-width="3.5" />
      <circle cx="0" cy="0" r="52" fill="{color['bg_tint']}" />
      <text x="0" y="12" font-family="'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="32" font-weight="700" fill="{color['bar']}" text-anchor="middle">{initials}</text>
    </g>'''

    badge_svg = ''
    if badge_str:
        badge_svg = f'''    <rect x="35" y="226" width="210" height="22" rx="11" fill="{color['badge']}" />
    <text x="140" y="241" font-family="'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11" font-weight="600" fill="{color['bar']}" text-anchor="middle">{badge_str}</text>'''

    email_svg = ''
    if email:
        email_svg = f'''    <text x="140" y="272" font-family="'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">{email}</text>'''

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="280" height="350" viewBox="0 0 280 350" fill="none">
  <defs>
    <filter id="card-shadow-{slug}" x="-10" y="-6" width="300" height="372" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#0F172A" flood-opacity="0.07" />
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.04" />
    </filter>
    <clipPath id="card-clip-{slug}">
      <rect x="0" y="0" width="280" height="350" rx="18" />
    </clipPath>
  </defs>

  <g filter="url(#card-shadow-{slug})">
    <!-- Card Base -->
    <rect x="0" y="0" width="280" height="350" rx="18" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />

    <!-- Color Bar -->
    <g clip-path="url(#card-clip-{slug})">
      <rect x="0" y="0" width="280" height="14" fill="{color['bar']}" />
      <circle cx="255" cy="7" r="3.5" fill="#FFFFFF" opacity="0.6" />
    </g>

    <!-- Photo or Monogram -->
{avatar_svg}

    <!-- Student Name -->
    <text x="140" y="206" font-family="'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="18" font-weight="700" fill="#0F172A" text-anchor="middle">{name}</text>

    <!-- Pronouns / Nickname -->
{badge_svg}

    <!-- Email Contact -->
{email_svg}

    <!-- Course Footer Pill -->
    <rect x="60" y="304" width="160" height="24" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <text x="140" y="320" font-family="'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="10" font-weight="600" fill="#94A3B8" text-anchor="middle" letter-spacing="0.5">DEVICE ART • FALL 2026</text>
  </g>
</svg>
'''
    out_file = OUTPUT_DIR / f'{slug}.svg'
    out_file.write_text(svg_content)
    print(f'Generated: {out_file.name} [{color["name"]}]')

print(f'Generated {len(students)} student cards in {OUTPUT_DIR}')

# Generate combined grid for 1-click import into Figma / Miro
cols = 5
card_w = 280
card_h = 350
gap_x = 24
gap_y = 28
padding = 40

rows = (len(students) + cols - 1) // cols
grid_w = padding * 2 + cols * card_w + (cols - 1) * gap_x
grid_h = padding * 2 + rows * card_h + (rows - 1) * gap_y

grid_elements = []
for idx, s in enumerate(students):
    slug = s['slug']
    r = idx // cols
    c = idx % cols
    x = padding + c * (card_w + gap_x)
    y = padding + r * (card_h + gap_y)
    
    # Read the card's inner SVG contents
    card_svg = (OUTPUT_DIR / f"{slug}.svg").read_text()
    # Extract inner content
    inner = card_svg.split("<svg", 1)[1].split(">", 1)[1].rsplit("</svg>", 1)[0]
    grid_elements.append(f'<g transform="translate({x}, {y})">\n{inner}\n</g>')

combined_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{grid_w}" height="{grid_h}" viewBox="0 0 {grid_w} {grid_h}" fill="none">
  <!-- Canvas Background -->
  <rect width="{grid_w}" height="{grid_h}" fill="#F8FAFC" rx="24" />
  
  <!-- Header Title -->
  <text x="{padding}" y="28" font-family="'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Device Art (Fall 2026) — Student Roster Cards</text>

  <!-- Student Cards Grid -->
  {''.join(grid_elements)}
</svg>'''

grid_file = OUTPUT_DIR / 'all_students_roster_grid.svg'
grid_file.write_text(combined_svg)
print(f'Generated combined grid: {grid_file.name} ({grid_w}x{grid_h})')
