with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<g id="clickable-area">')
end = html.find('<defs>', start)
if end == -1:
    end = html.find('</svg>', start)

clickable_content = html[start:end]
print("Clickable content ends with:")
print(clickable_content[-200:])
