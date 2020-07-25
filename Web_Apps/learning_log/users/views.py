from django.shortcuts import render, redirect
from django.contrib.auth import login
#We import this login function to login a user from the registration form if the credentials are correct.

from django.contrib.auth.forms import UserCreationForm
#We also import the default UserCreationForm, which makes it easy for us.
# It creates a form for users to register.

# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # No POST data, display a blank registration form:
        form = UserCreationForm()
    else:
        # POST data submitted, process completed form:
        form = UserCreationForm(data=request.POST)
        #If it's a submitted POST request, we create a form containing the request data.

        if form.is_valid():
            new_user = form.save()
            #If the data is valid, we save the form-data using the save function to the database
            # as a user object, which we assign to the new_user variable.

            # Log the user in and the redirect to home page:
            login(request, new_user)
            #When we've assigned the user to new_user, we log them in using the login function.
            
            return redirect('learning_logs:index')

    # Display a blank or invalid form:
    context = {'form': form}
    return render(request, 'registration/register.html', context)