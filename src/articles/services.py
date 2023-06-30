from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import F

from .models import Category, Article


def get_main_categories():
    return (Category.objects.filter(parent_category=None)
            .prefetch_related('sub_categories')
            .prefetch_related('sub_categories__articles')
            .order_by('order'))


def get_category_by_id(id: int):
    return Category.objects.get(pk=id)


def get_category_breadcrumbs(category: Category):
    categories = []
    parent = category.parent_category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]


def get_first_article_in_category(category_id: int):
    return Article.objects.filter(category_id=category_id).first()


def get_first_sub_category(category_id: int):
    return Category.objects.filter(parent_category_id=category_id).first()


def get_article_by_slug(slug: str):
    return Article.objects.get(slug=slug)


def get_article_breadcrumbs(article: Article):
    categories = []
    parent = article.category
    while parent:
        categories.append(parent)
        parent = parent.parent_category
    return categories[::-1]


def get_user_articles_paginator(user: User, page_number: int = 1, page_size: int = 10):
    articles = Article.objects.filter(user_id=user.pk).order_by('-created_at')
    paginator = Paginator(articles, page_size)
    return paginator.get_page(page_number)


def increment_article_views(article: Article):
    Article.objects.filter(pk=article.pk).update(views=F('views') + 1)
