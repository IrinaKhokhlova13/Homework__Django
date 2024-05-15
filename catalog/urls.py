from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, detail_product, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', detail_product, name='detail_product'),
    path('home/list/', products_list, name='products_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
