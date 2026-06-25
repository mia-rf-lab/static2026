import re

svg_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/chart__commitment-to-sdgs__env-impact__single-column-v.svg'
html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'

with open(svg_path, 'r', encoding='utf-8') as f:
    svg_lines = f.readlines()

left_paints = ["paint0_linear", "paint2_linear", "paint4_linear", "paint6_linear", "paint8_linear", "paint10_linear"]
right_paints = ["paint12_linear", "paint13_linear", "paint14_linear", "paint15_linear", "paint16_linear", "paint17_linear"]

new_svg_lines = []
for line in svg_lines:
    is_left = any(f'url(#{p}_' in line for p in left_paints)
    if is_left:
        line = line.replace('/>', ' class="battery-fill"/>')
    
    for p in right_paints:
        if f'url(#{p}_' in line:
            steps = 15
            match = re.search(r'height="(\d+)"', line)
            if match:
                steps = max(1, round(int(match.group(1)) / 10))
            if 'paint14' in line:
                steps = 18
            line = line.replace('/>', f' class="grid-fill" style="--steps: {steps};"/>')
            break
            
    new_svg_lines.append(line)

svg_str = "".join(new_svg_lines).strip()

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

img_tag = '<img src="../img/svg/chart__commitment-to-sdgs__env-impact__single-column-v.svg" alt="南亞科技產品規劃與規格演進">'

injection = f"""{svg_str}
<style>
.battery-fill, .grid-fill {{
    transform-origin: bottom;
    transform-box: fill-box;
    transform: scaleY(0);
}}
.battery-fill.is-animating {{
    transition: transform 1.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    transform: scaleY(1);
}}
.grid-fill.is-animating {{
    transition: transform 1.5s steps(var(--steps, 10), end);
    transform: scaleY(1);
}}
</style>
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const chartContainer = document.querySelector('.single-column-v');
    if (chartContainer) {{
        const svgs = chartContainer.querySelectorAll('svg');
        if (svgs.length > 0) {{
            const targetSvg = svgs[svgs.length - 1]; // Our injected SVG
            const observer = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        const fills = targetSvg.querySelectorAll('.battery-fill, .grid-fill');
                        fills.forEach(fill => fill.classList.add('is-animating'));
                        observer.unobserve(targetSvg);
                    }}
                }});
            }}, {{ threshold: 0.3 }});
            observer.observe(targetSvg);
        }}
    }}
}});
</script>"""

new_html = html_content.replace(img_tag, injection)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Updated successfully")
