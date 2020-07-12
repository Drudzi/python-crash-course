from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page:
    path('home/', views.home, name='home'),
    # Menu page:
    path('menu/', views.menu, name='menu'),
    # Detailed page about each pizza:
    path('menu/<int:pizza_id>/', views.pizza, name='pizza')
]