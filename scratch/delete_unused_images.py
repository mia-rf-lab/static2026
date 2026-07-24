import os
from pathlib import Path

def delete_unused_images(project_dir):
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

    # 4. Check and delete unused images
    unused_count = 0
    for img_path in all_images:
        filename = os.path.basename(img_path)
        if filename not in source_contents:
            print(f"Deleting: {img_path}")
            os.remove(img_path)
            unused_count += 1
            
    return unused_count

if __name__ == "__main__":
    project_dir = "/Users/mia/Desktop/static2026"
    print("Starting deletion process...")
    deleted = delete_unused_images(project_dir)
    print(f"Successfully deleted {deleted} unused images.")
