from django.contrib import admin
from django.urls import path, include
from SimpleApp.views import index

urlpatterns = [
    path('', index),
]
