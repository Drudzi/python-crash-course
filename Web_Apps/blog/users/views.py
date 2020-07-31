from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Page for registration of a user."""
    if request.method != 'POST':
        # No POST data submitted, create a blank form:
        form = UserCreationForm()
    else:
        # POST data submitted, process the completed form:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            
            # Login user, and redirect to the home page:
            login(request, new_user)
            return redirect('blogs:home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)