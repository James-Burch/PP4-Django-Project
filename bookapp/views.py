from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Booking, AvailableTime, Meta
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required
def booking(request):
    return render(request, "bookingpage.html")

def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "register.html", context)