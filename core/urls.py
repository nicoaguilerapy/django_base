from ast import Or
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('', home, name='home'),
]