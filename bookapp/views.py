# from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
# from .models import Booking, AvailableDate
# from django.utils import timezone
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import inlineformset_factory
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.messages import constants as messages
# from .forms import BookingForm

from django.shortcuts import render, redirect
from .models import Booking, Player
from .forms import BookingForm, PlayerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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

# @login_required
# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             # Check if the time slot is already booked
#             if Booking.objects.filter(date=booking.date, time_slot=booking.time_slot).exists():
#                 messages.error(request, "This time slot is already booked. Please choose another.")
#             else:
#                 booking.save()
#                 messages.success(request, 'Booking Successful')
#                 return redirect('booking_confirmation')  # Redirect to a booking confirmation page
#     else:
#         form = BookingForm()
        
#     return render(request, 'bookingpage.html', {'form': form})

# @login_required
# def user_bookings(request):
#     bookings = Booking.objects.filter(user=request.user)

#     if request.method == 'POST':
#         booking_id = request.POST.get("booking_id")
#         booking = get_object_or_404(Booking, id=booking_id, user=request.user)
#         form = BookingForm(request.POST, instance=booking)

#         if form.is_valid():
#             new_date = form.cleaned_data['date']
#             new_time_slot = form.cleaned_data['time_slot']
#             if Booking.objects.filter(date=new_date, time_slot=new_time_slot).exclude(id=booking_id).exists():
#                 messages.error(request, "This time slot is already booked. Please choose another.")
#             else:
#                 form.save()
#                 messages.success(request, 'Booking updated successfully.')
#                 return redirect('user_bookings')  # Reload the page to show updated bookings
#     else:
#         booking_forms = [(booking, BookingForm(instance=booking)) for booking in bookings]

#     return render(request, 'user_bookings.html', {'booking_forms': booking_forms})




@login_required
def booking_view(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        player_form = PlayerForm(request.POST)
        if booking_form.is_valid() and player_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            player = player_form.save(commit=False)
            player.booking = booking
            player.save()
            return redirect('my_bookings')
    else:
        booking_form = BookingForm()
        player_form = PlayerForm()
    return render(request, 'bookingpage.html', {'booking_form': booking_form, 'player_form': player_form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        player_formset = PlayerForm(request.POST, instance=booking)
        if booking_form.is_valid() and player_formset.is_valid():
            booking_form.save()
            player_formset.save()
            return redirect('my_bookings')
    else:
        booking_form = BookingForm(instance=booking)
        player_formset = PlayerForm(instance=booking)
    return render(request, 'edit_booking.html', {'booking_form': booking_form, 'player_formset': player_formset})
