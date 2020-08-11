"""This module defines the URLs for blogs-app."""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new_post, name='new_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
]