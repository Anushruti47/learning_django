from django.urls import path
from clinicapp import views

urlpatterns=[
    path("",views.homepage,name="homepage"),
    path("request-appoinment/",views.request_appointment,name="request_appointment"),
    path("home/",views.homepage,name="homepage"),
]