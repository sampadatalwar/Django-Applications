from django.shortcuts import render
import markdown2
from markdown2 import Markdown
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from django.db.models import Q

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(
        label = "Content",
        widget=forms.Textarea(
            attrs={
                "rows":10, 
                "cols":40
                }
        )
    )

class EditForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows":10, 
                "cols":40
                }
        )
    )


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    markdowner=Markdown()
    return render(request,"encyclopedia/entryPage.html",{
        "title" : title,
        "content": markdowner.convert(util.get_entry(title))    # Converting markdown into html format before passing into template.
    })

def createPage(request):
    if request.method  == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "encyclopedia/createPage.html",{
        "form" : NewPageForm()
        })
    return render(request, "encyclopedia/createPage.html",{
        "form" : NewPageForm()
    })

def editPage(request, title):
    if request.method  == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))

    else:
        populatedForm = NewPageForm({
        "title" : title,
        "content" : util.get_entry(title)
    })
    return render(request, "encyclopedia/editPage.html",{
        "form" : populatedForm
        })
    
def saveEditedPage(request):
    if request.method  == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "encyclopedia/editPage.html",{
            "form" : NewPageForm()
            })

def randomPage(request):
    entry = random.choice(util.list_entries())
    return entryPage(request,entry)


def search(request):

    string = request.GET.get('q')
    entries = util.list_entries()
    results = []
    for e in entries:
        if (string.lower() in e.lower()):
            results.append(e)

    return render(request, "encyclopedia/index.html", {
        "entries": results
    })


