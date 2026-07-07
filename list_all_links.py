import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

a_tags = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a\s*>', svg_content, re.DOTALL)
for href, a in a_tags:
    m = re.search(r'<g[^>]*id="([^"]+)"', a)
    if m:
        gid = m.group(1).encode('latin-1').decode('utf-8', errors='ignore')
        print(f"{gid}: {href}")
