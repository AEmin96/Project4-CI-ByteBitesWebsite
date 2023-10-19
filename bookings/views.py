from django.shortcuts import render, redirect
from .models import Booking
# from .forms import BookingForm
from django.contrib.auth.models import User


def book(request):
    if request.method == 'POST':
        date = request.POST.get('date') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=email.split('@')[0], email=email, password=password)
        new_user.save()
        new_book = Booking(date = date, user = new_user)
        new_book.save()
        return render(request, 'booking_success.html')
    else:
        print('Error')

    return render(request, 'book.html')

def mybookings(request):
    return render(request, 'mybookings.html')