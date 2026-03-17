from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import forms
from django.views import generic


#Регистрация
class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'
    


#Авторизация
from django.contrib.auth.views import LoginView, LogoutView
class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/congratulation/'


#Выход из аккаунта
from django.urls import reverse_lazy
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')





        
#Успешная авторизация
def cong_view(request):
    if request.method == 'GET':
        user = User.objects.all()
    return render(
        request,
        'cong.html',
        {
            'user': user
        }
    )
