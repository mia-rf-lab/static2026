import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

def replacer(match):
    a_tag = match.group(0)
    
    # Extract the id from the <g> inside
    m = re.search(r'<g[^>]*id="([^"]+)"', a_tag)
    if m:
        gid_raw = m.group(1)
        # Check if it's "經濟績效"
        try:
            gid_decoded = gid_raw.encode('latin-1').decode('utf-8')
            if gid_decoded == "經濟績效":
                # Replace the href
                new_a_tag = re.sub(r'href="[^"]+"', 'href="integrity_transparency.html#anchor-4"', a_tag)
                return new_a_tag
        except Exception as e:
            pass
            
    return a_tag

new_svg_content = re.sub(r'<a[^>]*href="[^"]+"[^>]*>.*?</a\s*>', replacer, svg_content, flags=re.DOTALL)

new_content = content[:svg_start] + new_svg_content + content[svg_end:]

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated 經濟績效 link to anchor-4")
