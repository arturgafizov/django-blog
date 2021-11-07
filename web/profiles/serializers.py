from rest_framework import serializers
from django.contrib.auth import get_user_model

from actions.choices import FollowStatus
from actions.models import Follower
from .models import Profile

from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profiles_set.avatar')
    follow = serializers.SerializerMethodField(method_name='get_follow_status')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'first_name', 'last_name', 'avatar',
                  'follow', 'followers_count', 'following_count')
        extra_kwargs = {
            'avatar': {'read_only': True},
        }

    def get_follow_status(self, obj):
        user = self.context['request'].user
        follow_obj = Follower.objects.filter(subscriber=user, to_user=obj).exists()
        if follow_obj:
            return FollowStatus.UNFOLLOW
        return FollowStatus.FOLLOW


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'mobile', 'avatar', 'location', 'website')
        # depth = 1
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # print(data)
        user = data.pop('user')
        data.update(user)
        return data


class UploadAvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    def save(self, **kwargs):
        self.instance.old_avatar_delete()
        super().save(**kwargs)

    class Meta:
        model = Profile
        fields = ('avatar',)


class UploadAvatarUserSerializer(serializers.Serializer):
    avatar = serializers.ImageField()

    def save(self):
        print(self.instance, self.validated_data)
        self.instance.old_avatar_delete()
        self.instance.avatar = self.validated_data.get('avatar')
        self.instance.save()


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mobile', 'location', 'url')

    def update(self, profile, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user = profile.user
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
        return super().update(profile, validated_data)


class ShortUserInfoSerializer(serializers.ModelSerializer):
    profile_url = serializers.URLField(source='get_profile_url')
    # avatar = serializers.ImageField(source='profiles_set.avatar')
    avatar_url = serializers.URLField(source='get_avatar_url')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'profile_url', 'avatar_url', )

    def get_avatar_url(self, user):
        request = self.context.get('request')
        print(request)
        avatar_url = user.profiles_set.avatar
        return request.build_absolute_uri(avatar_url)
