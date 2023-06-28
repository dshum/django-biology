from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'user',
        'created_at',
    )
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
