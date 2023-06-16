import json
import cv2
with open('test.json','r') as file:
    data = json.load(file)
    for item in data:
        for key, value in item.items():
            print(key)
            points = value['points']
            box = value['box']
            for i in range(0, len(points), 3):
                x, y, visible = points[i], points[i + 1], points[i + 2]
                if visible > 1:
                    image =  cv2.imread(fr'C:\Users\Rithvik\Desktop\Backup\New_images\{key + ".jpg"}', cv2.IMREAD_COLOR)
                    cv2.circle(image, (x, y), 6, (0, 0, 255), -1)
                    cv2.imwrite(fr'C:\Users\Rithvik\Desktop\Backup\New_images\{key + ".jpg"}', image)
