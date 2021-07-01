from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.serializers import PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny

from . import serializers
from . models import Profile
from . serializers import (ProfileSerializer, UploadAvatarUserSerializer)


class UploadAvatarView(GenericAPIView):
    serializer_class = UploadAvatarUserSerializer
    # parser_classes = [FileUploadParser, ]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user).select_related('user')

    def post(self, request):
        # print(request.data)
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileRetrieveView(GenericAPIView):
    template_name = 'profile/profile_detail.html'

    def get_serializer_class(self):
        print(self.request.method)
        if self.request.method == 'PUT':
            return serializers.UpdateUserProfileSerializer
        return serializers.ProfileSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user).select_related('user')

    def get(self, request):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        print(request.data)
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileViewSet(GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'change_password':
            return PasswordChangeSerializer

    def change_password(self, request):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': _('New password has been saved')})
