from django.shortcuts import render
from .models import Student, Course

def home(request):
    # Delete previous data
    Student.objects.all().delete()
    Course.objects.all().delete()

    # Create students
    alice=Student.objects.create(name="Alice")
    bob=Student.objects.create(name="Bob")
    carol=Student.objects.create(name="Carol")

    # Create courses
    python=Course.objects.create(name="Python")
    web=Course.objects.create(name="Web")
    django=Course.objects.create(name="Django")

    # Enroll Alice and Bob to python
    python.students.add(alice,bob)

    # Enroll Alice in Web
    web.students.add(alice)

    # Enroll carol in django
    django.students.add(carol,alice,bob)

    # Remove bob from python 
    python.students.remove(bob)

    # Clear students from web
    web.students.clear()

    # Enroll only carol in web
    web.students.set([carol])
    web.students.remove(carol)

    # Access alll students and courses
    students=Student.objects.all()
    courses=Course.objects.all()

    context={
        'students':students,
        'courses':courses
    }
    return render(request,"home.html",context)


