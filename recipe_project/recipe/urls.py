from django.urls import path
from recipe import views

urlpatterns=[
    path("recipe/<str:ingredient>",views.recipe_finder,name="recipe_finder"),

]