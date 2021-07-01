from django.db.models import IntegerChoices, TextChoices


class LikeStatus(IntegerChoices):
    LIKE = (1, 'like')
    DISLIKE = (-1, 'dislike')


class LikeObjChoices(TextChoices):
    ARTICLE = ('article', 'Article')
    COMMENT = ('comment', 'Comment')
