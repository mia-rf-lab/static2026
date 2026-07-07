with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

thead_idx = content.find('<div class="sticky-thead">')
tbody_idx = content.find('<div class="tbody-wrap', thead_idx)
if tbody_idx == -1:
    tbody_idx = content.find('<g id="table__commitment-to-sdgs__section--tabulation__tbody">')

print(f"thead div at {thead_idx}")
print(f"tbody start at {tbody_idx}")

svg_end_1 = content.find('</svg>', thead_idx)
print(f"first svg end at {svg_end_1}")

