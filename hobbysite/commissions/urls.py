from django.urls import path

from .views import *

urlpatterns = [
    path("commissions/list", commission_list, name="list"),
    path(
        "commissions/<int:pk>", commission_detail, name="commission_detail"
    ),
    path("commissions/add", commission_create, name="commission_create"),
    path("commissions/<int:pk>/edit", commission_update, name="commission_update"),
    path("commissions/jobapplication/<int:pk>", commission_jobapplication, name="commission_jobapplication"),
]

app_name = "commissions"
