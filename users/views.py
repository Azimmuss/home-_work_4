from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import CustomUser


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("users_list")
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if user:
            login(request, user)
            return redirect("users_list")

    return render(request, "users/login.html", {"form": form})


@login_required
def users_list(request):
    people = CustomUser.objects.all()
    return render(request, "users/users_list.html", {"users": people})


def logout_view(request):
    logout(request)
    return redirect("login")
