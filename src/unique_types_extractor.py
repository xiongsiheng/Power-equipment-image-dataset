# unique_types_extractor.py
# count unique 'type' values in the JSON annotation file

import json

# Load the JSON annotation file
with open(r"substation object detection/annotation.json", "r") as f:
    data = json.load(f)

unique_types = set()

# Loop through all images in the annotation
for img_key, img_data in data.items():
    regions = img_data.get("regions", [])
    for region in regions:
        region_attrs = region.get("region_attributes", {})
        type_value = region_attrs.get("type")
        if type_value:
            unique_types.add(type_value)

# Convert to list (optional)
unique_types = list(unique_types)

unique_types_processed = [t for t in unique_types if '+' not in t]

print("Unique 'type' values:", unique_types_processed)