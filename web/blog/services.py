from django.conf import settings
from django.db.models import Count

from .choices import ArticleStatus
from .models import Category, Article, Comment
from main.decorators import except_shell


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

    @staticmethod
    @except_shell((Article.DoesNotExist, ))
    def get_article(article_id: int):
        return Article.objects.get(id=article_id)

    @staticmethod
    @except_shell((Comment.DoesNotExist, ))
    def get_comment(comment_id: int):
        return Comment.objects.get(id=comment_id)
