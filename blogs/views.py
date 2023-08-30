from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostViewList(ListView):
    model = Post
    template_name = 'list_posts.html'
    
