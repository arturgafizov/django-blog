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
    FOLLOW = ('Follow', 'Follow')
    UNFOLLOW = ('Unfollow', 'Unfollow')


class UserActionChoices(IntegerChoices):
    FOLLOW_TO = (1, 'User {subscriber} follow to {to_user}')
    UNFOLLOW_TO = (2, 'User {subscriber} follow to {to_user}')
    LIKE_ARTICLE = (3, 'User {user} liked {article}')
    DISLIKE_ARTICLE = (4, 'User {user} disliked {article}')
    LIKE_COMMENT = (5, 'User {user} liked {comment}')
    DISLIKE_COMMENT = (6, 'User {user} disliked {comment}')
