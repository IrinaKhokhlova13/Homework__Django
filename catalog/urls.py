from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactsView, ProductListView, ProductDitailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts_list'),
    path('detail/<int:pk>/', ProductDitailView.as_view(), name='detail_product'),
    path('home/list/', ProductListView.as_view(), name='products_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
