import sys

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace year
html = html.replace('2025年永續目標', '2026年永續目標')

# Replace SDG 4
html = html.replace('<li>累積培育半導體人才 (自2021年起)≧1,500人</li>', '<li>累積培育半導體人才(自2021年起)≧1,500人</li>')

# Replace SDG 6
html = html.replace('<li>自2018年起累計單位產能用水量 (較2017年減少)>35.5%</li>', '<li>自2018年起累計單位產能用水量(較2017年減少)≧35.5%</li>')
html = html.replace('<li>水汙染主要指標平均百分比優於法規標準≥52%</li>', '<li>水汙染主要指標平均百分比優於法規標準≧55%</li>')

# Replace SDG 7
html = html.replace('<li>節能措施累積節能總量 (自2017年起)≧75,000 MWh</li>', '<li>節能措施累積節能總量(自2017年起)≧82,500 MWh</li>')
html = html.replace('<li>全年再生能源使用≧45,000MWh</li>', '<li>全年再生能源使用≧90,000MWh</li>')

# Replace SDG 8
html = html.replace('<li>失能傷害頻率<0.17< /li>', '<li>失能傷害頻率<0.16</li>')
html = html.replace('<li>失能傷害嚴重度<5.9< /li>', '<li>失能傷害嚴重度<5.7</li>')
html = html.replace('<li>自主檢查率>94%</li>', '<li>自主檢查率>94.1%</li>')

# Replace SDG 9
html = html.replace('<li>10奈米級DRAM製程及16Gb DDR5 產品達出貨驗證標準</li>', '<li>第三代10奈米級DRAM製程及16Gb DDR5 產品達出貨驗證標準</li>')
html = html.replace('<li>建立具備人工智慧輔助高效能生產線，累計開發150項智能系統</li>', '<li>建立具備人工智慧輔助高效能生產線，累計開發170項智能系統</li>')

# Replace SDG 13
html = html.replace('<li>製程全氟碳化物排放削減率≧93 %</li>', '<li>製程全氟碳化物排放削減率達93 %以上</li>')
html = html.replace('<li>100%原料不含全氟辛酸相關物質</li>', '<li>100%原料不含全氟辛酸（PFOA）相關物質</li>\n                  <li>外部稽核或勞動檢查結果無重大缺失</li>\n                  <li>職場不法侵害案件維持0事件</li>')

# Replace SDG 17
html = html.replace('<li>社會參與投入資源年成長比例 (人時) ≧10%</li>', '<li>社會參與投入資源年成長比例(人時) ≧10%</li>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
