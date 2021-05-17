from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(min_length=2, required=True)

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content', 'file')

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['name'] = user.full_name()
            validated_data['email'] = user.email
        return super().create(validated_data)
