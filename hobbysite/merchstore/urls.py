from django.urls import path

from .views import product_list, product_detail, product_create, product_update, product_cart, transaction_list


urlpatterns = [
    path('items', product_list, name='products'),
    path('item/<int:pk>', product_detail, name='product_detail'),
    path('item/add', product_create, name='product_create'),
    # path('item/<int:pk>/edit', product_update ),
    # path('cart', product_cart, ),
    # path('transactions', transaction_list),
]

app_name = 'merchstore'

