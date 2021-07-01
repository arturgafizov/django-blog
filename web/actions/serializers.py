from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import LikeDislike
from main.serializers import UserSerializer
from .choices import LikeObjChoices, LikeStatus
User = get_user_model()


class LikeDislikeSerializer(serializers.Serializer):
    model = serializers.ChoiceField(choices=LikeObjChoices.choices)
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    object_id = serializers.IntegerField()

    def save(self):
        # user = self.context['request'].user
        print(self.validated_data)
