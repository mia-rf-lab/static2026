import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

clickable_start = html.find('<g id="clickable-area">')
clickable_end = html.find('</svg>', clickable_start)
clickable = html[clickable_start:clickable_end]

# We need to understand what is inside clickable-area vs new SVG.
print(clickable[:500])
