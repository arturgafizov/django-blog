from django.conf import settings
from django.db.models import Count

from .choices import ArticleStatus
from .models import Category, Article, Comment


class BlogService:

    @staticmethod
    def category_queryset():
        return Category.objects.all()

    @staticmethod
    def get_active_articles():
        return Article.objects.filter(status=ArticleStatus.ACTIVE).annotate(comments_count=Count('comment_set'))

    @staticmethod
    def is_article_slug_exist(title):
        slug = Article.get_slug(title)
        return Article.objects.filter(slug=slug).exists()
