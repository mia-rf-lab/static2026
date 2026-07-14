import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/tw/innovative_technology.html'

with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'class="grid-fill"' in line and 'transform="translate(' in line:
        line = re.sub(r'transform="translate\(\s*([\d\.]+)\s+([\d\.]+)\s*\)"', r'x="\1" y="\2"', line)
    new_lines.append(line)

with open(html_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed rect transforms")
