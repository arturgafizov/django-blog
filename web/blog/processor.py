import random

from .models import Article, Category
from random import sample


def articles(request):
    user = request.user
    article = Article.objects.all()
    # article = article.values_list()
    # print(article)
    categories = Category.objects.all()
    print(categories)
    list_categories = [x.__str__() for x in categories]
    list_categories = sample(list_categories, 6)
    print(list_categories)
    return {'articles': Article.objects.all(), 'list_categories': list_categories, 'categories': categories}



