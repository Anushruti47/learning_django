from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Product Name")
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0, null=True)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(null=True, verbose_name="Customer Rating")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} - Rating: {self.rating}"
