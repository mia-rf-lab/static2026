with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

slide1 = """                <div class="swiper-slide">
                  <strong>2022-至今</strong>

                  <div class="container">
                    <h3>SEMI台灣永續製造委員會</h3>

                      <ul class="unordered">
                          <li>迎接半導體產業的永續挑戰</li>
                          <li>向半導體產業各相關行業先進學習各種永續作為</li>
                          <li>在半導體生產製造過程中發起協作計畫</li>
                          <li>與產業供應鏈共同推動節能減碳與各種永續活動</li>
                      </ul>
                  </div>
                </div>"""

slide2 = """                <div class="swiper-slide">
                  <strong>2022-至今</strong>

                  <div class="container">
                    <h3>SEMI氣候聯盟倡議</h3>

                      <ul class="unordered">
                          <li>協作: 透過共同方法、技術創新並保持密切溝通，持續減少溫室氣體排放</li>
                          <li>透明度: 每年發佈三大碳排放範圍相關之年度進度報告</li>
                          <li>雄心壯志: 設定近期及長期減碳目標，於2050年達成淨零碳排</li>
                      </ul>
                  </div>
                </div>"""

# Replace in content by finding the combined block
target = slide1 + "\n" + slide2
replacement = slide2 + "\n" + slide1

if target in content:
    content = content.replace(target, replacement)
    with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Swapped successfully.")
else:
    print("Target not found. Let me try with different whitespace.")
    
    # Try finding them individually and swapping
    idx1 = content.find(slide1.strip())
    idx2 = content.find(slide2.strip())
    
    print(f"idx1: {idx1}, idx2: {idx2}")
