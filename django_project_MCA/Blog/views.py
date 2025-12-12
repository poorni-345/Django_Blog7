from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Function-based view for home (optional if using ListView)
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'Blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html' 
    context_object_name = 'posts'     
    ordering = ['-data_posted']      

class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'
    context_object_name = 'post'            

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

