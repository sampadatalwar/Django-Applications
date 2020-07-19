from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "Tasks/to-do.html",{
        "tasks": request.session["tasks"]
    })

class AddTaskForm(forms.Form):      # Creating a form class, inheriting from forms.Form
    newTask = forms.CharField(label= "Enter new task")


def addTask(request):
    if request.method  == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["newTask"]     # Forms only get a cleaned_data attribute when is_valid() has been called
            request.session["tasks"] += [task]
            #tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index")) # app_name:path name
            #return render(request, "Tasks/to-do.html",{"tasks": tasks})
        else:
            return render(request, "Tasks/addTask.html",{
        "form" : form
        })
    return render(request, "Tasks/addTask.html",{
        "form" : AddTaskForm()
    })