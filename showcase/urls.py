from django.urls import path
from showcase.views import index, image

urlpatterns = [
    path('', index),
    path('image/', image)
]