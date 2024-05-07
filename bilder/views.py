from django.shortcuts import render
from .models import Bild

def list_images(request):
    images = Bild.objects.all()
    return render(request, 'bilder/image_list.html', {'images': images})

def search(request):
    query = request.GET.get('q', '')
    images = Bild.objects.filter(description__icontains=query)
    return render(request, 'bilder/search.html', {'images': images, 'query': query})
