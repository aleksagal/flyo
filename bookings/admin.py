from django.contrib import admin
from .models import Destination, Airline, FlightOffer, Reservation

admin.site.register(Destination)
admin.site.register(Airline)
admin.site.register(FlightOffer)
admin.site.register(Reservation)