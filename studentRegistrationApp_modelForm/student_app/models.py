from django.db import models

# Create your models here.
class Student(models.Model):
    CLASS_LEVEL_CHOICES=[
        ('1','Class 1'),
        ('2','Class 2'),
        ('3','Class 3'),
        ('4','Class 4'),
        ('5','Class 5'),
    ]
    SUBJECT_CHOICES=[
        ('maths','Mathematics'),
        ('science','Science'),
        ('eng','English'),
        ('history','History'),
        ('art','Arts')
    ]
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    class_level=models.CharField(choices=CLASS_LEVEL_CHOICES)
    favourite_subject=models.CharField(choices=SUBJECT_CHOICES)

    def __str__(self):
        return self.name