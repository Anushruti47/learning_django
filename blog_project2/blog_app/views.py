from django.shortcuts import render
from datetime import datetime

# Create your views here.
def weather_report(request):
    report={
            "city":"london",
            "temperature":13.59845,
            "condition":"partly cloudy",
            "forecast":"lights showers expected in the evening carry an umbrella.lights showers expected in the evening carry an umbrella."
            "lights showers expected in the evening carry an umbrella.",
            "time":datetime(2025, 4, 11, 23, 30),
            # "time":datetime.now()
        }
    return render(request,"blog_app.html",report)





