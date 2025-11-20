from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200,blank=False)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField(validators=[MinValueValidator(1800),MaxValueValidator(2023)])
    isbn=models.CharField(max_length=13,unique=True)
    genre=models.CharField(max_length=50,choices=[
        ('FIC','Fiction'),
        ('NON','Non-Fiction'),
        ('SCI','Science'),
        ('HIS','History')
    ])
    website=models.URLField(blank=True)

    def __str__(self):
        return self.title