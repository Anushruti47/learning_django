from django.shortcuts import render
from .models import Author,Book
from datetime import date

# Create your views here.
def home(request):
    return render(request,"home.html")

def book_list(request):
    if not Author.objects.exists():
        author1=Author.objects.create(name="George Orwell", birth_date=date(1903, 6, 25))
        author2 = Author.objects.create(name="J.K. Rowling", birth_date=date(1965, 7, 31))

        Book.objects.create(title="1984", author=author1, publication_date=date(1949, 6, 8), isbn="1234567890123")
        Book.objects.create(title="Animal Farm", author=author1, publication_date=date(1945, 8, 17), isbn="1234567890124")
        Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2, publication_date=date(1997, 6, 26), isbn="1234567890125")

    books=Book.objects.select_related("author").all()
    return render(request,"books.html",{"books":books})
