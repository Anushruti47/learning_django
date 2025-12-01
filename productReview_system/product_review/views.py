from django.shortcuts import render
from .models import Product, Review
from datetime import datetime

def home(request):
    # Sample Data
    if not Product.objects.exists():
        p1 = Product.objects.create(name="Laptop", description="Gaming laptop", price=1500.0, in_stock=True)
        p2 = Product.objects.create(name="Headphones", price=200.0)
        
        Review.objects.create(product=p1, rating=5, comment="Excellent performance")
        Review.objects.create(product=p1, rating=4)
        Review.objects.create(product=p2, rating=3, comment="Decent sound quality")

    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


