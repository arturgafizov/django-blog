from django.urls import path

from . views import ProfileRetrieveView, UploadAvatarView


urlpatterns = [
    path('', ProfileRetrieveView.as_view(), name='profile-detail'),
    path('avatar/', UploadAvatarView.as_view(), name='avatar_upload'),

]
