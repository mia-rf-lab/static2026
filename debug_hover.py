import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

# For each 'a' tag, check if it has a 'rect' inside
a_tags = re.findall(r'<a[^>]*>(.*?)</a\s*>', svg_content, re.DOTALL)
print(f"Total a tags: {len(a_tags)}")
missing_rect = 0
for a in a_tags:
    if '<rect ' not in a:
        missing_rect += 1
        # Try to find the id of the group inside to identify
        m = re.search(r'<g[^>]*id="([^"]+)"', a)
        if m:
            gid = m.group(1).encode('latin-1').decode('utf-8', errors='ignore')
            print(f"Missing rect for: {gid}")

print(f"Total missing rect: {missing_rect}")

