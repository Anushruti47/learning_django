from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

from .models import Movie

def update_movie_rating(request):
    if not Movie.objects.exists():
        Movie.objects.create(title="Inception", director="Christopher Nolan", release_year=2010, rating=8.8)
        Movie.objects.create(title="The Matrix", director="The Wachowskis", release_year=1999, rating=8.7)
        Movie.objects.create(title="Interstellar", director="Christopher Nolan", release_year=2014, rating=8.6)
        Movie.objects.create(title="Parasite", director="Bong Joon-ho", release_year=2019, rating=8.6)
        Movie.objects.create(title="Spirited Away", director="Hayao Miyazaki", release_year=2001, rating=8.6)

    try:
        movie=Movie.objects.get(id=1)
        old_rating=movie.rating
        movie.rating=9.2
        movie.save()

        message=f"Updated rating of '{movie.title}' from {old_rating} to {movie.rating}"

    except Movie.DoesNotExist:
        message="Movie not found"

    return render(request,"update_movie_rating.html",{'message':message})