import sys

with open("tw/materiality_analysis.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find index of "<h4>2024年溝通成效</h4>" under the "媒體" section. 
# We know the 媒體 section is the last one (accordion-7)
idx_media = content.find('data-jq-switcher-target="accordion-7"')

target = """                      <li>
                        <h4>關注主題</h4>


                          <ul class="unordered">
                              <li>氣候策略</li>
                              <li>經濟績效</li>
                              <li>誠信經營</li>
                              <li>研發與創新</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2024年溝通成效</h4>


                          <ul class="unordered">
                              <li>開啟線上、線下會議，透過雙向交流提升議和效益: 4場記者會、1場媒體餐敘</li>
                              <li>即時、透明地揭露公司營運狀況及永續相關訊息: 31篇新聞稿</li>
                          </ul>
                      </li>"""

replacement = """                      <li>
                        <h4>關注主題</h4>


                          <ul class="unordered">
                              <li>研發與創新</li>
                              <li>經濟績效</li>
                              <li>誠信經營</li>
                              <li>人才留任與員工福祉</li>
                              <li>人才招募</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2025年溝通成效</h4>


                          <ul class="unordered">
                              <li>開啟線上、線下會議，透過雙向交流提升議和效益：4場記者會、1場媒體餐敘</li>
                              <li>即時、透明地揭露公司營運狀況及永續相關訊息：24篇新聞稿、6篇ESG最新消息</li>
                          </ul>
                      </li>"""

# We'll just do a straight replace on the second half of the file
idx = content.find(target, idx_media)
if idx != -1:
    new_content = content[:idx] + replacement + content[idx+len(target):]
    with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success")
else:
    print("Target not found. Doing a fallback flexible replace.")
    import re
    # We'll match between <h4>關注主題</h4> and </ul>\n                      </li>\n                  </ul>
    
    # We can match lines 864 to 883
    
    start_str = "<li>\n                        <h4>關注主題</h4>"
    end_str = "31篇新聞稿</li>\n                          </ul>\n                      </li>"
    
    start_idx = content.find(start_str, idx_media)
    end_idx = content.find(end_str, idx_media)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + replacement.strip() + content[end_idx+len(end_str):]
        with open("tw/materiality_analysis.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Success via index range")
    else:
        print("Failed completely")

