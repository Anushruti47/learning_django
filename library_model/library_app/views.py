from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_book(request):
    book=Book.objects.create(
        isbn="9781735467207",
        title= "Django for Beginners",
        author= "William S. Vincent",
        publication_year= 2020        
    )
    all_books=Book.objects.all()
    context={
        'new_book':book,
        'all_books':all_books
    }
    return render(request,'books.html',context)