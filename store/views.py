# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', 
                  
        {'products':products}
                  
    )

def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful"))
            return redirect('home')  # Replace 'home' with your home view name
        else:
            messages.error(request, ('Invalid username or password.'))
            return redirect('login')  # Replace 'login' with your login view name
    else:
        return render(request, 'login.html',{})


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Login
            user = authenticate(username=username, password=password)

            login(request,user)

            messages.success(request, ('User creation successful'))
            return redirect("home")
        else:
            messages.success(request, ('Error ocurred'))
            return redirect("register.html")

    else:
        return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')