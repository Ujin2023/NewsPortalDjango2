from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class NewsList(ListView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'posts'



class NewsDetail(DetailView):
    model = Post
    template_name = 'default.html'
    cntext_object_name = 'post'
