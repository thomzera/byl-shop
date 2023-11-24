from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models as accounts_models


class RegistrationForm(UserCreationForm):

    class Meta:
        model = accounts_models.CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # classes
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        # labels
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar Senha'


class RegistrationFormComplete(forms.ModelForm):
    
    class Meta:
        model = accounts_models.CustomUser
        fields = ('nome', 'data_nascimento', 'numero_telefone', 'cidade', 'estado', 'cep', 'bairro', 'rua', 'numero', 'complemento')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # classes
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'form-control', 'placeholder': '13/08/1999'})
        self.fields['numero_telefone'].widget.attrs.update({'class': 'form-control'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control'})   
        self.fields['bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['rua'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['complemento'].widget.attrs.update({'class': 'form-control'})

        # labels
        self.fields['nome'].label = 'Nome Completo'
        self.fields['data_nascimento'].label = 'Data de Nascimento'
        self.fields['numero_telefone'].label = 'Celular'

        self.fields['data_nascimento'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']


class LoginForm(AuthenticationForm):

    class Meta:
        model = accounts_models.CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # classes
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-lg'})

        # labels
        self.fields['password'].label = 'Senha'
