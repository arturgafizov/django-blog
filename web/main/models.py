from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework.reverse import reverse_lazy
from .managers import UserManager
from urllib.parse import urljoin


class User(AbstractUser):

    username = None
    email = models.EmailField(_('Email address'), unique=True)
    following = models.ManyToManyField('self', related_name='followers', through='actions.Follower', symmetrical=False,
                                       blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('profiles:profile-detail', args=[self.id])

    @cached_property
    def get_profile_url(self):
        return urljoin(settings.BACKEND_SITE, str(self.get_absolute_url()))

    @cached_property
    def get_avatar_url(self):
        return urljoin(settings.BACKEND_SITE, str(self.profiles_set.avatar.url))

    def full_name(self):
        return super().get_full_name()

    def email_verified(self):
        return self.emailaddress_set.get(primary=True).verified
    email_verified.boolean = True

    def followers_count(self) -> int:
        return self.followers.count()

    def following_count(self) -> int:
        return self.following.count()
