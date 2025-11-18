from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    expiration_date=models.DateField()

    def __str__(self):
        return self.title