from django.shortcuts import render
from .models import Ingredient,Recipe

# Create your views here.
def home(request):
    # Delete all previous data
    Ingredient.objects.all().delete()
    Recipe.objects.all().delete()

    # Create ingredients
    flour=Ingredient.objects.create(name="Flour")
    butter=Ingredient.objects.create(name="Butter")
    milk=Ingredient.objects.create(name="Milk")
    sugar=Ingredient.objects.create(name="Sugar")
    egg=Ingredient.objects.create(name="Egg")
    chocolate=Ingredient.objects.create(name="Chocolate")
    soda=Ingredient.objects.create(name="Baking Soda")

    # Create recipes
    cake=Recipe.objects.create(name="Cake")
    sweet=Recipe.objects.create(name="Sweet")
    cookie=Recipe.objects.create(name="Cookie")

    # Add the ingredients to the recipes
    cake.ingredients.add(flour,butter,soda) 
    
    # Add the ingredients to the recipes
    sweet.ingredients.add(milk,sugar)

    # Add the ingredients to the recipes
    cookie.ingredients.add(chocolate,egg,sugar)

    ingredients=Ingredient.objects.all()
    recipes=Recipe.objects.all()

    return render(request,"home.html",{'ingredients':ingredients,'recipes':recipes})