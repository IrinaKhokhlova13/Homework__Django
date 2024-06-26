from django.contrib import admin

from catalog.models import Category, Product, Version

admin.site.register(Version)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_product', 'price', 'category', 'preview']
    list_filter = ['category']
    search_fields = ['name_product', 'description']
    list_editable = ['preview']



