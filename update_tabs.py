import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<ul class="split-tabs__content" data-animate="fadeInUp" data-animate-delay=".2">'
# Find the exact string of the start_marker
start_idx = content.find(start_marker)

# Find the end of the ul block. It should be the first </ul> that is a direct child.
# But it's easier to find the exact block ending with the tabs wrapper.
end_marker = '</ul>\n\n        </div>\n\n      </div>'
# Let's search for the end of the section instead.
end_marker = '</section>'
# wait, there's another section.
# The TNCFD Framework section ends with </section>.
# Let's just find the first <div class="wrapper --grid-container__full-width"> after start_idx
end_idx = content.find('</ul>\n        </div>\n\n        <div class="split-tabs js-switch-by-hover aos">', start_idx)
if end_idx == -1:
    end_idx = content.find('</ul>', content.find('cleaner-production-tabs-4', start_idx))
    # It might be </ul> then some divs. We just need to replace the entire ul block.
    # We can match everything from <ul class="split-tabs__content"... to the matching </ul>
    # It's safer to just replace from start_marker to the first <section> or whatever.
    
# Let's do it with regex
match = re.search(r'(<ul class="split-tabs__content".*?</ul>)', content, re.DOTALL)
if match:
    old_ul = match.group(1)
    # now we replace old_ul with new_html
    # wait, there are multiple <ul class="..."> in the document.
    
match = re.search(r'(<ul class="split-tabs__content".*?)(?=\s*</div>\s*</section>)', content, re.DOTALL)
if match:
    pass

# Another way: Just find the index of cleaner-production-tabs-4, then find the NEXT </ul> that closes the split-tabs__content.
t4_idx = content.find('cleaner-production-tabs-4', start_idx)
end_ul_idx = content.find('</ul>\n        </div>\n\n        <!--', t4_idx)
if end_ul_idx == -1:
    end_ul_idx = content.find('</ul>\n        </div>', t4_idx)

