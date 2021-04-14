from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')
router.register('category', views.CategoryViewSet, basename='category')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = [

]

urlpatterns += router.urls
