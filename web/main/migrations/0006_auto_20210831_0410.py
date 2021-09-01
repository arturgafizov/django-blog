# Generated by Django 3.1.7 on 2021-08-31 04:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0009_auto_20210818_1836'),
        ('main', '0005_auto_20210830_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', through='actions.Follower', to=settings.AUTH_USER_MODEL),
        ),
    ]