from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LikeDislikeView, FollowerView, UserActionView, UserFollowView

app_name = 'actions'

router = DefaultRouter()
# router.register('actions', LikeDislikeViewSet, basename='like_dislike')


urlpatterns = [
    path('actions/', LikeDislikeView.as_view(), name='like_dislike'),
    path('follow/', FollowerView.as_view(), name='follow'),
    path('user-action/', UserActionView.as_view(), name='user_action'),
    path('user/followers/', UserFollowView.as_view({'get': 'get_followers'}), name='user-followers'),
    path('user/following/', UserFollowView.as_view({'get': 'get_following'}), name='user-following'),
]

urlpatterns += router.urls
