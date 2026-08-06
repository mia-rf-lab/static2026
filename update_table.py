import re

with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the table section
start_marker = '<div class="swiper-slide" data-label="2025 Performance">'
end_marker = '</div>\n      </div>\n    </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = """<div class="swiper-slide" data-label="2025 Performance">
                   <h3>2025 Performance</h3>

                     <div class="container">
                       <h4>Greenhouse Gas (GHG) Management</h4>

                       <ul class="unordered">
                           <li>11.2% <sup>Note1</sup> reduction in Scope 1+2 GHG emissions compared to 2020 (Target:12.5%)</li>
                           <li>14.6% increase in Scope 3 GHG emissions per product unit compared to 2020 (Target:13.5%)</li>
                           <li>Reduction rate exceeding 93.6% in process perfluorocarbon (PFCs) emissions (Goal: 93%)</li>
                           <li>0 days of production interruption due to climate change-related disasters (Goal: 0 days)</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Energy Management</h4>

                       <ul class="unordered">
                           <li>Implementation of energy conservation measures that resulted in a cumulative energy savings of 78,773 MWh (2.84x10<sup>8</sup> MJ) from 2017 to 2025. (Goal:75,000 MWh ; 2.7x10<sup>8</sup> MJ)</li>
                           <li>Renewable energy usage of 80,160 MWh (2.89x10<sup>8</sup> MJ) (Goal:78,000 MWh ; 2.81x10<sup>8</sup> MJ)</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Water Management</h4>

                       <ul class="unordered">
                           <li>34% <sup>Note2</sup> reduction in total water consumption per unit of production capacity compared to 2017 (Goal: >35.5%)</li>
                           <li>Production losses due to water restrictions: 0 wafers (Goal: 0 wafers)</li>
                           <li>Average percentage in key water pollution indicators exceeds regulatory standards by 63% (Goal: by 52% or more)</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Waste and Pollution Prevention</h4>

                       <ul class="unordered">
                           <li>Number of environmental regulation violation cases: 0 (Goal: 0 cases)</li>
                           <li>On-site audit and guidance rate for waste treatment vendors: 98.4% (Goal: &ge; 98%)</li>
                           <li>Volatile organic compounds (VOCs) reduction rate >95.4% (Goal: >92%)</li>
                       </ul>

                     </div>
                 </div>
                 <div class="swiper-slide" data-label="2026 Goal">
                   <h3>2026 Goal</h3>

                     <div class="container">
                       <h4>Greenhouse Gas (GHG) Management</h4>

                       <ul class="unordered">
                           <li>15.0% reduction in Scope 1+2 GHG emissions compared to 2020</li>
                           <li>16.2% reduction in Scope 3 GHG emissions per product unit compared to 2020</li>
                           <li>Reduction amount exceeding 93% in process perfluorocarbon (PFC) emissions</li>
                           <li>0 days of production interruption due to climate change-related disasters</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Energy Management</h4>

                       <ul class="unordered">
                           <li>Implementation of energy conservation measures that resulted in a cumulative energy savings of 82,500 MWh (2.97x10<sup>8</sup> MJ) from 2017 to 2026.</li>
                           <li>Renewable energy usage of 90,000 MWh (3.24x10<sup>8</sup> MJ)</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Water Management</h4>

                       <ul class="unordered">
                           <li>>35.5% reduction in total water consumption per unit of production capacity compared to 2017</li>
                           <li>Production losses due to water restrictions: 0 wafers</li>
                           <li>Average percentage in key water pollution indicators exceeds regulatory standards by 55% or more</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Waste and Pollution Prevention</h4>

                       <ul class="unordered">
                           <li>Number of environmental regulation violation cases: 0</li>
                           <li>On-site audit and guidance rate for waste treatment vendors &ge; 98%</li>
                           <li>Volatile organic compounds (VOCs) reduction rate >95%</li>
                       </ul>

                     </div>
                 </div>
                 <div class="swiper-slide" data-label="Strategy">
                   <h3>Strategy</h3>

                     <div class="container">
                       <h4>Greenhouse Gas (GHG) Management</h4>

                       <ul class="unordered">
                           <li>SBT Target: Reduction of Scope 1+2 GHG emissions by 25% by 2030 compared to 2020 baseline; reduction of Scope 3 product unit emissions by 27% by 2030 compared to 2020 baseline.</li>
                           <li>Energy savings and carbon reduction: Setting short-, medium-, and long-term reduction targets and actively implementing relevant management measures.</li>
                           <li>Low-carbon manufacturing: Advancing production technologies to reduce GHG emissions during the manufacturing process.</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Energy Management</h4>

                       <ul class="unordered">
                           <li>Implementation of energy conservation measures: Systematic energy management via ISO 50001 to improve energy efficiency.</li>
                           <li>Innovative applications: Acquiring the latest energy conservation technologies and methods through external collaboration and training.</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Water Management</h4>

                       <ul class="unordered">
                           <li>Risk response: Establishing backup water sources as well as water reservoirs and coordinating water usage via inter-facility emergency response organizations.</li>
                           <li>Wastewater reclamation and reuse: Building categorized treatment systems and implementing multi-stage reuse mechanisms to improve reclamation rates.</li>
                           <li>Water usage reduction: Reducing water usage through daily management.</li>
                       </ul>

                     </div>
                     <div class="container">
                       <h4>Waste and Pollution Prevention</h4>

                       <ul class="unordered">
                           <li>Circular economy: Increasing reuse rate of waste for more efficient resource utilization.</li>
                           <li>Source reduction: Continuously promoting waste reduction and increasing recycling rates.</li>
                           <li>Volatile organic compounds (VOCs): Continuously enhancing prevention equipment.</li>
                       </ul>

                     </div>
                 </div>
             </div>
          </div>
        </div>
        <div class="notes-section" style="background: #f9f9f9; padding: 24px; border-radius: 8px; margin-top: 40px; font-size: 14px; color: #666; line-height: 1.8;">
          <ul style="list-style: none; padding: 0; margin: 0;">
            <li>Note 1: The annual carbon reduction target was not achieved as the 2025 market recovery drove greenhouse gas emissions beyond the levels projected in the original emission reduction plan.</li>
            <li>Note 2: Due to an issue with the MBR membrane in the wastewater treatment system, the volume of reclaimed water was reduced, resulting in water consumption per unit of production capacity not meeting the target.</li>
          </ul>
        </div>"""
    
    updated_content = content[:start_idx] + new_html + "\n" + content[end_idx:]
    with open('en/cleaner_production.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("Table updated successfully.")
else:
    print("Could not find markers.")
