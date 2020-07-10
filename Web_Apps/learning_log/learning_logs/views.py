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

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    #Our first view with a parameter other than request.
    # It will retrieve the integer stored in topic_id from the URL-pattern.

    topic = Topic.objects.get(id=topic_id)
    #Here we'll assign the topic-object assigned to the topic-id from the URL...
    # using the same method we used in the Django shell.
    #  The get() function gives us the topic we're currently working with.

    entries = topic.entry_set.order_by('-date_added')
    #We also need the entries associated with the current topic.
    # Once again, we recieve them using the same method as we did in the Django shell.
    #  To get them sorted by latest first, we use the order_by() function...
    #   and give it the date_added attribute, which sorts them by date added.
    #    The minus sign in front of date_added reverses the order, so the most recent come first. 

    context = {'topic': topic, 'entries': entries}
    #We enter the attributes above to the context, which let's us reach them from the template-file.

    return render(request, 'learning_logs/topic.html', context)