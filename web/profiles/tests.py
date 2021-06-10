from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase, override_settings
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
# Create your tests here.
from django.conf import settings
from rest_framework import status
from django.core import mail
import re

from main.services import UserService

User = get_user_model()


class ProfileApiTestCase(APITestCase):
    def test_forbidden_access(self):
        url = reverse_lazy('profiles:profile_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': settings.SUPERUSER_EMAIL,
            'password': settings.SUPERUSER_PASSWORD,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        url = reverse_lazy('profiles:profile_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
