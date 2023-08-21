from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import url
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, DetailView, ListView, FormView, UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin

from .forms import UploadImageForm, EditArticleForm, EditProfileForm
from .services import *


class NotFound(TemplateView):
    template_name = '404.html'


class Index(ListView):
    model = Category
    template_name = 'articles/index.html'
    ordering = 'order'

    def get_queryset(self):
        return get_main_categories()


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'articles/profile/index.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'articles/htmx/edit_profile_form.html'
    success_url = reverse_lazy('articles:profile.form')

    def get_object(self, **kwargs):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Your profile has been updated!'))
        return super().form_valid(form)


class UserArticles(LoginRequiredMixin, TemplateView):
    template_name = 'articles/profile/articles.html'


class UserArticleList(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/htmx/article_list.html'
    ordering = '-created_at'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search')
        return (super().get_queryset()
                .user(self.request.user)
                .search(search))


class CategoryMixin(ContextMixin):
    model = Category

    def get_context_data(self, object: Category, **kwargs):
        context = super().get_context_data(**kwargs)
        breadcrumbs = get_category_breadcrumbs(object)
        current_main_category = breadcrumbs[0]
        context.update({
            'main_categories': get_main_categories(),
            'breadcrumbs': breadcrumbs,
            'current_main_category': breadcrumbs[0],
        })
        return context


class ArticleContextMixin(ContextMixin):
    def get_context_data(self, object: Article, **kwargs):
        context = super().get_context_data(**kwargs)
        breadcrumbs = get_article_breadcrumbs(object)
        context.update({
            'main_categories': get_main_categories(),
            'breadcrumbs': breadcrumbs,
            'current_main_category': breadcrumbs[0],
        })
        return context


class ArticleDetailViewMixin(DetailView):
    model = Article

    def get(self, request, **kwargs):
        try:
            article = self.get_object()
        except Http404:
            return render(request, 'articles/404.html')

        return super().get(request, **kwargs)


class Category(CategoryMixin, DetailView):
    template_name = 'articles/category.html'

    def get(self, request, **kwargs):
        try:
            category = self.get_object()
        except Http404:
            return render(request, '404.html')

        article = get_first_article_in_category(category)
        if article:
            return redirect('articles:view', slug=article.slug)

        sub_category = get_first_sub_category(category)
        if sub_category:
            return redirect('articles:category', pk=sub_category.id)

        return super().get(request, **kwargs)


class ArticleView(ArticleContextMixin, ArticleDetailViewMixin):
    template_name = 'articles/view.html'

    def get_queryset(self):
        return super().get_queryset().published()


class ArticlePreview(LoginRequiredMixin, ArticleContextMixin, ArticleDetailViewMixin):
    template_name = 'articles/preview.html'


class ArticleCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'articles/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form': EditArticleForm()})
        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'articles/htmx/create_article_form.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user = self.request.user
        article.reading_time_minutes = 0
        article.save()

        messages.success(self.request, _('New article has been created!'))
        response = HttpResponse()
        response.headers['HX-Redirect'] = reverse_lazy('articles:preview', args=(article.pk,))
        return response


class ArticleEditView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form': EditArticleForm(instance=self.get_object())})
        return context


class ArticleEdit(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'articles/htmx/edit_article_form.html'

    def get_success_url(self):
        return reverse_lazy('articles:edit.form', kwargs=({'pk': self.object.pk}))


class ArticlePublish(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['publish']
    success_url = reverse_lazy('articles:profile.articles.list')

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        publish = int(request.GET.get('publish'))
        request.POST.update({'publish': publish})
        return super().post(request, **kwargs)


class ArticleConfirmDelete(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/htmx/confirm_delete_article.html'


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:profile.articles.list')


class UserImages(LoginRequiredMixin, TemplateView):
    template_name = 'articles/profile/images.html'


class UserImageList(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'articles/htmx/image_list.html'
    ordering = '-created_at'
    paginate_by = 8

    def get_queryset(self):
        search = self.request.GET.get('search')
        return (super().get_queryset()
                .user(self.request.user)
                .search(search))


class SidebarImageList(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'articles/htmx/sidebar_image_list.html'
    ordering = '-created_at'
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get('search')
        return super().get_queryset().search(search)


class ImageUpload(LoginRequiredMixin, CreateView):
    model = Image
    form_class = UploadImageForm
    template_name = 'articles/htmx/upload_image_form.html'
    success_url = reverse_lazy('articles:profile.images.form')

    def form_valid(self, form):
        image = form.save(commit=False)
        image.user = self.request.user
        image.save()
        if self.request.htmx:
            response = self.render_to_response({'form': UploadImageForm()})
            response['HX-Trigger'] = 'imageAdded'
            return response
        return super().form_valid(form)


class ImageConfirmDelete(LoginRequiredMixin, DetailView):
    model = Image
    template_name = 'articles/htmx/confirm_delete_image.html'

    def get_context_data(self, object: Image, **kwargs):
        mode = self.request.GET.get('mode')
        delete_url = 'articles:sidebar.images.delete' if mode == 'sidebar' else 'articles:images.delete'
        context = super(ImageConfirmDelete, self).get_context_data(**kwargs)
        context.update({
            'delete_url': delete_url,
        })
        return context


class ImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('articles:profile.images.list')


class SidebarImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('articles:sidebar.images.list')


class IncrementViews(DetailView):
    model = Article

    def render_to_response(self, context, **response_kwargs):
        object = self.get_object()
        if object.user.pk != self.request.user.pk:
            Article.objects.filter(pk=object.pk).update(views=F('views') + 1)
        return HttpResponse()
