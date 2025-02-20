from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from catalog.models import Product
from django.http import HttpResponseForbidden
from .forms import EditingForm, ProductUpdateForm


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_new.html'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_edit.html'
    permission_required = 'catalog.can_unpublish_product'

    # def post(self, request, pk):
    #     user_ = get_object_or_404(User, id=pk)
    #     if not request.user.has_perm('can_unpublish_product'):
    #         return HttpResponseForbidden('У вас нет прав доступа для редактирования')
    #
    #     if user_.has_perm('can_unpublish_product'):
    #         return ProductUpdateForm
    #
    #     if user_.is_staff:
    #         return EditingForm
    #
    #     raise PermissionDenied

    def get_form_class(self):
        user = self.request.user

        if user.is_staff:
            return EditingForm

        if user.has_perm('catalog.can_unpublish_product'):
            return ProductUpdateForm

        raise PermissionDenied
    #     user = self.request.user
    #     # product = get_object_or_404(Product)
    #     if user.is_staff:
    #         return EditingForm
    #     if user.has_perm('can_unpublish_product'):
    #         return ProductUpdateForm
    #     if user.has_perm('can_delete_product'):
    #         return ProductUpdateForm
    #
    #     return 'Мы там, где не хотели бы оказаться, но почему? как так вышло?'
    #     # raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_delete.html'
