from django.contrib.auth import get_user_model

from auth_app.utils import get_activate_key
from main.decorators import except_shell
from src.celery import app
from auth_app.tasks import test, sent_verify_email, sent_password_reset
from main.tasks import sent_email_user, send_information_email

User = get_user_model()


class CeleryService:

    @staticmethod
    def send_email_admin_contact(data: dict):
        print(data)
        pass
        # send_information_email(**data)

    @staticmethod
    def send_email_user_contact(**kwargs):
        print(kwargs)
        kwargs.pop('file', None)
        kwargs['content'] = {'message': kwargs['content']}
        sent_email_user.delay(**kwargs)

    @staticmethod
    def send_password_reset(data: dict):
        sent_password_reset.delay(**data)

    @staticmethod
    def send_email_confirm(user):
        key = get_activate_key(user)
        kwargs = {
            'to_email': user.email,
            'content': {
                'user': user.get_full_name(),
                'activate_url': key,
            }
        }
        sent_verify_email.delay(**kwargs)


class UserService:

    @staticmethod
    @except_shell((User.DoesNotExist,))
    def get_user(email):
        return User.objects.get(email=email)

