import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

a_tags = re.findall(r'<a([^>]*)>', svg_content)
for i, attrs in enumerate(a_tags):
    print(f"[{i}] a attributes: {attrs}")

