from django.shortcuts import render
from django.contrib.auth import  authenticate, login, logout
from django.http import JsonResponse
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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'base.html')  
        else:
            error_message = "Invalid email or password. Please try again."
            if request.is_ajax():
                return JsonResponse({'error_message': error_message}, status=400)

    return render(request, 'llogin.html') 