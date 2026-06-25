import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
new_svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/diagram__commitment-to-sdgs__diagram.svg'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find original clickable-area
start_idx = html.find('<g id="clickable-area">')
idx = start_idx
open_g = 0
end_idx = -1
while idx < len(html):
    if html.startswith('<g', idx):
        open_g += 1
        idx += 2
    elif html.startswith('</g>', idx):
        open_g -= 1
        if open_g == 0:
            end_idx = idx + 4
            break
        idx += 4
    else:
        idx += 1

if end_idx == -1:
    print("Could not parse clickable-area")
    exit(1)

clickable_area = html[start_idx:end_idx]

# Append .html to links in clickable-area to fix navigation errors locally
clickable_area = re.sub(r'href="([^"\.]+)"', r'href="\1.html"', clickable_area)

# Extract old SVG bounds
old_svg_start = html.find('<svg width="1201"')
old_svg_end = html.find('</svg>', old_svg_start) + 6

# Read new SVG
with open(new_svg_path, 'r', encoding='utf-8') as f:
    new_svg = f.read()

# Insert clickable_area into new SVG just before </svg>
new_svg = new_svg.replace('</svg>', f'\n{clickable_area}\n</svg>')

# Replace old SVG with new SVG in HTML
new_html = html[:old_svg_start] + new_svg + html[old_svg_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully injected clickable-area seamlessly!")
