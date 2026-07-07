import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

a_tags = re.findall(r'<a[^>]*>(.*?)</a\s*>', svg_content, re.DOTALL)
for i, a in enumerate(a_tags):
    if "ç¶“æ¿Ÿç¸¾æ•ˆ" in a:
        m = re.search(r'<a[^>]*href="([^"]+)"', svg_content[svg_content.find(a)-50 : svg_content.find(a)+len(a)])
        if m:
            print(f"Current link: {m.group(1)}")
        else:
            print(f"Link not found in match {i}")

