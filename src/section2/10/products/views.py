from django.views.generic.detail import DetailView as dv
from django.views.generic.list import ListView as lv
from pathlib import Path

from .models import Product, Manufacturer


class ProductDetailView(dv):
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(lv):
    model = Product
    template_name = 'products/product_list.html'
