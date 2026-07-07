import xml.etree.ElementTree as ET

new_svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix-2.svg"

try:
    tree = ET.parse(new_svg_file)
    root = tree.getroot()
    
    # Check for text elements
    texts = list(root.iter('{http://www.w3.org/2000/svg}text')) + list(root.iter('text'))
    print(f"Found {len(texts)} text elements.")
    for t in texts[:5]:
        content = "".join(t.itertext()).strip()
        print(f"Text ID: {t.attrib.get('id', 'None')}, Content: {content}")
        
    # Check for groups
    gs = list(root.iter('{http://www.w3.org/2000/svg}g')) + list(root.iter('g'))
    print(f"\nFound {len(gs)} group elements.")
    for g in gs[:10]:
        print(f"Group ID: {g.attrib.get('id', 'None')}, children: {len(g)}")
        
except Exception as e:
    print('Error:', e)
