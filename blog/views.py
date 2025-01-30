from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from blog.models import BlogEntry


class BlogsListView(ListView):
    model = BlogEntry
    template_name = 'blogs.html'
    context_object_name = 'blogentrance'


class BlogDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog_detail.html'
    context_object_name = 'blogentery'


class BlogCreateView(CreateView):
    model = BlogEntry
    template_name = 'blog_create.html'
    fields = ['header', 'content', 'preview']
    success_url = reverse_lazy('books')
