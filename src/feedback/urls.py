from django.urls import path

from .views import MessageCreateView, MessageCreate

urlpatterns = [
    path('', MessageCreateView.as_view(), name='create'),
    path('form', MessageCreate.as_view(), name='form'),
]
