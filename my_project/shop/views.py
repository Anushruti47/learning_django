from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my shop page!! You can redirect to about/ , details/ page as well...")
def about(request):
    return HttpResponse("This is about my shop...")
def details(request):
    return HttpResponse("These are the details of my shop page..." \
    "1. My shop is located in Jamsehdpur" \
    "2.My shop is open to all types of IT services")
