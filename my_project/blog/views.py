from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my blog page...u can visit about/ ,blog1/, blog2/ , blog3/ , blog4/ ")
def about(request):
    return HttpResponse("This is my about page!")
def blog1(request):
    return HttpResponse("Welcome to my blog1 page")
def blog2(request):
    return HttpResponse("Welcome to my blog2 page")
def blog3(request):
    return HttpResponse("Welcome to my blog3 page")
def blog4(request):
    return HttpResponse("Welcome to my blog4 page")