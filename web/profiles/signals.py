from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    print(sender, created, instance)

    if created:
        Profile.objects.create(user=instance)
