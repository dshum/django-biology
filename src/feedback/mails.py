from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from sentry_sdk import capture_exception

from .models import Message


def send_feedback_message(message: Message):
    body = render_to_string(template_name='feedback/mails/message.html', context={'message': message})
    to = ['{}<{}>'.format(*admin) for admin in settings.ADMINS]

    email_message = EmailMessage(subject=_('New message'), body=body, to=to)
    if message.email:
        email_message.reply_to.append(message.email)
    email_message.content_subtype = 'html'

    try:
        email_message.send()
    except Exception as e:
        capture_exception(e)

