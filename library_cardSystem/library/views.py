from django.shortcuts import render
from .models import Patron, LibraryCard

# Create your views here.
def home(request):
    Patron.objects.all().delete()
    LibraryCard.objects.all().delete()

    # Create Patrons
    p1=Patron.objects.create(name="Alice",email="alice@example.com")
    p2=Patron.objects.create(name="Bob",email="bob@example.com")

    # Create Library Cards
    LibraryCard.objects.create(patron=p1,card_number="LC1001")
    LibraryCard.objects.create(patron=p2,card_number="LC1002")

    patrons=Patron.objects.all()

    return render(request,"home.html",{'patrons':patrons})