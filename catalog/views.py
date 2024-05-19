#from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Contacts

class ContactsView(ListView):
    model = Contacts
    extra_context = {'title': 'Контакты'}
    template_name = 'catalog/contacts_list.html'


class ProductDitailView(DetailView):
    model = Product
    template_name = "catalog/detail_product.html"

class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"

class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"