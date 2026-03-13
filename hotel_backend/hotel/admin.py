from django.contrib import admin
from .models import *


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone']

@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ['room_type']

@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    pass