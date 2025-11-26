from django.shortcuts import render
from .models import Album,Track
from datetime import timedelta

# Create your views here.
def populate_data(request):
    if Album.objects.exists():
        return

    album1 = Album.objects.create(title="The Dark Side of the Moon", artist="Pink Floyd", release_date="1973-03-01")
    album2 = Album.objects.create(title="Thriller", artist="Michael Jackson", release_date="1982-11-30")

    Track.objects.create(title="Speak to Me", album=album1, duration=timedelta(minutes=1, seconds=30))
    Track.objects.create(title="Time", album=album1, duration=timedelta(minutes=7, seconds=6))
    Track.objects.create(title="Thriller", album=album2, duration=timedelta(minutes=5, seconds=57))
    Track.objects.create(title="Billie Jean", album=album2, duration=timedelta(minutes=4, seconds=54))

def homepage(request):

    populate_data(request)

    albums=Album.objects.all()
    tracks=Track.objects.select_related("album").all()

    return render(request,"homepage.html",{'albums':albums,'tracks':tracks})