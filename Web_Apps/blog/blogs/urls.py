"""This module defines the URLs for blogs-app."""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('home', views.home, name='home')
]