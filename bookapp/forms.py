from django import forms
from .models import Booking, Player

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']
        widgets = {
            'date': forms.SelectDateWidget(),  # Provides a dropdown
            'time': forms.Select(choices=[
                ('09:00:00', '9:00 AM'),
                ('10:00:00', '10:00 AM'),
                ('11:00:00', '11:00 AM'),
                ('12:00:00', '12:00 PM'),
                ('13:00:00', '1:00 PM'),
                ('14:00:00', '2:00 PM'),
                ('15:00:00', '3:00 PM'),
                ('16:00:00', '4:00 PM'),
            ]),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']
