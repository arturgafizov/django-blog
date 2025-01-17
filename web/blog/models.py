from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse_lazy
from django.utils.safestring import mark_safe
from . import managers
from .choices import ArticleStatus, CategoryLevel
from actions.models import LikeDislike
from actions.choices import LikeStatus

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='parent_set', blank=True, null=True)
    promoted = models.PositiveSmallIntegerField(choices=CategoryLevel.choices, default=CategoryLevel.BEGIN)
    objects = models.Manager()

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def save(self, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    # def get_absolute_url(self):
    #     return reverse_lazy('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article_set')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=ArticleStatus.choices, default=ArticleStatus.INACTIVE)
    image = models.ImageField(upload_to='articles/', blank=True, default='no-image-available.jpg')
    objects = models.Manager()
    votes = GenericRelation(LikeDislike, related_query_name='articles')

    def likes(self) -> int:
        return self.votes.filter(vote=LikeStatus.LIKE).count()

    def dislikes(self) -> int:
        return self.votes.filter(vote=LikeStatus.DISLIKE).count()

    @property
    def short_title(self):
        return self.title[:30]

    def __str__(self):
        # return '{id}' .format(id=self.id)
        return '{id} - {title} - {author}'.format(id=self.id, title=self.short_title, author=self.author)

    @staticmethod
    def get_slug(title):
        return slugify(title, allow_unicode=True)

    def save(self, **kwargs):
        self.slug = self.get_slug(self.title)
        return super().save(**kwargs)

    def get_absolute_url(self):
        url = 'blog:post-detail'
        return reverse_lazy(url, kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('-updated', '-created', 'id')

    def article_image(self):
        url = self.image.url if self.image else ''
        return mark_safe('<img src="%s" width="150" height="150" />' % (url, ))

    article_image.short_description = 'Image'


class Comment(models.Model):
    author = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment_set', blank=True)
    content = models.TextField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_set', blank=True, null=True)
    objects = models.Manager()
    votes = GenericRelation(LikeDislike, related_query_name='comments')

    def likes(self) -> int:
        return self.votes.filter(vote=LikeStatus.LIKE).count()

    def dislikes(self) -> int:
        return self.votes.filter(vote=LikeStatus.DISLIKE).count()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-created', )

    def __str__(self) -> str:
        return f'{self.id}, {self.author}, {self.content}'

    def save(self, **kwargs):
        return super().save(**kwargs)
