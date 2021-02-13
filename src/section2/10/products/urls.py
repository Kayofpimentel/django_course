from django.urls import path
from .views import ProductDetailView, ProductListView, manufacturer_detail_api, active_manufacturers_list, product_detail_api, product_list_api

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("api/products/", product_list_api, name="product-list-api"),
    path("api/products/<int:pk>", product_detail_api, name="product-detail-api"),
    path("api/manufacturers/<int:pk>", manufacturer_detail_api,
         name="manufacturer-detail-api"),
    path("api/manufacturers/active",
         active_manufacturers_list, name="active-manufacturers-api")
]
