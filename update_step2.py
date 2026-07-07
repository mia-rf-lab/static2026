import sys

with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# Block 1
old_h1 = "發放 <em>3,550</em> 份問卷調查關注程度"
new_h1 = "發放 <em>3,406</em> 份問卷調查關注程度"
content = content.replace(old_h1, new_h1)

old_p1 = "<p>除了透過日常營運過程與利害關係人的互動過程外，在發行報告書前，我們根據七大分類定義關鍵的利害關係人，進行問卷調查的發放，共計回收3,550份，員工 (3,476份)、股東/投資人 (2份) 、客戶 (24份)、供應商 (27份)、政府 (3份)、社會 (13份) 、媒體 (5份)，並分析各類利害關係人前五名關注的主題。</p>"
new_p1 = "<p>除了透過日常營運過程與利害關係人的互動過程外，在發行報告書前，我們根據七大分類定義關鍵的利害關係人，進行問卷調查的發放，共計回收3,406份，員工(3,342份)、股東/投資人(4份)、客戶(13份)、供應商(36份)、政府(3份)、社會(5份)、媒體(3份)，並分析各類利害關係人前五名關注的主題。</p>"
content = content.replace(old_p1, new_p1)

# Block 2
old_h2 = "<em>26</em> 份問卷衡量營運影響"
new_h2 = "<em>23</em> 份問卷衡量營運影響"
content = content.replace(old_h2, new_h2)

old_p2 = "由26位公司主管與同仁考量每個ESG議題對於組織營運的影響，鑑別出影響各營運因子的前五個關鍵ESG議題。"
new_p2 = "由23位公司主管與同仁考量每個ESG議題對於組織營運的影響，鑑別出影響各營運因子的前七個關鍵ESG議題。"
content = content.replace(old_p2, new_p2)

# Block 3
old_h3 = "<em>28</em> 位公司永續小組成員對外部影響的評估"
new_h3 = "<em>23</em> 位永續發展衝擊影響調查"
content = content.replace(old_h3, new_h3)

old_p3 = "辨識出與外部經濟、環境、人/人權相關的永續發展衝擊。"
new_p3 = "辨識出與外部經濟、環境、人權相關的永續發展衝擊。"
content = content.replace(old_p3, new_p3)

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

