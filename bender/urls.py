from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('bender-selection/', bender_selection, name='bender'),
]