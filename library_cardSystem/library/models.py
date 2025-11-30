from django.db import models

# Create your models here.
class Patron(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class LibraryCard(models.Model):
    patron=models.OneToOneField(Patron,on_delete=models.CASCADE)
    card_number=models.CharField(max_length=10,unique=True)
    issue_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Card {self.card_number} - {self.patron.name}"
