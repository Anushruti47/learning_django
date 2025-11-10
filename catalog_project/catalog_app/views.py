from django.shortcuts import render

# Create your views here.
def catalog_categories(request):
    catalog=[
        {
            "category": "Electronics",
            "products":[
                {"name":"Smartphone","price":699},
                {"name":"Laptop","price":999},
                {"name":"Bluetooth speaker","price":129},
            ]
        },
        {
            "category": "Home Appliances",
            "products":[
                {"name":"Air Conditioner","price":499},
                {"name":"Refrigerator","price":799},
                {"name":"Microwave oven","price":199},
            ]
        },
        {
            "category": "Books",
            "products":[
                {"name":"Atomic Habits","price":20},
                {"name":"Deep Work","price":18},
                {"name":"Clean Code","price":35},
            ]
        },
    ]
    return render(request,"catalog_app.html",{"catalog": catalog})