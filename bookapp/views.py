from django.shortcuts import render, redirect, get_object_or_404
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
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        if 'save_changes' in request.POST:
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                booking_form.save()
            return redirect('my_bookings')
        
        elif 'delete_booking' in request.POST:
            booking.delete()
            return redirect('my_bookings')
    
    else:
        booking_form = BookingForm(instance=booking)
        player_form = PlayerForm()  

    return render(request, 'edit_booking.html', {
        'booking_form': booking_form,
        'player_form': player_form,
        'booking': booking
    })
