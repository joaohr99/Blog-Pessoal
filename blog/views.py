# blog/views.py

from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        # Pega todos os posts, ordenados por data
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, "blog/about.html", {'title': 'Sobre'})
