from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactsView, ProductListView, ProductDitailView, ProductUpdateView, \
    ProductDeleteView, ProductCreateView, VersionListView, VersionCreateView, VersionUpdateView, VersionDetailView, \
    VersionDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts_list'),
    path('detail/<int:pk>/', ProductDitailView.as_view(), name='product_detail'),
    path('home/list/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_form'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('versions/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
