from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title=models.CharField(max_length=200)
    director=models.CharField(max_length=100)
    release_year=models.IntegerField()
    rating=models.FloatField()
    review_text=models.TextField(max_length=200)

    def __str__(self):
        return self.movie_title
