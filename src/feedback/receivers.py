from django.dispatch import receiver

from .mails import send_feedback_message
from .models import Message
from .signals import message_received


@receiver(message_received)
def send_message(sender, message: Message, **kwargs):
    send_feedback_message(message)
