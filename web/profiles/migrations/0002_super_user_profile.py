# Generated by Django 3.1.7 on 2021-06-10 17:15

from django.db import migrations
from django.conf import settings


def set_admin_profile(apps, schema_editor):
    user_obj = apps.get_model("main", "User")
    user_profile_obj = apps.get_model("profiles", "Profile")
    admin = user_obj.objects.get(email=settings.SUPERUSER_EMAIL)
    user_profile_obj.objects.create(user=admin)


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('main', '0002_set_superuser'),
    ]
    operations = [
        migrations.RunPython(set_admin_profile),
    ]
