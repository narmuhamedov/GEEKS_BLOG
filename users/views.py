from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import forms


#Регистрация
def register_view(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST, request.FILES)
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        #form = UserCreationForm()
        form = forms.CustomRegisterForm()
    
    return render(
        request,
        'register.html',
        {
            'form': form,
        }
    )

#Авторизация
def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/congratulation/')
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        'login.html',
        {
            "form": form,
        }
    )

#Выход из аккаунта
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


        
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
