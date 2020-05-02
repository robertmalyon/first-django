from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('portfolio-blog/', views.portfolio_blog, name='portfolio-blog'),
]
