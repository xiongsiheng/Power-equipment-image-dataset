# copy_example_images.py
# check all categories and copy 10 example images of each category to a new folder.

import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import shutil

# === Paths ===
root_dir = r"transmission line object detection"
output_dir = r"example images"

# === Create output directory if not exists ===
os.makedirs(output_dir, exist_ok=True)

# Dictionary: class_name → list of relative image paths
class_to_paths = defaultdict(list)

# === Step 1: Collect up to 10 image paths per class ===
for subdir, dirs, files in os.walk(root_dir):
    if os.path.basename(subdir) == "Annotations":  # Only process Annotations folders
        jpeg_folder = os.path.join(os.path.dirname(subdir), "JPEGImages")

        for file in files:
            if not file.lower().endswith(".xml"):
                continue

            xml_path = os.path.join(subdir, file)
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()

                # Get relative folder and filename
                # folder_tag = root.find("folder").text.strip()
                folder_tag = "JPEGImages"
                filename_tag = root.find("filename").text.strip()
                img_path = os.path.join(os.path.dirname(subdir), folder_tag, filename_tag)

                # Record classes
                for obj in root.findall("object"):
                    cls = obj.find("name").text.strip()
                    if len(class_to_paths[cls]) < 10:
                        class_to_paths[cls].append(img_path)

            except Exception as e:
                print(f"Error reading {xml_path}: {e}")

# === Step 2: Copy 10 images per class to Desktop ===
for cls, img_paths in class_to_paths.items():
    class_folder = os.path.join(output_dir, cls)
    os.makedirs(class_folder, exist_ok=True)

    for img_path in img_paths:
        try:
            if os.path.exists(img_path):
                dest_path = os.path.join(class_folder, os.path.basename(img_path))
                shutil.copy(img_path, dest_path)
            else:
                print(f"Skipped (not found): {img_path}")
        except PermissionError:
            print(f"Skipped (permission denied): {img_path}")
        except Exception as e:
            print(f"Skipped ({type(e).__name__}): {img_path} -> {e}")

print("\nDone! Example images saved to:")
print(output_dir)