from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def showmap(request):
    return render(request, 'map.html')

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('showmap')
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form, 'error': 'Invalid Login'})


def logout_view(request):
    logout(request)
    return redirect('showmap')

def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
        return redirect('showmap')
    else:
        form=RegisterForm()
        return render(request, 'signup.html', {'form':form})