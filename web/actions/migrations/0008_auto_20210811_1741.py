# Generated by Django 3.1.7 on 2021-08-11 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0007_subscribedtouser_usersubscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubscribed',
            name='to_user',
        ),
        migrations.RemoveField(
            model_name='usersubscribed',
            name='user',
        ),
        migrations.DeleteModel(
            name='SubscribedToUser',
        ),
        migrations.DeleteModel(
            name='UserSubscribed',
        ),
    ]
