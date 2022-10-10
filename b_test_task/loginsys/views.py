from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .forms import RegisterForm, LoginForm


def register_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('client:home')
    if request.method == 'GET':
        form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event:home')
  
    return render(request, 'registration/register.html', 
        {'register_form':form})


def login_view(request: HttpRequest) -> HttpResponse:
    data = {}
    if request.method == 'GET':
        form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            user = authenticate(request, username=cd['username'], 
                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('event:home')
            data['error'] = 'Логин или пароль неверный!'
    data['form'] = form
    return render(request, 'registration/login.html', data)


@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('event:home')