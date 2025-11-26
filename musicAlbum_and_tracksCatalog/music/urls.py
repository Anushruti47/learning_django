from django.urls import path
from music import views

urlpatterns=[
    path("",views.homepage,name="homepage"),
    path("home/",views.homepage,name="homepage"),
]