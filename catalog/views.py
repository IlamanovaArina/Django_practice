from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.models import Product
from .forms import EditingForm


class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_new.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_edit.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_delete.html'