new_html = """<ul class="split-tabs__content" data-animate="fadeInUp" data-animate-delay=".2">
              <li
                class="active"
                data-jq-switcher-target="cleaner-production-tabs-1"
                data-jq-switcher-group="cleaner-production-tabs"
              >
                <span>
                  Governance
                </span>

                <div class="tab-content">

                    <div class="tab-content__table">


                        <div class="row">
                          <div class="th">
                            <strong>Management Strategies and Actions</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>At the Board of Directors' governance level, nature and climate are listed as Board of Directors topics, and a Sustainable Development Committee was established to implement relevant management practices.</li>
                                    <li>At the executive level, management participates in quarterly sustainable management and risk management meetings to review performance and resolve action items. A cross-departmental Sustainability and Risk Management Division under the President Office is responsible for coordination.</li>
                                    <li>Efforts are underway to strengthen governance capabilities on nature and climate among the Board of Directors, management, and all employees.</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>2025 Implementation Status</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>In 2025, Nanya Technology convened a total of six Board meetings and two Sustainable Development Committee meetings.</li>
                                    <li>Each year, the Risk Management Steering Center evaluates the identified material nature- and climate-related risks. In 2025, response measures were implemented for 183 risks based on their risk levels, and the risks are continuously monitored.</li>
                                    <li>In 2025, Board members completed 111 hours of training , with courses covering a diverse range of topics such as ESG governance, economics, corporate governance, sustainable finance, carbon pricing mechanisms, climate change, power systems, risk management, and ESG-related laws and regulations.</li>
                                </ul>
                          </div>
                        </div>
                    </div>



                </div>
              </li>
              <li
                
                data-jq-switcher-target="cleaner-production-tabs-2"
                data-jq-switcher-group="cleaner-production-tabs"
              >
                <span>
                  Strategy
                </span>

                <div class="tab-content">

                    <div class="tab-content__table">


                        <div class="row">
                          <div class="th">
                            <strong>Management Strategies and Actions</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>Climate-related risks and opportunities that can reasonably be expected to affect the entity's outlook.</li>
                                    <li>Information on the current and anticipated impacts of climate-related risks and opportunities on the entity's business model and value chain.</li>
                                    <li>Impacts of climate-related risks and opportunities on the entity's current and anticipated financial position, financial performance, and cash flows.</li>
                                    <li>Climate-related scenario analysis and assessment of climate resilience.</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>2025 Implementation Status</strong>
                          </div>

                          <div class="td">
                                <a href="https://www.nanya.com/ESG/en/csr_report" target="_blank" style="color:#00BBDC; text-decoration: none;">Please refer to the chapter titled "Green " for 2025 Sustainability Report.</a>
                          </div>
                        </div>
                    </div>



                </div>
              </li>
              <li
                
                data-jq-switcher-target="cleaner-production-tabs-3"
                data-jq-switcher-group="cleaner-production-tabs"
              >
                <span>
                  Risk Management
                </span>

                <div class="tab-content">

                    <div class="tab-content__table">


                        <div class="row">
                          <div class="th">
                            <strong>Management Strategies and Actions</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>In line with the Company's Risk Management Procedure, we assess the materiality of risks and opportunities arising from various scenarios related to natural factors and climate change. Relevant response plans are formulated, integrated into the Enterprise Risk Management (ERM) framework, and regularly confirmed by senior management. A comprehensive contingency plan was formulated for nature- and climate-related risks.</li>
                                    <li>Imposition of Carbon Fees: Following the Ministry of Environment's 2024 announcement of fee-charging rates of carbon fees, with implementation starting in 2025 and fee imposition beginning in 2026.</li>
                                    <li>GHG emissions for Scopes 1, 2, and 3 are inventoried and verified annually to identify emission sources and prioritize management efforts.</li>
                                    <li>Promoting product life cycle assessments and addressing emission hotspots.</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>2025 Implementation Status</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>Key risks identified are primarily transition risks, including changes in the national energy structure, customer demand for low-carbon products, and the impact of fulfilling SBT commitments. These three mid-term risks are estimated to have a financial impact equivalent to approximately 3-4% of the Company's annual revenue.</li>
                                    <li>In response to the imposition of carbon fees in 2026, a carbon fee rate of NT$300 per tCO2 e was applied, resulting in a payment of NT$132 million, accounting for 0.002% of 2025 operating revenue.</li>
                                    <li>Major opportunities identified include product technology and new market development. As the net-zero trend continues, smart clean energy technologies are expected to drive growth in DRAM demand. According to IEA scenario analysis, the clean technology market is projected to triple by 2030. The Company will seize this opportunity by continuing to invest in innovative R&D resources, which accounted for 10.6% of total revenue in 2025.</li>
                                    <li>Based on the climate change water hazard maps published under the Taiwan Climate Change Projection Information and Adaptation Knowledge Platform (TCCIP), no risk of water shortage is projected under the RCP 8.5 mid-century scenario (2036–2065). Nanya Technology continues to promote water conservation and water recycling measures. Water consumption charges remain at the government's minimum applicable rate, with annual water fee increases limited to approximately 3%, resulting in a low impact on operating costs.</li>
                                    <li>GHG emissions in 2025 will be fully inventoried and verified by May 2026. A 100% product environmental footprint inventory has been completed. Management plan improvements have been launched for the top three carbon footprint hotspots identified in 2025.</li>
                                </ul>
                          </div>
                        </div>
                    </div>



                </div>
              </li>
              <li
                
                data-jq-switcher-target="cleaner-production-tabs-4"
                data-jq-switcher-group="cleaner-production-tabs"
              >
                <span>
                  Indicators and Targets
                </span>

                <div class="tab-content">

                    <div class="tab-content__table">


                        <div class="row">
                          <div class="th">
                            <strong>Management Strategies and Actions</strong>
                          </div>

                          <div class="td">


                                <ul class="unordered">
                                    <li>GHG-related Climate Indicators</li>
                                    <li>Compensation</li>
                                    <li>Basic Indicator Information for the Semiconductor Industry</li>
                                    <li>Disclosure of Targets Related to Climate Related Risks and Opportunities (Climate Related Targets)</li>
                                </ul>
                          </div>
                        </div>


                        <div class="row">
                          <div class="th">
                            <strong>2025 Implementation Status</strong>
                          </div>

                          <div class="td">
                                <p>GHG-related Climate Indicators</p>
                                <ul class="unordered">
                                    <li>GHG emissions of the Company are calculated in accordance with the methodologies specified by the GHG Protocol, and with reference to the emission factors published by the Ministry of Environment. The operational control approach is adopted to account for emissions from joint ventures and associated companies. This approach is selected as it reflects the Company's actual operational control more accurately, and ensures that GHG emissions data comprehensively and consistently represents the Company's operational impact. It also enables users to better understand performance related to climate-related risks and opportunities. The Scope 1, Scope 2, and Scope 3 GHG emissions generated during the reporting period of fiscal year 2025 are presented in "Mitigation – Greenhouse Gas Inventory," of 2025 Sustainability Report.</li>
                                </ul>
                                <p>Compensation</p>
                                <ul class="unordered">
                                    <li>To strengthen senior management's understanding of climate-related risk management, Nanya Technology links executive performance evaluation to climate goals. Through the sustainability assessment of senior executives, the Company regularly tracks the implementation progress of medium- to long-term targets. This performance is incorporated into executive performance evaluation and compensation review to assess the implementation progress of climate strategy targets.</li>
                                </ul>
                                <p>Disclosure of Targets Related to Climate Related Risks and Opportunities (Climate Related Targets)</p>
                                <ul class="unordered">
                                    <li>Nanya Technology has established a strategic target of achieving carbon neutrality by 2050, supported by specific sub-targets and indicators, including reductions in GHG emissions and improvements in energy efficiency. The Sustainable Development Committee and relevant management units hold regular performance review meetings to monitor progress and ensure the gradual achievement of the established strategic target.</li>
                                    <li>Nanya Technology responds to initiatives such as the Carbon Disclosure Project (CDP) and the Task Force on Climate-related Financial Disclosures (TCFD), as well as national policies on the 2050 net-zero emissions pathway. The Company references climate models and mitigation pathways developed by the Intergovernmental Panel on Climate Change (IPCC), and the Net Zero Emissions scenario of the International Energy Agency (IEA). Based on these frameworks, the Company has announced and committed to achieving carbon neutrality by 2050, in order to reduce exposure to climate risks, mitigate future carbon fee expenses, and enhance corporate resilience and sustainability competitiveness.</li>
                                </ul>
                          </div>
                        </div>
                    </div>



                </div>
              </li>
          </ul>"""

if start_idx != -1 and end_ul_idx != -1:
    updated_content = content[:start_idx] + new_html + content[end_ul_idx + 5:]
    with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("Tabs updated successfully.")
else:
    print(f"Could not find markers. start_idx={start_idx}, end_ul_idx={end_ul_idx}")
