from django.http import response
from django.http.response import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse as jr

from .models import Product, Manufacturer


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product-list.html'


def product_list_api(_):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}  # "pk", "name"
    response = jr(data)
    return response


def product_detail_api(_, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity
            }
        }
        response = jr(data)
    except Product.DoesNotExist:
        response = jr({
            "error": {
                "code": 404,
                "message": "The required product was not found."
            }
        }, status=404)
    return response


def manufacturer_detail_api(_, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)  # [:30]
        owned_products = manufacturer.products.all()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products": list(owned_products.values()),
        }}
        response = jr(data)
    except Manufacturer.DoesNotExist:
        response = jr({
            "error": 404,
            "message": "The required manufacturer does not exist"
        }, status=404)
    return response


def active_manufacturers_list(_):
    try:
        active_manufacturers = Manufacturer.objects.filter(active=True)
        data = {
            "active_manufacturers": list(active_manufacturers.values())
        }
        response = jr(data)
    except Manufacturer.DoesNotExist:
        response = jr({
            "error": {
                "code": 404,
                "message": "There are no active manufacturers."
            }
        }, status=404)
    return response
