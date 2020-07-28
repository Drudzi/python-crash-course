from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Page for registration of a user."""
    context = {}
    return render(request, 'registration/register.html', context)