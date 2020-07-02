"""Defines URL patterns for learning_logs."""
#Descriptive docstring to make it clear which urls.py we're working in.

from django.urls import path
#path is needed to map URLs to views.

from . import views
#We also import the views.py module from the same directory as this urls.py.
# The dot tells Django to look for a file in the same directory.

app_name = 'learning_logs'
#app_name helps Django distinguish this urls.py from other files with the same name in the project.

#The follwing urlpatterns variable is a list of individual pages that can be requested from this app.

# What defines the URL patterns?
#  A call to the path() function does.
#   The path funtion takes three arguments.

#   The first argument route and it takes a string that helps Django route the request properly.
#    Django tries to route the requested URL to a view.
#     It does that by searching through all URL patterns we've defined to find one matching the request.

#   The second argument is views and it specifies which function to call in views.py.
#    When a requested URL matches the pattern defined, Django calls the given function from views.py.

#   The third argument is kwargs (multiple arguments can be entered), but we'll use name.
#    name is very common, and it provides a name for this pattern so we can refer to it in other code sections.

urlpatterns = [
    # Home page:
    path('', views.index, name='index'),
]