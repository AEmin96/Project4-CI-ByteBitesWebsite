from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']


admin.site.register(Booking, BookingAdmin)
