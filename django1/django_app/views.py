from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Home page....Welcome to my first Django app")

def about(request):
    return HttpResponse("Google, now a subsidiary of Alphabet Inc., is a multinational technology company founded in 1998 by Larry Page and Sergey Brin, " \
    "known primarily for its revolutionary search engine. " \
    "It also provides a vast array of Internet services, software, hardware, and cloud computing products, including Chrome, Gmail, and Android." \
    " Headquartered in Mountain View, California, Google's mission is to organize the world's information and make it universally accessible and useful, " \
    "with its advertising business generating the majority of its revenue.")

# def blog1(request):
#     return HttpResponse("Welcome to my blog page!")

def services(request):
    return HttpResponse("Google offers Gmail for email,[169] Google Calendar for time-management and scheduling,[170] Google Maps and Google Earth for mapping, navigation and satellite imagery,[171] Google Drive for cloud storage of files,[172] Google Docs, Sheets and Slides for productivity,[172] Google Photos for photo storage and sharing,[173] Google Keep for note-taking,[174] Google Translate for language translation,[175] YouTube for video viewing and sharing,[176] Google My Business for managing public business information,[177] Google Classroom for managing assignments and communication in education,[178] and Duo for social interaction.[179] A job search product has also existed since before 2017,[180][181][182] Google for Jobs is an enhanced search feature that aggregates listings from job boards and career sites.[183] Google Earth, launched in 2005, allows users to see high-definition satellite pictures from all over the world for free through a client software downloaded to their computers.[184]")
