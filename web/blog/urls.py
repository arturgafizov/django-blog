from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from main.views import TemplateAPIView
from . import views

app_name = 'blog'

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('posts', views.ArticleViewSet, basename='post')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('new-article/', views.NewArticleView.as_view(template_name='blog/post_create.html'), name='new-post')
]

urlpatterns += router.urls
