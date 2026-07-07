import codecs

html_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/materiality_analysis.html"
svg_file = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__section--matrix-2.svg"

with codecs.open(svg_file, "r", "utf-8") as f:
    svg_content = f.read()

with codecs.open(html_file, "r", "utf-8") as f:
    html_content = f.read()

target = """      <stop stop-color="#B1B1B1" />
      <stop offset="1" stop-color="#8A8A8A" />
    </linearGradient>
  </defs>
</svg>"""

if target in html_content:
    print("Found target!")
    new_content = html_content.replace(target, target + "\n<br><br><h3 style='text-align:center;width:100%;margin-top:50px;color:red;font-size:24px;'>--- 以下為新版矩陣圖測試 ---</h3><br>\n" + svg_content)
    with codecs.open(html_file, "w", "utf-8") as f:
        f.write(new_content)
    print("Replaced!")
else:
    print("Target not found. Check the source formatting.")
