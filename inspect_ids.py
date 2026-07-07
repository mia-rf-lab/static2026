import xml.etree.ElementTree as ET

new_svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix-2.svg"

try:
    tree = ET.parse(new_svg_file)
    root = tree.getroot()
    
    gs = list(root.iter('{http://www.w3.org/2000/svg}g')) + list(root.iter('g'))
    ids = [g.attrib.get('id') for g in gs if g.attrib.get('id')]
    print("Found group IDs:", ids)
except Exception as e:
    print('Error:', e)
