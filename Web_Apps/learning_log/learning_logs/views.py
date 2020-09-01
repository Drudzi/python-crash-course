from django.shortcuts import render, redirect, get_object_or_404
#render() function renders a response based on data provided by views.
#The redirect() function is used to redirect a user back to a given page.
# redirect() takes the name of a view-function and redirects to that view, displaying its template. 

from django.contrib.auth.decorators import login_required
#This decorator checks if a user is logged in, and only runs the function below if so.
# If the user isn't logged in they'll be directed to the login page.

from django.http import Http404

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

@login_required #We apply this decorator to the topics function. Directors need @ in front.
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #We assign the topics attribute a queryset from the database of the topics.
    # Using function order_by(), we order by the date_added attribute in the Topic class/model.

    context = {'topics': topics}
    #Here we define the context attribute. A context is a dictionary,
    # where the keys are the names we'll use in our template to access our data and
    #  where the values are the data we need to send to the template.

    return render(request, 'learning_logs/topics.html', context)
    #When we're building a page that requires data, we also pass our context attribute
    # to the render function as our third argument.

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    #Our first view with a parameter other than request.
    # It will retrieve the integer stored in topic_id from the URL-pattern.

    topic = get_object_or_404(Topic, id=topic_id)
    #topic = Topic.objects.get(id=topic_id)
    # Here we'll assign the topic-object assigned to the topic-id from the URL...
    #  using the same method we used in the Django shell.
    #   The get() function gives us the topic we're currently working with.
    #    In Chapter 20 we switch Topic.objects.get() to get_object_or_404() to handle errors better.

    # Make sure the topic belongs to the current user:
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    #We also need the entries associated with the current topic.
    # Once again, we recieve them using the same method as we did in the Django shell.
    #  To get them sorted by latest first, we use the order_by() function...
    #   and give it the date_added attribute, which sorts them by date added.
    #    The minus sign in front of date_added reverses the order, so the most recent come first. 

    context = {'topic': topic, 'entries': entries}
    #We enter the attributes above to the context, which let's us reach them from the template-file.

    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        #Here we test whether it is a POST or GET request.
        #request.method gets what kind of request it is, a string in capital letters.
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
            
            new_topic = form.save(commit=False)
            #We call the save() function with commit=False so it doesn't directly save it to the database.
            # Now it's stored in the new_topic variable.
            #  We need to do this because Django needs to know which user the topic should belong to,
            #   and the user can be found in the request using request.user.

            new_topic.owner = request.user
            #Now that we've got the new topic object stored in new_topic, we can use the attributes of the Topic
            # model to access it's information.
            #  Django needs to assign a user to the owner attribute before saving it to the database.
            #   So we assign the request.user to the owner attribute of the new topic model object.

            new_topic.save()
            #Now we're ready to completely store it to the database.

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

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    #We get the topic object we are currently working with using the topic_id from the URL.

    # Make sure the topic belongs to the current user:
    check_topic_owner(request, topic)
     
    if request.method != 'POST':
        #If it's a GET request, we create a new empty form.
        # No data submitted, create a blank form:
        form = EntryForm()
    
    else:
        #A user has entered information and submitted it.
        # POST data submitted; process data:
        form = EntryForm(data=request.POST)
        #The first thing we do is to create a new instance of the EntryForm containing the data from the user.
        if form.is_valid():
            #If the form with the data from the user is valid...

            new_entry = form.save(commit=False)
            #We assign and save the form to new_entry while including the commit argument.
            # commit=False tells Django not to save it to the database, just assign it to the variable.
            #  We do this because we first want to assign the entry to the topic.

            new_entry.topic = topic
            #Here we assign the current topic object to the entry's topic attribute, so they connect.

            new_entry.save() 
            #Now, we are ready to save the entry object to the database with the associated topic.

            return redirect('learning_logs:topic', topic_id=topic_id)
            #This redirect call will need two arguments.
            # The first one should as always be the view-function we want to redirect to.
            #  And in this case, the topic() view function also needs a topic_id.
            #   We assign the current topic_id to the topic() view function as a keyword argument.
    
    #The code below will be execute if form is blank or invalid.
    # Display a blank or invalid form:
    context = {'form': form, 'topic': topic} #We assign the form to the context so we can display it in the template.
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        #If there is a GET request, we create a new form including the current Entry object.
        # The instance argument takes an instance/object and tells Django to create
        #  a new form prefilled with the data from that object.
        
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        #When it's a post request and the user has submitted data...
        # We create a form and give it the data from the POST-request as usual.
        #  We also assign the text-data to the current entry instance using the instance arg.
        #   This assigns the data to the right Entry-object.
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)


# Custom Helper Functions
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404