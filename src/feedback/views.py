from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, CreateView

from .forms import CreateMessageForm
from .models import Message
from .signals import message_received


class MessageCreateView(TemplateView):
    template_name = 'feedback/create.html'


class MessageCreate(CreateView):
    model = Message
    form_class = CreateMessageForm
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback:form')

    def get_initial(self):
        return {
            'name': self.request.user.first_name + ' ' + self.request.user.last_name,
            'email': self.request.user.email,
        } if self.request.user.is_authenticated else None

    def form_valid(self, form):
        message = form.save(commit=False)
        if self.request.user.is_authenticated:
            message.user = self.request.user
        message.save()
        message_received.send(sender='feedback_views_create', message=message)
        messages.success(self.request, _('Your message has been sent!'))
        return super().form_valid(form)
