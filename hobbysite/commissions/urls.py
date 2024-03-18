from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
path('commissions/list', CommissionListView.as_view(), name='list'),
path('commissions/<int:pk>', CommissionDetailView.as_view(), name='commission_detail')

]

# This might be needed, depending on your Django version
app_name = "commissions"