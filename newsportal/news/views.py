from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'title'
    template_name = 'news/news.html'
    context_object_name = 'news'

