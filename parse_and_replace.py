import re

html_file = "tw/materiality_analysis.html"
full_svg_file = "img/svg/table__commitment-to-sdgs__section--tabulation.svg"
tbody_svg_file = "img/svg/table__commitment-to-sdgs__section--tabulation__tbody.svg"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(full_svg_file, "r", encoding="utf-8") as f:
    full_svg = f.read()

with open(tbody_svg_file, "r", encoding="utf-8") as f:
    tbody_svg = f.read()

# 1. Extract thead from full_svg
thead_start = full_svg.find('<g id="table__commitment-to-sdgs__section--tabulation__thead">')
if thead_start == -1:
    print("Could not find thead group in full_svg")
    exit(1)

# Find the matching closing </g> for thead
open_g = 0
thead_end = -1
for m in re.finditer(r'<(/?g)\b', full_svg[thead_start:]):
    if m.group(1) == 'g':
        open_g += 1
    elif m.group(1) == '/g':
        open_g -= 1
        if open_g == 0:
            thead_end = thead_start + m.end()
            break

if thead_end == -1:
    print("Could not find closing </g> for thead")
    exit(1)

thead_content = full_svg[thead_start:thead_end]

# Wrap thead_content in an SVG tag
# Original HTML had <svg width="1200" height="116" viewBox="0 0 1200 116" fill="none" xmlns="http://www.w3.org/2000/svg">
thead_svg = f'<svg width="1200" height="116" viewBox="0 0 1200 116" fill="none" xmlns="http://www.w3.org/2000/svg">\n{thead_content}\n</svg>'

# 2. Extract tbody from tbody_svg
# The tbody_svg is just an SVG file.
# But original HTML had <g id="table__commitment-to-sdgs__section--tabulation__tbody"> wrapping the inner elements.
# Let's just use the tbody_svg directly, but ensure it's inside <div class="sticky-tbody">
# tbody_svg is already an <svg>...</svg> string.

# Now replace in HTML
# Find <div class="sticky-thead"> ... </div>
thead_div_start = html_content.find('<div class="sticky-thead">')
thead_svg_start = html_content.find('<svg', thead_div_start)
thead_svg_end = html_content.find('</svg>', thead_svg_start) + 6

html_content = html_content[:thead_svg_start] + thead_svg + html_content[thead_svg_end:]

# Find <div class="sticky-tbody"> ... </div>
tbody_div_start = html_content.find('<div class="sticky-tbody">')
tbody_svg_start = html_content.find('<svg', tbody_div_start)
tbody_svg_end = html_content.find('</svg>', tbody_svg_start) + 6

html_content = html_content[:tbody_svg_start] + tbody_svg + html_content[tbody_svg_end:]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully replaced SVGs in HTML")
