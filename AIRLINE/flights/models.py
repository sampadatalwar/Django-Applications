from django.db import models

# Create your models here.

class Flight(models.Model):
    origin = models.CharField(max_length = 64)
    destination = models.CharField(max_length = 64)
    duration = models.IntegerField()

    # returns string representation of objects
    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Airport(models.Model):
    city = models.CharField(max_length = 64)
    code = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.city} ({self.code})"