import re

file_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/tw/innovative_technology.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's replace CSS back to transform
css_old = """<style>
.battery-fill, .grid-fill {
    -webkit-clip-path: inset(100% 0 0 0);
    clip-path: inset(100% 0 0 0);
}
.battery-fill.is-animating {
    transition: -webkit-clip-path 3.0s cubic-bezier(0.2, 0.8, 0.2, 1) 0.5s, clip-path 3.0s cubic-bezier(0.2, 0.8, 0.2, 1) 0.5s;
    -webkit-clip-path: inset(0 0 0 0);
    clip-path: inset(0 0 0 0);
}
.grid-fill.is-animating {
    transition: -webkit-clip-path 3.0s steps(var(--steps, 10), end) 0.5s, clip-path 3.0s steps(var(--steps, 10), end) 0.5s;
    -webkit-clip-path: inset(0 0 0 0);
    clip-path: inset(0 0 0 0);
}
</style>"""

css_new = """<style>
.battery-fill, .grid-fill {
    transform: scaleY(0);
}
.battery-fill.is-animating {
    transition: transform 4s cubic-bezier(0.2, 0.8, 0.2, 1) 0.4s;
    transform: scaleY(1);
}
.grid-fill.is-animating {
    transition: transform 1.5s steps(var(--steps, 10), end) 0.4s;
    transform: scaleY(1);
}
</style>"""

# Replace CSS
html = html.replace(css_old, css_new)

# Let's add inline transform-origin style to each element
# DDR (top rows, y = 300px baseline):
# battery-fills: paint0, paint2, paint4
# grid-fills: paint13, paint14, paint15
html = html.replace('fill="url(#paint0_linear_367_47777)" class="battery-fill"', 'fill="url(#paint0_linear_367_47777)" class="battery-fill" style="transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint2_linear_367_47777)" class="battery-fill"', 'fill="url(#paint2_linear_367_47777)" class="battery-fill" style="transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint4_linear_367_47777)" class="battery-fill"', 'fill="url(#paint4_linear_367_47777)" class="battery-fill" style="transform-origin: 0 300px;"')

html = html.replace('fill="url(#paint13_linear_367_47777)" class="grid-fill" style="--steps: 15;"', 'fill="url(#paint13_linear_367_47777)" class="grid-fill" style="--steps: 15; transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint14_linear_367_47777)" class="grid-fill" style="--steps: 18;"', 'fill="url(#paint14_linear_367_47777)" class="grid-fill" style="--steps: 18; transform-origin: 0 300px;"')
html = html.replace('fill="url(#paint15_linear_367_47777)" class="grid-fill" style="--steps: 15;"', 'fill="url(#paint15_linear_367_47777)" class="grid-fill" style="--steps: 15; transform-origin: 0 300px;"')

# LPDDR (bottom rows, y = 661px baseline):
# battery-fills: paint6, paint8, paint10
# grid-fills: paint16, paint17, paint18
html = html.replace('fill="url(#paint6_linear_367_47777)" class="battery-fill"', 'fill="url(#paint6_linear_367_47777)" class="battery-fill" style="transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint8_linear_367_47777)" class="battery-fill"', 'fill="url(#paint8_linear_367_47777)" class="battery-fill" style="transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint10_linear_367_47777)" class="battery-fill"', 'fill="url(#paint10_linear_367_47777)" class="battery-fill" style="transform-origin: 0 661px;"')

html = html.replace('fill="url(#paint16_linear_367_47777)" class="grid-fill" style="--steps: 10;"', 'fill="url(#paint16_linear_367_47777)" class="grid-fill" style="--steps: 10; transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint17_linear_367_47777)" class="grid-fill" style="--steps: 4;"', 'fill="url(#paint17_linear_367_47777)" class="grid-fill" style="--steps: 4; transform-origin: 0 661px;"')
html = html.replace('fill="url(#paint18_linear_367_47777)" class="grid-fill" style="--steps: 15;"', 'fill="url(#paint18_linear_367_47777)" class="grid-fill" style="--steps: 15; transform-origin: 0 661px;"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Styles updated successfully!")
