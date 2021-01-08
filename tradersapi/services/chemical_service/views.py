from rest_framework.decorators import api_view
from .models import ChemicalTypeModel, ChemicalModel
from rest_framework.response import Response


@api_view(['GET'])
def get_all_chemical_types(request):
    return Response(ChemicalTypeModel.objects.all())


@api_view(['GET'])
def get_all_chemical(request):
    return Response(ChemicalModel.objects.all())
