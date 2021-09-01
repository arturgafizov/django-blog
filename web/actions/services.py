from django.conf import settings

from .models import LikeDislike, Follower, UserAction
from django.contrib.contenttypes.models import ContentType
from main.decorators import except_shell
from django.contrib.auth import get_user_model

User = get_user_model()

class ActionsService:
    @staticmethod
    @except_shell((LikeDislike.DoesNotExist, ))
    def get_like_dislike_obj(user, model, object_id):
        content_type = ContentType.objects.get_for_model(model)
        return LikeDislike.objects.get(user=user, content_type=content_type, object_id=object_id)

    @staticmethod
    def is_user_followed(user, to_user_id: int) -> bool:
        return Follower.objects.filter(subscriber=user, to_user_id=to_user_id).exists()

    @staticmethod
    def unfollow_user(user, to_user_id: int):
        return Follower.objects.filter(subscriber=user, to_user_id=to_user_id).delete()

    @staticmethod
    def create_action(user, action: str, target):
        UserAction.objects.create(user=user, action=action, content_object=target)

    @staticmethod
    def delete_action(user, action: str, target):
        UserAction.objects.delete(user=user, action=action, content_object=target)

    @staticmethod
    def get_followers(user):
        return user.followers.all() if user is not None else print('This id not in DB')

    @staticmethod
    def get_following(user):
        # print(user.following.all())
        return user.following.all() if user is not None else print('This id not in DB')

    @staticmethod
    @except_shell((User.DoesNotExist,))
    def get_user_by_id(user_id: int):
        return User.objects.get(id=user_id)
