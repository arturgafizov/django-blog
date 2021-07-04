from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
# Create your tests here.
from django.conf import settings
from rest_framework import status
from django.test import TestCase, override_settings

User = get_user_model()

locmem_email_backend = override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    CELERY_TASK_ALWAYS_EAGER=True,
)


class ContactUsApiTestCase(APITestCase):
    @locmem_email_backend                      # add decorator so that the emails do not go to the real mail
    def test_contact_us(self):
        url = reverse_lazy('contact_us:feedback')
        data = {
            'name': 'Admin',
            'email': settings.SUPERUSER_EMAIL,
            'content': 'Hello gays'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        print(response.data)

        data = {
            'name': 'Admin',
            'email': 'test@mail.com',
            'content': ''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
