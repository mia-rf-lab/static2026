import re

path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix grey blocks
html = html.replace('V211H701V125Z" fill="#E7E7E7"', 'V300H701V125Z" fill="#E7E7E7"')
html = html.replace('V271H580V125Z" fill="#E7E7E7"', 'V300H580V125Z" fill="#E7E7E7"')

new_grey_block = '<path d="M822 125C822 122.791 823.791 121 826 121H874C876.209 121 878 122.791 878 125V300H822V125Z" fill="#E7E7E7"/>\n          '
html = html.replace('<path d="M822 125C822 122.791 823.791 121 826 121H874C876.209 121 878 122.791 878 125V300H822V125Z" fill="url(#paint14_linear_223_30409)" class="grid-fill"', 
                    new_grey_block + '<path d="M822 125C822 122.791 823.791 121 826 121H874C876.209 121 878 122.791 878 125V300H822V125Z" fill="url(#paint14_linear_223_30409)" class="grid-fill"')

html = html.replace('V562H701V486Z" fill="#E7E7E7"', 'V661H701V486Z" fill="#E7E7E7"')
html = html.replace('V622H580V486Z" fill="#E7E7E7"', 'V661H580V486Z" fill="#E7E7E7"')
html = html.replace('V512H822V486Z" fill="#E7E7E7"', 'V661H822V486Z" fill="#E7E7E7"')

# Fix CSS to use clip-path instead of transform (which is buggy in Safari)
new_css = """
.battery-fill, .grid-fill {
    clip-path: inset(100% 0 0 0);
}
.battery-fill.is-animating {
    transition: clip-path 1.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    clip-path: inset(0 0 0 0);
}
.grid-fill.is-animating {
    transition: clip-path 2.5s steps(var(--steps, 10), end);
    clip-path: inset(0 0 0 0);
}
"""

# Replace old CSS
html = re.sub(r'\.battery-fill, \.grid-fill \{[\s\S]*?\}\n\.grid-fill\.is-animating \{[\s\S]*?\}', new_css.strip(), html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Grey blocks and clip-path fixed")
