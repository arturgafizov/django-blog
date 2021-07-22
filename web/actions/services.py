from django.conf import settings

from .models import LikeDislike, Follower
from django.contrib.contenttypes.models import ContentType
from main.decorators import except_shell


class ActionsService:
    @staticmethod
    @except_shell((LikeDislike.DoesNotExist, ))
    def get_like_dislike_obj(user, model, object_id):
        content_type = ContentType.objects.get_for_model(model)
        return LikeDislike.objects.get(user=user, content_type=content_type, object_id=object_id)

    @staticmethod
    @except_shell((Follower.DoesNotExist, ))
    def get_follower(user_id: int):
        return Follower.objects.filter(subscriber_id=user_id)
