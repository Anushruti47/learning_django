from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=100)
    cooking_time=models.IntegerField()

    def __str__(self):
        return self.name