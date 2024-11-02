from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Booking, AvailableTime, Meta
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, "home.html")

def booking(request):
    return render(request, "bookingpage.html")    