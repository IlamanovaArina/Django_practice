from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from catalog.models import Product, Category
from .forms import EditingForm, ProductUpdateForm
from .services import get_products_from_cache, get_products_by_category


class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_products_from_cache()


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'


@method_decorator(cache_page(60 * 15), name='dispatch')  # Кэширование
class ProductsBuCategoryListView(ListView):
    model = Product
    template_name = 'products_du_category.html'
    context_object_name = 'products'  # Изменить имя контекста на 'products'

    def get_queryset(self):
        """Функция возвращает список продуктов по заданной категории"""
        queryset = super().get_queryset()
        category = self.request.GET.get('category')

        if category:
            return get_products_by_category(self.request.GET.get('category'))
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Получаем все категории для отображения в фильтре
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

    def product_detail(self):
        pass


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
        else:
            raise PermissionDenied("У вас нет прав для обновления этого продукта.")
