from django.test import TestCase, override_settings
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
# Create your tests here.
from django.conf import settings
from rest_framework import status
from django.core import mail

locmem_email_backend = override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    CELERY_TASK_ALWAYS_EAGER=True,
)


class AuthApiTestCase(APITestCase):
    def test_sign_in(self):
        url = reverse_lazy('auth_app:api_login')
        data = {
            'email': settings.SUPERUSER_EMAIL,
            'password': settings.SUPERUSER_PASSWORD,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        data = {
            'email': 'oemr.m.aa@mail.ru',
            'password': 'string1985',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

    @locmem_email_backend
    def test_sigh_up(self):
        url = reverse_lazy('auth_app:api_sign_up')
        data = {
            'first_name': 'Hero',
            'last_name': 'HHH',
            'email': 'oemr.m.aa@mail.ru',
            'password1': 'string1985',
            'password2': 'string1986',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        print(response.data)
        self.assertEqual(response.json(), {'password2': ["The two password fields didn't match."]})

        data['password2'] = 'string1985'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(len(mail.outbox), 1)
        print('mail', mail.outbox[0])
        print(dir(mail.outbox[0]))
