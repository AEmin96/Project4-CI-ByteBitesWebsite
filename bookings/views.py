from django.shortcuts import render, redirect,get_object_or_404
from .models import Booking
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

def book(request):
    if request.method == 'POST':
        date = request.POST.get('date') 
        email = request.POST.get('email')
        password = request.POST.get('password')

        overlapping_bookings = Booking.objects.filter(date=date)

        overlap = overlapping_bookings.exists()
        if overlap:
            messages.error(request, 'This Date Is Already Booked, Please Choose Another Day!')
            return redirect('book')
        old_user = User.objects.filter(email=email).first()
        if old_user :
            messages.error(request, 'Email Already Exists!')
            return redirect('book')
        new_user = User.objects.create_user(username=email.split('@')[0], email=email, password=password)
        new_user.save()
        new_book = Booking(date = date, user = new_user)
        new_book.save()
        login(request, new_user)
        return render(request, 'booking_success.html')
    else:
        print('Error')

    return render(request, 'book.html')

def mybookings(request):
    mybooks = Booking.objects.filter(user=request.user).all()
    return render(request, 'mybookings.html',{'mybooks':mybooks})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.delete()
        return JsonResponse({'message': 'Booking deleted successfully'})

    return JsonResponse({'error': 'Invalid request method'})


def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_date = data.get('date')
            
            # Ensure that a new date is provided
            if new_date is not None:
                booking.date = new_date
                booking.save()
                return JsonResponse({'message': 'Booking updated successfully'})
            else:
                return JsonResponse({'error': 'Invalid date provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def newbook(request):
    if request.method == 'POST':
        date = request.POST.get('date') 
        
        overlapping_bookings = Booking.objects.filter(date=date)

        overlap = overlapping_bookings.exists()
        if overlap:
            messages.error(request, 'This Date Is Already Booked, Please Choose Another Day!')
            return redirect('book')
        
        new_book = Booking(date = date, user=request.user)
        new_book.save()
        
        return redirect("mybookings")
    else:
        print('Error')

    return redirect("mybookings")