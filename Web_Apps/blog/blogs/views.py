from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def home(request):
    """A home page, showing the posts in chronological order."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}

    return render(request, 'blogs/home.html', context)