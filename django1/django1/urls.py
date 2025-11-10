"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django_app import views
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Homepage!!")

urlpatterns = [
    # path("",include("django_app.urls")),
    # path("",views.home,name="home"),

    path("",home),
    path("home/",home),
    path("about/",views.about,name="about"),
    # path("blog1/",views.blog1,name="blog1"),
    path("services/",views.services,name="services"),
    # path('admin/', admin.site.urls),
]
