from django.http import request
from django.urls import path
from .views import HomePageView


urlpatterns=[ 
    path('', HomePageView, name='home'),
]