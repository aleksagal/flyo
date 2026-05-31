from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('flights/', views.flights_view, name='flights'),
    path('booking/<str:destination>/', views.booking_view, name='booking'),
    path('reserve/<int:flight_id>/', views.reserve_flight, name='reserve_flight'),
    path('reservations/', views.reservations, name='reservations'),
]