from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.reverse import reverse_lazy
from .models import Follower, LikeDislike, UserAction
from .services import ActionsService
from .choices import UserActionChoices

User = get_user_model()


@receiver(post_save, sender=Follower)
def user_started_follow(sender, created: bool, instance: Follower, **kwargs):
    print(sender, created, instance)

    if created:
        user = instance.subscriber

        subscriber = "<a href='{url}'> {full_name} </a>".format(
            url=reverse_lazy('profiles:profile-detail', kwargs={'pk': user.id}),
            full_name=user.full_name()
        )
        to_user = instance.to_user
        to_user = "<a href='{url}'> {full_name} </a>".format(
            url=reverse_lazy('profiles:profile-detail', kwargs={'pk': to_user.id}),
            full_name=to_user.full_name()
        )
        action: str = UserActionChoices.FOLLOW_TO.label.format(subscriber=subscriber, to_user=to_user)
        ActionsService.create_action(user, action, instance)
