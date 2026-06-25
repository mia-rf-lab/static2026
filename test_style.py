with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
styles = re.findall(r'<style.*?>.*?</style>', html, re.DOTALL)
for s in styles:
    print("Found style!")
    print(s[:500])
