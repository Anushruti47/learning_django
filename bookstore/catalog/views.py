from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the catalog of authors and books!!</h1>")


def author_page(request, username):
    return HttpResponse(
        f"""
        <h1>Author Page</h1>
        <p>Books by {username}</p>
        """
    )


def book_page(request, book_id):
    return HttpResponse(
    f"""
    <h1>Book Details</h1>
    <p>Details for book with ID:{book_id}</p>
    """
    )
