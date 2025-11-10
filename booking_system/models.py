from django.db import models

# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Trip Model
class Trip(models.Model):
    trip_name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    trip_image = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.trip_name} to {self.destination}"

# Ticket Model
class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Booked')
    
    def __str__(self):
        return f"Ticket for {self.customer.first_name} on {self.trip.trip_name}"
