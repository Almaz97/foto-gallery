from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from utils.tests import TestSetUp


class RegistrationLoginTest(TestSetUp):

    def test_registration(self):
        data = self.user_data
        data["password"] = "fortest2020"
        data["password2"] = "fortest2020"

        url = reverse('auth_register')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        data = {
            "username": "mark",
            "password": "fortest2020"
        }
        self._create_user()
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
