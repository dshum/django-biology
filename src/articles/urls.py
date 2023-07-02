from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='articles.index'),
    path('profile', views.profile, name='articles.profile'),
    path('profile/images', views.images, name='articles.profile.images'),
    path('categories/<int:id>', views.category, name='articles.category'),
    path('articles/<str:slug>', views.view, name='articles.view'),
    path('articles/<str:slug>/edit', views.edit, name='articles.edit'),
    path('articles/<str:slug>/increment_views', views.increment_views, name='articles.increment_views'),
]
