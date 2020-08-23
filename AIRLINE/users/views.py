from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if not request.user.is_authenticated:       # request object has user attribute associated with it, which has is_authenticated attribute.
                                                    #is_authenticated attribute tells if user is signed in or not.
        return HttpResponseRedirect(reverse("login_view"))

    return render(request, "users/index.html")

def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    return render(request, "users/logout.html")
