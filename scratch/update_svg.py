import os

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'
svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/img/svg/en__diagram__materiality-analysis-matrix.svg'

with open(html_path, 'r', encoding='utf-8') as f:
    html_lines = f.readlines()

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_content = f.read()

# Modify the SVG content to add styles if needed (like tw version)
svg_content = svg_content.replace('<svg width="1062" height="860" viewBox="0 0 1062 860" fill="none" xmlns="http://www.w3.org/2000/svg">', '<svg width="1062" height="860" style="max-width: 1062px; margin: 0 auto; display: block;" viewBox="0 0 1062 860" fill="none" xmlns="http://www.w3.org/2000/svg">')

start_idx = -1
end_idx = -1

for i, line in enumerate(html_lines):
    if '<div class="matrix-chart"' in line and start_idx == -1:
        start_idx = i
    if '</svg>' in line and start_idx != -1 and end_idx == -1:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_wrapper = """        <div class="matrix-chart" data-animate="fadeInUp" data-animate-delay=".4" style="max-width: 1062px; margin: 0 auto;">
            <span>Environmental topics</span>
            <span>Social topics</span>
            <span>Governance topics</span>
            <span>Potential ESG Topics</span>

"""
    
    # We replace from start_idx to end_idx with new wrapper + new SVG
    new_lines = html_lines[:start_idx] + [new_wrapper, svg_content, '\n'] + html_lines[end_idx+1:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully updated SVG matrix.")
else:
    print("Failed to find boundaries.")
