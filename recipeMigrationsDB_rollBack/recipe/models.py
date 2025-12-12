from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=200)
    ingredient=models.TextField()
    cookingTime=models.FloatField()

    def __str__(self):
        return self.name
