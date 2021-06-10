from django.urls import path

from . views import ProfileRetrieveView, UploadAvatarView

app_name = 'profiles'

urlpatterns = [
    path('', ProfileRetrieveView.as_view(), name='profile_detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),

]
