from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greetUser, name="greet") # custom route that allows us to specify any string in the url 
]