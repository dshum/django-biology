from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import url
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import UploadImageForm, EditArticleForm, EditProfileForm
from .services import *


def index(request):
    context = {
        'main_categories': get_main_categories(),
    }
    return render(request, 'articles/index.html', context)


def not_found(request):
    return render(request, '404.html')


@login_required
def profile(request):
    form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'articles/profile/index.html', context)


@login_required
def edit_profile_form(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, _('Your profile has been updated!'))

    context = {
        'form': form,
    }
    return render(request, 'articles/htmx/edit_profile_form.html', context)


@login_required
def user_articles(request):
    return render(request, 'articles/profile/articles.html')


@login_required
def user_images(request):
    return render(request, 'articles/profile/images.html')


@login_required
def articles_list(request):
    search = request.GET.get('search')
    page_number = request.GET.get('page')
    articles_page_obj = get_user_articles_paginator(request.user, search, page_number)
    context = {
        'articles_page_obj': articles_page_obj,
    }
    return render(request, 'articles/htmx/articles_list.html', context)


@login_required
def confirm_delete_article(request, id: int):
    article = get_object_or_404(Article, pk=id)

    context = {
        'article': article,
    }
    return render(request, 'articles/htmx/confirm_delete_article.html', context)


@login_required
def delete_article(request, id: int):
    request.user.articles.filter(pk=id).delete()
    return articles_list(request)


@login_required
def publish_article(request, id: int):
    article = get_object_or_404(Article, pk=id)
    publish = int(request.GET.get('publish'))
    article.publish = publish
    article.save()
    return articles_list(request)


@login_required
def upload_image_form(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            if request.user.is_authenticated:
                image.user = request.user
            image.save()
            messages.add_message(request, messages.SUCCESS, _('New image has been uploaded!'))

            form = UploadImageForm()
            response = render(request, 'articles/htmx/upload_image_form.html', {'form': form})
            response.headers['HX-Trigger'] = 'imageAdded'
            return response
    else:
        form = UploadImageForm()

    return render(request, 'articles/htmx/upload_image_form.html', {'form': form})


@login_required
def images_list(request):
    search = request.GET.get('search')
    page_number = request.GET.get('page')
    images_page_obj = get_user_images_paginator(request.user, search, page_number)
    context = {
        'images_page_obj': images_page_obj,
    }
    return render(request, 'articles/htmx/images_list.html', context)


@login_required
def confirm_delete_image(request, id: int):
    image = get_object_or_404(Image, pk=id)

    mode = request.GET.get('mode')
    delete_url = 'articles.sidebar.images.delete' if mode == 'sidebar' else 'articles.images.delete'
    context = {
        'image': image,
        'delete_url': delete_url,
    }
    return render(request, 'articles/htmx/confirm_delete_image.html', context)


@login_required
def delete_image(request, id: int):
    request.user.images.filter(pk=id).delete()
    return images_list(request)


@login_required
def sidebar_images_list(request):
    search = request.GET.get('search')
    page_number = request.GET.get('page')
    images_page_obj = get_sidebar_images_paginator(search, page_number)
    context = {
        'images_page_obj': images_page_obj,
    }
    return render(request, 'articles/htmx/sidebar_images_list.html', context)


@login_required
def delete_sidebar_image(request, id: int):
    request.user.images.filter(pk=id).delete()
    return sidebar_images_list(request)


def category(request, id: int):
    category = get_category_by_id(id)
    if not category:
        return render('articles/404.html')

    article = get_first_article_in_category(category)
    if article:
        return redirect('articles.view', slug=article.slug)

    sub_category = get_first_sub_category(category)
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
    if not article or not article.publish:
        return render(request, 'articles/404.html')

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


@login_required
def preview(request, id: int):
    article = get_article_by_id(id)
    if not article or (not article.publish and article.user != request.user):
        return render(request, 'articles/404.html')

    main_categories = get_main_categories()
    breadcrumbs = get_article_breadcrumbs(article)
    current_main_category = breadcrumbs[0]

    context = {
        'article': article,
        'breadcrumbs': breadcrumbs,
        'main_categories': main_categories,
        'current_main_category': current_main_category,
    }
    return render(request, 'articles/preview.html', context)


def increment_views(request, id: int):
    article = get_object_or_404(Article, pk=id)

    if article.user.pk != request.user.pk:
        increment_article_views(article)

    return HttpResponse()


@login_required
def create(request):
    form = EditArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def edit(request, id: int):
    article = get_article_by_id(id)
    if not article:
        return render(request, 'articles/404.html')
    elif article.user.pk != request.user.pk:
        return redirect('articles.view', slug=article.slug)

    form = EditArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


@login_required
def create_article_form(request):
    form = EditArticleForm(request.POST)
    context = {
        'form': form,
    }
    response = render(request, 'articles/htmx/create_article_form.html', context)

    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        article.reading_time_minutes = 0
        article.save()

        messages.add_message(request, messages.SUCCESS, _('New article has been created!'))
        response.headers['HX-Redirect'] = reverse('articles.view.preview', kwargs={'id': article.pk})

    return response


@login_required
def edit_article_form(request, id: int):
    article = get_object_or_404(Article, id)

    form = EditArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/htmx/edit_article_form.html', context)
