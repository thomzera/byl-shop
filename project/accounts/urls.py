from django.urls import path

from . import views as accounts_views

urlpatterns = [
    path('register/', view=accounts_views.UserRegister.as_view(), name='register'),
    path('login/', view=accounts_views.UserLogin.as_view(), name='login'),
    path('logout/', view=accounts_views.UserLogout.as_view(), name='logout'),
]