from django.urls import path
from rest_framework.routers import DefaultRouter

from . views import ProfileRetrieveView, UploadAvatarView, ProfileViewSet, ProfileDetailViewSet

app_name = 'profiles'

router = DefaultRouter()
router.register('profile', ProfileDetailViewSet, basename='profile')


urlpatterns = [
    path('', ProfileRetrieveView.as_view(), name='profile_detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),
    path('profile/change-password/', ProfileViewSet.as_view({'post': 'change_password'}), name='change_password')
]

urlpatterns += router.urls
