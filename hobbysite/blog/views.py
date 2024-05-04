from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class BlogListView(ListView):
    model = Article
    template_name = "blog_list.html"


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog_detail.html"
