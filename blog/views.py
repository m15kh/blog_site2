from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm

class PostViewList(ListView):
    model = Post
    template_name = 'blog/all_post.html'
    
class PostViewDetail(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

class PostViewNew(CreateView):
    form_class = PostForm
    template_name = 'blog/new_post.html'
    reverse_lazy = 'blog:all_post'

class PostViewEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'

class PostViewDelete(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_post')
