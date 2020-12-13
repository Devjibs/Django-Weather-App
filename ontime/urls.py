from django.contrib import admin
from django.urls import path
from . import views
from .views import search_it

urlpatterns = [
    path('search_it', views.search_it),
]
