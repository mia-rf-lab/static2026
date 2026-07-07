import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

a_tags = re.findall(r'<a[^>]*>(.*?)</a\s*>', svg_content, re.DOTALL)
for i, a in enumerate(a_tags):
    rect_match = re.search(r'<rect([^>]+)>', a)
    gid_match = re.search(r'<g[^>]*id="([^"]+)"', a)
    gid = gid_match.group(1).encode('latin-1').decode('utf-8', errors='ignore') if gid_match else f"unknown_{i}"
    
    if rect_match:
        attrs = rect_match.group(1)
        w = re.search(r'width="([^"]+)"', attrs)
        h = re.search(r'height="([^"]+)"', attrs)
        if w and h:
            width = float(w.group(1))
            height = float(h.group(1))
            if width > 300 or height > 100:
                print(f"{gid}: LARGE rect width={width}, height={height}")
        else:
            pass

print("Done checking rect sizes.")
