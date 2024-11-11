from django.contrib import admin
from django import forms
from .models import Booking, AvailableDate

# Register your models here.
admin.site.register(AvailableDate)
admin.site.register(Booking)
