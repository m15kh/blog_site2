from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.


class PostViewList(ListView):
    model = Post
    template_name = 'list_posts.html'
    
class DetailPost(DetailView):
    model = Post
    template_name = 'detail_post.html'