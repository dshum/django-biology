from django.urls import path

from . import views
from .views import (Index, NotFound, Category, Profile, ProfileUpdate,
                    UserArticles, UserArticleList, ArticleView, ArticlePreview,
                    ArticleConfirmDelete, ArticleDelete, ArticlePublish,
                    ArticleCreateView, ArticleCreate, ArticleEditView, ArticleEdit,
                    UserImages, UserImageList, SidebarImageList, ImageUpload,
                    ImageConfirmDelete, ImageDelete, SidebarImageDelete,
                    IncrementViews)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('404', NotFound.as_view(), name='404'),
    path('categories/<int:pk>', Category.as_view(), name='category'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile/form', ProfileUpdate.as_view(), name='profile.form'),
    path('profile/articles', UserArticles.as_view(), name='profile.articles'),
    path('profile/articles/list', UserArticleList.as_view(), name='profile.articles.list'),
    path('articles/create', ArticleCreateView.as_view(), name='create'),
    path('articles/create/form', ArticleCreate.as_view(), name='create.form'),
    path('articles/<int:pk>/edit', ArticleEditView.as_view(), name='edit'),
    path('articles/<int:pk>/edit/form', ArticleEdit.as_view(), name='edit.form'),
    path('articles/<int:pk>/publish', ArticlePublish.as_view(), name='publish'),
    path('articles/<slug:slug>', ArticleView.as_view(), name='view'),
    path('articles/<int:pk>/preview', ArticlePreview.as_view(), name='preview'),
    path('articles/<int:pk>/delete/confirm', ArticleConfirmDelete.as_view(), name='delete.confirm'),
    path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='delete'),
    path('articles/<int:pk>/increment-views', IncrementViews.as_view(), name='increment_views'),
    path('profile/images', UserImages.as_view(), name='profile.images'),
    path('profile/images/list', UserImageList.as_view(), name='profile.images.list'),
    path('sidebar/images/list', SidebarImageList.as_view(), name='sidebar.images.list'),
    path('profile/images/form', ImageUpload.as_view(), name='profile.images.form'),
    path('images/<int:pk>/delete/confirm', ImageConfirmDelete.as_view(), name='images.delete.confirm'),
    path('images/<int:pk>/delete', ImageDelete.as_view(), name='images.delete'),
    path('sidebar/<int:pk>/delete', SidebarImageDelete.as_view(), name='sidebar.images.delete'),
]
