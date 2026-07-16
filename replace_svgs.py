import re

html_file = "tw/materiality_analysis.html"
thead_file = "img/svg/table__commitment-to-sdgs__section--tabulation__thead.svg"
tbody_file = "img/svg/table__commitment-to-sdgs__section--tabulation.svg"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(thead_file, "r", encoding="utf-8") as f:
    thead_svg = f.read()

with open(tbody_file, "r", encoding="utf-8") as f:
    tbody_svg = f.read()

# Helper function to replace SVG inside a target div class
def replace_svg_in_div(html, div_class, new_svg):
    div_start = html.find(f'class="{div_class}"')
    if div_start == -1:
        # Fallback to general search if class formatting differs
        div_start = html.find(div_class)
        if div_start == -1:
            print(f"Could not find div with class: {div_class}")
            return None
            
    svg_start = html.find('<svg', div_start)
    if svg_start == -1:
        print(f"Could not find <svg inside div: {div_class}")
        return None
        
    svg_end = html.find('</svg>', svg_start)
    if svg_end == -1:
        print(f"Could not find matching </svg> inside div: {div_class}")
        return None
    svg_end += 6  # include </svg>
    
    return html[:svg_start] + new_svg + html[svg_end:]

# Replace tbody first (usually appears second, but let's do it cleanly)
new_html = replace_svg_in_div(html_content, "sticky-tbody", tbody_svg)
if new_html:
    new_html = replace_svg_in_div(new_html, "sticky-thead", thead_svg)
    if new_html:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_html)
        print("SVGs replaced successfully using div-based containers!")
    else:
        exit(1)
else:
    exit(1)
