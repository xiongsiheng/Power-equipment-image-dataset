# data_stat.py
# count total number of images and unique classes in the dataset

import os
import xml.etree.ElementTree as ET

# Root folder
root_dir = r"transmission line object detection"

# Supported image extensions
image_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

total_images = 0

# Walk through all subdirectories
for subdir, dirs, files in os.walk(root_dir):
    # Count only image files
    image_count = sum(1 for f in files if f.lower().endswith(image_exts))
    total_images += image_count

print(f"Total number of images: {total_images}")



# Set to hold all unique class names
unique_classes = set()

# Traverse all subdirectories
for subdir, dirs, files in os.walk(root_dir):
    if os.path.basename(subdir) == "Annotations":  # Only process Annotations folders
        for file in files:
            if file.lower().endswith(".xml"):
                xml_path = os.path.join(subdir, file)
                try:
                    tree = ET.parse(xml_path)
                    root = tree.getroot()
                    # Each <object> tag can contain a <name> (class label)
                    for obj in root.findall("object"):
                        name = obj.find("name").text.strip()
                        unique_classes.add(name)
                except Exception as e:
                    print(f"Error reading {xml_path}: {e}")

# Display all unique class names
print(f"Total unique classes: {len(unique_classes)}")
print("Class names:", sorted(unique_classes))