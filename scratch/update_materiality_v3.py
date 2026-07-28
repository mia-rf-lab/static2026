import os

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # Government Stats
    if '<strong>4</strong>' in line and 'Sustainable recognitions from government' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('4', '5')
    
    if '<strong>11</strong>' in line and 'Corporate visit from government' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('11', '20')

    # Government Topics
    if '<li>Customer Service</li>' in line and '<li>Sustainable Supplier Management</li>' in lines[i+1] and '<li>Employee Development</li>' in lines[i+2]:
        lines[i] = line.replace('Customer Service', 'Energy Management')
        lines[i+1] = lines[i+1].replace('Sustainable Supplier Management', 'Water Management')
        lines[i+2] = lines[i+2].replace('Employee Development', 'Waste and Recycling')
        lines[i+3] = lines[i+3].replace('Occupational Health and Safety', 'Occupational Health and Safety') # unchanged
        lines[i+4] = lines[i+4].replace('Human Rights', 'Corporate Governance')
        lines.insert(i+5, '                              <li>Ethical Management</li>\n')
        lines.insert(i+6, '                              <li>Economic Performance</li>\n')
        lines.insert(i+7, '                              <li>Product Quality</li>\n')
        lines.insert(i+8, '                              <li>Climate Strategy</li>\n')
        lines.insert(i+9, '                              <li>Social Engagement</li>\n')

    # Government Outcomes
    if '<h4>2024 outcome of communication</h4>' in line and 'We continue to disclose annual financial reports' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+5] = '                              <li>We participate in internal communications within the Taiwan Semiconductor Industry Association to jointly deliberate on more reasonable and feasible industry-related environmental regulations.</li>\n'
        lines.insert(i+6, '                              <li>We continue to monitor regulatory trends. In 2025, we participated in 20 government-organized regulatory promotion sessions, briefings, and consultation meetings.</li>\n')

    # Society Stats
    if '<strong>20,545,733</strong>' in line and 'Total investment in social engagement amounted to' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('20,545,733', '8,577,866')

    if '<strong>22</strong>' in line and 'The hours Nanya Technology has spent on social engagement increased' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('22', '11.6')
        
    # Society Topics
    if '<li>Talent Recruitmen</li>' in line and '<li>Climate Strategy</li>' in lines[i+1] and '<li>Green Products</li>' in lines[i+2]:
        lines[i] = line.replace('Talent Recruitmen', 'Ethical Management')
        lines[i+1] = lines[i+1].replace('Climate Strategy', 'Information Security and Privacy')
        lines[i+2] = lines[i+2].replace('Green Products', 'Product Quality')
        lines[i+3] = lines[i+3].replace('Energy Management', 'R&D and Innovation')
        lines[i+4] = lines[i+4].replace('Water Management', 'Climate Strategy')
        lines[i+5] = lines[i+5].replace('Green Factory', 'Green Products')
        lines[i+6] = lines[i+6].replace('Employee Diversity', 'Green Factory')
        lines[i+7] = lines[i+7].replace('Talent Retention and Employee Well-Being', 'Biodiversity')
        lines.insert(i+8, '                              <li>Occupational Health and Safety</li>\n')

    # Society Outcomes
    if '<h4>2024 outcome of communication</h4>' in line and 'Talent cultivation:' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+4] = lines[i+4].replace('1,536 people', '1,387 people').replace('3 sports talents', '5 sports talents').replace('5 national team members', '2 national team members')
        lines[i+5] = lines[i+5].replace('70.5 kg', '155.4 kg').replace('63.6 kg', '76.3 kg')
        lines[i+7] = '                              <li>Humanistic care: Enhancing domestic cultural industries with annual funding of NT$3 million.</li>\n'
        
    # Media Stats
    if '<strong>31</strong>' in line and 'Press releases' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('31', '24')
        
    # Media Topics
    if '<li>R&D and Innovation</li>' in line and '<li>Economic Performance</li>' in lines[i+1] and '<li>Ethical Management</li>' in lines[i+2]:
        lines[i] = line.replace('R&D and Innovation', 'Corporate Governance')
        lines[i+1] = lines[i+1].replace('Economic Performance', 'Ethical Management')
        lines[i+2] = lines[i+2].replace('Ethical Management', 'R&D and Innovation')
        lines[i+3] = lines[i+3].replace('Talent Retention and Employee Well-Being', 'Economic Performance')
        lines[i+4] = lines[i+4].replace('Talent Recruitment', 'Risk Management')
        lines.insert(i+5, '                              <li>Occupational Health and Safety</li>\n')
        lines.insert(i+6, '                              <li>Sustainable Supplier Management</li>\n')
        lines.insert(i+7, '                              <li>Product Quality</li>\n')
        lines.insert(i+8, '                              <li>Energy Management</li>\n')
        lines.insert(i+9, '                              <li>Employee Development</li>\n')
        lines.insert(i+10, '                              <li>Employee Diversity</li>\n')
        
    # Media Outcomes
    if '<h4>2024 outcome of communication</h4>' in line and 'We initiated online and offline meetings to enhance engagement effectiveness' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+5] = '                              <li>We disclosed the Company’s operational status and sustainability-related information in a timely and transparent manner: 24 press releases and 6 ESG news updates.</li>\n'

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
