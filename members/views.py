from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'base.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')

def logout(request):
    return render(request, 'book.html')

def llogin(request):

    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        User = get_user_model()
        email = request.POST['email'].lower()
        user = User.objects.filter(email=email).first()
        password = request.POST['password']
        if user and user.check_password(password):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('llogin')
    else:
        return render(request, 'llogin.html')