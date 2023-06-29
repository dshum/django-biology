from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from .models import Message


def send_feedback_message(message: Message):
    body = render_to_string(template_name='feedback/mails/message.html', context={'message': message})
    to = [f'{admin[0]}<{admin[1]}>' for admin in settings.ADMINS]

    email = EmailMessage(subject=_('New message'), body=body, to=to)
    email.content_subtype = 'html'
    email.send()
