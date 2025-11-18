from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import Book

def update_book_year_demo(request):
    if not Book.objects.exists():
        Book.objects.create(title="Django Basics",author="John Doe",publication_year=2018)
    # Book.objects.create(title="Django Basics",author="John Doe",publication_year=2018)

    try:
        book=Book.objects.get(id=1)
        old_year=book.publication_year

        # Update the publication year
        book.publication_year=2025
        book.save()

        message=f"Updated {book.title} from {old_year} to {book.publication_year}"

    except Book.DoesNotExist:
        message="Book not Found"

    return render(request,"update_book_year.html",{'message':message})

