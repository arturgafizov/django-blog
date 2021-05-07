from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.services import CeleryService
from auth_app.tasks import sent_email

User = get_user_model()


@receiver(post_save, sender=User)
def sent_mail_user(sender, created, instance, **kwargs):
    print(instance.id)
    # if created:
    #     CeleryService.send_email_confirm(instance)
