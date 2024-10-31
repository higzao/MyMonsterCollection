from django.shortcuts import render
from showcase.models import Can

def index (request):
    cans = Can.objects.all()
    return render(request, 'showcase/index.html', {'cans':cans})

def image (request):
    return render(request, 'showcase/image.html')