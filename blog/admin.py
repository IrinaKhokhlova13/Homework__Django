from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'photo']
    search_fields = ['title']
    list_editable = ['photo']