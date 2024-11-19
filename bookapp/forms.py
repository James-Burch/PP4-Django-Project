from django import forms
from .models import Booking, Player


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']
        widgets = {
            'date': forms.SelectDateWidget(attrs={
                    'aria-label': 'Select booking date',
                }),  # Provides a dropdown
            'time': forms.Select(choices=[
             ('07:00:00', '7:00 AM'),
             ('07:12:00', '7:12 AM'),
             ('07:24:00', '7:24 AM'),
             ('07:36:00', '7:36 AM'),
             ('07:48:00', '7:48 AM'),
             ('08:00:00', '8:00 AM'),
             ('08:12:00', '8:12 AM'),
             ('08:24:00', '8:24 AM'),
             ('08:36:00', '8:36 AM'),
             ('08:48:00', '8:48 AM'),
             ('09:00:00', '9:00 AM'),
             ('09:12:00', '9:12 AM'),
             ('09:24:00', '9:24 AM'),
             ('09:36:00', '9:36 AM'),
             ('09:48:00', '9:48 AM'),
             ('10:00:00', '10:00 AM'),
             ('10:12:00', '10:12 AM'),
             ('10:24:00', '10:24 AM'),
             ('10:36:00', '10:36 AM'),
             ('10:48:00', '10:48 AM'),
             ('11:00:00', '11:00 AM'),
             ('11:12:00', '11:12 AM'),
             ('11:24:00', '11:24 AM'),
             ('11:36:00', '11:36 AM'),
             ('11:48:00', '11:48 AM'),
             ('12:00:00', '12:00 PM'),
             ('12:12:00', '12:12 PM'),
             ('12:24:00', '12:24 PM'),
             ('12:36:00', '12:36 PM'),
             ('12:48:00', '12:48 PM'),
             ('13:00:00', '1:00 PM'),
             ('13:12:00', '1:12 PM'),
             ('13:24:00', '1:24 PM'),
             ('13:36:00', '1:36 PM'),
             ('13:48:00', '1:48 PM'),
             ('14:00:00', '2:00 PM'),
             ('14:12:00', '2:12 PM'),
             ('14:24:00', '2:24 PM'),
             ('14:36:00', '2:36 PM'),
             ('14:48:00', '2:48 PM'),
             ('15:00:00', '3:00 PM'),
             ('15:12:00', '3:12 PM'),
             ('15:24:00', '3:24 PM'),
             ('15:36:00', '3:36 PM'),
             ('15:48:00', '3:48 PM'),
             ('16:00:00', '4:00 PM')],
             attrs={
                    'aria-label': 'Select booking date',
                }),
        }


class PlayerForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Player
        fields = ['name']
