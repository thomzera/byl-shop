from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, RegistrationForm


class UserLogin(View):
    template_name = 'registration/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
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
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user and not isinstance(user, AnonymousUser):
                login(request, user)

            return redirect('index')
        return render(request, self.template_name, {'form': form})