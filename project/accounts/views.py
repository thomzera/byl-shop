from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from . import forms as accounts_forms
from . import models as accounts_models


class UserLogin(View):
    template_name = 'registration/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = accounts_forms.LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = accounts_forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form': form})


class UserLogout(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')


class UserRegister(View):
    template_name = 'registration/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = accounts_forms.RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = accounts_forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user and not isinstance(user, AnonymousUser):
                login(request, user)

            return redirect('register_complete', user_id=user.id)
        return render(request, self.template_name, {'form': form})
    

class UserRegisterComplete(View):
    template_name = 'registration/register_complete.html'

    def get(self, request, user_id):
        user = get_object_or_404(accounts_models.CustomUser, id=user_id)
        form = accounts_forms.RegistrationFormComplete(instance=user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, user_id):
        user = get_object_or_404(accounts_models.CustomUser, id=user_id)
        form = accounts_forms.RegistrationFormComplete(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, self.template_name, {'form': form})