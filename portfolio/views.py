from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    return render(request, 'portfolio/home.html')


def portfolio_blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'portfolio/portfolio-blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'portfolio/portfolio-blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
