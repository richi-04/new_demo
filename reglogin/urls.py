from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.update_profile),
    path("login", views.login_request),
    path("home",views.home)
]