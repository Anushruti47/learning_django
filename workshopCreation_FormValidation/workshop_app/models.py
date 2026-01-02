from django.db import models

# Create your models here.
class Workshop(models.Model):
    title=models.CharField(max_length=200)
    max_participants=models.IntegerField()
    registration_deadline=models.DateField()
    workshop_date=models.DateField()

    def __str__(self):
        return self.title