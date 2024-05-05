from django.urls import path

from .views import product_list, product_detail, product_create, product_update, product_cart, transaction_list


urlpatterns = [
    path('items', product_list, name='products'),
    path('item/<int:pk>', product_detail, name='product-detail'),
    
]

app_name = 'merchstore'

