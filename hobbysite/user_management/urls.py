from django.urls import path

from .views import profile_update

urlpatterns = [
    path("update/", profile_update, name="update"),
]
