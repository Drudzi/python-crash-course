from django.shortcuts import render
#render() function renders a response based on data provided by views.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
    #When a URL request matches the pattern we defined in urls.py, it will look for the given views-function.
    # If matched, Django passes the request object to the view function.
    #  For this index page, we won't need to process any data, so we only need the render function.
    #   The render() function takes two arguments, the current request object and a template.
    #    The template defines what the page should look like, we define index.html inside learning_logs.