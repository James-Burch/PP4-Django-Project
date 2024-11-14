# from django.contrib import admin
# from django import forms
# from .models import Booking, AvailableDate

# # Register your models here.
# admin.site.register(AvailableDate)
# admin.site.register(Booking)

from django.contrib import admin
from .models import Booking, Player

admin.site.register(Booking)
admin.site.register(Player)
