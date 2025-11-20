from django.shortcuts import render
from .models import Book
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

def create_books(request):
    messages = []

    # Only create sample data if DB is empty
    if not Book.objects.exists():
        sample_books = [
            {'title': 'Valid Book 1', 'author': 'Author A', 'publication_year': 2022,
             'isbn': '1111111111111', 'genre': 'FIC', 'website': 'https://example.com'},
            {'title': '', 'author': 'Author B', 'publication_year': 2010,
             'isbn': '2222222222222', 'genre': 'NON', 'website': 'https://example.com'},  # Invalid: title blank
            {'title': 'Valid Book 2', 'author': 'Author C', 'publication_year': 2018,
             'isbn': '1111111111111', 'genre': 'SCI', 'website': 'not-a-url'},  # Invalid: duplicate ISBN and bad URL
        ]

        for data in sample_books:
            try:
                book = Book(**data)
                book.full_clean()  # Run validations
                book.save()
                messages.append(f"✅ Added: {book.title}")
            except (ValidationError, IntegrityError) as e:
                messages.append(f"❌ Error adding book '{data.get('title', 'Unnamed')}': {e}")

    books = Book.objects.all()
    return render(request, 'books.html', {'books': books, 'messages': messages})

def home(request):
    return render(request, 'home.html')

