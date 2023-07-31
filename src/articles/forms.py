from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _, gettext

from .models import Image, Article, Category
from .services import get_grouped_categories


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=_('First name'), required=True, max_length=150,
                                 widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(label=_('Last name'), required=True, max_length=150,
                                widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label=_('Email'), required=True, max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditArticleForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), required=True, max_length=255,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    slug = forms.SlugField(label=_('Slug'), required=True, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    category = forms.IntegerField(label=_('Category'), required=True,
                                  widget=forms.Select(choices=get_grouped_categories()))
    level = forms.ChoiceField(label=_('Level'), required=True, choices=Article.Level.choices,
                              widget=forms.RadioSelect())
    content = forms.CharField(label=_('Text'), required=True,
                              widget=forms.Textarea(attrs={
                                  'class': 'textarea',
                                  'rows': 25,
                              }))
    publish = forms.BooleanField(label=_('Publish'), required=False,
                                 help_text=_('The article will be visible to all users.'))

    class Meta:
        model = Article
        fields = ('title', 'slug', 'category', 'level', 'content', 'publish')

    def clean_category(self):
        category_id = self.cleaned_data.get('category')
        return Category.objects.get(pk=category_id)


class UploadImageForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), required=True, max_length=255,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    image = forms.ImageField(label=_('Image'), required=True,
                             widget=forms.FileInput(attrs={'class': 'file-input'}))

    class Meta:
        model = Image
        fields = ('title', 'image')
