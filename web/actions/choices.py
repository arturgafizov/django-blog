from django.db.models import IntegerChoices, TextChoices
from django.utils.translation import gettext_lazy as _


class LikeStatus(IntegerChoices):
    LIKE = (1, 'like')
    DISLIKE = (-1, 'dislike')


class LikeObjChoices(TextChoices):
    ARTICLE = ('article', _('Article'))
    COMMENT = ('comment', _('Comment'))


class LikeIconStatus(TextChoices):
    LIKED = ('liked', 'Liked')
    DISLIKED = ('disliked', 'Disliked')
    EMPTY = ('empty', 'Empty')


class FollowStatus(TextChoices):
    FOLLOW = ('follow', 'Follow')
    UNFOLLOW = ('unfollow', 'Unfollow')
