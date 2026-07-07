with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()
tbody_g_idx = content.find('id="table__commitment-to-sdgs__section--tabulation__tbody"')
tbody_svg_start = content.rfind('<svg', 0, tbody_g_idx)
print(content[tbody_svg_start - 100 : tbody_svg_start])
