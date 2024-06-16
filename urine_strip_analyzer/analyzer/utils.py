# analyzer/utils.py

import cv2

def analyze_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (300, 100)) 
    colors = []
    for i in range(10):
        section = img[:, i*30:(i+1)*30, :]
        avg_color = cv2.mean(section)[:3]
        colors.append({
            'r': int(avg_color[2]),
            'g': int(avg_color[1]),
            'b': int(avg_color[0])
        })
    
    return colors
