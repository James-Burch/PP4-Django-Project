from django.shortcuts import render, HttpResponse
from .models import Booking, AvailableTime, Meta

# Create your views here.

def home(request):
    return render(request, "home.html")

def booking(request):
    return render(request, "bookingpage.html")    