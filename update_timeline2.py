with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace TCFD text
old_tcfd = "南亞科技積極落實企業永續發展，於2018年起就導入氣候變遷風險治理架構，並於2021年4月正式簽署支持由G20成立之國際金融穩定委員會（FSB）所發布的「氣候相關財務揭露建議」（TCFD），2021年發行南亞科第一本TCFD報告書，2022年發行第二本。於2023年開始導入TNFD揭露指引並整合TCFD架構，出版「氣候暨自然財務相關報告書」。2024年持續發行TNFD&TCFD報告書。"
new_tcfd = "南亞科技積極落實企業永續發展，於2018年起就導入氣候變遷風險治理架構，並於2021年4月正式簽署支持由G20成立之國際金融穩定委員會（FSB）所發布的「氣候相關財務揭露建議」（TCFD），2021年發行南亞科第一本TCFD報告書。於2023年開始導入TNFD揭露指引並整合TCFD架構，出版「氣候暨自然財務相關報告書」。2025年發行自然暨氣候報告。"
if old_tcfd in content:
    content = content.replace(old_tcfd, new_tcfd)
else:
    print("TCFD not found")

# Replace CDP text
old_cdp = "<li>2022-2023 年連續二年水安全為領導級「A」2024年水安全「A-」</li>"
new_cdp = "<li>2025年氣候變遷、水安全、供應鏈議合領導者「A List」</li>"
if old_cdp in content:
    content = content.replace(old_cdp, new_cdp)
else:
    print("CDP not found")

with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
