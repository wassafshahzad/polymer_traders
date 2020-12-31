from django.urls import path, include
from .views import get_hello_world

urlpatterns = [
    path('', get_hello_world)
]
