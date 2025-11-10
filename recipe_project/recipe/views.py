from django.shortcuts import render
from django.http import HttpResponse

RECIPES={
    "chicken":["Grilled Chicken Salad", "Chicken Alfredo Pasta", "Spicy Chicken Curry"],
    "tomato":["Tomato soup","Bruschetta","Caprese Salad"],
    "chocolate":["Chocolate Cake","Chocolate Mousse","Brownies"],
}

# Create your views here.

def recipe_finder(request,ingredient):
    recipes=RECIPES.get(ingredient.lower(),["No recipes found for this ingredient."])
    recipe_list="<ul>"+ "".join(f"<li>{recipe}</li>" for recipe in recipes) +"</ul>"
    return HttpResponse(
    f"""
    <h1>Recipes with {ingredient.capitalize()}</h1>
    {recipe_list}
    """
    )

