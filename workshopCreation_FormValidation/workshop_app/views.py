from django.shortcuts import render,redirect
from .forms import WorkshopForm
from .models import Workshop

# Create your views here.
def create_workshop_view(request):
    if request.method=="POST":
        form=WorkshopForm(request.POST)
        if form.is_valid():
            Workshop.objects.create(
                title=form.cleaned_data['title'],
                max_participants=form.cleaned_data['max_participants'],
                registration_deadline=form.cleaned_data['registration_deadline'],
                workshop_date=form.cleaned_data['workshop_date'],
            )
            return redirect("success_message")
    else:
        form=WorkshopForm()
    return render(request,"create_workshop.html",{'form':form})

def success_message_view(request):
    return render(request,"success_message.html")