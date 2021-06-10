import logging
from main.views import TemplateAPIView
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.viewsets import ModelViewSet
from main.pagination import DefaultPagination
from rest_framework.status import HTTP_201_CREATED

from .services import BlogService
from . import serializers
from .filters import ArticleFilter

from .models import Comment, Category, Article

logger = logging.getLogger(__name__)


class ViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    pagination_class = DefaultPagination


class CategoryViewSet(ViewSet):
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return BlogService.category_queryset()
        # return Category.objects.all()


class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2
    results_field = 'results'
    max_page_size = 100
    page_size_query_param = 'page_size'

    def render(self, data, *args, **kwargs):
        if not isinstance(data, list):
            data = data.get(self.results_field, [])
        return super(ArticlePageNumberPagination, self).render(data, *args, **kwargs)

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data.update(self.get_html_context())
        return response


class ArticleViewSet(ViewSet):
    filterset_class = ArticleFilter
    pagination_class = ArticlePageNumberPagination

    def get_template_name(self):
        if self.action == 'list':
            return 'blog/post_list.html'
        elif self.action == 'retrieve':
            return 'blog/post_detail.html'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ArticleSerializer
        return serializers.FullArticleSerializer

    def get_queryset(self):
        return BlogService.get_active_articles()

    def list(self, request, **kwargs):
        response = super().list(request, **kwargs)
        response.template_name = self.get_template_name()
        return response

    def retrieve(self, request, **kwargs):
        response = super().retrieve(request, **kwargs)
        response.template_name = self.get_template_name()
        return response


class CommentViewSet(ModelViewSet):
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.UpdateCommentSerializer
        if self.action == 'destroy':
            return serializers.UpdateCommentSerializer
        return serializers.CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewArticleView(TemplateAPIView):

    def get(self, request, *args, **kwargs):
        serializer = serializers.CategorySerializer(self.get_queryset(), many=True)
        data = {
            'categories': serializer.data
        }
        return Response(data)

    def get_queryset(self):
        return Category.objects.all()
