from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        null=True,
        blank=True,
        default=None,
        related_name='messages'
    )

    objects = models.Manager()

    def __str__(self) -> str:
        return f'#{self.pk} {self.message}'
