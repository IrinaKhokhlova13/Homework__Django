from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': product.name_product
    }
    return render(request, "catalog/detail_product.html", context)


def products_list(request):
    product = Product.objects.all()
    context = {
        'object': product
    }
    return render(request, "catalog/products_list.html", context)