import os
import re
from pathlib import Path

def find_unused_images(project_dir):
    img_dir = os.path.join(project_dir, 'img')
    
    # 1. Get all image files
    all_images = []
    for root, _, files in os.walk(img_dir):
        for file in files:
            if file == '.DS_Store':
                continue
            all_images.append(os.path.join(root, file))
            
    # 2. Get all source files to check for references
    source_files = []
    for root, _, files in os.walk(project_dir):
        # skip .git, dl_files, and img directories itself for source files
        if '/.git' in root or '/dl_files' in root or '/img' in root:
            continue
        for file in files:
            if file.endswith(('.html', '.css', '.js')):
                source_files.append(os.path.join(root, file))
                
    # 3. Read content of all source files
    source_contents = ""
    for sf in source_files:
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                source_contents += f.read() + "\n"
        except Exception as e:
            pass # ignore decode errors

    # 4. Check which images are unused
    unused_images = []
    for img_path in all_images:
        filename = os.path.basename(img_path)
        # Search for the filename in the concatenated source contents
        # This is a safe check: if the filename doesn't appear anywhere, it's definitely unused.
        if filename not in source_contents:
            unused_images.append(img_path)
            
    return unused_images, all_images

if __name__ == "__main__":
    project_dir = "/Users/mia/Desktop/static2026"
    unused, all_imgs = find_unused_images(project_dir)
    print(f"Total images found: {len(all_imgs)}")
    print(f"Unused images found: {len(unused)}")
    print("\nList of unused images:")
    for u in unused:
        print(u)
