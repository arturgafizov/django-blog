from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe

User = get_user_model()


def avatar_upload_patch(obj, filename: str):
    # print(filename.rsplit(".")[-1])
    return f"avatar_images/{obj.user_id}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_set')
    mobile = PhoneNumberField(null=True)
    location = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_upload_patch, default='default_avatar.jpeg')
    objects = models.Manager()
    website = models.CharField(null=True, max_length=200)

    def __str__(self) -> str:
        return f'{self.user} {self.id}'

    def save(self, **kwargs):
        return super().save(**kwargs)

    def old_avatar_delete(self):
        if self.avatar:
            self.avatar.delete()

    def avatar_image(self):
        url = self.avatar.url if self.avatar else ''
        return mark_safe('<img src="%s" width="150" height="150" />' % (url, ))

    avatar_image.short_description = 'Avatar'


class Address(models.Model):
    country = CountryField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_set')
    state = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
