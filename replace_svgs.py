import re

html_file = "tw/materiality_analysis.html"
thead_file = "img/svg/table__commitment-to-sdgs__section--tabulation__thead.svg"
tbody_file = "img/svg/table__commitment-to-sdgs__section--tabulation__tbody.svg"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(thead_file, "r", encoding="utf-8") as f:
    thead_content = f.read()

with open(tbody_file, "r", encoding="utf-8") as f:
    tbody_content = f.read()

# Extract just the SVG from the new files
thead_match = re.search(r'<svg.*?</svg>', thead_content, re.DOTALL | re.IGNORECASE)
tbody_match = re.search(r'<svg.*?</svg>', tbody_content, re.DOTALL | re.IGNORECASE)

if not thead_match or not tbody_match:
    print("Could not find SVG tags in the input files.")
    exit(1)

thead_svg = thead_match.group(0)
tbody_svg = tbody_match.group(0)

# Make sure they have the same layout properties as original if needed.
# The original has: <svg width="1200" height="116" viewBox="0 0 1200 116" fill="none" xmlns="http://www.w3.org/2000/svg">
# The new ones from figma probably have width/height/viewbox set correctly.

# Find the SVGs in the HTML file
thead_g_idx = html_content.find('id="table__commitment-to-sdgs__section--tabulation__thead"')
tbody_g_idx = html_content.find('id="table__commitment-to-sdgs__section--tabulation__tbody"')

if thead_g_idx == -1 or tbody_g_idx == -1:
    print("Could not find the target SVG groups in HTML.")
    exit(1)

thead_svg_start = html_content.rfind('<svg', 0, thead_g_idx)
thead_svg_end = html_content.find('</svg>', thead_g_idx) + 6

tbody_svg_start = html_content.rfind('<svg', 0, tbody_g_idx)
tbody_svg_end = html_content.find('</svg>', tbody_g_idx) + 6

if thead_svg_start == -1 or thead_svg_end == -1 or tbody_svg_start == -1 or tbody_svg_end == -1:
    print("Could not find the SVG boundaries in HTML.")
    exit(1)

# Replace them! (Replace tbody first so indices don't shift for thead)
new_html = html_content[:tbody_svg_start] + tbody_svg + html_content[tbody_svg_end:]
new_html = new_html[:thead_svg_start] + thead_svg + new_html[thead_svg_end:]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_html)

print("SVGs replaced successfully!")

