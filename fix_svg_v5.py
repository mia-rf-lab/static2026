import re
import subprocess

subprocess.run(['git', 'checkout', 'tw/commitment_to_sdgs.html'], cwd='/Users/mia/Desktop/0522南亞ESG 2026/static2025')

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
new_svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/diagram__commitment-to-sdgs__diagram.svg'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Modify the new SVG to add links
targets = {
    'y="56"': 'innovative_technology',
    'y="139"': 'harmonious_workplace',
    'y="222"': 'cleaner_production',
    'y="315"': 'responsible_procurement',
    'y="398"': 'common_good',
    'y="514"': 'integrity_transparency',
}

with open(new_svg_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if '<g filter="url(' in line and i + 1 < len(lines):
        next_line = lines[i+1]
        matched_target = None
        for y_pos, name in targets.items():
            if y_pos in next_line:
                matched_target = name
                break
        
        if matched_target:
            new_lines.append(f'<a href="{matched_target}.html">\n')
            new_lines.append(f'<g id="{matched_target}">\n')
            new_lines.append(line)
            
            open_g = 1
            i += 1
            while i < len(lines) and open_g > 0:
                current_line = lines[i]
                new_lines.append(current_line)
                
                open_g += len(re.findall(r'<g\b', current_line))
                open_g -= len(re.findall(r'</g>', current_line))
                
                if open_g == 0:
                    new_lines.append('</g>\n')
                    new_lines.append('</a>\n')
                
                i += 1
            continue

    new_lines.append(line)
    i += 1

modified_svg = "".join(new_lines)

# 2. Replace the entire <svg> block in HTML
svg_start = html.find('<svg width="1201" height="637"')
if svg_start == -1:
    svg_start = html.find('<svg') # Fallback if width/height differ

svg_end = html.find('</svg>', svg_start) + len('</svg>')

final_html = html[:svg_start] + modified_svg + html[svg_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Fix v5 completed successfully!")
