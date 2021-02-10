import tempfile

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from utils.tests import TestSetUp
from PIL import Image


class AlbumTest(TestSetUp):

    def setUp(self):
        super().setUp()
        self._create_user()
        self.client = APIClient()
        login_url = reverse('token_obtain_pair')

        data = {
            "username": "mark",
            "password": "fortest2020"
        }
        response = self.client.post(login_url, data, format='json')
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access']
        )

    def test_create_album(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        data = {
            'title': 'test title',
            'image': tmp_file
        }
        url = reverse('albums-list')
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
