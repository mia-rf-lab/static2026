import os

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '''          <p data-animate="fadeInUp" data-animate-delay="">Nanya conducts materiality analysis annually, and the results of the analysis allow us to understand the sustainability topics concerning our stakeholders. The organization responsible for sustainable development reports the stakeholder communication to the Board of Directors once a year. The relevant content in 2024 is as follows:</p>''',
        '''          <p data-animate="fadeInUp" data-animate-delay="">Nanya conducts materiality analysis annually, and the results of the analysis allow us to understand the sustainability topics concerning our stakeholders. The organization responsible for sustainable development reports the stakeholder communication to the Board of Directors once a year. The relevant content in 2025 is as follows:</p>'''
    ),
    (
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Numbers of semiconductor youth talents increase</b>

                        <span class="num">

                          <strong>40</strong>
                          <small>%</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>Return-to-work rate after parental leave</b>

                        <span class="num">

                          <strong>81.48</strong>
                          <small>%</small>
                        </span>
                      </div>
                  </li>''',
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Numbers of semiconductor youth talents increase</b>

                        <span class="num">

                          <strong>31</strong>
                          <small>%</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>Return-to-work rate after parental leave</b>

                        <span class="num">

                          <strong>86.36</strong>
                          <small>%</small>
                        </span>
                      </div>
                  </li>'''
    ),
    (
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Talent Retention and Employee Well-Being</li>
                              <li>Human Rights</li>
                              <li>Occupational Health and Safety</li>
                              <li>R&D and Innovation</li>
                              <li>Economic Performance</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2024 outcome of communication</h4>


                          <ul class="unordered">
                              <li>In 2024, 2 all-hands meetings were held in a hybrid format (in-person and video conference)</li>
                              <li>4 executive meetings were held.</li>
                              <li>A total of 4 production line operator meetings were held.</li>
                              <li>A total of 4 issues of the Nanya Technology newsletter were published.</li>
                              <li>A total of 4 in-person communication meetings with labor union representatives were held, complemented by a variety of communication channels.</li>
                          </ul>
                      </li>''',
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Talent Retention and Employee Well-Being</li>
                              <li>Human Rights and Labor Relations</li>
                              <li>Economic Performance</li>
                              <li>Employee Development</li>
                              <li>Occupational Health and Safety</li>
                              <li>R&D and Innovation</li>
                              <li>Product Quality</li>
                              <li>Social Engagement</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2025 Outcome of Communication</h4>


                          <ul class="unordered">
                              <li>In 2025, 2 all-hands meetings were held in a hybrid format (in-person and video conference)</li>
                              <li>4 executive meetings were held.</li>
                              <li>A total of 4 production line operator meetings were held.</li>
                              <li>A total of 4 issues of the Nanya Technology newsletter were published.</li>
                              <li>A total of 1 in-person communication meetings with labor union representatives were held, complemented by a variety of communication channels.</li>
                              <li>A total of 1 in-person labor management communication meeting was held, complemented by a variety of communication channels.</li>
                          </ul>
                      </li>'''
    ),
    (
        '''                  <li class="desc">
                    <p>The Company has set up a dedicated investor relations unit to provide transparent information on corporate operations, management strategies, and financial policies to our investors. This enables us to enhance the value of investors' investments.</p>
                  </li>''',
        '''                  <li class="desc">
                    <p>The Company has set up a dedicated investor relations unit to provide transparent information on corporate operations, management strategies, and financial policies to our investors. This enables us to DJSIenhance the value of investors' investments.</p>
                  </li>'''
    ),
    (
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Corporate Governance</li>
                              <li>Ethical Management</li>
                              <li>Economic Performance</li>
                              <li>R&D and Innovation</li>
                              <li>Risk Management</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2024 outcome of communication</h4>


                          <ul class="unordered">
                              <li>We responded to sustainable development issues of concern to shareholders and ensured their rights, including: the presence of sound corporate governance mechanisms, a diverse board of directors, ethical management, the Company's achievements in technological innovation and more.</li>
                              <li>We actively participated in domestic and international benchmark evaluations, quantifying ESG results: We received an MSCI ESG rating of AA, achieved consecutive inclusion in the DJSI World Index, and was ranked in the top 5% of the Corporate Governance Evaluation for the seventh time.</li>
                              <li>We shared information about our operational status, technological development progress, and market dynamics: 4 corporate investor conferences, 13 domestic and international institutional investor forums, and 60 institutional investor meetings.</li>
                          </ul>
                      </li>''',
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Employee Development</li>
                              <li>Talent Retention and Employee Well-Being</li>
                              <li>Climate strategy</li>
                              <li>Green Products</li>
                              <li>Corporate Governance</li>
                              <li>Sustainable Supplier Management</li>
                              <li>Employee Diversity</li>
                              <li>Human Rights and Labor Relations</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2025 Outcome of Communication</h4>


                          <ul class="unordered">
                              <li>We shared information about our operational status, technological development progress, and market dynamics: 4 corporate investor conferences, 17 domestic and international institutional investor forums, and 106 institutional investor meetings.</li>
                              <li>We actively participated in domestic and international benchmark evaluations, quantifying ESG results: We maintained our standing as a constituent of the DJSI World Index for consecutive years, while garnering a ranking within the top 6%-20% in the 12th Corporate Governance Evaluation.</li>
                          </ul>
                      </li>'''
    ),
    (
        '''                <img src="../img/svg/icon__materiality-analysis__section--accordion__client.svg" alt="">
                <h3>Customer</h3>
              </div>''',
        '''                <img src="../img/svg/icon__materiality-analysis__section--accordion__client.svg" alt="">
                <h3>Clients</h3>
              </div>'''
    ),
    (
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Completed customer platform parameter measurement services</b>

                        <span class="num">

                          <strong>1,032</strong>
                          <small>Cases</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>Customer technical exchange and courses</b>

                        <span class="num">

                          <strong>92</strong>
                          <small>Sessions</small>
                        </span>
                      </div>
                  </li>''',
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Completed customer platform parameter measurement services</b>

                        <span class="num">

                          <strong>1,142</strong>
                          <small>Cases</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>Customer technical exchange and courses</b>

                        <span class="num">

                          <strong>114</strong>
                          <small>Sessions</small>
                        </span>
                      </div>
                  </li>'''
    ),
    (
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Customer Service</li>
                              <li>R&D and Innovation</li>
                              <li>Ethical Management</li>
                              <li>Information Security and Privacy</li>
                              <li>Risk Management</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2024 outcome of communication</h4>


                          <ul class="unordered">
                              <li>Whenever customers need technical support, we assess their needs and provide assistance in resolving technical issues through in-person visits, phone calls, emails, or text messages.</li>
                              <li>To facilitate subsequent production and sales planning, we visited customers to assess their needs and understand market conditions.</li>
                              <li>We completed a customer satisfaction survey with 100% coverage, and achieved a satisfaction score of 95.7.</li>
                              <li>We conducted technical sharing sessions and provided training for our customers' technical and engineering personnel. A total of 96 sessions were completed.</li>
                              <li>We completed 1,032 customer platform parameter measurement services and 27 customer product joint qualification services, helping customers identify potential problems early, shorten verification time, and accelerate product launches.</li>
                          </ul>
                      </li>''',
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Ethical Management</li>
                              <li>R&D and Innovation</li>
                              <li>Sustainable Supplier Management</li>
                              <li>Product Quality</li>
                              <li>Corporate Governance</li>
                              <li>Risk Management</li>
                              <li>Customer Service</li>
                              <li>Economic Performance</li>
                              <li>Information Security and Privacy</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2025 Outcome of Communication</h4>


                          <ul class="unordered">
                              <li>Whenever customers need technical support, we assess their needs and provide assistance in resolving technical issues through in-person visits, phone calls, emails, or text messages.</li>
                              <li>To facilitate subsequent production and sales planning, we visited customers to assess their needs and understand market conditions.</li>
                              <li>We conducted technical sharing sessions and provided training for our customers' technical and engineering personnel. A total of 114 sessions were completed.</li>
                              <li>We completed a customer satisfaction survey with 100% coverage, and achieved a satisfaction score of 95.7.</li>
                              <li>We completed 1,142 customer platform parameter measurement services and 28 customer product joint qualification services, helping customers identify potential problems early, shorten verification time, and accelerate product launches.</li>
                          </ul>
                      </li>'''
    ),
    (
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Completion of SAQ by significant suppliers</b>

                        <span class="num">

                          <strong>100</strong>
                          <small>%</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>RMI-approved smelters identified in supply chain survey</b>

                        <span class="num">

                          <strong>255</strong>
                          <small>Smelters</small>
                        </span>
                      </div>
                  </li>''',
        '''                  <li class="anime-num-container">
                      <div class="anime-num">
                        <b>Completion of SAQ by significant suppliers</b>

                        <span class="num">

                          <strong>100</strong>
                          <small>%</small>
                        </span>
                      </div>
                      <div class="anime-num">
                        <b>RMI-approved smelters identified in supply chain survey</b>

                        <span class="num">

                          <strong>211</strong>
                          <small>Smelters</small>
                        </span>
                      </div>
                  </li>'''
    ),
    (
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Sustainable Supplier Management</li>
                              <li>Ethical Management</li>
                              <li>Climate Strategy</li>
                              <li>Occupational Health and Safety</li>
                              <li>Information Security and Privacy</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2024 outcome of communication</h4>


                          <ul class="unordered">
                              <li>Regular and ad-hoc review meetings were held each month to address delivery, inventory management, and cost-related matters.</li>
                              <li>In 2024, we had 85 critical material suppliers and 210 non-critical material suppliers, with a total of 295 SAQ responses distributed, achieving a 100% response rate.</li>
                              <li>We audited 19 high-risk suppliers, and the improvement rate reached 100%.</li>
                          </ul>
                      </li>''',
        '''                      <li>
                        <h4>Topic of concern</h4>


                          <ul class="unordered">
                              <li>Sustainable Supplier Management</li>
                              <li>Ethical Management</li>
                              <li>R&D and Innovation</li>
                              <li>Corporate Governance</li>
                              <li>Economic Performance</li>
                              <li>Information Security and Privacy</li>
                              <li>Risk Management</li>
                              <li>Energy Management</li>
                          </ul>
                      </li>
                      <li>
                        <h4>2025 Outcome of Communication</h4>


                          <ul class="unordered">
                              <li>Regular and ad-hoc review meetings were held each month to address delivery, inventory management, and cost-related matters.</li>
                              <li>80 critical material suppliers, 205 non-critical material suppliers, with a total of 285 SAQ responses distributed, achieving a 100% response rate.</li>
                              <li>We audited 20 high-risk suppliers, and the improvement rate reached 100%.</li>
                          </ul>
                      </li>'''
    )
]

modified = False
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        modified = True
    else:
        print(f"Warning: Could not find block to replace:\n{old[:100]}...\n")

if modified:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated the file.")
else:
    print("No modifications were made.")
