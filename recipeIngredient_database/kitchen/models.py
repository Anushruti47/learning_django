from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.ManyToManyField(Ingredient,related_name='recipes')

    def __str__(self):
        return self.name