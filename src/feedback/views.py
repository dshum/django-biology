from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from .forms import CreateMessageForm
from .models import Message
from .signals import message_received


def create(request):
    if request.user.is_authenticated:
        form = CreateMessageForm(initial={
            'name': request.user.first_name + ' ' + request.user.last_name,
            'email': request.user.email,
        })
    else:
        form = CreateMessageForm()

    return render(request, 'feedback/create.html', {'form': form})


def form(request):
    form = CreateMessageForm(request.POST)

    if form.is_valid():
        message = form.save(commit=False)
        if request.user.is_authenticated:
            message.user = request.user
        message.save()
        message_received.send(sender='feedback_views_create', message=message)
        messages.success(request, _('Your message has been sent!'))

        if request.user.is_authenticated:
            form = CreateMessageForm(initial={
                'name': request.user.first_name + ' ' + request.user.last_name,
                'email': request.user.email,
            })
        else:
            form = CreateMessageForm()

    return render(request, 'feedback/form.html', {'form': form})
