from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Message


class CreateMessageForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), required=True, max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label=_('Email (optional)'), required=False,
                             help_text=_('We will not give your email to anyone.'),
                             widget=forms.EmailInput(attrs={'class': 'input'}))
    message = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(attrs={'class': 'textarea'}))

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
