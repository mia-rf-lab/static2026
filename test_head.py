with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<head>')
end = html.find('</head>')
print(html[start:end+7])
