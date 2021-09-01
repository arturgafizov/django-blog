# Generated by Django 3.1.7 on 2021-08-22 09:19

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.jpeg', null=True, upload_to=profiles.models.avatar_upload_patch),
        ),
    ]
