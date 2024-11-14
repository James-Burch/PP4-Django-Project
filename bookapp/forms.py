from django import forms
from .models import Booking, Player

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']
