from django.urls import path

from . views import ProfileRetrieveView, UploadAvatarView, ProfileViewSet

app_name = 'profiles'

urlpatterns = [
    path('', ProfileRetrieveView.as_view(), name='profile_detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),
    path('profile/change-password/', ProfileViewSet.as_view({'post': 'change_password'}), name='change_password')
]
