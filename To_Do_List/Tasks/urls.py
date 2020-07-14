from django.urls import path
from . import views

# to avoid namespace collision
app_name = 'tasks'

urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.addTask, name = "addTask")
]