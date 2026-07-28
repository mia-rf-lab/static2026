import os

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/en/materiality_analysis.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'The relevant content in 2024 is as follows' in line:
        lines[i] = line.replace('2024 is as follows', '2025 is as follows')
        
    if '<strong>40</strong>' in line and 'Numbers of semiconductor youth talents increase' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('40', '31')

    if '<strong>81.48</strong>' in line and 'Return-to-work rate after parental leave' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('81.48', '86.36')
        
    if '<li>Human Rights</li>' in line and 'Talent Retention and Employee Well-Being' in lines[i-1]:
        lines[i] = line.replace('Human Rights', 'Human Rights and Labor Relations')
        lines[i+1] = lines[i+1].replace('Occupational Health and Safety', 'Economic Performance')
        lines[i+2] = lines[i+2].replace('R&D and Innovation', 'Employee Development')
        lines[i+3] = lines[i+3].replace('Economic Performance', 'Occupational Health and Safety')
        lines.insert(i+4, '                              <li>R&D and Innovation</li>\n')
        lines.insert(i+5, '                              <li>Product Quality</li>\n')
        lines.insert(i+6, '                              <li>Social Engagement</li>\n')

    if '<h4>2024 outcome of communication</h4>' in line and 'In 2024, 2 all-hands meetings were held' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+4] = lines[i+4].replace('In 2024', 'In 2025')
        lines[i+8] = lines[i+8].replace('A total of 4 in-person communication meetings', 'A total of 1 in-person communication meetings')
        lines.insert(i+9, '                              <li>A total of 1 in-person labor management communication meeting was held, complemented by a variety of communication channels.</li>\n')
        
    if 'This enables us to enhance the value of investors\' investments.' in line:
        lines[i] = line.replace('This enables us to enhance the value', 'This enables us to DJSIenhance the value')
        
    if '<li>Corporate Governance</li>' in line and '<li>Ethical Management</li>' in lines[i+1] and '<li>Economic Performance</li>' in lines[i+2] and '<li>R&D and Innovation</li>' in lines[i+3]:
        lines[i] = line.replace('Corporate Governance', 'Employee Development')
        lines[i+1] = lines[i+1].replace('Ethical Management', 'Talent Retention and Employee Well-Being')
        lines[i+2] = lines[i+2].replace('Economic Performance', 'Climate strategy')
        lines[i+3] = lines[i+3].replace('R&D and Innovation', 'Green Products')
        lines[i+4] = lines[i+4].replace('Risk Management', 'Corporate Governance')
        lines.insert(i+5, '                              <li>Sustainable Supplier Management</li>\n')
        lines.insert(i+6, '                              <li>Employee Diversity</li>\n')
        lines.insert(i+7, '                              <li>Human Rights and Labor Relations</li>\n')
        
    if '<h4>2024 outcome of communication</h4>' in line and 'We responded to sustainable development issues of concern to shareholders' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+4] = '                              <li>We shared information about our operational status, technological development progress, and market dynamics: 4 corporate investor conferences, 17 domestic and international institutional investor forums, and 106 institutional investor meetings.</li>\n'
        lines[i+5] = '                              <li>We actively participated in domestic and international benchmark evaluations, quantifying ESG results: We maintained our standing as a constituent of the DJSI World Index for consecutive years, while garnering a ranking within the top 6%-20% in the 12th Corporate Governance Evaluation.</li>\n'
        lines[i+6] = ''

    if '<h3>Customer</h3>' in line and 'icon__materiality-analysis__section--accordion__client.svg' in lines[i-1]:
        lines[i] = line.replace('Customer', 'Clients')
        
    if '<strong>1,032</strong>' in line and 'Completed customer platform parameter measurement services' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('1,032', '1,142')

    if '<strong>92</strong>' in line and 'Customer technical exchange and courses' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('92', '114')
        
    if '<li>Customer Service</li>' in line and '<li>R&D and Innovation</li>' in lines[i+1] and '<li>Ethical Management</li>' in lines[i+2]:
        lines[i] = line.replace('Customer Service', 'Ethical Management')
        lines[i+1] = lines[i+1].replace('R&D and Innovation', 'R&D and Innovation') # Unchanged
        lines[i+2] = lines[i+2].replace('Ethical Management', 'Sustainable Supplier Management')
        lines[i+3] = lines[i+3].replace('Information Security and Privacy', 'Product Quality')
        lines[i+4] = lines[i+4].replace('Risk Management', 'Corporate Governance')
        lines.insert(i+5, '                              <li>Risk Management</li>\n')
        lines.insert(i+6, '                              <li>Customer Service</li>\n')
        lines.insert(i+7, '                              <li>Economic Performance</li>\n')
        lines.insert(i+8, '                              <li>Information Security and Privacy</li>\n')
        
    if '<h4>2024 outcome of communication</h4>' in line and 'Whenever customers need technical support' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+7] = lines[i+7].replace('A total of 96 sessions were completed.', 'A total of 114 sessions were completed.')
        lines[i+8] = lines[i+8].replace('1,032 customer platform', '1,142 customer platform').replace('27 customer product', '28 customer product')
        # We need to re-order: The original order was:
        # 1. Whenever customers...
        # 2. To facilitate...
        # 3. We completed a customer satisfaction survey...
        # 4. We conducted technical sharing...
        # 5. We completed 1,032...
        
        # We need to swap 3 and 4!
        # wait, let me do this manually by just replacing the lines.
        lines[i+4] = '                              <li>Whenever customers need technical support, we assess their needs and provide assistance in resolving technical issues through in-person visits, phone calls, emails, or text messages.</li>\n'
        lines[i+5] = '                              <li>To facilitate subsequent production and sales planning, we visited customers to assess their needs and understand market conditions.</li>\n'
        lines[i+6] = '                              <li>We conducted technical sharing sessions and provided training for our customers\' technical and engineering personnel. A total of 114 sessions were completed.</li>\n'
        lines[i+7] = '                              <li>We completed a customer satisfaction survey with 100% coverage, and achieved a satisfaction score of 95.7.</li>\n'
        lines[i+8] = '                              <li>We completed 1,142 customer platform parameter measurement services and 28 customer product joint qualification services, helping customers identify potential problems early, shorten verification time, and accelerate product launches.</li>\n'
        
    if '<strong>255</strong>' in line and 'RMI-approved smelters identified in supply chain survey' in "".join(lines[max(0, i-10):i]):
        lines[i] = line.replace('255', '211')
        
    if '<li>Sustainable Supplier Management</li>' in line and '<li>Ethical Management</li>' in lines[i+1] and '<li>Climate Strategy</li>' in lines[i+2]:
        # lines[i] is unchanged
        # lines[i+1] is unchanged
        lines[i+2] = lines[i+2].replace('Climate Strategy', 'R&D and Innovation')
        lines[i+3] = lines[i+3].replace('Occupational Health and Safety', 'Corporate Governance')
        lines[i+4] = lines[i+4].replace('Information Security and Privacy', 'Economic Performance')
        lines.insert(i+5, '                              <li>Information Security and Privacy</li>\n')
        lines.insert(i+6, '                              <li>Risk Management</li>\n')
        lines.insert(i+7, '                              <li>Energy Management</li>\n')

    if '<h4>2024 outcome of communication</h4>' in line and 'Regular and ad-hoc review meetings' in lines[i+4]:
        lines[i] = line.replace('2024 outcome of communication', '2025 Outcome of Communication')
        lines[i+5] = lines[i+5].replace('In 2024, we had 85 critical material suppliers and 210 non-critical material suppliers, with a total of 295 SAQ responses distributed', '80 critical material suppliers, 205 non-critical material suppliers, with a total of 285 SAQ responses distributed')
        lines[i+6] = lines[i+6].replace('19 high-risk suppliers', '20 high-risk suppliers')

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
