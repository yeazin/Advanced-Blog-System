from django.shortcuts import render
from .models import Topics, Blog_Post
from .forms import Create_Post_Forms


# Create your views here.

def HomeView(request):
    topics = Topics.objects.all().order_by('-id')
    #topics = topics[:2]
    posts = Blog_Post.objects.all().order_by('-id')
    context = {'topics':topics}
    return render (request, 'blog/index.html', context)

# For creating Post

def Create_Post (request):
    forms = Create_Post_Forms()
    context = {'forms': forms}
    return render (request, 'blog/create_post.html', context)



