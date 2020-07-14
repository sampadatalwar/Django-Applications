from django.shortcuts import render
#from django.http import HttpResponse

tasks = ["A", "B", "C"]
# Create your views here.
def index(request):
    return render(request, "Tasks/to-do.html",{
        "tasks": tasks
    })

def addTask(request):
    return render(request, "Tasks/addTask.html")