from django.conf import settings
from django.dispatch import receiver

from .mails import MessageMail
from .models import Message
from .signals import message_received


@receiver(message_received)
def send_message_email(sender, message: Message, **kwargs):
    Mailer(MessageMail(message)) \
        .attach('mainecoon.jpg', 'cat') \
        .send()
