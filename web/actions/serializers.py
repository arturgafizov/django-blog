from rest_framework import serializers
from typing import Union
from django.contrib.auth import get_user_model
from main.serializers import UserSerializer
from .choices import LikeObjChoices, LikeStatus, LikeIconStatus, FollowStatus, UserActionChoices
from blog.services import BlogService
from .models import Follower, UserAction
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
        like_status = LikeIconStatus.LIKED if vote == LikeStatus.LIKE else LikeIconStatus.DISLIKED
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
                like_status = LikeIconStatus.EMPTY
            else:
                like_dislike.vote = vote
                like_dislike.save(update_fields=['vote'])
        return self.response_data(obj, like_status)

    def response_data(self, obj: Union[Article, Comment], like_status) -> dict:

        return {
            'like_count': obj.likes(),
            'dislike_count': obj.dislikes(),
            'like_status': like_status,
        }


class FollowerSerializer(serializers.Serializer):
    to_user = serializers.IntegerField(min_value=1)

    def save(self):
        subscriber = self.context['request'].user
        to_user: int = self.validated_data['to_user']

        if not ActionsService.is_user_followed(subscriber, to_user):
            subscriber.rel_from.create(to_user_id=to_user)
            follow_status = FollowStatus.UNFOLLOW
        else:
            ActionsService.unfollow_user(subscriber, to_user)
            follow_status = FollowStatus.FOLLOW

        return self.response_data(follow_status)

    def response_data(self, follow_status) -> dict:

        return {
            'follow_status': follow_status,
        }


class ActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=UserActionChoices.choices)
    object_id = serializers.IntegerField()


class UserFollowSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profiles_set.avatar')
    profile_url = serializers.URLField(source='get_absolute_url')
    follow = serializers.SerializerMethodField(method_name='get_follow_status')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'profile_url', 'follow', )

    def get_follow_status(self, obj):
        user = self.context['request'].user
        follow_obj = Follower.objects.filter(subscriber=user, to_user=obj).exists()
        if follow_obj:
            return FollowStatus.UNFOLLOW
        return FollowStatus.FOLLOW
