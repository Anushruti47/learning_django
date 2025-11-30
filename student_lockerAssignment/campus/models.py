from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name
    
class Locker(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    locker_number=models.CharField(max_length=10,unique=True)
    location=models.CharField(max_length=10)

    def __str__(self):
        return f"Locker - {self.locker_number} for {self.student.name}"