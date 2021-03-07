from django.http import response
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


class UserProfileListCreateTestCase(APITestCase):
    fixtures = ['data.json']

    def test_get_user_profle_success(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user_profile_fail_unauthorized(self):
        data = {
            "name": "WASSSAF",
            "phone_number": "+923344103962"
        }
        response = self.client.post(reverse("profile"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_profile_fail_db_validation(self):
        user = User.objects.get(username="Test2")
        self.client.force_authenticate(user=user)
        data = {
            "name": "WASSSAF",
            "phone_number": "+923344103962"
        }
        response = self.client.post(reverse("profile"), data)
        self.assertEqual(response.data['phone_number'][0],
                         "UserProfileModel with this phone number already exists.")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_profile_success(self):
        user = User.objects.get(username="Test2")
        self.client.force_authenticate(user=user)
        data = {
            "name": "Test2",
            "phone_number": "+923366466467"
        }
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserProductTestCreateRetriveCases(APITestCase):
    fixtures = ['data.json']
    data = {
        "quantity": "10 drum",
        "price_per_bad": "10",
        "chemical": 2,
        "chemical_type": 1
    }

    def test_create_user_product_fail_401(self):
        response = self.client.post(reverse('get_product'), self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_product_fail_400_chemical_not_exist(self):
        data = {
            "quantity": "10 drum",
            "price_per_bad": "10",
            "chemical": 100,
            "chemical_type": 1
        }
        user = User.objects.get(username="Test2")
        self.client.force_authenticate(user=user)
        response = self.client.post(reverse('get_product'), data)
        self.assertEqual(response.data['chemical'][0].code, 'does_not_exist')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_product_fail_400_chemical_not_exist(self):
        data = {
            "quantity": "10 drum",
            "price_per_bad": "10",
            "chemical": 1,
            "chemical_type": 100
        }
        user = User.objects.get(username="Test2")
        self.client.force_authenticate(user=user)
        response = self.client.post(reverse('get_product'), data)
        self.assertEqual(
            response.data['chemical_type'][0].code, 'does_not_exist')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_product_fail_400_profle_not_exist(self):
        user = User.objects.get(username="Test2")
        self.client.force_authenticate(user=user)
        response = self.client.post(reverse('get_product'), self.data)
        self.assertEqual(
            response.data['non_field_errors'][0].code, 'invalid')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
