import sys

with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# Block 1
old_h1 = "確認 <em>15</em> 個重大議題，其餘 <em>8</em> 個潛在ESG議題"
new_h1 = "確認 <em>15</em> 個重大議題，其餘 <em>9</em> 個潛在ESG議題"
content = content.replace(old_h1, new_h1)

old_p1 = "<p>根據計算與分析的結果，鑑別出利害關係人關注、對營運具有衝擊、對外部永續發展問卷中同時被利害關係人關注，且對營運衝擊與外部永續衝擊具有影響之主題。南亞科技參考前年度16個重大主題，所設定的長期目標，與今年度問卷調查的結果進行比較，作為判斷2024年重大主題的判斷原則之一。</p>"
new_p1 = "<p>根據計算與分析的結果，鑑別出利害關係人關注、對營運具有衝擊、公司顯著之永續風險與機會、對外部永續發展問卷中具有影響之議題。南亞科技參考前年度16個重大主題，所設定的長期目標，與今年度問卷調查的結果進行比較，作為判斷2025年重大主題的判斷原則之一。除考慮四份問卷結果與長期目標外，南亞科技將重大議題與高階主管永續發展評核的薪酬連結，作為定義重大議題的參考來源之一。</p>"
content = content.replace(old_p1, new_p1)

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

