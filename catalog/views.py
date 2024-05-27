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



class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_from.html'
    success_url = reverse_lazy('catalog:product_list')

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
    success_url = reverse_lazy('catalog:product_list')

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
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить продукт'
        return context




class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(current_version=True)
            if active_versions:
                product.name_version = active_versions.last().name_version
                product.number_version = active_versions.last().number_v
        context_data['object_list'] = products
        return context_data


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        queryset = Version.objects.all()
        products = Product.objects.all()
        for product in products:
            print(product)
            versions = Version.objects.filter(product=product)
            # print(queryset.product == product)
            return versions
        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionDetailView(DetailView):
    model = Version
    template_name = "catalog/version_detail.html"


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:versions')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_version'] = 'Удалить версию'
        return context