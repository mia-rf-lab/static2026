import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Air Pollution Control
old_air = "In 2024, the VOCs emission intensity per unit of production capacity was 12.9 g VOCs/kpcs 4Gb eq."
new_air = "In 2025, the VOCs emission intensity per unit of production capacity was 13.4 g VOCs/kpcs 4Gb eq."
content = content.replace(old_air, new_air)

# Update Strengthened Wastewater Management
old_water = "We have remained committed to water pollution prevention, and continue to upgrade and invest in wastewater treatment facilities. 28 distinct pipelines are used to segregate and convey the different types of wastewater within the facility, In 2024, total wastewater discharge reached 2,864 million liters. Due to non-conforming handling of the membrane bioreactor (MBR) system during wastewater treatment, the volume of water reclaimed decreased, leading to an increase in wastewater discharge. As a result, total wastewater discharge in 2024 rose by 17.1% compared to 2023."
new_water = "We have remained committed to water pollution prevention and continue to upgrade and invest in wastewater treatment facilities. 28 distinct pipelines are used to segregate and convey the different types of wastewaters within the facility, In 2025, total wastewater discharge reached 3,017 million liters. Due to non-conforming handling of the membrane bioreactor (MBR) system during wastewater treatment, the volume of water reclaimed decreased, leading to an increase in wastewater discharge. As a result, total wastewater discharge in 2025 rose by 5.4% compared to 2024."
content = content.replace(old_water, new_water)

with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Pollution sections updated.")
