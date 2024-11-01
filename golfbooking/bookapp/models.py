from django.db import models
from django.contrib.auth.models import User
from datetime import date, time, datetime

# Create your models here.
class AvailableTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    # Check if a time is already booked
    is_booked = models.BooleanField(default=False)

class Meta:
    # Stop duplicate dates/times
    unique_together = ('date', 'time')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slot = models.OneToOneField(AvailableTime, on_delete=models.CASCADE, null=True, default=1)
    booked_at = models.DateTimeField(default=datetime.now)
