import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the matrix svg
# Assuming it's chart__commitment-to-sdgs__section--matrix-2 or similar
# Let's search for the one with 1062 width or something
start_idx = content.find('id="text-env-aspect"')
if start_idx == -1:
    # Just look for all a href in the file
    matches = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a\s*>', content, re.DOTALL)
    print("Found links:")
    for m in set(m[0] for m in matches):
        print(m)
else:
    # Get the whole SVG block
    svg_start = content.rfind('<svg', 0, start_idx)
    svg_end = content.find('</svg>', start_idx)
    svg_content = content[svg_start:svg_end]
    
    # Find all 'a' tags
    a_tags = re.findall(r'<a[^>]*>.*?</a\s*>', svg_content, re.DOTALL)
    print(f"Found {len(a_tags)} linked elements in SVG.")
    
    # Let's see what g ids exist in the svg
    g_ids = re.findall(r'<g[^>]+id="([^"]+)"', svg_content)
    print("\nAll g IDs in SVG:")
    for gid in sorted(set(g_ids)):
        print(gid)

