from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from rest_framework.reverse import reverse_lazy

from profiles.models import Profile
from .models import Follower, LikeDislike, UserAction
from .services import ActionsService
from .choices import UserActionChoices

User = get_user_model()


@receiver(post_save, sender=Follower)
def user_started_follow(sender, instance: Follower, **kwargs):
    print(sender, instance)
    template = 'actions/start_follow.html'
    data = {
        'subscriber': instance.subscriber,
        'to_user': instance.to_user,
    }

    action = render_to_string(template, data)
    user = instance.subscriber
    ActionsService.create_action(user, action, instance)


@receiver(post_save, sender=Follower)
def user_finished_follow(sender, instance: Follower, **kwargs):
    print(sender, instance)
    template = 'actions/finish_follow.html'
    data = {
        'subscriber': instance.subscriber,
        'to_user': instance.to_user,
    }

    action = render_to_string(template, data)
    user = instance.subscriber
    ActionsService.create_action(user, action, instance)


@receiver(post_save, sender=Profile)
def user_changed_avatar(sender, created: bool, instance: Profile, **kwargs):
    print(sender, created, instance)
    template = 'actions/change_avatar.html'
    data = {
        'avatar': instance.avatar,
    }

    action = render_to_string(template, data)
    user = instance.user
    ActionsService.create_action(user, action, instance)
