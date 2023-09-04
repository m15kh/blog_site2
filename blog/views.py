from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm




class PostViewList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/all_post.html'
    login_url = 'login'
    
class PostViewDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    login_url = 'login'


class PostViewNew(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/new_post.html'
    reverse_lazy = 'blog:all_post'
    login_url = 'login'


class PostViewEdit(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'
    login_url = 'login'


class PostViewDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_post')
    login_url = 'login'
