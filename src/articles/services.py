from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import F, Q

from .models import Category, Article, Image


def get_main_categories():
    return (Category.objects.category(None)
            .prefetch_related('sub_categories')
            .prefetch_related('sub_categories__articles'))


def get_grouped_categories():
    categories = []
    main_categories = (Category.objects.category(None)
                       .prefetch_related('sub_categories'))
    for main_category in main_categories:
        if main_category.sub_categories.count():
            sub_categories = [(sub_category.id, sub_category.title) for sub_category in
                              main_category.sub_categories.all()]
            categories.append((main_category.title, sub_categories))
    return categories


def get_category_breadcrumbs(category: Category):
    categories = []
    parent = category.parent_category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]


def get_first_article_in_category(category: Category):
    return Article.objects.category(category).published().first()


def get_first_sub_category(category: Category):
    return Category.objects.category(category).first()


def get_article_breadcrumbs(article: Article):
    categories = []
    parent = article.category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]
