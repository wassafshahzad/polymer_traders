import json
from django.urls import reverse
from .services.chemical_service.models import ChemicalModel
from .services.chemical_service.models import ChemicalTypeModel
from rest_framework import status
from rest_framework.test import APITestCase
from .services.chemical_service.serializers import ChemicalSerializer, ChemicalTypeSerializer

class ChemicalTestCase(APITestCase):

    def test_chemical(self):
        data = {"chemical_name": "SO2"}
        response = self.client.get("/trader/api/chemical_service/chemical/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ChemicalTypeTestCase(APITestCase):
    def test_type(self):
        data = { "chem_type" : "scrapping" }
        response = self.client.get("/trader/api/chemical_service/chemialtype/", data)
        self. assertEqual(response.status_code, status.HTTP_200_OK)
