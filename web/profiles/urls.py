from django.urls import path
from rest_framework.routers import DefaultRouter

from . views import ProfileRetrieveView, UploadAvatarView, ProfileViewSet, ProfileDetailViewSet, ChatView, \
    ShortUserInfoView, ListShortUserInfoView

app_name = 'profiles'

router = DefaultRouter()
router.register('profile', ProfileDetailViewSet, basename='profile')


urlpatterns = [
    path('', ProfileRetrieveView.as_view(), name='profile_detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),
    path('profile/change-password/', ProfileViewSet.as_view({'post': 'change_password'}), name='change_password'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('profile/short/<pk>/', ShortUserInfoView.as_view(), name='short_user_info'),
    path('profile/short/', ListShortUserInfoView.as_view(), name='list_short_user_info'),
]

urlpatterns += router.urls
