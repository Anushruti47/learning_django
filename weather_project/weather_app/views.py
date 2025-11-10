from django.shortcuts import render

# Create your views here.
def weather_display(request):
    weather_data={
        'condition':'xyz',
        'temperature':70,
    }
    return render(request,'weather_app.html',weather_data)