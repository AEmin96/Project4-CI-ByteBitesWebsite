from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.models import User

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the current user to the booking
            booking.save()
            new_user = User.objects.create_user(email=form.email, password=form.password)
            new_user.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'bookings/book.html', {'form': form})