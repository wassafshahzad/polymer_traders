from django.http import response
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse


class UserProfileListCreateTestCase(APITestCase):
    fixtures = ['data.json']

    def test_get_user_profle(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user_profile_fail(self):
        data = {
            "name": "WASSSAF",
            "phone_number": "+923344103962"
        }
        response = self.client.post(reverse("profile"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
