from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse


class ChemicalTestCase(APITestCase):

    def test_chemical(self):
        data = {"chemical_name": "SO2"}
        response = self.client.get(reverse('get_chemicals'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ChemicalTypeTestCase(APITestCase):
    def test_type(self):
        data = {"chem_type": "scrapping"}
        response = self.client.get(reverse('get_chemical_types'), data)
        self. assertEqual(response.status_code, status.HTTP_200_OK)
