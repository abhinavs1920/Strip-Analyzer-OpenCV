# analyzer/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .services import analyze_image_service

def index(request):
    return render(request, 'analyzer/index.html')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        path = default_storage.save('temp.jpg', ContentFile(image.read()))
        image_path = f"./{path}"
        
        colors = analyze_image_service(image_path)
        
        default_storage.delete(path)
        
        return JsonResponse(colors, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)
