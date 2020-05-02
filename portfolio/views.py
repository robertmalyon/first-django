from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def portfolio_blog(request):
    return render(request, 'portfolio/portfolio-blog.html')
