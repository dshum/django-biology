from django.urls import path

from . import views

urlpatterns = [
    path('', views.create, name='feedback.create'),
    path('form', views.form, name='feedback.form'),
]
