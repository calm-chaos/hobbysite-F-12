from django.urls import path

from .views import MerchStoreListView, MerchStoreDetailView

urlpatterns = [
    path('items', MerchStoreListView.as_view(), name='merchstore-list'),
    path('item/<int:pk>', MerchStoreDetailView.as_view(), name='merchstore-detail'),
]

app_name = 'merchstore'

