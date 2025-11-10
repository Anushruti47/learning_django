from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def movie_detail(request, movie_id, title):
    return HttpResponse(
        f"""
    <h1>Movie Details</h1>
    <p><strong>ID:</strong>{movie_id}</p>
    <p><strong>Title:</strong>{title}</p>
"""
    )
