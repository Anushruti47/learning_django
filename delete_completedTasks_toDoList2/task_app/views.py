from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    return render(request,"home.html")

def tasks(request):
    if not Task.objects.exists():
        Task.objects.create(title="Buy groceries", completed=True)
        Task.objects.create(title="Do laundry", completed=False)
        Task.objects.create(title="Clean room", completed=True)
        Task.objects.create(title="Write report", completed=False)
    
    tasks=Task.objects.all()

    return render(request,"tasks.html",{'tasks':tasks})

def delete_completed_tasks(request):

    Task.objects.filter(completed=True).delete()
    
    tasks=Task.objects.all()

    return render(request,"tasks.html",{'tasks':tasks})