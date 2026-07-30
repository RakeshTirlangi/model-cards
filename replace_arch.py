import os
import re

dir_path = "/home/tanuh-cbr/Pictures/model_cards2"

image_map = {
    "BrainGPT.md": "braingpt.png",
    "Med3DVLM.md": "med3dvlm.png",
    "MedGemma-1.5.md": "medgemma.png",
    "Merlin.md": "merlin.png",
    "RAD3D-Prefix.md": "rad3d.png",
    "VILA-M3.md": "vila_m3.png"
}

for md_file, img_name in image_map.items():
    file_path = os.path.join(dir_path, md_file)
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Pattern to find ## Architecture and the subsequent ```text block
    # We want to replace the ```text ... ``` block under ## Architecture
    
    pattern = re.compile(r'(## Architecture\n\n### High-Level Design\n\n)```text\n.*?\n```', re.DOTALL)
    if pattern.search(content):
        replacement = r'\g<1>![Architecture](./arch_img/' + img_name + ')'
        new_content = pattern.sub(replacement, content, count=1)
    else:
        # Try without High-Level Design
        pattern2 = re.compile(r'(## Architecture\n\n)```text\n.*?\n```', re.DOTALL)
        if pattern2.search(content):
            replacement = r'\g<1>![Architecture](./arch_img/' + img_name + ')'
            new_content = pattern2.sub(replacement, content, count=1)
        else:
            print(f"Could not find architecture block in {md_file}")
            continue

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {md_file}")
