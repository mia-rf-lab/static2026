with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()
start = html.find('<linearGradient id="paint0_linear_317_223"')
end = html.find('</linearGradient>', start)
print(html[start:end+17])
