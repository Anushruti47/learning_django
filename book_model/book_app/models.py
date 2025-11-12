from django.db import models

# Create your models here.
class Book (models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()
    isbn=models.CharField(max_length=13)

    def __str__(self):
        return self.title
    
# python manage.py shell
# from book_app.models import Book

# new_book = Book(
#     title="Django for Beginners",
#     author="William S. Vincent",
#     publication_year=2020,
#     isbn="9781735467207"
# )
# new_book.save()
# Book.objects.all()

# <QuerySet [<Book: Django for Beginners>]>

