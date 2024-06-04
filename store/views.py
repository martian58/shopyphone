from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from .models import Product
from django.db.models import Q

from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.models import User
from .models import Mail
from django.shortcuts import redirect

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', 
                  
        {'products':products}
                  
    )

def about(request):
    return render(request, 'about.html', {})


def product(request,pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product.html', {'product':product})


def search_results(request):
    query = request.GET.get('query')
    products = None
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'home.html', {'query': query, 'products': products})



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

def contact_us(request,):
    if request.method == 'POST':
        # name = request.POST['name']
        to_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject,
            message,  
            settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False
            )
        
        Mail.objects.create(
            subject=subject,
            message=message,  
            from_email=settings.EMAIL_HOST_USER,
            to_email=to_email,
            )
    return render(request, 'contact.html')