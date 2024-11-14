# from django.db import models
# from django.contrib.auth.models import User
# from datetime import date, time, datetime
# from django import forms

# Create your models here.

# class AvailableDate(models.Model):
#     date = models.DateField(unique=True)

#     def __str__(self):
#         return str(self.date)

# class Booking(models.Model):
#     TIME_SLOTS = [
#         ('9:00 AM', '9:00 AM'),
#         ('12:00 PM', '12:00 PM'),
#         ('3:00 PM', '3:00 PM'),
#         ('6:00 PM', '6:00 PM'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.ForeignKey(AvailableDate, on_delete=models.CASCADE)
#     time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('date', 'time_slot')

#     def __str__(self):
#         return f"{self.user} - {self.date} at {self.time_slot}"

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"

class Player(models.Model):
    booking = models.ForeignKey(Booking, related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

