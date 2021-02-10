from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.user_data = {
            "username": "mark",
            "password": "fortest2020",
            "email": "ex_3@gmail.com",
            "first_name": "Mark",
            "last_name": "Troyan"
        }

    def _create_user(self):
        user = User.objects.create(**self.user_data)
        user.set_password("fortest2020")
        user.save()
        return user
