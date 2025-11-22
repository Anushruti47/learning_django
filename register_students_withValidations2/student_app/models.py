from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Student(models.Model):
    COURSE_CHOICES=[
        ('CS','Computer Science'),
        ('ME','Mechanical Engineering'),
        ('EE','Electrical Engineeirng'),
        ('CE','Civil Engineering')
    ]
    name=models.CharField(blank=False,max_length=100)
    email=models.EmailField(blank=False,unique=True)
    roll_number=models.CharField(max_length=10,unique=True)
    course=models.CharField(choices=COURSE_CHOICES)
    year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])
    profile_url=models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
