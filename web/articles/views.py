from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from .models import Article, Category, Comment
from . import serializers


class ArticleViewSet(ModelViewSet):
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ShortArticleSerializer
        return serializers.ArticleSerializer

    def get_queryset(self):
        # user = self.request.user
        # return Article.objects.filter(author=user)
        return Article.objects.all().annotate(comment_count=Count('comment_set'))


class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.all()


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
