from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)
    release_year=models.IntegerField()
    rating=models.FloatField()

    def __str__(self):
        return self.title
    
    # from movie_app.models import Movie
    # Movie.objects.all().delete()

    # new_movie = Movie(
    #     title="Birdman",
    #     genre="Comedy/Drama",
    #     release_year=2014,
    #     rating=7.7
    # )
    # new_movie.save()

# new_movie = Movie(
#         title="Amaran",
#         genre="Romantic",
#         release_year=2024,
#         rating=8.1
#     )