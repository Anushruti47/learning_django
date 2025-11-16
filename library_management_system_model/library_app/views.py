from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import Book

def book_list(request):
    if not Book.objects.exists:
        Book.objects.create(title="Harry Potter",author="J.K. Rowling",publication_year=2002,isbn="9257641369874",genre="Fiction")
        Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2020, isbn="9781735467207", genre="Programming")
        Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937, isbn="9780547928227", genre="Fiction")
        Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960, isbn="9780061120084", genre="Fiction")
        Book.objects.create(title="A Brief History of Time", author="Stephen Hawking", publication_year=1988, isbn="9780553380163", genre="Science")
        Book.objects.create(title="The Pragmatic Programmer", author="Andrew Hunt", publication_year=1999, isbn="9780201616224", genre="Programming")
        Book.objects.create(title="Clean Code", author="Robert C. Martin", publication_year=2008, isbn="9780132350884", genre="Programming")
        Book.objects.create(title="1984", author="George Orwell", publication_year=1949, isbn="9780451524935", genre="Fiction")

    all_books=Book.objects.all()

    fiction_books=Book.objects.filter(genre="Fiction")

    try:
        first_book=Book.objects.get(id=1)
    except Book.DoesNotExist:
        first_book=None
    
    books_by_title=Book.objects.all().order_by('title')

    first_5_books=Book.objects.all()[:5]

    context={
        'all_books':all_books,
        'fiction_books':fiction_books,
        'first_book':first_book,
        'books_by_title':books_by_title,
        'first_5_books':first_5_books
    }
    return render(request,'book_list.html',context)
