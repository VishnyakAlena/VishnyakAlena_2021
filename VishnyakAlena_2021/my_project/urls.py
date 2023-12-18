from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('my_project/', views.my_project),
]