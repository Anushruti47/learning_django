from django.urls import path
from recipe_app import views

urlpatterns=[
    path('recipe/',views.recipe,name="recipe"),
]