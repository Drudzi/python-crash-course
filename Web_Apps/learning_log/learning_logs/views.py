from django.shortcuts import render, redirect
#render() function renders a response based on data provided by views.
#The redirect() function is used to redirect a user back to a given page.
# redirect() takes the name of a view-function and redirects to that view, displaying its template. 

from .models import Topic, Entry
#We import the models associated with the data we'll need in our views.

from .forms import TopicForm, EntryForm
#We also import the forms we need.

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

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        #Here we test whether it is a POST or GET request.
        # No data submitted, create a blank form:
        form = TopicForm() #Creating a form instance without arguments creates a blank form.
    else:
        #If a form of information has been submitted, it's a POST request.
        # POST data submitted; process data:
        form = TopicForm(data=request.POST)
        #Data has been submitted and has been stored in request.POST.
        # We create a form object using the data argument to which we assign the submitted form data.

        if form.is_valid():
            #Before we save the data to the database, we need to ensure it's valid.
            # The is_valid() method checks that all required fields in our form...
            #  have been filled in and that the data matches the field types that are expected.
            #   For an example, it checks that the length of text is less than 200 characters,
            #    which we specified inside Topic in models.py.
            #     Also worth noting is that all fields in a form are required by default.
            
            form.save() #If the data is valid, we'll save it to the database using save() method.

            return redirect('learning_logs:topics')
            #When we've saved the data, we use redirect() and give it the topics page...
            # to return them to the topics page where they hopefully will see their new topic.

            #Note that a return statement ends a function call, so if it goes through the code below won't.
        
    #If either a new blank form has been created or if submitted data was invalid...
    # it will run the code below and display a blank form.
    #  If data was invalid, it will also display some default error messages.

    # Display a blank or invalid form:
    context = {'form': form} #We give the blank form to the context so we can work with it in the template.
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""