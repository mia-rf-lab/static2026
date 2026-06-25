import re
path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

fixes = [
    ('transform="translate(701 211)"', 'x="701" y="211"'),
    ('transform="translate(580 271)"', 'x="580" y="271"'),
    ('transform="translate(701 562)"', 'x="701" y="562"'),
    ('transform="translate(580 622)"', 'x="580" y="622"'),
    ('transform="translate(822 512)"', 'x="822" y="512"')
]

for old, new in fixes:
    html = html.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Transforms fixed")
