from django.contrib import admin

from . models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'location', 'avatar_image', )
    search_fields = ['location', ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'user', 'city',)
    search_fields = ('city',)
