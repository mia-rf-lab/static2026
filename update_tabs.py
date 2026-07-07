import re

html_file = "tw/common_good.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Tab 1: 人才培育
tab1_new = """                              <ul class="unordered">
                                    <li>教育地球公民永續概念</li>
                                    <li>培養青年解決問題的設計思維</li>
                                    <li>扶植技術人才，以解決半導體人才供應穩定</li>
                                    <li>培育專才</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>商業效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>主管擔任業師 (主管參與4位)</li>
                                    <li>網路曝光 (臉書平台1篇)</li>
                                    <li>支持專業技能運動員 (7名)</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>社會效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>推廣永續教育至學生數為1,387人</li>
                                    <li>贊助運動員經費 ($174,000元)</li>
                                </ul>"""

# Tab 2: 環境保育
tab2_new = """                              <ul class="unordered">
                                    <li>提升民眾的環境知識與素養，建立環境守護之觀念與永續意識</li>
                                    <li>從小地方開始，清潔整理還給大眾一個乾淨的環境</li>
                                    <li>守護生物多樣性，防止棲地劣化與外來種入侵，造成生物多樣性的消失</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>商業效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>員工向心力 (598員工參與人次)</li>
                                    <li>網路曝光率 (社群媒體互動數2,946)</li>
                                    <li>環保倡議 (參與2個環保倡議活動)</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>社會效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>環境生態多樣性 (移除小花蔓澤蘭155.4公斤)</li>
                                    <li>海洋友善 (移除海洋廢棄物76.3公斤)</li>
                                </ul>"""

# Tab 3: 人文關懷
tab3_new = """                              <ul class="unordered">
                                    <li>以人為本提升全民人文素養及寬廣視野</li>
                                    <li>支持地方文化藝術發展</li>
                                    <li>協助在地文史團體深耕家鄉</li>
                                    <li>給予弱勢關懷，提供平台讓各種團體推廣理念</li>
                                    <li>宣導責任消費理念，發展共生、共好生活</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>商業效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>員工向心力 (454員工參與人次)</li>
                                    <li>愛心公益 (感謝狀3張)</li>
                                    <li>小農推廣 (8家)</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>社會效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>責任消費 (義賣及小農市集消費共計約$312,924元商品)</li>
                                    <li>創造友善就業與銷售機會 (資助16個單位)</li>
                                    <li>繁榮社區環境 (採購288公斤公平貿易咖啡)</li>
                                    <li>推廣責任消費 (5間學校)</li>
                                </ul>"""

# Tab 4: 敦親睦鄰
tab4_new = """                              <ul class="unordered">
                                    <li>關注在地福祉，結合鄰里服務，推廣鄰里美好，落實社福工作</li>
                                    <li>結合社會資源，推動地方永續經營</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>商業效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>鄰里關係強化 (感謝狀1張)</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>社會效益</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>深化社區溝通 (協助改善道路設施，造福周遭鄰里共有16,433人受惠)</li>
                                </ul>"""

import re
def replace_tab(content, tab_id, new_html):
    # Find the target block using data-jq-switcher-target
    pattern = r'(data-jq-switcher-target="common-good-tabs-alpha-' + tab_id + r'".*?<div class="td">\s*)(<ul class="unordered">.*?</ul\s*>)(.*?)'
    
    # Actually, the simplest way is to match from `<div class="td">` after "解決的社會問題" to the end of "社會效益" list.
    
    # Let's find the start of the tab content:
    start_str = f'data-jq-switcher-target="common-good-tabs-alpha-{tab_id}"'
    start_pos = content.find(start_str)
    
    if start_pos == -1:
        print(f"Tab {tab_id} not found!")
        return content
        
    first_td_pos = content.find('<ul class="unordered">', start_pos)
    
    # Find the end of "社會效益" section (the third </ul> in this tab content)
    end_pos = first_td_pos
    for _ in range(3):
        end_pos = content.find('</ul>', end_pos) + 5
        
    if tab_id == '3':
        # tab 3 might have more or fewer lists, let's just find the 3rd row's ul end
        pass
    
    return content[:first_td_pos] + new_html + content[end_pos:]

content = replace_tab(content, '1', tab1_new)
content = replace_tab(content, '2', tab2_new)
content = replace_tab(content, '3', tab3_new)
content = replace_tab(content, '4', tab4_new)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Tabs updated successfully!")
