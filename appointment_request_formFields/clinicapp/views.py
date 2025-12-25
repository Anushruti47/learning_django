from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import AppointmentForm

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

@csrf_exempt
def request_appoinment(request):
    form=AppointmentForm()
    context={
        'form':form,
    }
    return render(request,"request_appointment.html",context)

