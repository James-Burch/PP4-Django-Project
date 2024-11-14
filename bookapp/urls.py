from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="Register"),
    path('booking/', views.booking_view, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]