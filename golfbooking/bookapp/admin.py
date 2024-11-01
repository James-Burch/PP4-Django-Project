from django.contrib import admin
from .models import AvailableTime, Booking

# Register your models here.
admin.site.register(AvailableTime)
admin.site.register(Booking)
