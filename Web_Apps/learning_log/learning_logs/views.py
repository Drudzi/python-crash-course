from django.shortcuts import render
#render() function renders a response based on data provided by views.

from .models import Topic
#We import the models associated with the data we'll need in our views.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
    #When a URL request matches the pattern we defined in urls.py, it will look for the given views-function.
    # If matched, Django passes the request object to the view function.
    #  For this index page, we won't need to process any data, so we only need the render function.
    #   The render() function takes two arguments, the current request object and a template.
    #    The template defines what the page should look like, we define index.html inside learning_logs.

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    #We assign the topics attribute a queryset from the database of the topics.
    # Using function order_by(), we order by the date_added attribute in the Topic class/model.

    context = {'topics': topics}
    #Here we define the context attribute. A context is a dictionary,
    # where the keys are the names we'll use in our template to access our data and
    #  where the values are the data we need to send to the template.

    return render(request, 'learning_logs/topics.html', context)
    #When we're building a page that requires data, we also pass our context attribute
    # to the render function as our third argument.