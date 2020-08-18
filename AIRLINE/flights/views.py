from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight,Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id = flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights=flight).all() # Passengers excluding the ones that are already on this flight
    })

def book_flight(request, flight_id):
    if request.method == "POST":
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        flight = Flight.objects.get(pk=flight_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,))) 
    
