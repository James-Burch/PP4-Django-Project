from django import forms
from .models import Booking, AvailableDate

class BookingForm(forms.ModelForm):
    date = forms.ModelChoiceField(queryset=AvailableDate.objects.all())
    time_slot = forms.ChoiceField(choices=Booking.TIME_SLOTS)

    class Meta:
        model = Booking
        fields = ['date', 'time_slot']
