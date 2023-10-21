from django.contrib import admin
from .models import Booking

admin.site.register(Booking)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['username', 'date']


admin.site.register(Booking, BookingAdmin)
