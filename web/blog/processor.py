import random

from .models import Article, Category
from random import sample


def categories(request):
    categories = Category.objects.filter(promoted=0)[:5]
    # print(categories)
    # list_categories = [x.__str__() for x in categories]
    # list_categories = sample(list_categories, 7)
    # print(list_categories)
    return {'categories': categories}
