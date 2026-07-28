import os
import re

svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/img/svg/en__diagram__materiality-analysis-matrix.svg'
html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_lines = f.readlines()

link_mapping = {
    '&#230;&#176;&#180;&#231;&#174;&#161;&#232;&#163;&#161;': 'cleaner_production.html#anchor-3',
    '&#229;&#187;&#162;&#230;&#163;&#132;&#231;&#137;&#169;&#232;&#136;&#135;&#229;&#190;&#170;&#231;&#146;&#176;&#229;&#134;&#141;&#229;&#136;&#169;&#231;&#148;&#168;': 'cleaner_production.html#anchor-4',
    '&#230;&#176;&#163;&#229;&#128;&#153;&#231;&#173;&#150;&#231;&#149;&#165;': 'cleaner_production.html#anchor-1',
    '&#232;&#131;&#189;&#230;&#186;&#144;&#231;&#174;&#161;&#231;&#144;&#134;': 'cleaner_production.html#anchor-2',
    '&#231;&#182;&#160;&#232;&#137;&#178;&#231;&#148;&#162;&#229;&#147;&#129;': 'innovative_technology.html#anchor-3',
    '&#232;&#129;&#183;&#230;&#165;&#173;&#229;&#129;&#165;&#229;&#186;&#183;&#232;&#136;&#135;&#229;&#174;&#137;&#229;&#133;&#168;': 'harmonious_workplace.html#anchor-6',
    '&#228;&#186;&#186;&#230;&#137;&#141;&#231;&#149;&#153;&#228;&#187;&#187;&#232;&#136;&#135;&#229;&#147;&#161;&#229;&#183;&#165;&#231;&#166;&#143;&#231;&#165;&#137;': 'harmonious_workplace.html#anchor-2',
    '&#228;&#186;&#186;&#230;&#172;&#138;&#232;&#136;&#135;&#229;&#139;&#158;&#232;&#179;&#135;&#233;&#151;&#156;&#228;&#191;&#130;': 'harmonious_workplace.html#anchor-5',
    '&#229;&#147;&#161;&#229;&#183;&#165;&#231;&#153;&#188;&#229;&#177;&#149;': 'harmonious_workplace.html#anchor-3',
    '&#231;&#164;&#190;&#230;&#156;&#131;&#229;&#143;&#131;&#232;&#136;&#135;': 'common_good.html#anchor-2',
    '&#231;&#160;&#148;&#231;&#153;&#188;&#232;&#136;&#135;&#229;&#137;&#181;&#230;&#150;&#176;': 'innovative_technology.html#anchor-1',
    '&#232;&#170;&#160;&#228;&#191;&#161;&#231;&#182;&#147;&#231;&#135;&#159;': 'integrity_transparency.html#anchor-4',
    '&#228;&#190;&#155;&#230;&#135;&#137;&#229;&#149;&#134;&#230;&#176;&#184;&#231;&#186;&#140;&#231;&#174;&#161;&#231;&#144;&#134;': 'responsible_procurement.html#anchor-1',
    '&#233;&#162;&#168;&#233;&#154;&#170;&#231;&#174;&#161;&#231;&#144;&#134;': 'integrity_transparency.html#anchor-2',
    '&#229;&#174;&#162;&#230;&#136;&#182;&#230;&#156;&#141;&#229;&#139;&#153;': 'integrity_transparency.html#anchor-5',
    '&#231;&#182;&#160;&#232;&#137;&#178;&#229;&#183;&#165;&#229;&#187;&#160;': 'cleaner_production.html#anchor-1',
    '&#231;&#182;&#147;&#230;&#191;&#159;&#231;&#184;&#190;&#230;&#149;&#136;': 'integrity_transparency.html#anchor-4',
    '&#229;&#133;&#172;&#229;&#143;&#184;&#230;&#178;&#187;&#231;&#144;&#134;': 'integrity_transparency.html#anchor-1',
    '&#231;&#148;&#162;&#229;&#147;&#129;&#229;&#147;&#129;&#232;&#179;&#170;': 'integrity_transparency.html#anchor-5',
    '&#229;&#147;&#161;&#229;&#183;&#165;&#229;&#164;&#154;&#229;&#133;&#131;&#229;&#140;&#150;': 'harmonious_workplace.html#anchor-1',
    '&#229;&#147;&#161;&#229;&#183;&#165;&#229;&#164;&#154;&#229;&#133;&#131;&#229;&#140;&#150;_2': 'harmonious_workplace.html#anchor-1',
    '&#230;&#176;&#184;&#231;&#186;&#140;&#229;&#142;&#159;&#230;&#157;&#144;&#230;&#150;&#153;': 'cleaner_production.html#anchor-4',
    '&#231;&#148;&#159;&#231;&#137;&#169;&#229;&#164;&#154;&#230;&#168;&#163;&#230;&#128;&#167;': 'cleaner_production.html#anchor-1',
    '&#232;&#179;&#135;&#232;&#168;&#138;&#229;&#174;&#137;&#229;&#133;&#168;&#232;&#136;&#135;&#233;&#154;&#177;&#231;&#167;&#129;&#229;&#133;&#168;': 'integrity_transparency.html#anchor-3',
}

new_svg_lines = []
active_link_stack = []

for line in svg_lines:
    if '<svg width=' in line:
        line = line.replace('<svg width="1062" height="860"', '<svg width="1062" height="860" style="max-width: 1062px; margin: 0 auto; display: block;"')
    
    # Check for <g id="...">
    g_match = re.search(r'<g id="([^"]+)"', line)
    
    # We also need to handle closing </g> correctly if we inserted an <a> tag
    # A single line could have <g...> or </g>
    
    is_closing_g = '</g>' in line
    is_opening_g = '<g' in line
    
    added_a_tag = False
    
    if g_match:
        gid = g_match.group(1)
        if gid in link_mapping:
            url = link_mapping[gid]
            # Replace the <g id="..."> with <a href="url"><g id="...">
            line = line.replace(g_match.group(0), f'<a href="{url}">{g_match.group(0)}')
            active_link_stack.append(True)
            added_a_tag = True
            
    if is_opening_g and not added_a_tag:
        active_link_stack.append(False)
        
    if is_closing_g:
        was_linked = active_link_stack.pop()
        if was_linked:
            line = line.replace('</g>', '</g></a>')
            
    new_svg_lines.append(line)

svg_content_with_links = "".join(new_svg_lines)

# Now put it into the HTML file
with open(html_path, 'r', encoding='utf-8') as f:
    html_lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(html_lines):
    if '<div class="matrix-chart"' in line and start_idx == -1:
        start_idx = i
    if '</svg>' in line and start_idx != -1 and end_idx == -1:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_wrapper = """        <div class="matrix-chart" data-animate="fadeInUp" data-animate-delay=".4">
            <span>Environmental topics</span>
            <span>Social topics</span>
            <span>Governance topics</span>
            <span>Potential ESG Topics</span>

"""
    new_lines = html_lines[:start_idx] + [new_wrapper, svg_content_with_links, '\n'] + html_lines[end_idx+1:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully added interactive links and updated HTML.")
else:
    print("Failed to find boundaries in HTML.")
