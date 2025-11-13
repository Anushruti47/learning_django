from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.CharField(max_length=200)
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.name


product=Product(
    name="MacBook Air",
    price=67000,
    description="MacBook Air M1, 8GB RAM,256 GB SSD",
    stock=50
)

product=Product(
    name="HP Intel Core",
    price=43000,
    description="i3 12th generation, 8GB RAM,512 GB SSD",
    stock=80
)