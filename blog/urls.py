from django.urls import path

from .apps import BlogConfig
from .views import BlogsListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogsListView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/blog/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]