from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"base.html")

# def recipe_list(request):
#     recipe_list=["Spaghetti Carbonara","Vegetable Stir Fry","Chicken Curry","Avocado Toast"]
#     return render(request,"recipe_app.html",{'recipe_list' : recipe_list})




