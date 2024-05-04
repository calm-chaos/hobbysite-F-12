from django.urls import path

from .views import *

urlpatterns = [
    path("", user_profile, name="user-profile"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register, name="register-profile"),
]

app_name = "user_management"
