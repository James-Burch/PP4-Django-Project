from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="Booking"),
    path('create-booking/', views.create_booking, name='create_booking'),
    path("register/", views.register, name="Register"),
]