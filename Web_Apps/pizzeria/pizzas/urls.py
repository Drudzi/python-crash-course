from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page:
    path('home', views.home, name='home'),
]