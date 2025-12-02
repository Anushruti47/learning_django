from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name="Event name")
    description=models.TextField(blank=True)
    fee=models.FloatField(default=0.0,null=True)
    is_online=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="registrations")
    participant_name=models.CharField(max_length=100,verbose_name="Participant Name")
    participant_email=models.EmailField(null=True)
    number_of_tickets=models.IntegerField(default=1)
    registered_at=models.DateTimeField(null=True,verbose_name="Registered At")

    def __str__(self):
        return f"{self.participant_name} - {self.event.name}"