import cv2
import xml.etree.ElementTree as ET
import os

def read_xml(xmlFile,image):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for obj in root.findall('.//object'):
        name = obj.find('name').text
        xmin = int(obj.find('bndbox/xmin').text)
        xmax = int(obj.find('bndbox/xmax').text)
        ymin = int(obj.find('bndbox/ymin').text)
        ymax = int(obj.find('bndbox/ymax').text)
        if name != "14":
            draw_circle(image,xmin,xmax,ymin,ymax,name)
        else:
            draw_rectangle(image,xmin,xmax,ymin,ymax,name)

def draw_circle(image,x_min, x_max, y_min, y_max,name):
    center_x = (x_min + x_max) // 2
    center_y = (y_min + y_max) // 2
    cv2.circle(image, (center_x, center_y),6, (0,255,0), -1)
    cv2.putText(image,name,((center_x + 8), (center_y + 8)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)

def draw_rectangle(image, x_min, x_max,y_min,y_max,name):
    cv2.rectangle(image,(x_min,y_min), (x_max,y_max),(0,255,0),6)
    cv2.putText(image,name,(((x_max -x_min) - 5),(y_max- y_min)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)

for xml_file in os.listdir(r"C:\Users\Rithvik\Desktop\Backup\annotation_13"):
    xml_path = fr'C:\Users\Rithvik\Desktop\Backup\annotation_13\{xml_file}'
    jpg_path = fr'C:\Users\Rithvik\Desktop\Backup\Images\{xml_file.split(".")[0] + ".jpg"}'
    if os.path.exists(xml_path) and os.path.exists(jpg_path):
        image = cv2.imread(jpg_path, cv2.IMREAD_COLOR)
        read_xml(xml_path,image)
        cv2.imwrite(jpg_path, image)

for xml in os.listdir(r"C:\Users\Rithvik\Desktop\Backup\annotation_14"):
    xml_path = fr'C:\Users\Rithvik\Desktop\Backup\annotation_14\{xml}'
    jpg_path = fr'C:\Users\Rithvik\Desktop\Backup\Images\{xml.split(".")[0] + ".jpg"}'
    if os.path.exists(xml_path) and os.path.exists(jpg_path):
        image = cv2.imread(jpg_path, cv2.IMREAD_COLOR)
        read_xml(xml_path,image)
        cv2.imwrite(jpg_path, image)

