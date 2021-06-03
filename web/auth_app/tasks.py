from django.contrib.auth import get_user_model
from django.template.loader import get_template
from src.celery import app
from django.core.mail import send_mail

UserModel = get_user_model()


@app.task
def test(**kwargs):
    print(kwargs)
    return kwargs


@app.task
def sent_email(user_id):
    user = UserModel.objects.get(pk=user_id)
    send_mail(
        'Testing2 send mail',
        'You have registered on the site Django-blog',
        'djangoblog.artur@gmail.com',
        [user.email],
    )
    return {'status': True}
