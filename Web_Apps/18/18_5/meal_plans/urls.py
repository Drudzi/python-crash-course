"""Defines the URL patterns for Meal Plans."""

from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Home page:
    path('home', views.home, name='home')
]