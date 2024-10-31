from django.shortcuts import render, get_object_or_404
from showcase.models import Can

def index (request):
    cans = Can.objects.all()
    return render(request, 'showcase/index.html', {'cans':cans})

def image (request, can_id):
    can = get_object_or_404(Can, pk=can_id)
    return render(request, 'showcase/image.html', {"can":can})