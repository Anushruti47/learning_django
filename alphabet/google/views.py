from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Know more about our company here!!")

def services(request):
    return HttpResponse("Explore the services explored by our company here...")
