from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="Booking"),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path("register/", views.register, name="Register"),
]