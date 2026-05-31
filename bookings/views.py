from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination, Airline, FlightOffer, Reservation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    error = None

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "register":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if User.objects.filter(username=email).exists():
                error = "Account with this email already exists."
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                login(request, user)
                return redirect("flights")

        elif action == "login":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("flights")
            else:
                error = "Invalid email or password."

    return render(request, "bookings/login.html", {"error": error})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def flights_view(request):
    destinations = Destination.objects.all()

    has_reservations = False

    if request.user.is_authenticated:
        has_reservations = Reservation.objects.filter(
            user=request.user
        ).exists()

    return render(request, 'bookings/flights.html', {
        'destinations': destinations,
        'has_reservations': has_reservations,
    })

@login_required
def booking_view(request, destination):
    selected_destination = get_object_or_404(Destination, name=destination)
    airlines = Airline.objects.all()
    offers = None
    trip_type = None
    departure_date = None
    return_date = None

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
        "trip_type": trip_type,
        "departure_date": departure_date,
        "return_date": return_date,
    })

@login_required
def reserve_flight(request, flight_id):
    if request.method != "POST":
        return redirect("flights")

    flight = get_object_or_404(FlightOffer, id=flight_id)

    trip_type = request.POST.get("trip_type", "one_way")
    departure_date = request.POST.get("departure_date")
    return_date = request.POST.get("return_date") or None

    if not departure_date:
        return redirect("flights")

    already_reserved = Reservation.objects.filter(
        user=request.user,
        destination=flight.to_destination.name,
        departure_city=flight.from_city,
        airline=flight.airline.name,
        departure_date=departure_date,
        return_date=return_date,
    ).exists()

    if not already_reserved:
        Reservation.objects.create(
            user=request.user,
            destination=flight.to_destination.name,
            departure_city=flight.from_city,
            airline=flight.airline.name,
            price=flight.price,
            baggage=flight.baggage_included,
            trip_type=trip_type,
            departure_date=departure_date,
            return_date=return_date,
        )

    return redirect("reservations")

@login_required
def reservations(request):
    reservations = Reservation.objects.filter(
        user=request.user
    ).order_by("-created_at")
    return render(request, "bookings/reservations.html", {
        "reservations": reservations
    })

