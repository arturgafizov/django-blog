from django.contrib import admin

from .models import Category, Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'get_category', 'article_image', )
    search_fields = ['category__name', ]
    exclude = ('slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    search_fields = ['parent', ]
    exclude = ('slug',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', )
