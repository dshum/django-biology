from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .services import (get_main_categories, get_first_article_in_category, get_first_sub_category, get_article_by_slug,
                       get_article_breadcrumbs, get_category_by_id, get_category_breadcrumbs)


# @cache_page(60 * 5)
# @vary_on_cookie
def index(request):
    context = {
        'main_categories': get_main_categories(),
    }
    return render(request, 'articles/index.html', context)


# @cache_page(60 * 5)
# @vary_on_cookie
def category(request, id: int):
    category = get_category_by_id(id)
    if not category:
        raise Http404

    article = get_first_article_in_category(id)
    if article:
        return redirect('articles.view', slug=article.slug)

    sub_category = get_first_sub_category(id)
    if sub_category:
        return redirect('articles.category', id=sub_category.id)

    main_categories = get_main_categories()
    breadcrumbs = get_category_breadcrumbs(category)
    current_main_category = breadcrumbs[0]

    context = {
        'category': category,
        'breadcrumbs': breadcrumbs,
        'main_categories': main_categories,
        'current_main_category': current_main_category,
    }
    return render(request, 'articles/category.html', context)


# @cache_page(60 * 5)
# @vary_on_cookie
def view(request, slug: str):
    article = get_article_by_slug(slug)
    if not article:
        raise Http404

    main_categories = get_main_categories()
    breadcrumbs = get_article_breadcrumbs(article)
    current_main_category = breadcrumbs[0]

    context = {
        'article': article,
        'breadcrumbs': breadcrumbs,
        'main_categories': main_categories,
        'current_main_category': current_main_category,
    }
    return render(request, 'articles/view.html', context)


def edit(request, slug: str):
    article = get_article_by_slug(slug)
    if not article:
        raise Http404

    if article.user.pk != request.user.pk:
        return redirect('articles.view', slug=article.slug)

    context = {
        'article': article,
        'breadcrumbs': get_article_breadcrumbs(article),
    }
    return render(request, 'articles/edit.html', context)
