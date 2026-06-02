from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    starting_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="destinations/", null=True, blank=True)

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FlightOffer(models.Model):
    from_city = models.CharField(max_length=100)
    to_destination = models.ForeignKey(Destination, on_delete=models.CASCADE,null=True, blank=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)
    baggage_included = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_city} → {self.to_destination} | {self.airline} | {self.price}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    baggage = models.BooleanField(default=True)
    trip_type = models.CharField(max_length=20, default="One way")
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.departure_city} → {self.destination}"
