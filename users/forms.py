from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "phone",
            "address",
            "birth_date",
            "passport_number",
            "city",
            "country",
            "gender",
            "job",
            "company",
            "extra_info",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
