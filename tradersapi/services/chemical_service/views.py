from rest_framework.decorators import api_view
from .models import ChemicalTypeModel, ChemicalModel
from .serializers import *
from rest_framework.response import Response


@api_view(['GET'])
def get_all_chemical_types(request):
    return Response(data=ChemicalTypeSerializer(ChemicalTypeModel.objects.all(), many=True).data)


@api_view(['GET'])
def get_all_chemical(request):
    return Response(data=ChemicalSerializer(ChemicalModel.objects.all()), many=True)
