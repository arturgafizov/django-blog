from django.contrib import admin

# Register your models here.
from actions.models import LikeDislike, Follower, UserAction


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ('vote', 'user', 'date')


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'to_user', 'date')


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'date')
