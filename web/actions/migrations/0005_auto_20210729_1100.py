# Generated by Django 3.1.7 on 2021-07-29 11:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0004_action'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Action',
            new_name='UserAction',
        ),
    ]
