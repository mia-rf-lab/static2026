import xml.etree.ElementTree as ET

with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

svg_start = html.find('<svg')
svg_end = html.find('</svg>') + 6
svg = html[svg_start:svg_end]

try:
    ET.fromstring(svg)
    print("SVG is valid XML!")
except Exception as e:
    print("SVG is invalid!", e)
