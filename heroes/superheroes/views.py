from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def superheroes_home(request):
    return HttpResponse(
        f"""
    <h1>Welcome to the Superheroes Database</h1>
    <p>Discover your favourite superheroes</p>
    <ul>
        <li>Spider-Man</li>
        <li>Iron Man</li>
        <li>Wonder Woman</li>
    </ul>
    <p>Append the path that you created for each superheroes after /superheroes to see their profiles.</p>
    """
    )


def spiderman_review(request):
    return HttpResponse(
        f"""
    <h1>Spider-Man</h1>
    <p><strong>Real name:</strong>Peter Parker</p>
    <p><strong>Powers:</strong>Super strength, agility, wall-crawing, web shooting.</p>
    <p><strong>Bio:</strong>Bitten by a radioactive spider, Peter Parker fights crime as spider-man.</p>    
    """
    )


def ironman_review(request):
    return HttpResponse(
        f"""
    <h1>Iron Man</h1>
    <p><strong>Real name:</strong>Tony Stark</p>
    <p><strong>Powers:</strong>Genius intellect, powered armor suit, advanced weaponary.</p>
    <p><strong>Bio:</strong>A billionaire genius who built a high-tech suit to protect the world.</p>    
    """
    )

def wonderwoman_review(request):
    return HttpResponse(
        f"""
    <h1>Wonder Woman</h1>
    <p><strong>Real name:</strong>Diana Prince</p>
    <p><strong>Powers:</strong>Super strength, speed, flight, magic also.</p>
    <p><strong>Bio:</strong>An Amazon warrier princess who fights for justice and peace.</p>    
    """
    )
