import xml.etree.ElementTree as ET

old_svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix.svg"
new_svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix-2.svg"

def extract_ids(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    ids = []
    for elem in root.iter():
        if 'id' in elem.attrib:
            ids.append(elem.attrib['id'])
    return ids

old_ids = extract_ids(old_svg_file)
new_ids = extract_ids(new_svg_file)

print("Old SVG IDs (first 30):", [id for id in old_ids if not id.startswith('Vector')][:30])
print("New SVG IDs (first 30):", [id for id in new_ids if not id.startswith('Vector')][:30])
