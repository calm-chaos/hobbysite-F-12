from django.urls import path

from .views import MerchStoreListView, MerchStoreDetailView

urlpatterns = [
    path('items', MerchStoreListView.as_view(), name='products'),
    path('item/<int:pk>', MerchStoreDetailView.as_view(), name='product-detail'),
]

app_name = 'merchstore'

