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


@app.task
def sent_verify_email(**kwargs):
    print(kwargs)
    html_template = get_template('auth_app/email/email_verify.html')
    subject = 'Confirm your email'
    render_content = html_template.render(kwargs.get('content'))
    to_email = kwargs.get('to_email')
    send_mail(subject=subject,
              message='',
              from_email=None,
              recipient_list=[to_email, ],
              html_message=render_content)


@app.task
def sent_password_reset(**kwargs):
    print(kwargs)
    html_template = get_template('auth_app/email/email_password_reset.html')
    subject = 'Confirm your password'
    render_content = html_template.render(kwargs.get('content'))
    to_email = kwargs.get('to_email')
    send_mail(subject=subject,
              message='',
              from_email=None,
              recipient_list=[to_email, ],
              html_message=render_content)
