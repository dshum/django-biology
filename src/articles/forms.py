from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Image


class UploadImageForm(forms.ModelForm):
    title = forms.CharField(label=_('Title'), required=True, max_length=255,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    image = forms.ImageField(label=_('Image'), required=True,
                             widget=forms.FileInput(attrs={'class': 'file-input'}))

    class Meta:
        model = Image
        fields = ('title', 'image')
