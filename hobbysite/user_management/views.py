from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


def user_profile(request):
    profile = request.user.profile
    return render(request, "registration/user_profile.html", {"profile": profile})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_management:user-profile")
    else:
        form = RegistrationForm()
    return render(request, "registration/profile_create.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("user_management:user-profile")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")


def update_profile(request):
    return render(request, "registration/profile_update.html")


def reset_password(request):
    return render(request, "registration/password_reset.html")
