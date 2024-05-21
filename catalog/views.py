#from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version
from django.urls import reverse_lazy

class ContactsView(ListView):
    model = Contacts
    extra_context = {'title': 'Контакты'}
    template_name = 'catalog/contacts_list.html'


class ProductDitailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    extra_context = {'title': 'Продукты на любой вкус'}

class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"

class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_from.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        return context

    def form_valid(self, form):
        product = form.save()
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_from.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        context['title'] = 'Изменить продукт'
        return context

    def get_form_class(self):
        return ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить продукт'
        return context