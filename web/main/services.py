from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy

from auth_app.utils import get_activate_key
from main.decorators import except_shell
from src.celery import app
from main.tasks import send_information_email
from django.conf import settings

User = get_user_model()


class CeleryService:

    @staticmethod
    def send_email_admin_contact(instance, request, **kwargs, ):
        kwargs.pop('file', None)
        kwargs['content'] = {'message': kwargs['content']}
        print('admin', kwargs)
        subject = 'User feedback'
        html_email_template_name = 'email/email_admin_feedback.html'
        url = reverse_lazy(f'admin:{instance._meta.app_label}_feedback_change', args=(instance.id,))

        context = {
            'name': kwargs.get('name'),
            'link_admin': request.build_absolute_uri(url)
        }
        to_email = settings.ADMIN_EMAILS
        send_information_email.delay(subject, html_email_template_name, context, to_email)

    @staticmethod
    def send_email_user_contact(**kwargs):
        kwargs.pop('file', None)
        kwargs['content'] = {'message': kwargs['content']}
        print('user', kwargs)
        subject = 'User feedback'
        html_email_template_name = 'email/email_request_feedback.html'
        context = {'name': kwargs.get('name')}
        to_email = kwargs.get('email')
        send_information_email.delay(subject, html_email_template_name, context, to_email)

    @staticmethod
    def send_password_reset(data: dict):
        data.pop('file', None)
        data['content'] = data.get('content')
        print(data)
        subject = 'Confirm your password'
        html_email_template_name = 'auth_app/email/email_password_reset.html'
        context = {'content': data['content']}
        print(context)
        to_email = data.get('to_email')
        send_information_email.delay(subject, html_email_template_name, context, to_email)
        # sent_password_reset.delay(**data)

    @staticmethod
    def send_email_confirm(user, **kwargs):
        key = get_activate_key(user)
        kwargs.pop('file', None)
        kwargs['content'] = {'message': ''}
        print('user', kwargs)
        subject = 'Confirm your email'
        html_email_template_name = 'auth_app/email/email_verify.html'
        context = {
            'user': user.get_full_name(),
            'activate_url': key,
        }
        to_email = user.email,
        send_information_email.delay(subject, html_email_template_name, context, to_email)


class UserService:

    @staticmethod
    @except_shell((User.DoesNotExist,))
    def get_user(email):
        return User.objects.get(email=email)

    @staticmethod
    def make_user_active(user):
        user.is_active = True
        user.save(update_fields=['is_active'])
        return user

    @staticmethod
    def get_users(users_id: list):
        return User.objects.filter(id__in=users_id)
