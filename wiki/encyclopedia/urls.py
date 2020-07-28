from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("NewPage", views.createNewPage, name="newPage"),
    path("test", views.test, name="test"),
    path("CreatePage", views.createPage, name="createPage"),
    path("EditPage/<str:title>", views.editPage, name= "editPage"),
    path("SaveEditedPage", views.saveEditedPage, name="saveEditedPage"),
    path("RandomPage", views.randomPage, name= "randomPage"),
    path("<str:title>", views.entryPage, name="entryPage")
    
]
