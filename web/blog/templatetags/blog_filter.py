from django import template
from datetime import datetime
from django.conf import settings
register = template.Library()


@register.simple_tag
def phonenumber():
    return "+7850554142"


@register.filter(name='timefilter')
def timefilter(date):
    print(date)
    time = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    print(time)
    return time


@register.simple_tag
def github_url():
    return settings.GITHUB_ACCOUNT



