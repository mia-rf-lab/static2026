import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Water Resource Management Paragraph 1
old_p1 = "In 2023, the Company adopted the Alliance for Water Stewardship Standard (AWS), and was awarded AWS's highest certification level, Platinum, following its 2023 assessment."
new_p1 = "In 2023, the Company adopted the Alliance for Water Stewardship Standard (AWS) and, following its 2023 assessment, was awarded AWS's highest certification level, Platinum, in 2024."
content = content.replace(old_p1, new_p1)

# Water Resource Management Paragraph 2
old_p2 = 'From 2022 to 2024, we also received the Taiwan Corporate Sustainability Award\'s Water Resource Management Leadership Award for three consecutive years. In 2024, the Company was awarded Platinum-level certification by the Alliance for Water Stewardship Standard, affirming its commitment to tackling climate change and water resource management while contributing to global sustainability goals.'
new_p2 = 'From 2022 to 2024, we also received the Taiwan Corporate Sustainability Award\'s Water Resource Management Leadership Award for three consecutive years, affirming its commitment to tackling climate change and water resource management while contributing to global sustainability goals.'
content = content.replace(old_p2, new_p2)

# Water Resource Risk Management
old_p3 = "reaching 5,590 million liters in 2024. Through internal adaptation capacity and water recycling systems, Nanya Technology can operate for up to 21 days without an external water supply."
new_p3 = "reaching 5,530 million liters in 2025. Through internal adaptation capacity and water recycling systems, Nanya Technology can operate for up to 14 days without an external water supply."
content = content.replace(old_p3, new_p3)

with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections updated.")
