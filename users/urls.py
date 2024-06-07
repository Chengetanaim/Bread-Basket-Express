from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]