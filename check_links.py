import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

a_tags = re.findall(r'<a[^>]*>(.*?)</a\s*>', svg_content, re.DOTALL)
for a in a_tags:
    if "ç¶“æ¿Ÿç¸¾æ•ˆ" in a:  # 經濟績效
        print("經濟績效 link block:")
        print(a[:200])
        m = re.search(r'href="([^"]+)"', svg_content[svg_content.find(a)-50:svg_content.find(a)+50])
        if m: print("Found href:", m.group(1))

