import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

thead_g_idx = content.find('id="table__commitment-to-sdgs__section--tabulation__thead"')
tbody_g_idx = content.find('id="table__commitment-to-sdgs__section--tabulation__tbody"')

# Find enclosing svg start
thead_svg_start = content.rfind('<svg', 0, thead_g_idx)
thead_svg_end = content.find('</svg>', thead_g_idx) + 6

tbody_svg_start = content.rfind('<svg', 0, tbody_g_idx)
tbody_svg_end = content.find('</svg>', tbody_g_idx) + 6

print(f"thead svg: {thead_svg_start} to {thead_svg_end}")
print(f"tbody svg: {tbody_svg_start} to {tbody_svg_end}")

if tbody_svg_start == thead_svg_start:
    print("THEY ARE IN THE SAME SVG!")
else:
    print("They are in separate SVGs.")
