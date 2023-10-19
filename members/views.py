from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request, 'base.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')

def llogin(request):
    return render(request, 'llogin.html')

def logout(request):
    return render(request, 'book.html')