with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/online_svg.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("clickable-area found:", "clickable-area" in html)
print("innovative_technology found:", "innovative_technology" in html)
