from django.contrib.auth.models import User

from .models import Message


class MessageMail(Mailable):
    def __init__(self, message: Message):
        super().__init__(
            subject="New message",
            to=('Denis', 'denis-shumeev@yandex.ru'),
            template="feedback/mails/message.html",
            scope={"message": message, 'logo': 'cat'}
        )
