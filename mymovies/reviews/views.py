from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(""
    "<h2>Welcome to Movie Reviews</h2>" \
    "<p>Check out reviews for some amazing movies</p>" \
    "<ul>"
    "<li>Inception</li>" \
    "<li>Interstellar</li>" \
    "<li>The Dark Knight</li>" \
    "</ul>" \
    "<p>Append the movies title in lowercase without spaces after reviews/ to see the reviews.</p>")

def inception_review(request):
    return HttpResponse(f"""
        <h2>Inception(2010)</h2>
        <p><strong>Rating 8.8/10</strong></p>    
        <p><strong>Review:</strong> A mind-blowing thriller with stunning visuals and a complex storyline.</p>
    """)

def interstellar_review(request):
    return HttpResponse(f"""
        <h2>Interstellar(2014)</h2>
        <p><strong>Rating 8.6/10</strong></p>    
        <p><strong>Review:</strong> A visually stunning space epic exploring love, time and survival.</p>
    """)

def the_dark_knight_review(request):
    return HttpResponse(f"""
        <h2>The Dark Knight(2008)</h2>
        <p><strong>Rating 9.0/10</strong></p>    
        <p><strong>Review:</strong> A masterpiece featuring an iconic Joker performance by Health Ledger.</p>
    """)
