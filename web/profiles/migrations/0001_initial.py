# Generated by Django 3.1.7 on 2021-06-09 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('location', models.CharField(max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=profiles.models.avatar_upload_patch)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
