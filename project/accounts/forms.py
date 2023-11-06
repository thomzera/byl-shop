from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models as accounts_models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = accounts_models.CustomUser
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = accounts_models.CustomUser  # Use o modelo de usuário personalizado
