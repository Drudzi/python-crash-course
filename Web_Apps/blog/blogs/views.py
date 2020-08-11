from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm

# Create your views here.
def home(request):
    """A home page, showing the posts in chronological order."""
    posts = BlogPost.objects.order_by('-date_added') #minus before date_added places newest first.
    context = {'posts': posts}

    return render(request, 'blogs/home.html', context)

@login_required
def new_post(request):
    """The page for submitting new posts."""
    if request.method != 'POST':
        # No data submitted, so create an empty form
        form = PostForm()
    else:
        # POST data submitted, process that data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:home')
    
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Page for editing posts."""
    post = BlogPost.objects.get(id=post_id)
    check_post_owner(request, post)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)


# Custom Helper Functions
def check_post_owner(request, post):
    """Raise 404 if user is not the owner."""
    if post.owner != request.user:
        raise Http404