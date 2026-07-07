import os
from bs4 import BeautifulSoup
import glob

base_dir = "/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw"
html_files = glob.glob(f"{base_dir}/*.html")

mapping = {}

for html_file in html_files:
    basename = os.path.basename(html_file)
    if basename in ['index.html', 'materiality_analysis.html']: continue
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Anchors are usually like id="anchor-1"
    # The title might be an <h2> or <h3> nearby, or inside a container
    for elem in soup.find_all(id=lambda x: x and x.startswith('anchor-')):
        anchor_id = elem.get('id')
        url = f"{basename.replace('.html', '')}#{anchor_id}"
        
        # Try to find the title. Usually in an h2 or h3 with class anchor-heading or within the same section
        heading = elem.find(['h2', 'h3', 'h4'])
        if not heading:
            # Maybe it's a div, and heading is inside
            heading = elem.find_next(['h2', 'h3', 'h4'])
        
        if heading:
            title = heading.get_text(strip=True)
            mapping[title] = url
            print(f"{title} -> {url}")

print("Done mapping.")
