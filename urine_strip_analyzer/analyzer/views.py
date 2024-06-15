from django.shortcuts import render

def index(request):
    return render(request, 'analyzer/index.html')

import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        path = default_storage.save('temp.jpg', ContentFile(image.read()))
        image_path = f"./{path}"
        
        # Process the image
        colors = analyze_image(image_path)
        
        # Remove the temp image file
        default_storage.delete(path)
        
        return JsonResponse(colors, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def analyze_image(image_path):
    img = cv2.imread(image_path)
    
    # Resize image if needed
    img = cv2.resize(img, (300, 100)) # assuming a fixed size for simplicity
    
    # Assuming 10 equally spaced color sections
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
