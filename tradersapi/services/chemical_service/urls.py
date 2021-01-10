from django.urls import path
from .views import *


urlpatterns = [
    path('chemical/', get_all_chemical),
    path('chemialtype/', get_all_chemical_types),
]
