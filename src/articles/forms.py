from django import forms
from django.utils.translation import gettext_lazy as _, gettext

from .models import Image, Article


class EditArticleForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), required=True, max_length=255,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    slug = forms.SlugField(label=_('Slug'), required=True, max_length=255,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    level = forms.ChoiceField(label=_('Level'), required=True, choices=Article.Level.choices,
                              widget=forms.RadioSelect())
    content = forms.CharField(label=_('Text'), required=True,
                              widget=forms.Textarea(attrs={
                                  'class': 'textarea',
                                  'rows': 25,
                              }))
    publish = forms.BooleanField(label=_('Publish'), required=False)

    class Meta:
        model = Article
        fields = ('title', 'slug', 'level', 'content', 'publish')


class UploadImageForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), required=True, max_length=255,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    image = forms.ImageField(label=_('Image'), required=True,
                             widget=forms.FileInput(attrs={'class': 'file-input'}))

    class Meta:
        model = Image
        fields = ('title', 'image')
