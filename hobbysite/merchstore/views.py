from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product


class MerchStoreListView(ListView):
    model = ProductType
    template_name = 'product_list.html'


class MerchStoreDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'