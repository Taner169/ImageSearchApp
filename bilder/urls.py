from django.urls import path
from .views import list_images, search

urlpatterns = [
    path('list-images/', list_images, name='list_images'),
    path('search/', search, name='search'),
]
