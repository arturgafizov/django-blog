from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.serializers import UserSerializer, ShortUserInfoSerializer
from .serializers import UserJwtSerializer, UsersIdSerializer
from .services import UserService

User = get_user_model()


class TemplateAPIView(APIView):
    permission_classes = (AllowAny,)
    template_name = ''

    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    def get(self, request, *args, **kwargs):
        return Response()


class UserView(GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request):
        """Current user view

            Using this construction you can load related fields (select_related and prefetch_related) in queryset
        """

        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)


class IndexView(TemplateAPIView):
    template_name = 'index.html'


class UserJwtView(GenericAPIView):
    serializer_class = UserJwtSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class UsersIdView(GenericAPIView):
    serializer_class = UsersIdSerializer

    def post(self, request):
        # print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data['users_id'])
        # qs = User.objects.filter(id__in=serializer.data['users_id'])
        qs = UserService.get_users(serializer.data['users_id'])
        data = ShortUserInfoSerializer(qs, many=True, context=self.get_serializer_context()).data
        print(data)
        return Response(data)
