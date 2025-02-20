from itertools import product

from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
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

    def form_valid(self, form):
        # Устанавливаем владельца на текущего авторизованного пользователя
        form.instance.owner = self.request.user
        # self.permissions_owner()
        return super().form_valid(form)

    # def permissions_owner(self):
    #     app_perm = Permission.objects.get(codename='add_product')
    #     change_perm = Permission.objects.get(codename='change_product')
    #     delete_perm = Permission.objects.get(codename='delete_product')
    #     view_perm = Permission.objects.get(codename='view_product')
    #
    #     self.request.user.user_permissions.add(app_perm, change_perm)
    #     self.request.user.save()

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_edit.html'
    permission_required = 'catalog.can_unpublish_product'

    def get_form_class(self):
        user = self.request.user
        if user.is_staff:
            return EditingForm
        if user == self.object.owner:
            return EditingForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductUpdateForm
        raise PermissionDenied

    # def get(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     self.check_permissions(request.user, product)
    # #
    # def post(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     self.check_permissions(request.user, product)
    # #
    # def check_permissions(self, user, product):
    #     if product.owner != user.email:
    #         raise PermissionDenied("У вас нет прав для редактирования этого продукта.")
    #     else:
    #         return EditingForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_delete.html'
