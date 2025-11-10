from django.urls import path
from weather_app import views

urlpatterns=[
    path("",views.weather_display,name='weather_display'),
]