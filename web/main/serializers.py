from django.contrib.auth import get_user_model
from rest_framework import serializers

from actions.choices import FollowStatus

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profiles_set.avatar')
    follow = serializers.SerializerMethodField(method_name='get_follow_status')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'first_name', 'last_name', 'avatar', 'follow')
        extra_kwargs = {
            'avatar': {'read_only': True},
        }

    def get_follow_status(self, obj):
        user = self.context['request'].user
        follow_obj = user.following.filter(to_user=obj).exists()
        if follow_obj:
            return FollowStatus.UNFOLLOW
        return FollowStatus.FOLLOW
