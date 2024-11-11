from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Booking, AvailableDate
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required
def booking(request):
    form = BookingForm()
    return render(request, "bookingpage.html", {'form': form})


def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "register.html", context)

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Check if slot is already booked
            if Booking.objects.filter(date=booking.date, time_slot=booking.time_slot).exists():
                messages.error(request, "This time slot is already booked. Please choose another.")
            else:
                booking.save()
                messages.success(request, "Your booking was successful!")
                return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'bookingpage.html', {'form': form})
