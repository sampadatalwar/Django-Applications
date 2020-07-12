from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello") # HttpResponse is a class created by Django. It needs to be imported.

def greet(request, name):
    return HttpResponse("Hello "+ name.capitalize())  

def greetUser(request, name):
    return render(request, "hello/greet.html",{     # Rendering external html page. greet.html is present in templates/hello directory
        "name": name.capitalize()
    }) 

"""
Instead of keeping file greet.html in templates, we keep it in templates/hello in order to namespace the html files.
So if there are multiple html files with same name in multiple different apps, they don't conflict with each other.
Hence it is Django best practice to namespace html files like this.

"""
