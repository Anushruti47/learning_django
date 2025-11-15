from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_movie(request):
    movie=Movie.objects.create(
        title="Inception",
        director="Christopher Nolan",
        release_year=2010,
        imdb_id="tt1375666"
    )

    all_movies=Movie.objects.all()

    context={
        'new_movie':movie,
        'all_movies':all_movies
    }

    return render(request,'movies.html',context)
