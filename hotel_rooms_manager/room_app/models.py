from django.db import models

# Create your models here.
class Room(models.Model):
    room_number=models.IntegerField()
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price_per_night=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"{self.room_type} - Room{self.room_number}"
