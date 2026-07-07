import codecs

html_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/materiality_analysis.html"

with codecs.open(html_file, "r", "utf-8") as f:
    html_content = f.read()

# find the new SVG opening tag (width="1062")
target = '<svg width="1062" height="860"'
if target in html_content:
    new_content = html_content.replace(target, '<svg width="1062" height="860" style="max-width: 1062px; margin: 0 auto; display: block;"')
    with codecs.open(html_file, "w", "utf-8") as f:
        f.write(new_content)
    print("Fixed width!")
else:
    print("Target not found.")
