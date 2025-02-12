from django.urls import path

from catalog.apps import CatalogConfig
from .views import HomeListView, ContactsTemplateView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name="home"),
    path('contacts/', ContactsTemplateView.as_view(), name="contacts"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('home/product/new/', ProductCreateView.as_view(), name="product_new"),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name="product_edit"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
]