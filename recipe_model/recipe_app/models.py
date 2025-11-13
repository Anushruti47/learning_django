from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=100)
    cooking_time=models.IntegerField()
    difficulty=models.CharField(max_length=50,default="Medium")
    state=models.CharField(max_length=100,default="Jharkhand")

    def __str__(self):
        return self.name
    
# recipe = Recipe(
#     name="Pasta Primavera",
#     cuisine="Italian",
#     cooking_time=30,
#     difficulty="easy",
#     state="Haryana"
# )

# recipe = Recipe(
#     name="Idli Dosa",
#     cuisine="South Indian",
#     cooking_time=15
# )

# print("New Recipe created:")
# print(f"Recipe Name: {recipe.name}")
# print(f"Cuisine: {recipe.cuisine}")
# print(f"Cooking Time: {recipe.cooking_time}")
# print(f"Difficulty: {recipe.difficulty}")