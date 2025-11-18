from django.shortcuts import render
from .models import Tasks

# Create your views here.
def home(request):
    return render(request,"home.html")

def tasks(request):
    if not Tasks.objects.exists():
        Tasks.objects.create(title="Buy groceries", completed=True)
        Tasks.objects.create(title="Do laundry", completed=False)
        Tasks.objects.create(title="Clean room", completed=True)
        Tasks.objects.create(title="Write report", completed=False)

    tasks=Tasks.objects.all()

    return render(request,"tasks.html",{'tasks':tasks})

def delete_completed_tasks(request):
    
    Tasks.objects.filter(completed=True).delete()

    tasks=Tasks.objects.all()
    
    return render(request,"tasks.html",{'tasks':tasks})
