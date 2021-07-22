from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profiles_set.avatar')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'first_name', 'last_name', 'avatar',)
        extra_kwargs = {
            'avatar': {'read_only': True},
        }
