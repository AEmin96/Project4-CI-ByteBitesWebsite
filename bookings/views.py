from django.shortcuts import render, redirect
from .models import Booking
# from .forms import BookingForm
from django.contrib.auth.models import User


def book(request):
    if request.method == 'POST':
        date = request.POST.get('date') 
        email = request.POST.get('email')
        password = request.POST.get('password')
#            new_user = User.objects.create_user(email=form.email, password=form.password)
#            new_user.save()
        return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})