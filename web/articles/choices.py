from django.db.models import IntegerChoices


class ArticleStatus(IntegerChoices):
    ACTIVE = (1, 'Active')
    INACTIVE = (0, 'Inactive')
