from bs4 import BeautifulSoup
import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
new_svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/diagram__commitment-to-sdgs__diagram.svg'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract old SVG
old_svg_match = re.search(r'(<svg width="1201" height="637" viewBox="0 0 1201 637" fill="none" xmlns="http://www.w3.org/2000/svg">.*?</svg>)', html_content, re.DOTALL)
if not old_svg_match:
    print("Could not find old SVG")
    exit(1)
old_svg = old_svg_match.group(1)

# Extract clickable-area using BeautifulSoup
soup = BeautifulSoup(old_svg, 'html.parser')
clickable_area = soup.find('g', id='clickable-area')
if not clickable_area:
    print("Could not find clickable-area")
    exit(1)

# Modify the clickable area to be invisible but clickable
clickable_area['opacity'] = '0'
clickable_area['pointer-events'] = 'all'

# Read new SVG
with open(new_svg_path, 'r', encoding='utf-8') as f:
    new_svg_raw = f.read()

# Insert the clickable area into the new SVG right before </svg>
new_svg_soup = BeautifulSoup(new_svg_raw, 'html.parser')
svg_tag = new_svg_soup.find('svg')
svg_tag.append(clickable_area)

new_svg_str = str(svg_tag)

# Replace old SVG with new SVG
new_html = html_content.replace(old_svg, new_svg_str)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully replaced SVG in tw/commitment_to_sdgs.html")
