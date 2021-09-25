from django.urls import path
from .views import index, home, weather, uploads

urlpatterns = [
    path('plants', index),
    path('', home),
    path('weather', weather),
    path('upload', uploads),
]
