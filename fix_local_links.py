import re

html_file = "tw/materiality_analysis.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# We only want to fix the links inside the matrix SVG
# Let's find the matrix SVG
# It usually has an ID or we can just replace all anchor links that don't have .html and aren't http
# Example: <a href="cleaner_production#anchor-1"> -> <a href="cleaner_production.html#anchor-1">

def replacer(match):
    full_match = match.group(0)
    url = match.group(1)
    hash_part = match.group(2) or ""
    
    # Ignore if it already has .html or is an external link or javascript
    if ".html" in url or url.startswith("http") or url.startswith("javascript"):
        return full_match
        
    return f'href="{url}.html{hash_part}"'

# Regex to match href="some_page#anchor"
# \1 = some_page, \2 = #anchor
new_content = re.sub(r'href="([^"#.]+)(#[^"]+)?"', replacer, content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed local links successfully!")
