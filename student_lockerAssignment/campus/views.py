from django.shortcuts import render
from .models import Student,Locker

# Create your views here.
def homepage(request):

    # Delete all previous records
    Student.objects.all().delete()
    Locker.objects.all().delete()

    # Create Students
    s1=Student.objects.create(name="Alice",roll_number="S101")
    s2=Student.objects.create(name="Bob",roll_number="S102")

    # Create lockers
    Locker.objects.create(student=s1,locker_number="L101",location="Kashi")
    Locker.objects.create(student=s2,locker_number="L102",location="Ujjain")

    students=Student.objects.all()
    # lockers=Locker.objects.all()

    return render(request,"homepage.html",{'students':students})

