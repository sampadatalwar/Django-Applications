from django.db import models

# Create your models here.

#subclass of Model
class Airport(models.Model):
    city = models.CharField(max_length = 64)
    code = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # returns string representation of objects
    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    flights = models.ManyToManyField(Flight, blank = True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

