from django.db import models

# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=200)
    artist=models.CharField(max_length=100)
    release_date=models.DateField()

    def __str__(self):
        return self.title
    
class Track(models.Model):
    title=models.CharField(max_length=200)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    duration=models.DurationField()

    def __str__(self):
        return f"{self.title} ({self.album.title})"
