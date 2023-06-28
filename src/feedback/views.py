from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext_lazy as _

from .forms import CreateMessageForm
from .models import Message
from .signals import message_received


def index(request):
    messages = Message.objects.recent()
    paginator = Paginator(messages, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feedback/index.html', {'messages_page_obj': page_obj})


def create(request):
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.user = request.user
            message.save()
            # message_received.send(sender='feedback_create_message', message=message)
            messages.add_message(request, messages.SUCCESS, _('Your message has been sent!'))
            return redirect('feedback.create')
    elif request.user.is_authenticated:
        form = CreateMessageForm(initial={
            'name': request.user.first_name + ' ' + request.user.last_name,
            'email': request.user.email,
        })
    else:
        form = CreateMessageForm()

    return render(request, 'feedback/create.html', {'form': form})
