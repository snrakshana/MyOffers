from django.urls import path
from . import views

urlpatterns = [
    path("home", views.homepage, name="home"),
    path("navbar", views.navbar, name="navbar"),

]
