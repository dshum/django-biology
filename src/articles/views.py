from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from .forms import UploadImageForm
from .services import *


# @cache_page(60 * 5)
# @vary_on_cookie
def index(request):
    context = {
        'main_categories': get_main_categories(),
    }
    return render(request, 'articles/index.html', context)


@login_required
def profile(request):
    page_number = request.GET.get('page')
    articles_page_obj = get_user_articles_paginator(request.user, page_number)
    context = {
        'articles_page_obj': articles_page_obj,
    }
    return render(request, 'articles/profile.html', context)


@login_required
def images(request):
    form = UploadImageForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/images.html', context)


def upload_image_form(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save(commit=False)
        if request.user.is_authenticated:
            image.user = request.user
        image.save()
        messages.add_message(request, messages.SUCCESS, _('New image has been uploaded!'))

        form = UploadImageForm()
        response = render(request, 'articles/upload_image_form.html', {'form': form})
        response.headers['HX-Trigger'] = 'newImage'
        return response

    return render(request, 'articles/upload_image_form.html', {'form': form})


def images_list(request):
    page_number = request.GET.get('page')
    images_page_obj = get_user_images_paginator(request.user, page_number)
    context = {
        'images_page_obj': images_page_obj,
    }
    return render(request, 'articles/images_list.html', context)


def delete_image(request, id: int):
    request.user.images.filter(pk=id).delete()
    return images_list(request)


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

    images = Image.objects.all()

    context = {
        'article': article,
        'images': images,
    }
    return render(request, 'articles/edit.html', context)


def increment_views(request, slug: str):
    article = get_article_by_slug(slug)
    if not article:
        raise Http404

    if article.user.pk != request.user.pk:
        increment_article_views(article)

    return HttpResponse()
