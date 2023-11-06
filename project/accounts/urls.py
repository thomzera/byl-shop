from django.urls import path

from . import views as accounts_views

urlpatterns = [
    path('register/', view=accounts_views.register, name='register'),
    path('login/', view=accounts_views.user_login, name='login'),
    path('logout/', view=accounts_views.user_logout, name='logout'),
]
