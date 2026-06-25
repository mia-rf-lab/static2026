import re

html_path = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'

# Restore the file to original state first
import subprocess
subprocess.run(['git', 'checkout', 'tw/commitment_to_sdgs.html'], cwd='/Users/mia/Desktop/0522南亞ESG 2026/static2025')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Print the top-left box Y coordinate from unclickable-area to see if layout changed
match = re.search(r'<path d="M583 0H263V36H583V0Z" fill="#F6F6F6" />', html)
if match:
    print("Found top-left rect at Y=0")
else:
    print("Top-left rect not at Y=0")

