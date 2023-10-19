from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def menu(request):
    return render(requst, 'menu.html')

def book(request):
    return render(requst, 'book.html')

def llogin(request):
    return render(requst, 'llogin.html')