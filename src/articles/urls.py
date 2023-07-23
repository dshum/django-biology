from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='articles.index'),
    path('profile', views.profile, name='articles.profile'),
    path('profile/articles', views.user_articles, name='articles.profile.articles'),
    path('profile/images', views.user_images, name='articles.profile.images'),
    path('profile/images/form', views.upload_image_form, name='articles.profile.images.form'),
    path('profile/images/list', views.images_list, name='articles.profile.images.list'),
    path('profile/images/delete/<int:id>', views.delete_image, name='articles.images.delete'),
    path('categories/<int:id>', views.category, name='articles.category'),
    path('articles/create', views.create, name='articles.create'),
    path('articles/<str:slug>', views.view, name='articles.view'),
    path('articles/<int:id>/preview', views.preview, name='articles.view.preview'),
    path('articles/<int:id>/edit', views.edit, name='articles.edit'),
    path('articles/create/form', views.article_create_form, name='articles.form.create'),
    path('articles/<int:id>/form', views.article_form, name='articles.form'),
    path('articles/sidebar/images/list', views.sidebar_images_list, name='articles.sidebar.images.list'),
    path('articles/<int:id>/increment_views', views.increment_views, name='articles.increment_views'),
    path('404', views.not_found),
]
