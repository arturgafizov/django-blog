from rest_framework import serializers
from typing import Union
from django.contrib.auth import get_user_model
from main.serializers import UserSerializer
from .choices import LikeObjChoices, LikeStatus
from blog.services import BlogService
from .services import ActionsService
from blog.models import Article, Comment

User = get_user_model()


class PositiveIntegerField(serializers.IntegerField):
    min_value = 1


class LikeDislikeSerializer(serializers.Serializer):
    model = serializers.ChoiceField(choices=LikeObjChoices.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField()

    def save(self):
        user = self.context['request'].user
        print(self.validated_data)
        model = self.validated_data['model']
        object_id = self.validated_data['object_id']
        vote: int = self.validated_data['vote']
        if model == LikeObjChoices.ARTICLE:
            obj: Article = BlogService.get_article(object_id)
        else:
            obj: Comment = BlogService.get_comment(object_id)
        like_dislike = ActionsService.get_like_dislike_obj(user, obj, object_id)
        print(obj, like_dislike)
        if not like_dislike:
            obj.votes.create(user=user, vote=vote)
        else:
            if like_dislike.vote == vote:
                like_dislike.delete()
            else:
                like_dislike.vote = vote
                like_dislike.save(update_fields=['vote'])
        return self.response_data(obj)

    def response_data(self, obj: Union[Article, Comment]) -> dict:
        return {
            'like_count': obj.likes(),
            'dislike_count': obj.dislikes(),
        }


class FollowerSerializer(serializers.Serializer):
    to_user = serializers.IntegerField(min_value=1)

    # def save(self):
    #     user = self.context['request'].user
    #     to_user = self.validated_data['to_user']
