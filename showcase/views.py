from django.shortcuts import render

def index (request):
    return render(request, 'showcase/index.html')

def image (request):
    return render(request, 'showcase/image.html')