from django.urls import path
from .views import home
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('portfolio-blog/', PostListView.as_view(), name='portfolio-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(),
         name='portfolio-post-detail'),
]

#path('portfolio-blog/', views.portfolio_blog, name='portfolio-blog'),
