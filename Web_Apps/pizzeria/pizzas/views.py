from django.shortcuts import render

from .models import Pizza, Topping

# Create your views here.
def home(request):
    """The home page."""
    return render(request, 'pizzas/home.html')

def menu(request):
    """The menu page."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/menu.html', context)

def pizza(request, pizza_id):
    """The detailed page about each pizza on the menu."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)