from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dev", views.dev, name="dev"),
    path("bojack", views.bojack, name="bojack"), 
    path("<str:name>", views.greet, name="greet")
]
