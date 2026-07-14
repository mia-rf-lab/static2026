import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/tw/innovative_technology.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('V211H701V125Z', 'V300H701V125Z')
html = html.replace('V271H580V125Z', 'V300H580V125Z')
html = html.replace('V562H701V486Z', 'V661H701V486Z')
html = html.replace('V622H580V486Z', 'V661H580V486Z')
html = html.replace('V512H822V486Z', 'V661H822V486Z')

new_path = '<path d="M822 125C822 122.791 823.791 121 826 121H874C876.209 121 878 122.791 878 125V300H822V125Z" fill="#E7E7E7"/>\n'
if new_path not in html:
    html = html.replace('<line x1="822" y1="130.5"', new_path + '<line x1="822" y1="130.5"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed grey paths")
