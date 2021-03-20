from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def Register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.info(request, 'Hello ' + username + ' You can login to profile!')
                return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def Login(request):
    if request.user.is_authenticated:
        return HttpResponse('Current user is authenticated...!')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('user is logged in...!')
            else:
                messages.info(request, 'Username OR password is incorrect!')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.info(request, 'You can login into your profile again..!')
    return redirect('login')

