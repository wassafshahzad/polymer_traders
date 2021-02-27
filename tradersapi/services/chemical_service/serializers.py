from rest_framework import serializers
from .models import ChemicalModel, ChemicalTypeModel


class ChemicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalModel
        fields = "__all__"


class ChemicalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalTypeModel
        fields = "__all__"
