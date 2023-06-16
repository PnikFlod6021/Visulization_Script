import json
from PIL import Image

with open("test.json", "r") as file:
    input_json = file.read()

data = json.loads(input_json)

output_data = {
    "images": [],
    "annotations": []
}
id = 1
for item in data:
    for image_id, image_data in item.items():
        image = Image.open(fr'C:\Users\Rithvik\Desktop\Backup\New_images\{image_id + ".jpg"}')
        image_width, image_height = image.size
        image = {
            "license": None,
            "file_name": f"{image_id}.png",
            "coco_url": None,
            "height": image_height,
            "width": image_width,
            "id": id
        }
        output_data["images"].append(image)

        annotation = {
            "segmentation": None,
            "num_keypoints": len(image_data["points"]) // 3,
            "area": (image_data["box"][2]) * (image_data["box"][3]),
            "iscrowd": 0,
            "keypoints": image_data["points"],
            "image_id": id,
            "bbox": image_data["box"],
            "category_id": 1,
            "id": id,
            "inmodal_bbox": None,
            "inmodal_seg": None
        }
        output_data["annotations"].append(annotation)
        id += 1

end_data = {
    "categories": [
        {
            "supercategory": "cow",
            "id": 1,
            "name": "cattle",
            "keypoints": [
                "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13"
            ],
            "skeleton": [
                [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 13]
            ]
        }
    ]
}
output_data.update(end_data)

output_json = json.dumps(output_data, indent=4)

with open("output.json", "w") as file:
    file.write(output_json)
