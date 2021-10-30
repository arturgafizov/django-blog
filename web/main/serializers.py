from django.contrib.auth import get_user_model
from jwt import DecodeError
from rest_framework import serializers, request
from django.conf import settings
from actions.choices import FollowStatus
from actions.models import Follower
import jwt

from profiles.serializers import ShortUserInfoSerializer

User = get_user_model()


class UserJwtSerializer(serializers.Serializer):
    jwt = serializers.CharField()

    def validate_jwt(self, jwt_token):
        try:
            token = (jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"]))
            print(token['user_id'])
            self.user = User.objects.get(id=token['user_id'])

        except (DecodeError, User.DoesNotExist) as e:
            raise serializers.ValidationError(e)
        return jwt_token

    @property
    def data(self):
        return ShortUserInfoSerializer(self.user, context=self.context).data
