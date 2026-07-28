import os
import re

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '''                  <strong>Selection of <em>23</em> ESG Topics</strong>\n\n                  <p>We identified topics relevant to Nanya Technology's operations from both internal and external perspectives. Topic sources include international sustainability regulation standards (GRI Standards, SBSC, SDGs, TCFD, TNFD, SBTi), industry-specific topics (RBA, SASB), sustainability ratings (DJSI, CDP, MSCI ESG Rating, FTSE 4 GOOD Emerging Index), stakeholder communication processes, and internal business goals. A total of 23 ESG topics were consolidated for Nanya Technology.</p>''',
        '''                  <strong>Selection of <em>24</em> ESG Topics</strong>\n\n                  <p>We identified ESG topics relevant to Nanya Technology's operations from both internal and external perspectives. Our sources include international sustainability regulation standards (GRI Standards, ISSB, SDGs, TCFD, TNFD, SBTi, ESRS), industry-specific topics (RBA, SASB), sustainability ratings (DJBIC, CDP, MSCI ESG Rating, FTSE 4 GOOD Emerging Index), stakeholder communication processes, and internal business goals. A total of 24 ESG topics were consolidated for Nanya Technology. Compared to the previous year, Product Quality was added this year to better align with international sustainability trends and the focus of industry peers, while Human Rights was renamed to Human Rights and Labor Relations.</p>'''
    ),
    (
        '''                  <strong><em>3,550</em> Questionnaires on Stakeholders' Concerns about Sustainability</strong>\n\n                  <p>In addition to ongoing engagement with stakeholders through daily operations, before publishing the report, we conducted a questionnaire targeting the seven key stakeholder categories identified. A total of 3,550 responses were collected and broken down as follows: employees (3,476 responses), shareholders/investors (2 responses), customers (24 responses), suppliers (27 responses), government agencies (3 responses), community (13 responses), and media (5 responses). The results were analyzed to identify the top five topics of concern for each stakeholder group.</p>''',
        '''                  <strong><em>3,406</em> Questionnaires on Stakeholders' Concerns about Sustainability</strong>\n\n                  <p>In addition to ongoing engagement with stakeholders through daily operations, before publishing the report, we conducted a questionnaire targeting the seven key stakeholder categories identified. A total of 3,406 responses were collected and broken down as follows: employees (3,342 responses), shareholders/ investors (4 responses), customers (13 responses), suppliers (36 responses), government agencies (3 responses), society (5 responses), and media (3 responses). The results were analyzed to identify the top seven topics of concern for each stakeholder group.</p>'''
    ),
    (
        '''                  <strong><em>26</em> Managers and Employees Consider the Impact of Issues on Operations</strong>\n\n                  <p>In line with the concept of Double Materiality, Nanya Technology followed the principle of Financial Materiality to assess the operational impact level of each ESG topic on operational factors such as revenue growth, customer satisfaction, employee cohesion, cost, and reputation. A total of 26 Company executives and employees evaluate the influence of each ESG topic on the organization's operations, identifying the top five key ESG topics affecting each operational factor.</p>''',
        '''                  <strong><em>23</em> Managers and Employees Consider the Impact of Issues on Operations</strong>\n\n                  <p>In line with the concept of Double Materiality, Nanya Technology followed the principle of Financial Materiality to assess the operational impact level of each ESG topic on operational factors such as revenue growth, customer satisfaction, employee cohesion, cost, and reputation. A total of 23 Company executives and employees evaluate the influence of each ESG topic on the organization's operations, identifying the top seven key ESG topics affecting each operational factor.</p>'''
    ),
    (
        '''                  <strong>Assessment of External Impacts by the Company's <em>28</em> Sustainability Team Members</strong>\n\n                  <p>In terms of Impact Materiality, Nanya Technology adopted both monetary and non-monetary analysis and identify sustainable development impacts related to the external economy, environment, and human rights.</p>\n\n                  <ul class="unordered">\n                      <li>Defining External Sustainable Development Impacts: Nanya Technology adopted methodologies from organizations such as the Value Balancing Alliance (VBA), the Harvard Business School's Impact-Weighted Accounts research project, and the London Benchmarking Group (LBG). Taking into account its own operational context, Nanya Technology systematically identified and defined 20 external sustainable development impacts related to its operations, covering economic, environmental, and human rights dimensions.\n</li>\n                  </ul>''',
        '''                  <strong>Assessment of External Impacts by the Company's <em>24</em> Sustainability Team Members</strong>\n\n                  <p>The Company identifies potential risks and opportunities for 24 ESG topics based on the principle of Financial Materiality. Supervisors and colleagues driving sustainability initiatives are invited to complete questionnaires to quantitatively assess financial impacts—including probability, revenue, costs, and capital expenditures—to identify significant sustainability risks and opportunities.</p>'''
    ),
    (
        '''                  <strong>Corresponding to <em>15</em> Material Topics and <em>8</em> Potential Topics</strong>\n\n                  <p>Based on the calculation and analysis results, we identified topics that are simultaneously of high concern to stakeholders, significantly impact operations, and are highlighted in the external sustainable development questionnaire. We also pinpointed topics that are relevant to both operational impact and external sustainable development impact.<br> Nanya Technology referred to the long-term goals set for the 16 material topics identified in the previous year and compared them with the results of this year's questionnaire. This comparison served as one of the key criteria for determining the material topics for 2024.</p>''',
        '''                  <strong>Corresponding to <em>15</em> Material Topics and <em>9</em> Potential ESG Topics</strong>\n\n                  <p>Nanya Technology referred to the long-term goals set for the material issues identified in the previous year and compared them with the results of this year's questionnaire. This comparison served as one of the key criteria determining the material issues for 2025.</p>'''
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
