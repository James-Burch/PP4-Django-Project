from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("booking/", views.booking, name="Booking"),
    # path('create-booking/', views.create_booking, name='create_booking'),
    # path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    # path('my-bookings/', views.user_bookings, name='user_bookings'),
    path("register/", views.register, name="Register"),


    path('booking/', views.booking_view, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]