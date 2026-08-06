import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Raw Material Reduction
old_p1 = "Nanya Technology regularly reviews the rationality and appropriateness of raw material usage in production, and simplifies manufacturing processes to reduce material consumption. The Company's designated team sets annual raw material reduction targets and regularly reviews overall performance in raw material reduction. In 2024, a total of 20 proposals for raw material usage improvements were completed via the Kaizen Proposal System, including the development of new processes and formulas as well as reducing process duration to reduce consumption. Among the 2024 improvement proposals, process parameter optimization and volume reduction improved slurry usage efficiency in the CMP area, achieving a maximum annual reduction of 135.4 metric tons in consumption."
new_p1 = "Nanya Technology regularly reviews the rationality and appropriateness of raw material usage in production, and simplifies manufacturing processes to reduce material consumption. The Company's designated team sets annual raw material reduction targets and regularly reviews overall performance in raw material reduction. In 2025, a total of 32 proposals for raw material usage improvements were completed via the Kaizen Proposal System, including the development of new processes and formulas as well as reducing process duration to reduce consumption. Among the improvement projects implemented in 2025, the dry-free suck back (DFS) function was introduced in the PH area. By adjusting the photoresist nozzle cleaning formulation, the cleaning cycle was gradually extended from 1 hour to 24 hours. This effectively improved photoresist utilization efficiency, reducing the consumption of seven types of photoresist by approximately 34 liters per month(~97%), representing the most significant raw material reduction improvement project."
content = content.replace(old_p1, new_p1)

# Waste Reduction Technology
old_p2 = "Nanya Technology invested NT$8.19 million to build an electrolytic regeneration system for copper waste liquids. After resin adsorption and regeneration, the system produces high-concentration copper sulfate waste liquid, which is then electrolyzed to recover copper foil. Through the Copper Together project, the Company collaborated with Ming Chi University of Technology and New Taipei City-based artist Ching-Tai Chuang to turn recycled copper foil into artwork, enhancing engagement with stakeholders. The copper foil is also reused as industrial-grade raw material, achieving the benefits of resource circularity. In 2024, a total of 1,070 kilograms of copper foil was produced."
new_p2 = "Nanya Technology's R&D team invested NT$8.29 million to establish an electrolytic regeneration system for copper waste solution. The system uses resin adsorption followed by regeneration to produce high-concentration copper sulfate solution, which is then electrolyzed to recover copper foil. In addition to eliminating the need for external disposal of copper-containing waste liquid, the recovered copper foil can be further processed into industrial-grade raw materials for reuse, achieving resource circulation. In 2025, a total of 980 kg of copper foil was produced."
content = content.replace(old_p2, new_p2)

with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections updated.")
