import re

with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

clickable_start = html.find('<g id="clickable-area">')
clickable_end = html.find('</svg>', clickable_start)
clickable = html[clickable_start:clickable_end]

links = re.findall(r'<a href="([^"]+)">(.*?)</a>', clickable, re.DOTALL)
for href, content in links:
    match = re.search(r'<rect x="([^"]+)" y="([^"]+)"|<path d="M873 ([0-9]+)H633', content)
    if match:
        print(f"Link: {href}, Y-pos: {match.groups()}")
    else:
        # Check if it has a vector path that indicates position
        match = re.search(r'<path[^>]*d="M\d+\s+(\d+)[A-Z]', content)
        if match:
            print(f"Link: {href}, Y-pos: {match.group(1)}")
