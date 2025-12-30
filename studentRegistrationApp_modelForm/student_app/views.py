from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def add_student_view(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form=StudentForm()
    return render(request,"add_student.html",{'form':form})

def thank_you_view(request):
    return render(request,"thank_you.html")

def student_list_view(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{'students':students})