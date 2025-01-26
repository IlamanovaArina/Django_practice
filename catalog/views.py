from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    if request.method == 'GET':
        return render(request, 'home.html', context=context)
    return render(request, 'home.html', context=context)


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    return render(request, 'contacts.html')


def one_product(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    context = {
        'product': product
    }
    return render(request, 'product.html', context=context)


# def one_product(request, id_product):
#     product = get_object_or_404(Product, id=id_product)
#
#     # Получение ID предыдущего и следующего товара
#     previous_product = Product.objects.filter(id__lt=id_product).order_by('-id').first()
#     next_product = Product.objects.filter(id__gt=id_product).order_by('id').first()
#
#     context = {
#         'product': product,
#         'previous_product': previous_product,
#         'next_product': next_product,
#     }
#     return render(request, 'product.html', context=context)