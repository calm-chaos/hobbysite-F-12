from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ProductType, Product, Transaction


def product_list(request):
    return render()


def product_detail(request):
    return render()


@login_required
def product_create(request):
    return render()


@login_required
def product_update(request):
    return render()


@login_required
def product_cart(request):
    return render()


@login_required
def transaction_list(request):
    return render()

