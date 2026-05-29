from django.shortcuts import render, redirect
from .models import Destination, Airline, FlightOffer, Reservation

def login_view(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if first_name and last_name and email and phone:
            return redirect('flights')

    return render(request, 'bookings/login.html')


def flights_view(request):
    destinations = Destination.objects.all()

    return render(request, 'bookings/flights.html', {
        'destinations': destinations
    })

def booking_view(request, destination):
    selected_destination = Destination.objects.get(name=destination)
    airlines = Airline.objects.all()
    offers = None

    if request.method == "POST":
        from_city = request.POST.get("from_city")
        airline_id = request.POST.get("airline")
        trip_type = request.POST.get("trip_type")
        departure_date = request.POST.get("departure_date")
        return_date = request.POST.get("return_date")

        offers = FlightOffer.objects.filter(
            from_city=from_city,
            to_destination=selected_destination
        )

        if airline_id:
            offers = offers.filter(airline_id=airline_id)

    return render(request, "bookings/booking.html", {
        "destination": destination,
        "airlines": airlines,
        "offers": offers,
    })


# Create your views here.
