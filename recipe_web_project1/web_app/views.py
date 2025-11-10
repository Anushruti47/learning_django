from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def recipe_list(request):
    recipes=[
        "Spaghetti Carbonara",
        "Vegetable Stir Fry",
        "Chicken Curry",
        "Avocado Toast"
    ]
    return render(request,'recipe_list.html',{'recipes':recipes})
