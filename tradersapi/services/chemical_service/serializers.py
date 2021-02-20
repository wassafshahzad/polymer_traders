from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import ChemicalModel, ChemicalProduct, ChemicalTypeModel


class ChemicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalModel
        fields = "__all__"


class ChemicalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalTypeModel
        fields = "__all__"


class ChemicalProductSerializer(serializers.ModelSerializer):
    chemical = ChemicalSerializer(read_only=True)
    chemical_type = ChemicalTypeSerializer(read_only=True)

    class Meta:
        model = ChemicalProduct
        fields = '__all__'
