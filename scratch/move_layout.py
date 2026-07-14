import re

file_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2026/tw/innovative_technology.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the dashboard col value to "12億485"
html = html.replace('<em>6億1,717</em>', '<em>12億485</em>')

# 2. Extract the animated SVG + CSS + JS block
# It starts around the <svg> tag and goes until the end of the script tag
svg_start_idx = html.find('<svg width="942" height="735"')
script_end_tag = '</script>\n        </div>\n      </div>'
script_end_idx = html.find(script_end_tag) + len(script_end_tag)

# Let's find the exact block containing the svg, styles, and script
# The block is inside:
# <div class="single-column-v">
#   <img src="../img/svg/chart__innovative-technology__anchor-4__single-column-v.svg" ...>
#   <svg ...> ... </svg>
#   <style> ... </style>
#   <script> ... </script>
# </div>
# </div>

# Let's target the parent:
second_duplicate_pattern = re.compile(
    r'<div class="wrapper aos">\s*<div class="wording">\s*<h4 class="--centered"[^>]*>南亞科技產品規劃與規格演進</h4>\s*</div>\s*<div class="single-column-v">\s*<img src="\.\./img/svg/chart__innovative-technology__anchor-4__single-column-v\.svg"[^>]*>.*?<script>.*?</script>\s*</div>\s*</div>',
    re.DOTALL
)

match = second_duplicate_pattern.search(html)
if not match:
    # Let's try to locate the svg and script directly
    print("Could not match the regex pattern. Let's do manual slice.")
    # Let's find the container of anchor-4
    anchor4_img_idx = html.find('chart__innovative-technology__anchor-4__single-column-v.svg')
    start_wrapper_idx = html.rfind('<div class="wrapper aos">', 0, anchor4_img_idx)
    # The end of wrapper is after the script
    end_script_idx = html.find('</script>', anchor4_img_idx)
    end_wrapper_idx = html.find('</div>', end_script_idx)
    end_wrapper_idx = html.find('</div>', end_wrapper_idx + 6) # second closing div
    
    second_block = html[start_wrapper_idx:end_wrapper_idx+6]
else:
    second_block = match.group(0)

# We want to extract the content inside the <div class="single-column-v"> of the second block
# which has the <img> + <svg> + <style> + <script>
inner_content_match = re.search(r'<div class="single-column-v">(.*?)</div>\s*</div>$', second_block, re.DOTALL)
if inner_content_match:
    inner_content = inner_content_match.group(1).strip()
else:
    # Fallback
    inner_content = ""

print("Extracted second duplicate inner content.")

# 3. Find the first duplicate (which has anchor-3 image)
first_duplicate_pattern = re.compile(
    r'<div class="wrapper aos">\s*<div class="wording">\s*<h4 class="--centered"[^>]*>南亞科技產品規劃與規格演進</h4>\s*</div>\s*<div class="single-column-v">.*?</div>\s*</div>',
    re.DOTALL
)

# Let's locate the first duplicate block
first_anchor_idx = html.find('chart__innovative-technology__anchor-3__single-column-v.svg')
first_wrapper_start = html.rfind('<div class="wrapper aos">', 0, first_anchor_idx)
first_wrapper_end = html.find('</div>', first_anchor_idx)
first_wrapper_end = html.find('</div>', first_wrapper_end + 6)

first_block = html[first_wrapper_start:first_wrapper_end+6]

# Replace the inner single-column-v content of the first block with the extracted animated content
# The first block's inner single-column-v is currently:
# <div class="single-column-v">
#   <img src="../img/svg/chart__innovative-technology__anchor-3__single-column-v.svg" ...>
# </div>
new_first_block = f"""<div class="wrapper aos">
          <div class="wording">
            <h4 class="--centered" data-animate="fadeInUp" data-animate-delay=".2">南亞科技產品規劃與規格演進</h4>
          </div>

          <div class="single-column-v aos">
            {inner_content}
          </div>
        </div>"""

# 4. Perform the replacements in html
# Replace the first block with the animated version
html = html.replace(first_block, new_first_block)

# Remove the second block completely
html = html.replace(second_block, '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Layout moved and cleaned up successfully!")
