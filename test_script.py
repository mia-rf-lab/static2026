with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
scripts = re.findall(r'<script.*?>.*?</script>', html, re.DOTALL)
for s in scripts:
    if 'innovative_technology' in s or 'hover' in s or 'Group' in s or 'Vector' in s or 'diagram' in s:
        print(s[:500])
