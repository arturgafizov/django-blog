from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
# Create your tests here.
from django.conf import settings
from rest_framework import status
from django.test import TestCase, override_settings

from blog.models import Category

User = get_user_model()

# Create your tests here.


class BlogApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData')
        data = {
            'name': 'bike',
        }
        cls.category = Category.objects.create(**data)
        cls.user = User.objects.create_user(email='oemr.m.aa@mail.ru', password='string1986')

    def setUp(self) -> None:
        print('setUp')

    def test_create_article(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': settings.SUPERUSER_EMAIL,
            'password': settings.SUPERUSER_PASSWORD,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # self.client.force_login()
        if self.user.is_authenticated:
            url = reverse_lazy('blog:post-list')
            data = {
                'title': 'Sport',
                'category': self.category.id,
                'content': 'Test content',
            }

            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
            print(response.data)

        url = reverse_lazy('blog:post-list')
        data = {
            'title': 'Sport',
            'category': self.category.id,
            'content': 'Test content',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        print(response.data)

    def test_create_article_forbidden(self):
        url = reverse_lazy('auth_app:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = reverse_lazy('blog:post-list')
        data = {
            'title': 'Sport',
            'category': self.category.id,
            'content': 'Test content',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("Create article forbidden", response.data)
