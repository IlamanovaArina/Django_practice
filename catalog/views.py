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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_delete.html'
    permission_required = 'catalog.can_delete_product'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == request.user:
            return super().dispatch(request, *args, **kwargs)
            # Проверка разрешения can_unpublish_product
        if request.user.has_perm('catalog.can_unpublish_product'):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied("У вас нет прав для обновления этого продукта.")


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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = EditingForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product_edit.html'
    permission_required = 'catalog.can_unpublish_product'

    def get_form_class(self):
        """Определяется какую форму применить: для редактирования всей
        страницы или только признак публикации(для модераторов) """
        user = self.request.user
        if user == self.object.owner or user.is_staff:
            return EditingForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductUpdateForm
        raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        """ Отвечает за обработку входящих HTTP-запросов и выбор правильного метода обработки
        в зависимости от типа запроса (GET, POST и тд.) """
        self.object = self.get_object()
        if self.object.owner == request.user:
            return super().dispatch(request, *args, **kwargs)

        # Проверка разрешения can_unpublish_product
        if request.user.has_perm('catalog.can_unpublish_product'):
            return super().dispatch(request, *args, **kwargs)
        # elif not request.user.has_perm('product.can_unpublish_product'):
        #     raise PermissionDenied("У вас нет прав для обновления этого продукта.")
        else:
            raise PermissionDenied("У вас нет прав для обновления этого продукта.")