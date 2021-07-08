from rest_framework import serializers

from main.serializers import UserSerializer
from .models import Category, Article, Comment
from .services import BlogService


class ParentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'content', 'updated', 'article',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.EmailField(required=False)
    child = ParentCommentSerializer(many=True, read_only=True, source='parent_set')

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'content', 'child', 'updated', 'article', 'parent',
        )
        ref_name = "Comment_Article"

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        if not user.is_authenticated and not attrs.get('author'):
            raise serializers.ValidationError('Введите емаил')
        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            validated_data['author'] = user.email
            validated_data['user'] = user
        return Comment.objects.create(**validated_data)


class UpdateCommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    class Meta:
        model = Comment

        fields = ('id', 'content', 'updated',)

    def validate(self, attrs):
        user = self.context.get('request').user
        if not user.is_authenticated and user != self.instance.user:
            if self.context.get('request').method == 'PUT':
                raise serializers.ValidationError({'content': 'Вы не можете редактировать комментарий'})
            raise serializers.ValidationError({'content': 'Вы не можете удалить комментарий'})
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    # url = serializers.SlugField(source='get_absolute_url', allow_unicode=True)
    slug = serializers.SlugField(read_only=True, allow_unicode=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent', )


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url')
    author = UserSerializer()
    category = CategorySerializer()
    comments_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'author', 'category', 'created', 'updated', 'comments_count', 'image',
                  'likes', 'dislikes')
        read_only_fields = ('author', 'comments_count', 'url')


class FullArticleSerializer(ArticleSerializer):
    # comments = CommentSerializer(source='comment_set', many=True, data=Comment.objects.filter(parent__isnull=True))
    comments = serializers.SerializerMethodField(method_name='get_root_comments')

    def get_root_comments(self, obj):
        queryset = obj.comment_set.filter(parent__isnull=True)
        serializer = CommentSerializer(many=True, source='comment_set', instance=queryset)
        return serializer.data

    class Meta(ArticleSerializer.Meta):
        fields = ArticleSerializer.Meta.fields + ('content', 'comments',)


class CreateArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'category', 'image', 'content')

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)

    def validate_title(self, title: str):
        BlogService.is_article_slug_exist(title)
        if BlogService.is_article_slug_exist(title):
            raise serializers.ValidationError("This title already exists")
        return title
