import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Greenhouse Gas Inventory text
content = content.replace("The Company conducts its GHG inventory with reference to ISO 14064-1, Ministry of Environment's Climate Change Response Act, Regulations for the Management of the Inventory, Registration, and Verification of Greenhouse Gas Emissions, Greenhouse Gas Emissions Inventory Guidelines, and the WBCSD/WRI GHG Protocol. Organizational boundaries are defined using the 100% operational control approach. At present, all Scope 1, Scope 2, and Scope 3 GHG emissions are verified by SGS, a third-party certification institution, in accordance with international standards.",
"The Company conducts its GHG inventory with reference to ISO 14064 1, Ministry of Environment's Climate Change Response Act, Regulations for the Management of the Inventory, Registration, and Verification of Greenhouse Gas Emissions, Greenhouse Gas Emissions Inventory Guidelines, and the WBCSD/WRI GHG Protocol. Organizational boundaries are defined using the 100% operational control approach.")

# 2. Update 2024 to 2025 in GHG emissions
content = content.replace("GHG emissions in 2024 totaled 409,138 metric tons CO<sub>2</sub>e ,the main sources of emissions were purchased electricity.",
"GHG emissions in 2025 totaled 417,308 metric tons CO2e ,the main sources of emissions were purchased electricity.")
content = content.replace("<strong>GHG emissions in 2024</strong>", "<strong>GHG emissions in 2025</strong>")

# 3. Update Scope 3 GHG emissions categories in 2024 to 2025
content = content.replace("<strong>Scope 3 GHG emissions categories in 2024</strong>", "<strong>Scope 3 GHG emissions categories in 2025</strong>")

# 4. Update Percentages of 2024 Scope 1 and Scope 2 Emissions by Category -> Percentages of 2025 Emissions by Category
content = content.replace("Percentages of 2024 Scope 1 and Scope 2 Emissions by Category", "Percentages of 2025 Emissions by Category")

with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections updated.")
