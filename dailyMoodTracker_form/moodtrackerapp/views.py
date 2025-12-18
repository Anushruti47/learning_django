from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import MoodTrackerForm

# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

@csrf_exempt
def track_mood(request):
    form=MoodTrackerForm()
    context={
        'form_title':"Mood Tracker App",
        'form':form
    }
    return render(request,"track_mood_page.html",context)