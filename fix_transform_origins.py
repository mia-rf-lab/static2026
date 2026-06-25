import re

path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Modify CSS
html = html.replace('transform-box: fill-box;', '/* transform-box removed for absolute transform-origin */')
html = html.replace('transition: transform 1.5s steps(var(--steps, 10), end);', 'transition: transform 2.5s steps(var(--steps, 10), end);')

# Top row left
html = html.replace('fill="url(#paint0_linear_223_30409)" class="battery-fill"', 'fill="url(#paint0_linear_223_30409)" class="battery-fill" style="transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint2_linear_223_30409)" class="battery-fill"', 'fill="url(#paint2_linear_223_30409)" class="battery-fill" style="transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint4_linear_223_30409)" class="battery-fill"', 'fill="url(#paint4_linear_223_30409)" class="battery-fill" style="transform-origin: 0 300px;"')

# Bottom row left
html = html.replace('fill="url(#paint6_linear_223_30409)" class="battery-fill"', 'fill="url(#paint6_linear_223_30409)" class="battery-fill" style="transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint8_linear_223_30409)" class="battery-fill"', 'fill="url(#paint8_linear_223_30409)" class="battery-fill" style="transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint10_linear_223_30409)" class="battery-fill"', 'fill="url(#paint10_linear_223_30409)" class="battery-fill" style="transform-origin: 0 661px;"')

def add_origin_300(match):
    return match.group(1) + ' transform-origin: 0 300px;"'
def add_origin_661(match):
    return match.group(1) + ' transform-origin: 0 661px;"'

html = re.sub(r'(fill="url\(#paint12_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_300, html)
html = re.sub(r'(fill="url\(#paint13_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_300, html)
html = re.sub(r'(fill="url\(#paint14_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_300, html)

html = re.sub(r'(fill="url\(#paint15_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_661, html)
html = re.sub(r'(fill="url\(#paint16_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_661, html)
html = re.sub(r'(fill="url\(#paint17_linear_223_30409\)" class="grid-fill" style="--steps: \d+;)', add_origin_661, html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Transforms Origins and Speed fixed")
