from django.urls import path

from .apps import BlogConfig
from .views import BlogsListView, BlogDetailView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogsListView.as_view(), name='blogs'),
    path('blog/<int:id>', BlogDetailView.as_view(), name='blog'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
]