import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update tab title
content = content.replace("Electricity Consumption from 2020 to 2023", "2022-2025 Electricity Consumption")

# Update Greenhouse Gas Reduction (just in case there are minor differences, but it looked identical)
# Actually, the text for Greenhouse gas reduction was:
# "The Company actively promotes voluntary emission reductions and participates in the annual voluntary GHG reduction program launched by the Industrial Development Administration, Ministry of Economic Affairs. Given the high global warming potential (GWP) of perfluorocarbons (PFCs), we have implemented phased GHG reduction plans since 2006. During facility planning, we procured high-efficiency local scrubbers. Currently, the thin-film and etching areas use burn-type PFC local scrubbers, which use high temperatures from combustion to destroy PFCs. To reduce fugitive PFC emissions, Nanya Technology established local scrubber acceptance criteria for PFC reduction rates: CF4 gas treatment efficiency must exceed 90%, reduction rates of C3F8, C4F6, C4F8, CHF3, CH2F2, and SF6 must exceed 95%, and NF3 reduction must exceed 99%. After installation, all local scrubbers undergo PFC abatement verification using FTIR to align with future reduction trends."
# Image text:
# "The Company actively promotes voluntary emission reductions. During facility planning, we procured high-efficiency local scrubbers. Currently, the thin-film and etching areas use burn-type PFC local scrubbers, which use high temperatures from combustion to destroy PFCs. To reduce fugitive PFCs emissions, Nanya Technology established local scrubber acceptance criteria for PFCs reduction rates: CF4 gas treatment efficiency must exceed 90%, reduction rates of C3 F8 , C4 F6 , C4 F8 , CHF3 , CH2 F2 , and SF6 must exceed 95%, and NF3 reduction must exceed 99%. After installation, all local scrubbers undergo PFC abatement verification using FTIR3 to align with future reduction trends."
# The image removed the first two sentences about "participates in the annual voluntary GHG reduction program..." and "Given the high global warming potential...".
# Also "PFC emissions" became "PFCs emissions", "PFC reduction rates" became "PFCs reduction rates".
# Let's replace the whole paragraph.
old_ghg = "The Company actively promotes voluntary emission reductions and participates in the annual voluntary GHG reduction program launched by the Industrial Development Administration, Ministry of Economic Affairs. Given the high global warming potential (GWP) of perfluorocarbons (PFCs), we have implemented phased GHG reduction plans since 2006. During facility planning, we procured high-efficiency local scrubbers. Currently, the thin-film and etching areas use burn-type PFC local scrubbers, which use high temperatures from combustion to destroy PFCs. To reduce fugitive PFC emissions, Nanya Technology established local scrubber acceptance criteria for PFC reduction rates: CF<sub>4</sub> gas treatment efficiency must exceed 90%, reduction rates of C<sub>3</sub>F<sub>8</sub>, C<sub>4</sub>F<sub>6</sub>, C<sub>4</sub>F<sub>8</sub>, CHF<sub>3</sub>, CH<sub>2</sub>F<sub>2</sub>, and SF<sub>6</sub> must exceed 95%, and NF<sub>3</sub> reduction must exceed 99%. After installation, all local scrubbers undergo PFC abatement verification using FTIR to align with future reduction trends."
new_ghg = "The Company actively promotes voluntary emission reductions. During facility planning, we procured high-efficiency local scrubbers. Currently, the thin-film and etching areas use burn-type PFC local scrubbers, which use high temperatures from combustion to destroy PFCs. To reduce fugitive PFCs emissions, Nanya Technology established local scrubber acceptance criteria for PFCs reduction rates: CF<sub>4</sub> gas treatment efficiency must exceed 90%, reduction rates of C<sub>3</sub>F<sub>8</sub>, C<sub>4</sub>F<sub>6</sub>, C<sub>4</sub>F<sub>8</sub>, CHF<sub>3</sub>, CH<sub>2</sub>F<sub>2</sub>, and SF<sub>6</sub> must exceed 95%, and NF<sub>3</sub> reduction must exceed 99%. After installation, all local scrubbers undergo PFC abatement verification using FTIR3 to align with future reduction trends."
content = content.replace(old_ghg, new_ghg)

with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections updated.")
