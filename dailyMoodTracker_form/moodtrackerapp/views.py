from django.shortcuts import render
from .forms import MoodTrackerForm

# Create your views here.
def track_mood(request):
    form=MoodTrackerForm()

    context={
        'form_title':"Mood Tracker App",
        'form':form
    }
    return render(request,"moodtracker.html",context)