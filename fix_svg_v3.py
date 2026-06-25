import re
import subprocess

subprocess.run(['git', 'checkout', 'tw/commitment_to_sdgs.html'], cwd='/Users/mia/Desktop/0522南亞ESG 2026/static2025')

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
new_svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/diagram__commitment-to-sdgs__diagram.svg'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(new_svg_path, 'r', encoding='utf-8') as f:
    new_svg = f.read()

# 1. Extract new_defs and new_graphics
defs_match = re.search(r'<defs>(.*?)</defs>', new_svg, re.DOTALL)
new_defs = defs_match.group(1) if defs_match else ""

new_graphics = re.sub(r'<defs>.*?</defs>', '', new_svg, flags=re.DOTALL)
new_graphics_match = re.search(r'<svg[^>]*>(.*?)</svg>', new_graphics, re.DOTALL)
new_graphics = new_graphics_match.group(1) if new_graphics_match else new_graphics

# 2. Inject new_defs into old HTML's <defs>
defs_end_idx = html.find('</defs>')
html = html[:defs_end_idx] + '\n' + new_defs + '\n' + html[defs_end_idx:]

# 3. Replace unclickable-area
unclickable_start = html.find('<g id="unclickable-area">')
idx = unclickable_start + len('<g id="unclickable-area">')
open_g = 1
end_idx = -1
while idx < len(html):
    if html.startswith('<g ', idx) or html.startswith('<g>', idx):
        open_g += 1
        idx += 2
    elif html.startswith('</g>', idx):
        open_g -= 1
        if open_g == 0:
            end_idx = idx
            break
        idx += 4
    else:
        idx += 1

if end_idx == -1:
    print("Could not find matching </g> for unclickable-area")
    exit(1)

html = html[:unclickable_start + len('<g id="unclickable-area">')] + '\n' + new_graphics + '\n' + html[end_idx:]

# 4. Fix clickable-area hrefs to append .html
clickable_start = html.find('<g id="clickable-area">')
clickable_end = html.find('</svg>', clickable_start)
clickable_area = html[clickable_start:clickable_end]

clickable_area = re.sub(r'href="([^"\.]+)"', r'href="\1.html"', clickable_area)

html = html[:clickable_start] + clickable_area + html[clickable_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fix v3 completed successfully!")
