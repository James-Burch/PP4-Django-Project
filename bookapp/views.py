from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Booking, AvailableDate
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants as messages
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required
def booking(request):
    form = BookingForm()
    return render(request, "bookingpage.html", {'form': form})

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

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
            # Check if the time slot is already booked
            if Booking.objects.filter(date=booking.date, time_slot=booking.time_slot).exists():
                messages.error(request, "This time slot is already booked. Please choose another.")
            else:
                booking.save()
                messages.success(request, 'Booking Successful')
                return redirect('booking_confirmation')  # Redirect to a booking confirmation page
    else:
        form = BookingForm()
        
    return render(request, 'bookingpage.html', {'form': form})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        booking_id = request.POST.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            new_date = form.cleaned_data['date']
            new_time_slot = form.cleaned_data['time_slot']
            if Booking.objects.filter(date=new_date, time_slot=new_time_slot).exclude(id=booking_id).exists():
                messages.error(request, "This time slot is already booked. Please choose another.")
            else:
                form.save()
                messages.success(request, 'Booking updated successfully.')
                return redirect('user_bookings')  # Reload the page to show updated bookings
    else:
        booking_forms = [(booking, BookingForm(instance=booking)) for booking in bookings]

    return render(request, 'user_bookings.html', {'booking_forms': booking_forms})