from rest_framework import serializers

from profiles.models import Profile
from main.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'mobile', 'avatar', 'location',)
        # depth = 1
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)
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
