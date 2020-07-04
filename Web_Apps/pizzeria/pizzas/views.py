from django.shortcuts import render

# Create your views here.
def home(request):
    """The home page."""
    return render(request, 'pizzas/home.html')