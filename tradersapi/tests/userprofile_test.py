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
