from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name=models.CharField(max_length=200)
    students=models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name