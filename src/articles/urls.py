from django.urls import path

from . import views
from .views import NotFoundView, UserArticlesView, UserImagesView, ArticleDetailView, ArticlePreviewDetailView, \
    IndexView, UserArticleListView, UserImageListView, SidebarImageListView

urlpatterns = [
    path('categories/<int:id>', views.category, name='category'),

    path('profile', views.profile, name='profile'),
    path('profile/form', views.edit_profile_form, name='profile.form'),
    path('profile/articles/delete/<int:id>/confirm', views.confirm_delete_article,
         name='delete.confirm'),
    path('profile/articles/delete/<int:id>', views.delete_article, name='delete'),
    path('profile/articles/publish/<int:id>', views.publish_article, name='publish'),
    path('profile/images/form', views.upload_image_form, name='profile.images.form'),
    path('profile/images/delete/<int:id>/confirm', views.confirm_delete_image, name='images.delete.confirm'),
    path('profile/images/delete/<int:id>', views.delete_image, name='images.delete'),

    path('articles/create', views.create, name='create'),
    path('articles/<int:id>/edit', views.edit, name='edit'),
    path('articles/create/form', views.create_article_form, name='form.create'),
    path('articles/<int:id>/form', views.edit_article_form, name='form'),
    path('articles/sidebar/images/delete/<int:id>', views.delete_sidebar_image, name='sidebar.images.delete'),
    path('articles/<int:id>/increment_views', views.increment_views, name='increment_views'),

    path('', IndexView.as_view(), name='index'),
    path('404', NotFoundView.as_view(), name='404'),
    path('profile/articles', UserArticlesView.as_view(), name='profile.articles'),
    path('profile/articles/list', UserArticleListView.as_view(), name='profile.articles.list'),
    path('profile/images', UserImagesView.as_view(), name='profile.images'),
    path('profile/images/list', UserImageListView.as_view(), name='profile.images.list'),
    path('sidebar/images/list', SidebarImageListView.as_view(), name='sidebar.images.list'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='view'),
    path('<int:pk>/preview', ArticlePreviewDetailView.as_view(), name='preview'),
]
