from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.list import DetailView

from .models import Product
# Create your views here.

class MerchStoreListView(ListView):
    model = Product
    template_name = 'merchstore_list.html'


class MerchStoreDetailView(DetailView):
    model = Product
    template_name = 'merchstore_detail.html'