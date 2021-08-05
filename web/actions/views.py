import logging
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from . import services
from .models import LikeDislike
from .serializers import LikeDislikeSerializer, FollowerSerializer, ActionSerializer
from profiles.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)


class LikeDislikeView(GenericAPIView):
    serializer_class = LikeDislikeSerializer

    def get_queryset(self):
        return LikeDislike.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)


class FollowerView(GenericAPIView):
    serializer_class = FollowerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)


class UserActionView(GenericAPIView):
    serializer_class = ActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
