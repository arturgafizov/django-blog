from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from main.views import TemplateAPIView
from . import views

app_name = 'auth_app'

router = DefaultRouter()

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]

urlpatterns += [
    path('sign-in/', views.LoginView.as_view(), name='api_login'),
    path('sign-up/', views.SignUpView.as_view(), name='api_sign_up'),
    path('sign-up/verify/', views.VerifyEmailView.as_view(), name='api_sign_up_verify'),
    path('password/reset/', views.PasswordResetView.as_view(), name='api_forgot_password'),
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='api_password_reset_confirm'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls

urlpatterns += [
    path('password-reset/<uidb64>/<token>/', TemplateView.as_view(template_name='auth_app/link_password_confirm.html'),
         name='password_reset_confirm'),
    path('verify-email/<key>/', TemplateView.as_view(template_name='auth_app/email_confirm.html'),
         name='account_verification'),
]

if settings.ENABLE_RENDERING:
    from . import template_views as t_views

    urlpatterns += [
        path('login/', t_views.LoginView.as_view(), name='login'),
        path('register/', t_views.SignUpView.as_view(), name='sign_up'),
        path('password-recovery/', t_views.PasswordRecoveryView.as_view(), name='password_recovery'),
        path('verify-sent/', TemplateAPIView.as_view(template_name='auth_app/verification_sent.html'),
             name='verification_sent'),
        path('password-reset-sent/', TemplateAPIView.as_view(template_name='auth_app/password_reset_sent.html'),
             name='reset_email_sent'),

    ]
