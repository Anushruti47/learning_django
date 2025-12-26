from django import path
from feedbackapp import views

urlpatterns=[
    path("",views.homepage,name="homepage"),
    path("home/",views.homepage,name="homepage"),
]