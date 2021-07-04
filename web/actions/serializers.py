from rest_framework import serializers

from django.contrib.auth import get_user_model
from main.serializers import UserSerializer
from .choices import LikeObjChoices, LikeStatus
from blog.services import BlogService
from .services import ActionsService
from blog.models import Article, Comment

User = get_user_model()


class LikeDislikeSerializer(serializers.Serializer):
    model = serializers.ChoiceField(choices=LikeObjChoices.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField()

    def save(self):
        user = self.context['request'].user
        print(self.validated_data)
        model = self.validated_data['model']
        object_id = self.validated_data['object_id']
        vote = self.validated_data['vote']
        if model == LikeObjChoices.ARTICLE:
            obj: Article = BlogService.get_article(object_id)
        else:
            obj: Comment = BlogService.get_comment(object_id)
        like_dislike = ActionsService.get_like_dislike_obj(user, obj, object_id)
        print(obj, like_dislike)
        if not like_dislike:
            obj.votes.create(user=user, vote=vote)
        else:
            pass
