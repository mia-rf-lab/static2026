import xml.etree.ElementTree as ET
import sys
import re

svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix-2.svg"
html_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/materiality_analysis.html"

url_mapping = {
    '綠色工廠': 'cleaner_production#anchor-1',
    '經濟績效': 'integrity_transparency#anchor-1',
    '研發與創新': 'innovative_technology#anchor-1',
    '誠信經營': 'integrity_transparency#anchor-4',
    '公司治理': 'integrity_transparency#anchor-1',
    '產品品質': 'integrity_transparency#anchor-5',
    '職業健康與安全': 'harmonious_workplace#anchor-6',
    '人才留任與員工福祉': 'harmonious_workplace#anchor-2',
    '人權與勞資關係': 'harmonious_workplace#anchor-5',
    '員工多元化': 'harmonious_workplace#anchor-1',
    '員工發展': 'harmonious_workplace#anchor-3',
    '水管裡': 'cleaner_production#anchor-3',
    '永續原材料': 'cleaner_production#anchor-4',
    '生物多樣性': 'cleaner_production#anchor-1',
    '廢棄物與循環再利用': 'cleaner_production#anchor-4',
    '氣候策略': 'cleaner_production#anchor-1',
    '能源管理': 'cleaner_production#anchor-2',
    '供應商永續管理': 'responsible_procurement#anchor-1',
    '風險管理': 'integrity_transparency#anchor-2',
    '資訊安全與隱私全': 'integrity_transparency#anchor-3',
    '綠色產品': 'innovative_technology#anchor-3',
    '社會參與': 'common_good#anchor-2',
    '客戶服務': 'integrity_transparency#anchor-5'
}

ET.register_namespace("", "http://www.w3.org/2000/svg")

try:
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Use standard IDs
    env_g = ET.Element('{http://www.w3.org/2000/svg}g', id='text-env-aspect')
    social_g = ET.Element('{http://www.w3.org/2000/svg}g', id='text-social-aspect')
    gov_g = ET.Element('{http://www.w3.org/2000/svg}g', id='text-ec-aspect')
    issues_g = ET.Element('{http://www.w3.org/2000/svg}g', id='text-issues-aspect')
    
    # Parse defs to map gradients to colors
    paint_cat = {}
    defs = root.find('.//{http://www.w3.org/2000/svg}defs')
    if defs is not None:
        for grad in defs.findall('{http://www.w3.org/2000/svg}linearGradient'):
            grad_id = grad.attrib.get('id', '')
            colors = [stop.attrib.get('stop-color', '').upper() for stop in grad.findall('{http://www.w3.org/2000/svg}stop')]
            col_str = str(colors)
            if '1DA637' in col_str or '6CCC74' in col_str:
                paint_cat[grad_id] = env_g
            elif 'FF7A00' in col_str or 'FF9E45' in col_str:
                paint_cat[grad_id] = social_g
            elif '4985C6' in col_str or '859FD1' in col_str:
                paint_cat[grad_id] = gov_g
            else:
                paint_cat[grad_id] = issues_g
                
    parents_map = {c: p for p in tree.iter() for c in p}
    
    groups_by_id = {}
    
    for g in list(root.iter('{http://www.w3.org/2000/svg}g')):
        raw_id = g.attrib.get('id', '')
        if not raw_id: continue
        
        try:
            decoded_id = raw_id.encode('latin-1').decode('utf-8')
        except:
            decoded_id = raw_id
            
        clean_id = re.sub(r'_\d+$', '', decoded_id)
        
        if clean_id in url_mapping:
            if clean_id not in groups_by_id:
                groups_by_id[clean_id] = []
            groups_by_id[clean_id].append(g)

    processed = 0
    for clean_id, group_list in groups_by_id.items():
        
        cat_group = issues_g
        found_color = False
        for g in group_list:
            for path in g.iter('{http://www.w3.org/2000/svg}path'):
                fill = path.attrib.get('fill', '')
                if fill.startswith('url(#'):
                    paint_id = fill.split('url(#')[1].split(')')[0]
                    if paint_id in paint_cat:
                        cat_group = paint_cat[paint_id]
                        found_color = True
                        break
            if found_color:
                break
                
        print(f"Processing {clean_id} (found {len(group_list)} fragments) -> {cat_group.attrib['id']}")
            
        a_tag = ET.Element('{http://www.w3.org/2000/svg}a', href=url_mapping[clean_id])
        
        min_x, max_x = 9999, -9999
        min_y, max_y = 9999, -9999
        
        for g in group_list:
            for path in g.iter('{http://www.w3.org/2000/svg}path'):
                d = path.attrib.get('d', '')
                coords = [float(x) for x in re.findall(r'-?\d+\.?\d*', d)]
                if coords:
                    for i in range(0, len(coords)-1, 2):
                        min_x = min(min_x, coords[i])
                        max_x = max(max_x, coords[i])
                        min_y = min(min_y, coords[i+1])
                        max_y = max(max_y, coords[i+1])
        
        if min_x < max_x and min_y < max_y:
            pad = 10
            rect = ET.Element('{http://www.w3.org/2000/svg}rect', 
                              x=str(min_x - pad), y=str(min_y - pad), 
                              width=str(max_x - min_x + pad*2), height=str(max_y - min_y + pad*2), 
                              fill="transparent")
            a_tag.append(rect)
        
        for g in group_list:
            parent = parents_map[g]
            parent.remove(g)
            a_tag.append(g)
        
        cat_group.append(a_tag)
        processed += 1

    print(f"Processed {processed} merged groups.")
    
    root.append(env_g)
    root.append(social_g)
    root.append(gov_g)
    root.append(issues_g)
    
    new_svg_content = ET.tostring(root, encoding='utf-8').decode('utf-8')
    new_svg_final = new_svg_content.replace('<svg', '<svg width="1062" height="860" style="max-width: 1062px; margin: 0 auto; display: block;"')
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    start_new = html_content.find('<svg width="1062"')
    if start_new != -1:
        end_new = html_content.find('</svg>', start_new) + 6
        new_html = html_content[:start_new] + new_svg_final + html_content[end_new:]
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Replaced injected SVG with the corrected groups!")
    else:
        print("Could not find the SVG in HTML to replace.")

except Exception as e:
    print('Error:', e)
