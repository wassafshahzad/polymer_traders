from rest_framework.decorators import api_view
from .models import ChemicalTypeModel
from rest_framework.response import Response


@api_view(['GET'])
def get_all_chemical_types(request):
