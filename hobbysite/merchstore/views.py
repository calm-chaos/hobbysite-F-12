from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ProductType, Product, Transaction
from .forms import ProductForm, TransactionForm
from user_management.models import Profile


@login_required
def product_list(request):
    user_products = Product.objects.filter(owner__user=request.user)
    all_products = Product.objects.exclude(owner__user=request.user)

    ctx = {
        "user_products": user_products,
        "product_list": all_products
    }
    return render(request, 'product_list.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    transactionForm = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
    ctx = {
        "product": product,
        "form": transactionForm
    }
    return render(request, 'product_detail.html', ctx)


@login_required
def product_create(request):
    productForm = ProductForm()
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            product = productForm.save(commit=False)
            currentUser = Profile.objects.get(user=request.user)
            product.owner = currentUser
            product = productForm.save()
    ctx = {
        "form": productForm
    }
    return render(request, 'product_create.html', ctx)


@login_required
def product_update(request, pk):
    return render()


@login_required
def product_cart(request):
    return render()


@login_required
def transaction_list(request):
    return render()

