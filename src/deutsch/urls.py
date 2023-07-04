from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='deutsch.index'),
    path('<str:slug>', views.wordlist, name='deutsch.wordlist'),
]
