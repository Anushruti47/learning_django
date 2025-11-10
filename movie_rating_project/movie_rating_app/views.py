from django.shortcuts import render

# Create your views here.
def movie_rating(request):
    movie={
        'title':"Inception",
        'rate':9,
    }
    return render(request,'movie_rating_app.html',movie)