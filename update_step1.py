import sys

with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update intro paragraph
old_intro = "遵循GRI準則建立系統化的重大性分析方法，在鑑別與選擇、決定優先順序及確認與審查三大階段的流程下，識別屬於我們的重大永續議題，並研擬對應的長期永續目標。"
new_intro = "遵循GRI準則建立系統化的重大性分析方法，在鑑別與確認、決定優先順序及確認與批准四大階段的流程下，識別屬於我們的重大永續議題，並研擬對應的長期永續目標。"
content = content.replace(old_intro, new_intro)

# 2. Update step titles
content = content.replace("鑑別及選擇", "鑑別與確認")
content = content.replace("確認及審查", "確認與批准")

# 3. Update Step 1 - Block 1
old_p1 = "<p>依據GRI準則及國際標準AA 1000 SES利害關係人議合標準，透過永續發展工作會議，鑑別7大利害關係人族群，包括：員工、股東/投資人、客戶、供應商、政府、社會、媒體。針對7大利害關係人族群進行前五名關注主題的蒐集與分析，並且確認溝通管道，將利害關係人關切的主題納入永續發展日常工作及年度計畫。</p>"
new_p1 = "<p>依據 GRI 準則及國際標準 AA1000SES 利害關係人議合標準（Stakeholder Engagement Standard），南亞科技透過利害關係人鑑別，確認七大利害關係人族群，包括：員工、股東/投資人、客戶、供應商、政府、社會及媒體。公司針對上述七大利害關係人類別蒐集與分析其所關注之前七項議題，並建立相應之溝通管道。透過持續議合與回饋機制，將利害關係人關切的議題納入公司永續發展之日常管理與年度行動計畫中，以強化企業與利害關係人之溝通與合作。</p>"
content = content.replace(old_p1, new_p1)

# 4. Update Step 1 - Block 2 Heading
old_h2 = "選擇 <em>23</em> 個ESG主題"
new_h2 = "確認 <em>24</em> 個ESG主題"
content = content.replace(old_h2, new_h2)

# 5. Update Step 1 - Block 2 Content
old_p2 = "<p>從內外部觀點切入，辨識跟南亞科技營運相關的主題，主題來源包括國際永續規範與標準 (GRI Standards, SBSC, SDGs ,TCFD, TNFD, SBTi)、產業特定主題 (RBA, SASB)、永續評比 (DJSI, CDP, MSCI ESG Rating, FTSE４GOOD Emerging Index)、利害關係人溝通過程、內部經營目標等，彙整23個屬於南亞科技的ESG議題。</p>"
new_p2 = "<p>從內外部觀點切入，辨識跟南亞科技營運相關的議題，議題來源包括國際永續規範與標準(GRI Standards, ISSB, SDGs, TCFD, TNFD, SBTi ,ESRS)、產業特定主題(RBA, SASB)、永續評比(DJBIC, CDP, MSCI ESG Rating, FTSE 4 GOOD Emerging Index)、利害關係人溝通過程、內部經營目標等，彙整24個屬於南亞科技的ESG議題。相較於前年，本年度新增「產品品質」議題，以更貼近國際永續發展趨勢及同業關注重點；並將「人權」更名為「人權與勞資關係」。</p>"
content = content.replace(old_p2, new_p2)

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

