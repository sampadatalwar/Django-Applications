import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "birthday/isItBirthday.html",{
        "birthday" : now.month == 8 and now.day == 27       # value of birthday will be true when its 27/08
    })