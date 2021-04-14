from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from rest_framework.reverse import reverse_lazy
from .choices import ArticleStatus

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='parent_set', blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

    def get_absolute_url(self):
        return reverse_lazy('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='category_set')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    hidden = models.SmallIntegerField(choices=ArticleStatus.choices, default=ArticleStatus.ACTIVE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True, default='no_image.jpeg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles_set')
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=200)

    objects = models.Manager()

    def get_category(self):
        return ",".join([str(p.name) for p in self.category.all()])

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)

    def get_absolute_url(self):
        return reverse_lazy('article-detail', kwargs={'slug': self.slug})

    def article_image(self):
        url = self.image.url if self.image else ''
        return mark_safe('<img src="%s" width="150" height="150" />' % (url, ))

    article_image.short_description = 'Image'


class Comment(models.Model):
    author = models.EmailField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_set')
    content = models.TextField(max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_set', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_comment', null=True, blank=True)
    objects = models.Manager

    def __str__(self) -> str:
        return f'{self.id}, {self.author}, {self.content}'
