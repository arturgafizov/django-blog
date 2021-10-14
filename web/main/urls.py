from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView
from .views import UserView, IndexView, UserJwtView
from django.conf import settings


urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/jwt/', UserJwtView.as_view(), name='user_jwt'),
]

if settings.ENABLE_RENDERING:
    urlpatterns += [path('', IndexView.as_view(), name='index')]
else:
    urlpatterns += [path('', login_required(RedirectView.as_view(pattern_name='admin:index')))]
