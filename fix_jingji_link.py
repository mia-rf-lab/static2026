import re
with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('id="text-env-aspect"')
svg_start = content.rfind('<svg', 0, start_idx)
svg_end = content.find('</svg>', start_idx)
svg_content = content[svg_start:svg_end]

# Find the <a> tag that contains "ç¶“æ¿Ÿç¸¾æ•ˆ" (經濟績效)
# We can iterate over all <a> tags and replace if found
def replacer(match):
    a_tag = match.group(0)
    if "ç¶“æ¿Ÿç¸¾æ•ˆ" in a_tag:
        # replace the href
        new_a_tag = re.sub(r'href="[^"]+"', 'href="integrity_transparency.html#anchor-4"', a_tag)
        return new_a_tag
    return a_tag

new_svg_content = re.sub(r'<a[^>]*>(.*?)</a\s*>', replacer, svg_content, flags=re.DOTALL)

new_content = content[:svg_start] + new_svg_content + content[svg_end:]

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated 經濟績效 link to anchor-4")
