from rest_framework import serializers

from main.services import CeleryService
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(min_length=2, required=False)

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content', 'file')

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['name'] = user.full_name()
            validated_data['email'] = user.email

        instance = super().create(validated_data)
        CeleryService.send_email_admin_contact(instance, self.context.get('request'), **validated_data, )
        CeleryService.send_email_user_contact(**validated_data)
        return instance

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_authenticated:
            if not attrs.get('name') or not attrs.get('email'):
                raise serializers.ValidationError('Name and email required!')
        print(attrs)
        return attrs
