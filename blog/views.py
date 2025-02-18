from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import BlogEntry


class BlogsListView(ListView):
    model = BlogEntry
    template_name = 'blogs.html'
    context_object_name = 'blogentrance'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog_detail.html'
    context_object_name = 'blogentery'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity_views += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogEntry
    template_name = 'blog_create.html'
    fields = ['header', 'content', 'preview', 'publication_attribute',]
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    template_name = 'blog_edit.html'
    fields = ['header', 'content', 'preview']
    success_url = reverse_lazy('blog:blogs')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    template_name = 'blog_delete.html'
    success_url = '/blogs/'

