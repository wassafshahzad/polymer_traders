from django.urls import path
from .views import *


urlpatterns = [
    path('chemical/', get_all_chemical, name='get_chemicals'),
    path('chemialtype/', get_all_chemical_types, name='get_chemical_types'),
]
