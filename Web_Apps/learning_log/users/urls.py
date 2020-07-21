"""Defines URL patterns for the users app."""

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Include default auth URLs:
    path('', include('django.contrib.auth.urls')),
]